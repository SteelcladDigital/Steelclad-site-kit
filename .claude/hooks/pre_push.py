"""PreToolUse (Bash): before any `git push`, build and check every client the push changes.

Blocks the push if a site fails to build, or a launched site has lead/tracking/placeholder problems.
A push that touches build.py or core/ checks every client.
"""
import os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _kit

data = _kit.read_input()
cmd = (data.get("tool_input") or {}).get("command", "")
if not re.search(r"\bgit\b[^;&|\n]*\bpush\b", cmd):
    sys.exit(0)


def git(*a):
    r = subprocess.run(["git", *a], cwd=_kit.ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


changed = None
for base in ("@{u}", "origin/HEAD", "origin/main"):
    out = git("diff", "--name-only", f"{base}..HEAD")
    if out is not None:
        changed = [l for l in out.splitlines() if l]
        break

if changed is None or any(_kit.is_shared(p) for p in changed):
    targets = _kit.all_clients(False)          # unknown base or kit change: check everyone
else:
    targets = sorted({c for c in map(_kit.client_of, changed) if c and os.path.exists(os.path.join(_kit.ROOT, "clients", c, "site.py"))})

must, fyi = [], []
for c in targets:
    m, f = _kit.verify(c)
    must += m
    fyi += f

if must:
    _kit.block("Push blocked. These would reach Cloudflare:\n- " + "\n- ".join(must) +
               ("\n\nAlso not to launch standard:\n- " + "\n- ".join(fyi) if fyi else ""))
sys.exit(0)
