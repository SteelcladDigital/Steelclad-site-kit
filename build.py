#!/usr/bin/env python3
"""
Steelclad Site Kit — static, SEO-first websites for local businesses.

  python3 build.py <client>              -> dist/<client>/      deploy build (clean URLs)
  python3 build.py <client> --preview    -> preview/<client>/   relative links, opens from files / artifact
  python3 build.py --list                -> list clients

Each client lives in clients/<client>/site.py and exports CONFIG (see clients/_template/site.py).
Optional clients/<client>/assets/ is copied into the site's /assets/ (logo, photos, og-image).
"""
import json, os, shutil, sys, html, importlib.util, re
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
esc = html.escape
TODAY = date.today().isoformat()

# ============================================================== icons
I = {
 "calendar":'<path d="M7 3v3M17 3v3M4 9h16M5 5h14a1 1 0 011 1v13a1 1 0 01-1 1H5a1 1 0 01-1-1V6a1 1 0 011-1z"/><path d="M9 14l2 2 4-4"/>',
 "leaf":'<path d="M5 19c0-8 5-14 15-15-1 10-7 15-15 15z"/><path d="M5 19l7-7"/>',
 "sparkle":'<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16l.7 1.8 1.8.7-1.8.7L19 21l-.7-1.8-1.8-.7 1.8-.7z"/>',
 "wrench":'<path d="M14.7 6.3a4 4 0 00-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 005.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>',
 "bolt":'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "search":'<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
 "layers":'<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "shield":'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "phone":'<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>',
 "chat":'<path d="M4 5h16v11H8l-4 4z"/>',
 "home":'<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>',
 "badge":'<circle cx="12" cy="9" r="6"/><path d="M8.5 13.5L7 21l5-3 5 3-1.5-7.5"/>',
 "check":'<path d="M5 12l5 5 9-10"/>',
 "doc":'<path d="M6 3h9l4 4v14H6z"/><path d="M9 12h7M9 16h7M9 8h3"/>',
 "pin":'<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "star":'<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
 "heart":'<path d="M12 20s-8-5-8-11a4.5 4.5 0 018-2.8A4.5 4.5 0 0120 9c0 6-8 11-8 11z"/>',
 "cup":'<path d="M4 8h12v6a5 5 0 01-5 5H9a5 5 0 01-5-5z"/><path d="M16 10h2a2 2 0 010 4h-2M8 3v2M12 3v2"/>',
 "truck":'<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>',
 "thermo":'<path d="M10 4a2 2 0 014 0v9a4 4 0 11-4 0z"/><path d="M12 9v6"/>',
 "drop":'<path d="M12 3s6 7 6 11a6 6 0 01-12 0c0-4 6-11 6-11z"/>',
 "tool":'<path d="M3 21l6-6M14 4l6 6-8 8-6-6z"/>',
 "users":'<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0112 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15 14a5 5 0 016 6"/>',
 "menu":'<path d="M4 7h16M4 12h16M4 17h16"/>',
 "fb":'<path d="M14 8h3V4h-3a4 4 0 00-4 4v2H7v4h3v7h4v-7h3l1-4h-4V8z" fill="currentColor" stroke="none"/>',
 "ig":'<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/>',
}
def icon(name, cls=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I.get(name, I["check"])}</svg>'

FONT_FILES = {f[:-6] for f in os.listdir(os.path.join(ROOT, "core", "fonts"))}
FONT_FAMILY = {"oswald":"Oswald","inter":"Inter","fraunces":"Fraunces","playfair-display":"Playfair Display","outfit":"Outfit",
  "space-grotesk":"Space Grotesk","dm-sans":"DM Sans","archivo":"Archivo","nunito-sans":"Nunito Sans","manrope":"Manrope",
  "bricolage-grotesque":"Bricolage Grotesque","source-serif-4":"Source Serif 4"}

TEXTURES = {
 "ripples": "M0 60c40-20 80 20 120 0s80-20 120 0M0 140c40-20 80 20 120 0s80-20 120 0M0 220c40-20 80 20 120 0s80-20 120 0",
 "lines": "M0 0L240 240M-120 0L120 240M120 0L360 240",
 "grid": "M0 0H240M0 60H240M0 120H240M0 180H240M0 0V240M60 0V240M120 0V240M180 0V240",
}


# ============================================================== blog: posts + mini markdown
def parse_post(path):
    """Post file = front matter between --- lines (key: value) + Markdown body."""
    raw = open(path, encoding="utf-8").read()
    meta, body = {}, raw
    if raw.startswith("---"):
        _, fm, body = raw.split("---", 2)
        for line in fm.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1); meta[k.strip()] = v.strip().strip('"')
    for k in ("services", "areas", "tags"):
        meta[k] = [x.strip() for x in meta.get(k, "").split(",") if x.strip()]
    meta["draft"] = meta.get("draft", "false").lower() in ("true", "yes", "1")
    base = os.path.basename(path)[:-3]
    meta.setdefault("slug", re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base))
    meta.setdefault("date", base[:10] if re.match(r"\d{4}-\d{2}-\d{2}", base) else TODAY)
    meta["body_md"] = body.strip()
    meta["words"] = len(re.findall(r"\w+", body))
    return meta

def md_inline(t, link):
    t = esc(t, quote=False)
    t = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", lambda m: f'<img src="{link(m.group(2))}" alt="{m.group(1)}" loading="lazy">', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{link(m.group(2))}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t

def markdown(md, link):
    """Small Markdown subset: ## / ### headings (# is demoted to ## so a post keeps one H1),
    paragraphs, - and 1. lists, > quotes, images, links, bold, italic."""
    out, para, lst = [], [], None
    def flush():
        nonlocal para, lst
        if para: out.append("<p>" + md_inline(" ".join(para), link) + "</p>"); para = []
        if lst: out.append(f"<{lst[0]}>" + "".join(f"<li>{md_inline(i, link)}</li>" for i in lst[1]) + f"</{lst[0]}>"); lst = None
    for line in md.splitlines():
        st = line.strip()
        if not st: flush(); continue
        m = re.match(r"^(#{1,4})\s+(.*)", st)
        if m:
            flush(); lvl = min(max(len(m.group(1)), 2), 4)
            hid = re.sub(r"[^a-z0-9]+", "-", m.group(2).lower()).strip("-")
            out.append(f'<h{lvl} id="{hid}">{md_inline(m.group(2), link)}</h{lvl}>'); continue
        m = re.match(r"^([-*]|\d+\.)\s+(.*)", st)
        if m:
            kind = "ol" if m.group(1)[0].isdigit() else "ul"
            if para:
                out.append("<p>" + md_inline(" ".join(para), link) + "</p>"); para = []
            if lst and lst[0] != kind: flush()
            lst = lst or (kind, []); lst[1].append(m.group(2)); continue
        if st.startswith(">"):
            flush(); out.append("<blockquote><p>" + md_inline(st.lstrip("> "), link) + "</p></blockquote>"); continue
        if lst: flush()
        para.append(st)
    flush()
    return "\n".join(out)


# ============================================================== builder
class Site:
    def __init__(self, client, preview):
        path = os.path.join(ROOT, "clients", client, "site.py")
        spec = importlib.util.spec_from_file_location("site_cfg", path)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        self.c = mod.CONFIG; self.client = client; self.preview = preview
        self.b = self.c["business"]; self.D = self.b["domain"].rstrip("/")
        self.L = self.c["labels"]; self.pages = {}
        self.out = os.path.join(ROOT, "preview" if preview else "dist", client)
        self.client_assets = os.path.join(ROOT, "clients", client, "assets")
        T = self.c.get("tiers") or {}; self.tiers = T if T.get("enabled") else None
        A = self.c.get("areas") or {}; self.areas = A if A.get("enabled") else None
        R = self.c.get("resource") or {}; self.resource = R if R.get("enabled") else None
        B = self.c.get("blog") or {}; self.blog = B if B.get("enabled") else None
        self.posts = []
        if self.blog:
            pdir = os.path.join(ROOT, "clients", client, "posts")
            if os.path.isdir(pdir):
                for f in sorted(os.listdir(pdir)):
                    if f.endswith(".md"):
                        p = parse_post(os.path.join(pdir, f))
                        if not p["draft"]: self.posts.append(p)
            self.posts.sort(key=lambda p: p["date"], reverse=True)

    # ---------- links
    def href(self, cur, target):
        if not self.preview: return "/" + (target + "/" if target else "")
        depth = len([s for s in cur.split("/") if s])
        return "../" * depth + (target + "/index.html" if target else "index.html")
    def asset(self, cur, name):
        if not self.preview: return "/assets/" + name
        depth = len([s for s in cur.split("/") if s]); return "../" * depth + "assets/" + name
    def canon(self, path): return self.D + "/" + (path + "/" if path else "")

    # ---------- theme
    def theme_css(self):
        t = self.c["theme"]; col = t["colors"]
        disp, body = t["fonts"]["display"], t["fonts"]["body"]
        for f in (disp, body):
            if f not in FONT_FILES: raise SystemExit(f"Font '{f}' not in core/fonts. Options: {sorted(FONT_FILES)}")
        radius = {"sharp": ("4px", "6px"), "soft": ("14px", "999px"), "round": ("22px", "999px")}[t.get("radius", "soft")]
        tex = TEXTURES.get(t.get("texture", "ripples"))
        sec = col["secondary"].replace("#", "%23")
        tex_css = f"url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240' viewBox='0 0 240 240'%3E%3Cpath d='{tex}' fill='none' stroke='{sec}' stroke-width='2'/%3E%3C/svg%3E\")" if tex else "none"
        dark = col.get("accent_text", "#121c35").replace("#", "%23")
        faces = "".join(f'@font-face{{font-family:"{FONT_FAMILY[f]}";src:url(fonts/{f}.woff2) format("woff2");font-weight:100 900;font-display:swap}}\n' for f in {disp, body})
        return faces + f''':root{{
--c-primary:{col["primary"]};--c-primary-deep:{col["primary_deep"]};--c-secondary:{col["secondary"]};--c-secondary-deep:{col["secondary_deep"]};
--c-secondary-wash:{col["secondary_wash"]};--c-accent:{col["accent"]};--c-accent-text:{col.get("accent_text","#121c35")};
--c-surface:{col["surface"]};--c-ink:{col.get("ink","#16213a")};--c-muted:{col.get("muted","#4a5674")};--c-line:#dfe3ea;--c-white:#fff;
--radius:{radius[0]};--btn-radius:{radius[1]};--shadow:0 10px 30px rgba(18,28,53,.12);
--display:"{FONT_FAMILY[disp]}",system-ui,sans-serif;--body:"{FONT_FAMILY[body]}",system-ui,-apple-system,"Segoe UI",sans-serif;
--heading-case:{t.get("heading_case","none")};--wrap:1180px;--texture:{tex_css};
--chk-white:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M4 8.5l2.5 2.5L12 5.5' fill='none' stroke='white' stroke-width='2'/%3E%3C/svg%3E");
--chk-dark:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M4 8.5l2.5 2.5L12 5.5' fill='none' stroke='{dark}' stroke-width='2'/%3E%3C/svg%3E");
}}
'''

    # ---------- logo
    def logo(self, cur):
        lg = self.c["logo"]
        if lg["type"] == "svg": return lg["svg"]
        if lg["type"] == "image": return f'<img src="{self.asset(cur, lg["file"])}" alt="{esc(self.b["name"])}" width="{lg.get("width",160)}" height="{lg.get("height",58)}">'
        return '<span class="logo-text">' + "<br>".join(esc(x) for x in lg["lines"]) + "</span>"

    # ---------- schema
    def business_schema(self):
        b = self.b
        addr = {"@type": "PostalAddress", "addressLocality": b["address"]["locality"], "addressRegion": b["address"]["region"], "addressCountry": "US"}
        if b["address"].get("street"): addr["streetAddress"] = b["address"]["street"]
        if b["address"].get("zip"): addr["postalCode"] = b["address"]["zip"]
        s = {"@type": b["schema_type"], "@id": self.D + "/#business", "name": b["legal_name"], "alternateName": b["name"],
             "url": self.D + "/", "telephone": b["tel"], "description": b["description"], "address": addr,
             "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": d, "opens": o, "closes": c} for d, o, c in b["hours"]],
             "sameAs": [u for u in b.get("social", {}).values() if u]}
        logo = self.c["logo"].get("file") or "logo.svg"; s["logo"] = s["image"] = self.D + "/assets/" + logo
        if b.get("geo"): s["geo"] = {"@type": "GeoCoordinates", "latitude": b["geo"][0], "longitude": b["geo"][1]}
        if b.get("price_range"): s["priceRange"] = b["price_range"]
        if b.get("email"): s["email"] = b["email"]
        if b.get("knows_about"): s["knowsAbout"] = b["knows_about"]
        served = [{"@type": "AdministrativeArea", "name": x} for x in b.get("counties", [])]
        if self.areas: served += [{"@type": "City", "name": f'{a["city"]}, {b["address"]["region"]}'} for a in self.areas["pages"]]
        if served: s["areaServed"] = served
        if self.tiers:
            s["hasOfferCatalog"] = {"@type": "OfferCatalog", "name": self.tiers["nav_label"], "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": t["name"], "description": t["for"]}} for t in self.tiers["items"]]}
        return s
    def crumbs_schema(self, trail):
        return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": self.canon(p)} for i, (n, p) in enumerate(trail)]}
    @staticmethod
    def faq_schema(faqs):
        return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    def service_schema(self, name, desc, path, cities=None):
        s = {"@type": "Service", "name": name, "description": desc, "url": self.canon(path), "provider": {"@id": self.D + "/#business"}, "serviceType": name}
        cities = cities or ([a["city"] for a in self.areas["pages"]] if self.areas else [self.b["address"]["locality"]])
        s["areaServed"] = [{"@type": "City", "name": f'{c}, {self.b["address"]["region"]}'} for c in cities]
        return s

    # ---------- chrome
    def header(self, cur):
        b, L = self.b, self.L
        def ca(p): return ' aria-current="page"' if cur == p else ""
        items = []
        if self.tiers: items.append(f'<li><a class="nl" href="{self.href(cur,self.tiers["slug"])}"{ca(self.tiers["slug"])}>{esc(self.tiers["nav_label"])}</a></li>')
        svc = "".join(f'<li><a href="{self.href(cur,self.svc_path(s))}">{esc(s["name"])}</a></li>' for s in self.c["services"])
        sh = self.c["services_hub"]
        items.append(f'<li><a class="nl" href="{self.href(cur,sh["slug"])}"{ca(sh["slug"])}>{esc(sh["nav_label"])} ▾</a><ul class="dropdown">{svc}</ul></li>')
        if self.areas:
            dd = ""
            for g in self.areas["groups"]:
                dd += f'<li class="sep">{esc(g["name"])}</li>' + "".join(f'<li><a href="{self.href(cur,a["slug"])}">{esc(a["city"])}</a></li>' for a in self.areas["pages"] if a["slug"] in g["slugs"])
            items.append(f'<li><a class="nl" href="{self.href(cur,self.areas["hub_slug"])}"{ca(self.areas["hub_slug"])}>{esc(self.areas["nav_label"])} ▾</a><ul class="dropdown">{dd}</ul></li>')
        if self.resource: items.append(f'<li><a class="nl" href="{self.href(cur,self.resource["slug"])}"{ca(self.resource["slug"])}>{esc(self.resource["nav_label"])}</a></li>')
        if self.blog: items.append(f'<li><a class="nl" href="{self.href(cur,self.blog["index_slug"])}"{ca(self.blog["index_slug"])}>{esc(self.blog["nav_label"])}</a></li>')
        items.append(f'<li><a class="nl" href="{self.href(cur,"about")}"{ca("about")}>About</a></li>')
        promise = f'<span class="promise"><span class="dot"></span><span>{esc(L["topbar_promise"])}</span></span>' if L.get("topbar_promise") else "<span></span>"
        return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">{promise}<span><span class="hide-sm">{esc(b["hours_text"])} · </span><a href="tel:{b["tel"]}">{esc(L["phone_prefix"])} {b["phone"]}</a></span></div></div>
<header class="site-header"><div class="wrap">
<a class="logo" href="{self.href(cur,"")}" aria-label="{esc(b["name"])} home">{self.logo(cur)}</a>
<nav class="nav" id="nav" aria-label="Main"><ul>{"".join(items)}</ul></nav>
<div class="header-cta"><a class="btn btn-gold" href="{self.href(cur,"contact")}">{esc(L["cta"])}</a>
<button class="menu-toggle" aria-label="Open menu" aria-controls="nav" aria-expanded="false">{icon("menu")}</button></div>
</div></header>'''

    def footer(self, cur):
        b, L = self.b, self.L
        svc = "".join(f'<li><a href="{self.href(cur,self.svc_path(s))}">{esc(s["name"])}</a></li>' for s in self.c["services"])
        if self.tiers: svc = f'<li><a href="{self.href(cur,self.tiers["slug"])}">{esc(self.tiers["nav_label"])}</a></li>' + svc
        col3 = ""
        if self.areas:
            col3 = '<div><h4>Service Areas</h4><ul>' + "".join(f'<li><a href="{self.href(cur,a["slug"])}">{esc(self.areas["link_prefix"])} {esc(a["city"])}, {b["address"]["region"]}</a></li>' for a in self.areas["pages"]) + "</ul></div>"
        else:
            addr = b["address"]; street = f'{esc(addr["street"])}<br>' if addr.get("street") else ""
            col3 = f'<div><h4>Visit</h4><p>{street}{esc(addr["locality"])}, {addr["region"]} {addr.get("zip","")}</p><p>{esc(b["hours_text"])}</p></div>'
        social = "".join(f'<a href="{u}" aria-label="{k.title()}">{icon("fb" if k=="facebook" else "ig")}</a>' for k, u in b.get("social", {}).items() if u and k in ("facebook", "instagram"))
        company = [("about", "About Us"), ("contact", L["cta"])]
        if self.resource: company.insert(1, (self.resource["slug"], self.resource["nav_label"]))
        if self.blog: company.insert(1, (self.blog["index_slug"], self.blog["nav_label"]))
        if self.areas: company.append((self.areas["hub_slug"], "All Service Areas"))
        comp = "".join(f'<li><a href="{self.href(cur,p)}">{esc(n)}</a></li>' for p, n in company)
        legal = " · ".join(f'<a href="{self.href(cur,s)}">{esc(n)}</a>' for s, n in self.c.get("legal_pages", []))
        return f'''<footer class="site-footer"><div class="wrap"><div class="cols">
<div><a class="logo" href="{self.href(cur,"")}">{self.logo(cur)}</a><p style="margin-top:16px">{esc(L["footer_blurb"])}</p>
<p><a href="tel:{b["tel"]}"><strong>{b["phone"]}</strong></a><br>{esc(b["hours_text"])}</p><div class="social">{social}</div></div>
<div><h4>{esc(L.get("footer_services_title","Services"))}</h4><ul>{svc}</ul></div>{col3}
<div><h4>Company</h4><ul>{comp}</ul></div>
</div><div class="legal"><span>© {date.today().year} {esc(b["legal_name"])}. All rights reserved.</span><span>{legal}</span></div></div></footer>
<nav class="mbar" aria-label="Quick actions"><a href="tel:{b["tel"]}">{icon("phone")}Call</a><a href="{L.get("mbar_second_href") or "sms:"+b["tel"]}">{icon(L.get("mbar_second_icon","chat"))}{esc(L.get("mbar_second_label","Text"))}</a><a class="go" href="{self.href(cur,"contact")}">{icon("calendar")}{esc(L["cta_short"])}</a></nav>'''

    def page(self, cur, title, meta, body, schema=None, trail=None, noindex=False, og_override=None, og_type="website"):
        brand = self.b["name"]; base = title.split(" | ")[0]
        title = f"{base} | {brand}" if len(base) + len(brand) <= 62 else base
        ig = self.c.get("integrations", {})
        graph = [self.business_schema(), {"@type": "WebPage", "@id": self.canon(cur) + "#webpage", "url": self.canon(cur), "name": title, "description": meta,
                 "isPartOf": {"@type": "WebSite", "@id": self.D + "/#website", "url": self.D + "/", "name": brand}, "about": {"@id": self.D + "/#business"}, "dateModified": TODAY}]
        if trail: graph.append(self.crumbs_schema(trail))
        graph += schema or []
        ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
        gtm = f"<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{ig['gtm_id']}');</script>" if ig.get("gtm_id") else "<!-- GTM: set integrations.gtm_id -->"
        chat = f'<script src="https://widgets.leadconnectorhq.com/loader.js" data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" data-widget-id="{ig["ghl_chat_widget_id"]}"></script>' if ig.get("ghl_chat_widget_id") else "<!-- GHL chat: set integrations.ghl_chat_widget_id -->"
        fonts = {self.c["theme"]["fonts"]["display"], self.c["theme"]["fonts"]["body"]}
        pre = "".join(f'<link rel="preload" href="{self.asset(cur,"fonts/"+f+".woff2")}" as="font" type="font/woff2" crossorigin>' for f in fonts)
        og = og_override or self.c.get("og_image", "og-image.jpg")
        rss = f'<link rel="alternate" type="application/rss+xml" title="{esc(brand)}" href="{self.D}/{self.blog["index_slug"]}/rss.xml">' if self.blog and self.posts else ""
        return f'''<!DOCTYPE html>
<html lang="en-US"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(meta)}">
<link rel="canonical" href="{self.canon(cur)}"><meta name="robots" content="{'noindex' if noindex else 'index, follow, max-image-preview:large'}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{esc(brand)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(meta)}">
<meta property="og:url" content="{self.canon(cur)}"><meta property="og:image" content="{self.D}/assets/{og}"><meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="US-{self.b["address"]["region"]}"><meta name="geo.placename" content="{esc(self.b["address"]["locality"])}">
<meta name="theme-color" content="{self.c["theme"]["colors"]["primary"]}"><link rel="icon" href="{self.asset(cur,"favicon.svg")}" type="image/svg+xml">
{pre}<link rel="stylesheet" href="{self.asset(cur,"theme.css")}"><link rel="stylesheet" href="{self.asset(cur,"site.css")}">
<script type="application/ld+json">{ld}</script>{gtm}{rss}
</head><body>
{self.header(cur)}
<main id="main">
{body}
</main>
{self.footer(cur)}
<script src="{self.asset(cur,"site.js")}" defer></script>{chat}
</body></html>'''

    # ---------- shared blocks
    def divider(self, sand=False):
        d = self.c["theme"].get("divider", "wave")
        if d == "none": return ""
        path = "M0 30c120-20 240-20 360 0s240 20 360 0 240-20 360 0 240 20 360 0v30H0z" if d == "wave" else "M0 60L1440 6V60z"
        return f'<svg class="wave{" sand" if sand else ""}" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="{path}" fill="currentColor"/></svg>'
    def texture(self): return '<div class="caustics"></div>' if self.c["theme"].get("texture", "ripples") != "none" else ""

    def page_hero(self, cur, trail, h1, lead, ctas=True, sand=False):
        bc = " / ".join(f'<a href="{self.href(cur,p)}">{esc(n)}</a>' for n, p in trail[:-1]) + f' / <span>{esc(trail[-1][0])}</span>'
        btns = f'<div class="btn-row" style="margin-top:22px"><a class="btn btn-gold" href="{self.href(cur,"contact")}">{esc(self.L["cta_long"])}</a><a class="btn btn-ghost" href="tel:{self.b["tel"]}">{esc(self.L["phone_prefix"])} {self.b["phone"]}</a></div>' if ctas else ""
        lead_html = f'<p class="lead">{lead}</p>' if lead else ""
        return f'''<section class="hero page-hero on-dark">{self.texture()}<div class="wrap"><div><nav class="crumbs" aria-label="Breadcrumb">{bc}</nav><h1>{h1}</h1>{lead_html}{btns}</div></div>{self.divider(sand)}</section>'''

    def tier_cards(self, cur):
        T = self.tiers; out = []
        for p in T["items"]:
            items = "".join(f'<li class="plus">{esc(i)}</li>' if i.endswith(":") else f"<li>{esc(i)}</li>" for i in p["items"])
            price = p.get("price") or T["price_label"]
            out.append(f'''<article class="plan{' featured' if p.get('featured') else ''}" id="plan-{p["slug"]}"><span class="badge">{esc(p["tag"])}</span>
<h3>{esc(p["name"])}</h3><p class="for">{esc(p["for"])}</p><div class="price">{esc(price)}<small>{esc(p.get("price_note") or T["price_note"])}</small></div>
<ul>{items}</ul><a class="btn {'btn-gold' if p.get('featured') else 'btn-outline'}" href="{self.href(cur,"contact")}#plan-{p["slug"]}">{esc(T["card_cta"].format(name=p["name"]))}</a></article>''')
        return f'<div class="plans">{"".join(out)}</div>'

    def compare_table(self):
        T = self.tiers
        def cell(v):
            if v == 1 or v is True: return '<td class="y" aria-label="Included">✓</td>'
            if not v: return '<td class="n" aria-label="Not included">—</td>'
            return f"<td>{esc(str(v))}</td>"
        heads = "".join(f'<th scope="col"{" class=hl" if t.get("featured") else ""}>{esc(t["name"])}</th>' for t in T["items"])
        rows = "".join(f"<tr><td>{esc(r[0])}</td>{''.join(cell(v) for v in r[1:])}</tr>" for r in T["compare"])
        return f'<div class="table-scroll"><table class="compare"><thead><tr><th scope="col">What\'s included</th>{heads}</tr></thead><tbody>{rows}</tbody></table></div>'

    def quiz(self, cur):
        T = self.tiers; Q = T["quiz"]
        data = esc(json.dumps([{"slug": t["slug"], "name": t["name"], "why": t["why"]} for t in T["items"]]))
        sets = ""
        for i, q in enumerate(Q["questions"]):
            opts = "".join(f'<label><input type="radio" name="q{i}" data-tier="{tier}"> {esc(lbl)}</label>' for lbl, tier in q["options"])
            sets += f'<fieldset><legend>{i+1}. {esc(q["q"])}</legend><div class="opts">{opts}</div></fieldset>'
        return f'<form class="quiz" id="plan-finder" data-tiers="{data}" onsubmit="return false">{sets}<div class="quiz-result" id="quiz-result" aria-live="polite"><h3></h3><p></p><a class="btn btn-gold" href="{self.href(cur,"contact")}">{esc(self.L["cta_long"])}</a></div></form>'

    def reviews_block(self):
        cards = "".join(f'<figure class="review"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><blockquote>“{esc(t)}”</blockquote><figcaption><cite>{esc(n)}<span>{esc(c)}</span></cite></figcaption></figure>' for n, c, t in self.c["reviews"])
        url = self.c.get("integrations", {}).get("google_reviews_url")
        more = f'<p style="text-align:center;margin-top:28px"><a class="btn btn-outline" href="{url}">Read more reviews on Google</a></p>' if url else ""
        return f'<div class="reviews">{cards}</div>{more}'

    @staticmethod
    def faq_block(faqs): return '<div class="faq">' + "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs) + "</div>"

    def cta_band(self, cur, h=None, p=None):
        h = h or self.L["cta_band_title"]; p = p or self.L["cta_band_text"]
        return f'''<section><div class="wrap"><div class="cta-band"><div><h2>{h}</h2><p>{p}</p></div>
<div class="btn-row"><a class="btn btn-gold" href="{self.href(cur,"contact")}">{esc(self.L["cta"])}</a><a class="btn btn-ghost" href="tel:{self.b["tel"]}">{self.b["phone"]}</a></div></div></div></section>'''

    def svc_path(self, s): return f'{self.c["services_hub"]["slug"]}/{s["slug"]}'
    def service_cards(self, cur, exclude=None):
        return '<div class="grid-3">' + "".join(
            f'<a class="card" href="{self.href(cur,self.svc_path(s))}"><span class="ic">{icon(s["icon"])}</span><h3>{esc(s["name"])}</h3><p>{esc(s["short"])}</p><span class="more">Learn more →</span></a>'
            for s in self.c["services"] if s["slug"] != exclude) + "</div>"

    def area_block(self, cur):
        A = self.areas; cols = ""
        for g in A["groups"]:
            links = "".join(f'<li><a href="{self.href(cur,a["slug"])}">{esc(a["city"])}</a></li>' for a in A["pages"] if a["slug"] in g["slugs"])
            cols += f'<div class="county"><h3>{esc(g["name"])} <small>{esc(g.get("note",""))}</small></h3><ul class="city-links">{links}</ul></div>'
        return f'<div class="grid-2">{cols}</div><p style="text-align:center;margin-top:24px;color:var(--c-muted)">{esc(A["outside_note"])} <a href="tel:{self.b["tel"]}">{self.b["phone"]}</a></p>'

    def hero_visual(self, cur):
        h = self.c["home"]; lay = self.c["theme"].get("hero_layout", "card")
        if lay == "image" and h.get("hero_image"):
            return f'<div class="hero-photo"><img src="{self.asset(cur,h["hero_image"])}" alt="{esc(h.get("hero_image_alt",""))}" width="800" height="1000" fetchpriority="high"></div>'
        if lay == "card" and h.get("hero_card"):
            k = h["hero_card"]
            stats = "".join(f'<div class="reading"><b>{esc(v)}</b><small>{esc(l)}</small></div>' for v, l in k.get("stats", []))
            checks = "".join(f"<li>{esc(x)}</li>" for x in k.get("checks", []))
            return f'''<aside class="hanger{'' if k.get("hanger") else ' plain'}" aria-label="{esc(k["title"])}">{f'<span class="sample">{esc(k["badge"])}</span>' if k.get("badge") else ""}
<div class="tag">{esc(k["label"])}</div><p class="hanger-title">{esc(k["title"])}</p><div class="date">{esc(k.get("sub",""))}</div>
{f'<div class="readings">{stats}</div>' if stats else ""}{f'<ul class="checks">{checks}</ul>' if checks else ""}{f'<p class="note">{esc(k["note"])}</p>' if k.get("note") else ""}</aside>'''
        return ""

    def trail(self, *parts): return [("Home", "")] + list(parts)

    # ============================================================== pages
    def home(self):
        cur = ""; h = self.c["home"]; L = self.L
        lay = self.c["theme"].get("hero_layout", "card"); vis = self.hero_visual(cur)
        if not vis: lay = "centered"
        proof = "".join(f"<span>{icon('check')}{esc(x)}</span>" for x in h.get("proof", []))
        sec2 = f'<a class="btn btn-ghost" href="{self.href(cur,h["secondary_cta"][1])}">{esc(h["secondary_cta"][0])}</a>' if h.get("secondary_cta") else ""
        hero = f'''<section class="hero on-dark layout-{lay}">{self.texture()}<div class="wrap"><div>
<span class="eyebrow">{esc(h["eyebrow"])}</span><h1>{h["h1"]}</h1><p class="lead">{esc(h["lead"])}</p>
<div class="btn-row" style="margin-top:26px"><a class="btn btn-gold" href="{self.href(cur,"contact")}">{esc(L["cta_long"])}</a>{sec2}</div>
<div class="hero-proof">{proof}</div></div>{vis}</div>{self.divider()}</section>'''
        S = {}
        S["trust"] = '<section class="trust"><div class="wrap">' + "".join(f'<div>{icon(i)}<span>{esc(t)}<small>{esc(s)}</small></span></div>' for i, t, s in h["trust"]) + "</div></section>"
        if self.tiers:
            T = self.tiers
            S["tiers"] = f'''<section><div class="wrap"><div class="section-head center"><span class="eyebrow">{esc(T["nav_label"])}</span><h2>{esc(T["home_title"])}</h2><p class="lead">{esc(T["home_lead"])}</p></div>
{self.tier_cards(cur)}<p style="text-align:center;margin-top:30px"><a href="{self.href(cur,T["slug"])}"><strong>See the full comparison →</strong></a></p></div></section>'''
            S["quiz"] = f'<section><div class="wrap"><div class="section-head center"><span class="eyebrow">{esc(T["quiz"]["eyebrow"])}</span><h2>{esc(T["quiz"]["title"])}</h2></div>{self.quiz(cur)}</div></section>' if T.get("quiz") else ""
        if h.get("why"):
            w = h["why"]
            items = "".join(f'<li>{icon(i)}<div><b>{esc(t)}</b>{esc(d)}</div></li>' for i, t, d in w["items"])
            S["why"] = f'''<section class="bg-navy on-dark"><div class="wrap grid-2"><div><span class="eyebrow">{esc(w["eyebrow"])}</span>
<p class="bigquote">{w["quote_html"]}</p><p style="color:rgba(255,255,255,.72)">{esc(w["body"])}</p></div><ul class="promise-list">{items}</ul></div></section>'''
        if h.get("steps"):
            st = h["steps"]
            S["steps"] = f'<section class="bg-sand"><div class="wrap"><div class="section-head"><span class="eyebrow">{esc(st["eyebrow"])}</span><h2>{esc(st["title"])}</h2></div><div class="steps">' + "".join(f'<div class="step"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in st["items"]) + "</div></div></section>"
        sh = self.c["services_hub"]
        S["services"] = f'<section><div class="wrap"><div class="section-head"><span class="eyebrow">{esc(sh["nav_label"])}</span><h2>{esc(sh["home_title"])}</h2><p class="lead">{esc(sh["home_lead"])}</p></div>{self.service_cards(cur)}</div></section>'
        S["reviews"] = f'<section class="bg-sand"><div class="wrap"><div class="section-head center"><span class="eyebrow">Reviews</span><h2>{esc(L["reviews_title"])}</h2></div>{self.reviews_block()}</div></section>' if self.c["reviews"] else ""
        if self.areas:
            S["areas"] = f'<section class="bg-sand"><div class="wrap"><div class="section-head center"><span class="eyebrow">{esc(self.areas["nav_label"])}</span><h2>{esc(self.areas["home_title"])}</h2></div>{self.area_block(cur)}</div></section>'
        S["visit"] = self.visit_block(cur) if not self.areas else ""
        if self.blog and self.posts:
            S["blog"] = (f'<section><div class="wrap"><div class="section-head"><span class="eyebrow">{esc(self.blog["nav_label"])}</span>'
                         f'<h2>{esc(self.blog.get("home_title","Latest articles"))}</h2></div>{self.post_cards(cur, self.posts[:3])}'
                         f'<p style="margin-top:24px"><a href="{self.href(cur,self.blog["index_slug"])}"><strong>All articles →</strong></a></p></div></section>')
        S["faq"] = f'<section><div class="wrap"><div class="section-head center"><span class="eyebrow">FAQ</span><h2>Common questions</h2></div>{self.faq_block(self.c["faqs"])}</div></section>'
        S["cta"] = self.cta_band(cur)
        order = h.get("order", ["trust", "tiers", "why", "steps", "services", "reviews", "quiz", "areas", "visit", "blog", "faq", "cta"])
        body = hero + "".join(S.get(k, "") for k in order)
        self.pages[cur] = self.page(cur, h["title"], h["meta"], body, [self.faq_schema(self.c["faqs"])])

    def visit_block(self, cur):
        b = self.b; a = b["address"]
        if not a.get("street"): return ""
        rows = "".join(f"<tr><td>{esc(d)}</td><td>{esc(t)}</td></tr>" for d, t in b.get("hours_table", []))
        maps = "https://www.google.com/maps/search/?api=1&query=" + re.sub(r"\s+", "+", f'{b["name"]} {a["street"]} {a["locality"]} {a["region"]}')
        return f'''<section class="bg-sand"><div class="wrap grid-2"><div><span class="eyebrow">Visit us</span><h2>{esc(self.L.get("visit_title","Come see us"))}</h2>
<p class="lead">{esc(a["street"])}, {esc(a["locality"])}, {a["region"]} {a.get("zip","")}</p><a class="btn btn-navy map-link" href="{maps}">Get directions</a></div>
<div class="aside" style="position:static"><h3>Hours</h3><table class="hours-table">{rows}</table></div></div></section>'''

    def tiers_page(self):
        T = self.tiers; cur = T["slug"]; trail = self.trail((T["nav_label"], cur))
        pe = T.get("pricing_explainer")
        pricing = f'''<section class="bg-sand"><div class="wrap grid-2"><div><span class="eyebrow">Pricing</span><h2>{esc(pe["title"])}</h2>{pe["body_html"]}
<a class="btn btn-navy" href="{self.href(cur,"contact")}">{esc(self.L["cta_long"])}</a></div><div><h3>{esc(pe["factors_title"])}</h3><ul class="checklist">{"".join("<li>"+esc(f)+"</li>" for f in pe["factors"])}</ul></div></div></section>''' if pe else ""
        quiz = f'<section><div class="wrap"><div class="section-head center"><span class="eyebrow">{esc(T["quiz"]["eyebrow"])}</span><h2>{esc(T["quiz"]["title"])}</h2></div>{self.quiz(cur)}</div></section>' if T.get("quiz") else ""
        compare = f'<section class="bg-sand"><div class="wrap"><div class="section-head"><span class="eyebrow">Side by side</span><h2>Compare what\'s included</h2><p class="lead">{esc(T["compare_lead"])}</p></div>{self.compare_table()}</div></section>' if T.get("compare") else ""
        body = self.page_hero(cur, trail, T["h1"], esc(T["lead"])) + f'<section><div class="wrap"><div class="section-head center"><h2>{esc(T["home_title"])}</h2></div>{self.tier_cards(cur)}</div></section>{compare}{quiz}{pricing}' + \
            f'<section><div class="wrap"><div class="section-head center"><span class="eyebrow">FAQ</span><h2>{esc(T["nav_label"])} questions</h2></div>{self.faq_block(T["faqs"])}</div></section>{self.cta_band(cur)}'
        self.pages[cur] = self.page(cur, T["title"], T["meta"], body, [self.faq_schema(T["faqs"]), self.service_schema(T["nav_label"], T["meta"], cur)], trail)

    def services_hub(self):
        sh = self.c["services_hub"]; cur = sh["slug"]; trail = self.trail((sh["nav_label"], cur))
        extra = f'<section class="bg-sand"><div class="wrap"><div class="section-head center"><span class="eyebrow">{esc(self.tiers["nav_label"])}</span><h2>{esc(self.tiers["home_title"])}</h2></div>{self.tier_cards(cur)}</div></section>' if self.tiers else ""
        body = self.page_hero(cur, trail, sh["h1"], esc(sh["lead"])) + f'<section><div class="wrap"><div class="section-head"><h2>{esc(sh["home_title"])}</h2></div>{self.service_cards(cur)}</div></section>{extra}{self.cta_band(cur)}'
        self.pages[cur] = self.page(cur, sh["title"], sh["meta"], body, None, trail)

    def service_page(self, s):
        sh = self.c["services_hub"]; cur = self.svc_path(s); trail = self.trail((sh["nav_label"], sh["slug"]), (s["name"], cur))
        inc = "".join(f'<div class="inc"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in s["included"])
        signs = "".join(f"<li>{esc(x)}</li>" for x in s.get("signs", []))
        faq_html = f'<h2>Questions about {esc(s["name"].lower())}</h2>{self.faq_block(s["faqs"])}' if s.get("faqs") else ""
        where = ""
        if self.areas:
            near = " · ".join(f'<a href="{self.href(cur,a["slug"])}">{esc(a["city"])}</a>' for a in self.areas["pages"])
            where = f'<h2>Where we offer {esc(s["name"].lower())}</h2><p>{esc(self.areas["service_where_text"])} {near}.</p>'
        alt = f'<a class="btn btn-ghost" href="{self.href(cur,self.tiers["slug"])}">Compare {esc(self.tiers["nav_label"].lower())}</a>' if self.tiers else ""
        body = self.page_hero(cur, trail, esc(s["h1"]), esc(s["lead"])) + f'''
<section><div class="wrap layout-side"><div class="prose"><h2>{esc(s["included_title"])}</h2><div class="included">{inc}</div>
{f'<h2>{esc(s["signs_title"])}</h2><ul class="checklist">{signs}</ul>' if signs else ""}{faq_html}{where}</div>
<aside class="aside"><h3>{esc(self.L["aside_title"])}</h3><p>{esc(self.L["aside_text"])}</p><a class="phone" href="tel:{self.b["tel"]}">{self.b["phone"]}</a>
<a class="btn btn-gold" href="{self.href(cur,"contact")}">{esc(self.L["cta"])}</a>{alt}<p style="margin:12px 0 0;font-size:.85rem">{esc(self.L["aside_badges"])}</p></aside></div></section>
{self.related_posts_block(cur, "services", s["slug"]) if self.blog else ""}<section class="bg-sand"><div class="wrap"><div class="section-head"><span class="eyebrow">More</span><h2>Other ways we can help</h2></div>{self.service_cards(cur, exclude=s["slug"])}</div></section>{self.cta_band(cur)}'''
        sch = [self.service_schema(s["name"], s["meta"], cur)] + ([self.faq_schema(s["faqs"])] if s.get("faqs") else [])
        self.pages[cur] = self.page(cur, s["title"], s["meta"], body, sch, trail)

    def areas_hub(self):
        A = self.areas; cur = A["hub_slug"]; trail = self.trail((A["nav_label"], cur))
        body = self.page_hero(cur, trail, A["hub_h1"], esc(A["hub_lead"])) + f'<section><div class="wrap"><div class="section-head center"><h2>{esc(A["home_title"])}</h2></div>{self.area_block(cur)}</div></section>{self.cta_band(cur)}'
        self.pages[cur] = self.page(cur, A["hub_title"], A["hub_meta"], body, None, trail)

    def area_page(self, a):
        A = self.areas; cur = a["slug"]; R = self.b["address"]["region"]
        trail = self.trail((A["nav_label"], A["hub_slug"]), (f'{a["city"]}, {R}', cur))
        local = "".join(f'<div class="inc"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in a["local"])
        nearby = "".join(f'<li><a href="{self.href(cur,x["slug"])}">{esc(x["city"])}</a></li>' for x in A["pages"] if x is not a)
        faqs = a["faqs"] + [(q.format(city=a["city"]), ans.format(city=a["city"])) for q, ans in A.get("shared_faqs", [])]
        svc = "".join(f'<li><a href="{self.href(cur,self.svc_path(s))}">{esc(s["name"])} in {esc(a["city"])}</a></li>' for s in self.c["services"][:A.get("services_listed", 5)])
        tiers = f'<h2>{esc(self.tiers["nav_label"])} in {esc(a["city"])}</h2><p>{A["tiers_blurb_html"]} <a href="{self.href(cur,self.tiers["slug"])}">Compare →</a></p>' if self.tiers else ""
        f = lambda s: s.format(city=esc(a["city"]), region=R)
        body = self.page_hero(cur, trail, f(A["page_h1"]), esc(a["intro"])) + f'''
<section><div class="wrap layout-side"><div class="prose"><h2>{f(A["local_title"])}</h2><div class="included">{local}</div>{tiers}
<h2>Services in {esc(a["city"])}</h2><ul class="checklist">{svc}</ul><h2>{esc(a["city"])} FAQ</h2>{self.faq_block(faqs)}
<p style="color:var(--c-muted);font-size:.92rem">Serving {esc(a["city"])}, {esc(a["county"])} · ZIP codes {esc(a["zips"])}</p></div>
<aside class="aside"><h3>{f(A["aside_title"])}</h3><p>{esc(self.L["aside_text"])}</p><a class="phone" href="tel:{self.b["tel"]}">{self.b["phone"]}</a>
<a class="btn btn-gold" href="{self.href(cur,"contact")}">{esc(self.L["cta"])}</a><p style="margin:14px 0 6px;font-weight:700;color:#fff">Also serving</p><ul class="city-links" style="grid-template-columns:1fr">{nearby}</ul></aside></div></section>
{self.related_posts_block(cur, "areas", a["slug"], self.blog.get("area_related_title", "Tips for {city}").format(city=a["city"])) if self.blog else ""}{f'<section class="bg-sand"><div class="wrap"><div class="section-head center"><span class="eyebrow">Reviews</span><h2>What our neighbors say</h2></div>{self.reviews_block()}</div></section>' if self.c["reviews"] else ""}{self.cta_band(cur)}'''
        sch = [self.service_schema(f(A["page_title"]), a["intro"], cur, [a["city"]]), self.faq_schema(faqs)]
        self.pages[cur] = self.page(cur, f(A["page_title"]), f(A["page_meta"]), body, sch, trail)

    def resource_page(self):
        R = self.resource; cur = R["slug"]; trail = self.trail((R["nav_label"], cur))
        cards = "".join(f'<article class="month"><small>{esc(k)}</small><h3>{esc(t)}</h3><ul>{"".join("<li>"+esc(i)+"</li>" for i in items)}</ul></article>' for k, t, items in R["cards"])
        body = self.page_hero(cur, trail, R["h1"], esc(R["lead"]), sand=True) + f'''<section class="bg-sand" style="padding-top:40px"><div class="wrap"><h2 class="skip">{esc(R["nav_label"])}</h2><div class="cal">{cards}</div></div></section>
<section><div class="wrap"><div class="section-head center"><span class="eyebrow">FAQ</span><h2>{esc(R["faq_title"])}</h2></div>{self.faq_block(R["faqs"])}</div></section>{self.cta_band(cur, R["cta_title"], R["cta_text"])}'''
        sch = [self.faq_schema(R["faqs"]), {"@type": "Article", "headline": R["h1"], "author": {"@id": self.D + "/#business"}, "publisher": {"@id": self.D + "/#business"}, "dateModified": TODAY, "mainEntityOfPage": self.canon(cur)}]
        self.pages[cur] = self.page(cur, R["title"], R["meta"], body, sch, trail)


    # ---------- blog
    def post_path(self, p): return f'{self.blog["post_prefix"]}/{p["slug"]}'
    def post_link(self, cur):
        def link(u):
            if u.startswith(("http://", "https://", "mailto:", "tel:", "#")): return u
            if u.startswith("/assets/"): return self.asset(cur, u[len("/assets/"):])
            if u.startswith("/"): return self.href(cur, u.strip("/"))
            return u
        return link
    @staticmethod
    def nice_date(d):
        y, m, dd = d.split("-")
        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        return f"{months[int(m)-1]} {int(dd)}, {y}"
    def read_time(self, p): return max(1, round(p["words"] / 220))
    def post_cards(self, cur, posts, h="h3"):
        out = []
        for p in posts:
            img = f'<img class="post-thumb" src="{self.asset(cur,p["image"])}" alt="{esc(p.get("image_alt",""))}" loading="lazy">' if p.get("image") else ""
            out.append(f'<a class="card post-card" href="{self.href(cur,self.post_path(p))}">{img}<span class="kicker">{esc(p.get("category",""))}</span>'
                       f'<{h}>{esc(p["title"])}</{h}><p>{esc(p.get("description",""))}</p><span class="more">{self.nice_date(p["date"])} · {self.read_time(p)} min read</span></a>')
        return '<div class="grid-3">' + "".join(out) + "</div>"
    def related_posts_block(self, cur, key, val, title="Related articles"):
        rel = [p for p in self.posts if val in p.get(key, [])][:3]
        if not rel: return ""
        return (f'<section><div class="wrap"><div class="section-head"><span class="eyebrow">{esc(self.blog["nav_label"])}</span>'
                f'<h2>{esc(title)}</h2></div>{self.post_cards(cur, rel)}</div></section>')

    def blog_index(self):
        B = self.blog; cur = B["index_slug"]; trail = self.trail((B["nav_label"], cur))
        cats = sorted({p.get("category") for p in self.posts if p.get("category")})
        chips = "".join(f'<span class="chip">{esc(c)}</span>' for c in cats)
        chips_html = f'<div class="chips">{chips}</div>' if chips else ""
        listing = self.post_cards(cur, self.posts) if self.posts else "<p>New articles are on the way.</p>"
        body = (self.page_hero(cur, trail, B["h1"], esc(B["lead"]), ctas=False) +
                f'<section><div class="wrap"><div class="section-head"><h2>{esc(B.get("list_title","Latest articles"))}</h2>{chips_html}</div>{listing}</div></section>' +
                self.cta_band(cur))
        sch = [{"@type": "Blog", "@id": self.canon(cur) + "#blog", "name": B["title"], "url": self.canon(cur), "publisher": {"@id": self.D + "/#business"},
                "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": self.canon(self.post_path(p)), "datePublished": p["date"]} for p in self.posts]}]
        self.pages[cur] = self.page(cur, B["title"], B["meta"], body, sch, trail)

    def post_page(self, p):
        B = self.blog; cur = self.post_path(p); trail = self.trail((B["nav_label"], B["index_slug"]), (p["title"], cur))
        author = p.get("author") or B.get("default_author") or self.b["name"]
        upd = f' · Updated {self.nice_date(p["updated"])}' if p.get("updated") else ""
        meta_line = f'<p class="post-meta">By {esc(author)} · {self.nice_date(p["date"])}{upd} · {self.read_time(p)} min read</p>'
        hero_img = f'<img class="post-hero-img" src="{self.asset(cur,p["image"])}" alt="{esc(p.get("image_alt",""))}" width="1200" height="630">' if p.get("image") else ""
        body_html = markdown(p["body_md"], self.post_link(cur))
        svc = [s for s in self.c["services"] if s["slug"] in p["services"]]
        svc_links = "".join(f'<li><a href="{self.href(cur,self.svc_path(s))}">{esc(s["name"])}</a></li>' for s in svc)
        area_links = ""
        if self.areas and p["areas"]:
            area_links = "".join(f'<li><a href="{self.href(cur,a["slug"])}">{esc(a["city"])}, {self.b["address"]["region"]}</a></li>'
                                 for a in self.areas["pages"] if a["slug"] in p["areas"])
        aside_links = ""
        if svc_links: aside_links += f'<p class="aside-label">Related services</p><ul class="city-links" style="grid-template-columns:1fr">{svc_links}</ul>'
        if area_links: aside_links += f'<p class="aside-label">Areas we serve</p><ul class="city-links" style="grid-template-columns:1fr">{area_links}</ul>'
        others = [o for o in self.posts if o is not p]
        rel = sorted(others, key=lambda o: (len(set(o["services"]) & set(p["services"])) + (o.get("category") == p.get("category")), o["date"]), reverse=True)[:3]
        rel_html = ""
        if rel:
            rel_html = (f'<section class="bg-sand"><div class="wrap"><div class="section-head"><span class="eyebrow">Keep reading</span>'
                        f'<h2>More from the {esc(B["nav_label"].lower())}</h2></div>{self.post_cards(cur, rel)}</div></section>')
        bc = " / ".join(f'<a href="{self.href(cur,pp)}">{esc(n)}</a>' for n, pp in trail[:-1])
        body = (f'<section class="hero page-hero on-dark">{self.texture()}<div class="wrap"><div><nav class="crumbs" aria-label="Breadcrumb">{bc}</nav>'
                f'<span class="eyebrow">{esc(p.get("category", B["nav_label"]))}</span><h1>{esc(p["title"])}</h1>'
                f'<p class="lead">{esc(p.get("description",""))}</p>{meta_line}</div></div>{self.divider()}</section>'
                f'<section><div class="wrap layout-side"><article class="prose post-body">{hero_img}{body_html}</article>'
                f'<aside class="aside"><h2 class="h3">{esc(self.L["aside_title"])}</h2><p>{esc(self.L["aside_text"])}</p>'
                f'<a class="phone" href="tel:{self.b["tel"]}">{self.b["phone"]}</a>'
                f'<a class="btn btn-gold" href="{self.href(cur,"contact")}">{esc(self.L["cta"])}</a>{aside_links}</aside></div></section>'
                f'{rel_html}{self.cta_band(cur)}')
        is_person = author != self.b["name"] and author != self.b["legal_name"]
        bp = {"@type": "BlogPosting", "@id": self.canon(cur) + "#article", "headline": p["title"][:110], "description": p.get("description", ""),
              "datePublished": p["date"], "dateModified": p.get("updated") or p["date"], "mainEntityOfPage": self.canon(cur),
              "author": ({"@type": "Person", "name": author, "worksFor": {"@id": self.D + "/#business"}} if is_person else {"@id": self.D + "/#business"}),
              "publisher": {"@id": self.D + "/#business"}, "wordCount": p["words"], "inLanguage": "en-US"}
        if p.get("category"): bp["articleSection"] = p["category"]
        if p.get("image"): bp["image"] = f'{self.D}/assets/{p["image"]}'
        if svc: bp["about"] = [{"@type": "Service", "name": s["name"], "url": self.canon(self.svc_path(s))} for s in svc]
        self.pages[cur] = self.page(cur, p.get("seo_title") or p["title"], p.get("description", ""), body, [bp], trail,
                                    og_override=p.get("image"), og_type="article")

    def rss(self):
        B = self.blog
        items = "".join(f'<item><title>{esc(p["title"])}</title><link>{self.canon(self.post_path(p))}</link><guid>{self.canon(self.post_path(p))}</guid>'
                        f'<description>{esc(p.get("description",""))}</description></item>' for p in self.posts[:20])
        return (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{esc(B["title"])}</title>'
                f'<link>{self.canon(B["index_slug"])}</link><description>{esc(B["meta"])}</description>{items}</channel></rss>')

    def about_page(self):
        A = self.c["about"]; cur = "about"; trail = self.trail(("About", cur))
        body = self.page_hero(cur, trail, A["h1"], esc(A["lead"])) + f'''<section><div class="wrap grid-2"><div class="prose"><span class="eyebrow">Our story</span><h2>{esc(A["story_title"])}</h2>{A["story_html"]}</div>
<div><h3>{esc(A["list_title"])}</h3><ul class="checklist">{"".join("<li>"+esc(x)+"</li>" for x in A["list"])}</ul></div></div></section>
{f'<section class="bg-sand"><div class="wrap"><div class="section-head center"><span class="eyebrow">Reviews</span><h2>What our customers say</h2></div>{self.reviews_block()}</div></section>' if self.c["reviews"] else ""}{self.cta_band(cur)}'''
        self.pages[cur] = self.page(cur, A["title"], A["meta"], body, None, trail)

    def contact_page(self):
        C = self.c["contact"]; cur = "contact"; trail = self.trail((self.L["cta"], cur)); b = self.b
        fid = self.c.get("integrations", {}).get("ghl_form_id")
        if fid:
            form = f'<div class="form-card"><iframe src="https://api.leadconnectorhq.com/widget/form/{fid}" style="width:100%;height:{C.get("ghl_height",760)}px;border:none;border-radius:4px" id="inline-{fid}" data-layout="{{\'id\':\'INLINE\'}}" data-form-id="{fid}" title="{esc(self.L["cta"])}"></iframe><script src="https://link.msgsndr.com/js/form_embed.js"></script></div>'
        else:
            selects = ""
            for i, (lbl, opts) in enumerate(C["selects"]):
                selects += f'<div class="full"><label for="f-s{i}">{esc(lbl)}</label><select id="f-s{i}" name="s{i}">' + "".join(f"<option>{esc(o)}</option>" for o in opts) + "</select></div>"
            if self.areas:
                selects = '<div class="full"><label for="f-city">City</label><select id="f-city" name="city">' + "".join(f"<option>{esc(a['city'])}</option>" for a in self.areas["pages"]) + "<option>Other / not sure</option></select></div>" + selects
            if self.tiers:
                selects += '<div class="full"><label for="f-plan">Interested in</label><select id="f-plan" name="plan"><option value="">Not sure yet</option>' + "".join(f'<option value="{t["slug"]}">{esc(t["name"])}</option>' for t in self.tiers["items"]) + "</select></div>"
            form = f'''<form class="form-card" data-demo><!-- DEMO FORM: set integrations.ghl_form_id to replace with the GoHighLevel form -->
<div class="form-grid"><div><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
<div><label for="f-phone">Mobile phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
<div class="full"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div>{selects}
<div class="full"><label for="f-msg">{esc(C["message_label"])}</label><textarea id="f-msg" name="message" rows="4"></textarea></div></div>
<button class="btn btn-gold" type="submit" style="width:100%;margin-top:16px">{esc(C["submit"])}</button><p class="form-note">{esc(C["note"])}</p>
<div class="form-msg" role="status">Preview only: this form will submit into your GoHighLevel pipeline once the GHL form is connected.</div></form>'''
        nxt = "".join(f"<li>{esc(x)}</li>" for x in C["next_steps"])
        body = self.page_hero(cur, trail, C["h1"], esc(C["lead"]), ctas=False, sand=True) + f'''<section class="bg-sand" style="padding-top:40px"><div class="wrap layout-side"><div>{form}</div>
<aside class="aside"><h2 class="h3">{esc(self.L["phone_prefix"])}</h2><a class="phone" href="tel:{b["tel"]}">{b["phone"]}</a><p>{esc(b["hours_text"])}</p>
<h2 class="h3" style="margin-top:20px">What happens next</h2><ul class="checklist" style="color:rgba(255,255,255,.86)">{nxt}</ul></aside></div></section>'''
        self.pages[cur] = self.page(cur, C["title"], C["meta"], body, None, trail)

    def legal_pages(self):
        for slug, name in self.c.get("legal_pages", []):
            self.pages[slug] = self.page(slug, name, f'{name} for {self.b["legal_name"]}.',
                self.page_hero(slug, self.trail((name, slug)), esc(name), "", ctas=False) +
                f'<section><div class="wrap prose"><!-- TODO before launch: paste {name} text --><p>[Paste the {esc(name)} text here before launch.]</p></div></section>')

    # ============================================================== write
    def build(self):
        self.home(); self.services_hub(); self.about_page(); self.contact_page(); self.legal_pages()
        for s in self.c["services"]: self.service_page(s)
        if self.tiers: self.tiers_page()
        if self.areas:
            self.areas_hub()
            for a in self.areas["pages"]: self.area_page(a)
        if self.resource: self.resource_page()
        if self.blog:
            self.blog_index()
            for p in self.posts: self.post_page(p)
        if os.path.exists(self.out): shutil.rmtree(self.out)
        for path, h in self.pages.items():
            d = os.path.join(self.out, path); os.makedirs(d, exist_ok=True)
            open(os.path.join(d, "index.html"), "w").write(h)
        A = os.path.join(self.out, "assets"); os.makedirs(os.path.join(A, "fonts"))
        for f in ("site.css", "site.js"): shutil.copy(os.path.join(ROOT, "core", f), A)
        for f in {self.c["theme"]["fonts"]["display"], self.c["theme"]["fonts"]["body"]}: shutil.copy(os.path.join(ROOT, "core", "fonts", f + ".woff2"), os.path.join(A, "fonts"))
        open(os.path.join(A, "theme.css"), "w").write(self.theme_css())
        if self.c["logo"]["type"] == "svg":
            open(os.path.join(A, "logo.svg"), "w").write(self.c["logo"]["svg"].replace("<svg ", f'<svg xmlns="http://www.w3.org/2000/svg" style="background:{self.c["theme"]["colors"]["primary"]}" ', 1))
        open(os.path.join(A, "favicon.svg"), "w").write(self.c.get("favicon_svg") or
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="{self.c["theme"]["colors"]["primary"]}"/><text x="16" y="22" text-anchor="middle" font-family="sans-serif" font-weight="700" font-size="16" fill="#fff">{esc(self.b["name"][0])}</text></svg>')
        if not os.path.exists(os.path.join(self.client_assets, self.c.get("og_image", "og-image.jpg"))): self.make_og(os.path.join(A, "og-image.jpg"))
        if os.path.isdir(self.client_assets): shutil.copytree(self.client_assets, A, dirs_exist_ok=True)
        if not self.preview:
            self.pages_404()
            post_dates = {self.post_path(p): (p.get("updated") or p["date"]) for p in self.posts} if self.blog else {}
            urls = "".join(f"<url><loc>{self.canon(p)}</loc><lastmod>{post_dates.get(p, TODAY)}</lastmod></url>" for p in self.pages if p != "404")
            if self.blog and self.posts:
                open(os.path.join(self.out, self.blog["index_slug"], "rss.xml"), "w").write(self.rss())
            open(os.path.join(self.out, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
            open(os.path.join(self.out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {self.D}/sitemap.xml\n")
            open(os.path.join(self.out, "_redirects"), "w").write("".join(f"{a}  {b}  301\n" for a, b in self.c.get("redirects", [])))
        print(f"[{self.client}] built {len(self.pages)} pages -> {os.path.relpath(self.out, ROOT)}/")

    def make_og(self, path):
        """Branded 1200x630 social share image (used when the client has no og-image.jpg of their own)."""
        try:
            from PIL import Image, ImageDraw, ImageFont
        except ImportError:
            print("  (pip install pillow to auto-generate og-image.jpg)"); return
        col = self.c["theme"]["colors"]; hx = lambda h: tuple(int(h.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        im = Image.new("RGB", (1200, 630), hx(col["primary"])); d = ImageDraw.Draw(im)
        d.rectangle([0, 600, 1200, 630], fill=hx(col["accent"])); d.rectangle([80, 120, 200, 128], fill=hx(col["secondary"]))
        font = lambda f, sz: ImageFont.truetype(os.path.join(ROOT, "core", "fonts", f + ".woff2"), sz) if False else None
        def load(sz, bold=True):
            for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "DejaVuSans.ttf"]:
                try: return ImageFont.truetype(p, sz)
                except OSError: pass
            return ImageFont.load_default()
        d.text((80, 160), self.b["name"], font=load(72), fill=(255, 255, 255))
        import textwrap
        y = 270
        for line in textwrap.wrap(re.sub("<[^>]+>", "", self.c["home"]["title"]), 40)[:3]:
            d.text((80, y), line, font=load(40, False), fill=hx(col["secondary_wash"])); y += 56
        d.text((80, 500), f'{self.b["phone"]}  ·  {self.b["domain"].split("//")[-1]}', font=load(34), fill=hx(col["accent"]))
        im.save(path, quality=88)

    def pages_404(self):
        h = self.page("404", "Page not found", "Page not found.", self.page_hero("404", self.trail(("Not found", "404")), "That page isn't here", "It may have moved. Try the menu above or give us a call."), noindex=True)
        open(os.path.join(self.out, "404.html"), "w").write(h)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    clients = sorted(d for d in os.listdir(os.path.join(ROOT, "clients")) if not d.startswith("_") and os.path.exists(os.path.join(ROOT, "clients", d, "site.py")))
    if "--list" in sys.argv or not args:
        print("Clients:", ", ".join(clients) or "(none)"); print("Usage: python3 build.py <client|--all> [--preview]"); sys.exit(0)
    targets = clients if args[0] == "all" else args
    for c in targets: Site(c, "--preview" in sys.argv).build()
