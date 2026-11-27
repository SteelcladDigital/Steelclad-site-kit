"""Shared helpers for the Steelclad Site Kit hooks (.claude/hooks/).

Every hook reads Claude Code's hook JSON from stdin. Exit 2 = block (stderr is fed back to Claude).
Session state lives in .claude/state/ (gitignored).
"""
import html, importlib.util, json, os, re, subprocess, sys, time

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATE = os.path.join(ROOT, ".claude", "state")
APPROVALS = os.path.join(STATE, "approvals.json")
APPROVAL_HOURS = 4


# ------------------------------------------------------------------ hook I/O
def read_input():
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def block(msg):
    """Exit 2: blocks PreToolUse / keeps Claude working on Stop / shows feedback on PostToolUse."""
    print(msg.rstrip(), file=sys.stderr)
    sys.exit(2)


# ------------------------------------------------------------------ state
def _load(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return default


def _save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=1)
    os.replace(tmp, path)


def session_state(sid):
    return _load(os.path.join(STATE, f"session-{sid or 'unknown'}.json"), {"client": None, "touched": [], "stop_blocks": 0})


def save_session(sid, st):
    _save(os.path.join(STATE, f"session-{sid or 'unknown'}.json"), st)


def approved(name):
    """True if `scope.py allow <name>` was run in the last APPROVAL_HOURS hours."""
    t = _load(APPROVALS, {}).get(name)
    return bool(t) and time.time() - t < APPROVAL_HOURS * 3600


def approve(name):
    a = _load(APPROVALS, {})
    a[name] = time.time()
    _save(APPROVALS, a)


# ------------------------------------------------------------------ paths and clients
def rel(path):
    if not path:
        return None
    p = os.path.abspath(path if os.path.isabs(path) else os.path.join(ROOT, path))
    r = os.path.relpath(p, ROOT)
    return None if r.startswith("..") else r.replace(os.sep, "/")


def client_of(relpath):
    m = re.match(r"clients/([^/]+)/", relpath or "")
    return m.group(1) if m else None


def is_shared(relpath):
    return relpath == "build.py" or (relpath or "").startswith("core/")


def all_clients(include_demo=True):
    d = os.path.join(ROOT, "clients")
    return sorted(c for c in os.listdir(d)
                  if os.path.exists(os.path.join(d, c, "site.py")) and (include_demo or not c.startswith("_")))


def config(client):
    path = os.path.join(ROOT, "clients", client, "site.py")
    spec = importlib.util.spec_from_file_location(f"cfg_{client.replace('-', '_')}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CONFIG


# ------------------------------------------------------------------ build + scan
def build(client):
    """Deploy build (same command Cloudflare runs). Returns (ok, output)."""
    r = subprocess.run([sys.executable, "build.py", client], cwd=ROOT, capture_output=True, text=True, timeout=120)
    out = (r.stdout + r.stderr).strip()
    return r.returncode == 0, "\n".join(out.splitlines()[-25:])


GHL_MARKERS = re.compile(r"leadconnector|msgsndr|gohighlevel|@@GHL|\bGHL\b", re.I)
HARD = "!"   # prefix: lead/tracking/credibility problems; these block launched sites


PLACEHOLDERS = re.compile(r"lorem ipsum|\bTODO\b|\bTBD\b|\bFIXME\b|\[(?:placeholder|insert|client)[^\]]*\]|\{\{[^}]*\}\}|\b555-\d{4}\b|\bexample\.com\b", re.I)


def _visible_text(h):
    h = re.sub(r"<(script|style)\b.*?</\1>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<!--.*?-->", " ", h, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", h))


def scan(client):
    """Check the deploy build in dist/<client>/ against Steelclad standards.
    Returns a list of issues; ones starting with HARD block launched sites, the rest are standards to fix."""
    cfg = config(client)
    ig = cfg.get("integrations", {})
    areas = cfg.get("areas") or {}
    region = cfg.get("business", {}).get("address", {}).get("region", "")
    out = os.path.join(ROOT, "dist", client)
    issues = []
    if not os.path.isdir(out):
        return [f"No build output in dist/{client}/"]

    pages = []
    for dp, _, fs in os.walk(out):
        for f in fs:
            if f.endswith((".html", ".js")):
                p = os.path.join(dp, f)
                pages.append((os.path.relpath(p, out), open(p, encoding="utf-8", errors="ignore").read()))
    html_pages = [(p, h) for p, h in pages if p.endswith(".html")]

    # 1. GHL-free sites must carry no GHL code at all
    if ig.get("form_mode") == "web3forms":
        hits = [p for p, h in pages if GHL_MARKERS.search(h)]
        if hits:
            issues.append(HARD + f"Web3Forms site still contains GHL code in {len(hits)} file(s), e.g. {hits[0]}")

    # 2. Tracking: GTM on every page when set, or an explicit opt-out
    gtm = ig.get("gtm_id")
    if gtm:
        missing = [p for p, h in html_pages if gtm not in h and not p.startswith("404")]
        if missing:
            issues.append(HARD + f"GTM {gtm} missing from {len(missing)} page(s), e.g. {missing[0]}")
    elif ig.get("form_mode") == "web3forms" and not ig.get("no_analytics"):
        issues.append(HARD + "No integrations.gtm_id and no integrations.no_analytics opt-out: leads can't be measured")

    # 3. Placeholder / template text in what visitors actually read
    ph = []
    for p, h in html_pages:
        m = PLACEHOLDERS.search(_visible_text(h))
        if m:
            ph.append(f"{p}: \"{m.group(0)}\"")
    if ph:
        issues.append(HARD + f"Placeholder text on {len(ph)} page(s): " + "; ".join(ph[:3]))

    # 4. Basic on-page SEO on every indexable page
    seo = []
    for p, h in html_pages:
        if p.startswith("404") or 'name="robots" content="noindex' in h:
            continue
        t = re.search(r"<title>(.*?)</title>", h, re.S)
        d = re.search(r'<meta name="description" content="([^"]*)"', h)
        h1 = len(re.findall(r"<h1[\s>]", h))
        if not t or not t.group(1).strip():
            seo.append(f"{p}: no <title>")
        if not d or not d.group(1).strip():
            seo.append(f"{p}: no meta description")
        if h1 != 1:
            seo.append(f"{p}: {h1} <h1> tags")
    if seo:
        issues.append(f"On-page SEO gaps on {len(seo)} item(s): " + "; ".join(seo[:4]))

    # 5. Footer standard: compact service areas, never one "Service <City>, ST" link per city
    if areas.get("enabled"):
        idx = dict(html_pages).get("index.html", "")
        foot = re.search(r"<footer.*?</footer>", idx, re.S)
        if foot and region:
            long_links = re.findall(r">[^<>]{2,60}, " + re.escape(region) + r"</a>", foot.group(0))
            if long_links:
                issues.append(f"Footer lists {len(long_links)} '<Service> <City>, {region}' links; set areas.footer: \"compact\" (Steelclad footer standard)")

    # 6. Share image committed (Cloudflare builds can't generate one without Pillow)
    og = cfg.get("og_image", "og-image.jpg")
    if not os.path.exists(os.path.join(ROOT, "clients", client, "assets", og)):
        issues.append(f"clients/{client}/assets/{og} not committed: social share image may be missing on Cloudflare")

    return issues


def verify(client):
    """Build + scan one client. Returns (must_fix, fyi).
    must_fix = build failures, plus hard issues on launched sites. Everything else is reported, not blocking."""
    ok, out = build(client)
    if not ok:
        return [f"[{client}] build failed:\n{out}"], []
    launched = config(client).get("launched", False)
    must, fyi = [], []
    for i in scan(client):
        hard = i.startswith(HARD)
        (must if hard and launched else fyi).append(f"[{client}] " + i.lstrip(HARD))
    return must, fyi
