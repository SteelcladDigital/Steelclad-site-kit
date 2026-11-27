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
 "mail":'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "cake":'<path d="M4 21h16M5 21v-7a2 2 0 012-2h10a2 2 0 012 2v7"/><path d="M5 16c2 1.5 4.5 1.5 7 0s5-1.5 7 0M12 12V8"/><path d="M12 3c1 1.2 1 2.6 0 3.5-1-.9-1-2.3 0-3.5z"/>',
 "cookie":'<circle cx="12" cy="12" r="9"/><circle cx="9" cy="9" r="1" fill="currentColor"/><circle cx="15" cy="10" r="1" fill="currentColor"/><circle cx="10" cy="15" r="1" fill="currentColor"/><circle cx="15.5" cy="15" r="1" fill="currentColor"/>',
 "cupcake":'<path d="M6 12h12l-1.5 9h-9z"/><path d="M6 12a3 3 0 01.5-5.5A4 4 0 0112 4a4 4 0 015.5 2.5A3 3 0 0118 12"/><path d="M10 12l.5 9M14 12l-.5 9"/>',
 "gift":'<rect x="3" y="9" width="18" height="12" rx="1"/><path d="M3 13h18M12 9v12M12 9c-2-4-6-4-6-1.5S9 9 12 9zm0 0c2-4 6-4 6-1.5S15 9 12 9z"/>',
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
        # business.phone is optional: email/form-only businesses (e.g. home bakers) get email links wherever a phone link would go
        self.has_phone = bool(self.b.get("phone"))
        self.rh = f'tel:{self.b["tel"]}' if self.has_phone else f'mailto:{self.b.get("email", "")}'
        self.rt = self.b["phone"] if self.has_phone else self.b.get("email", "")
        self.reach_verb = self.L.get("reach_verb", "Call or text" if self.has_phone else "Email")
        self.cta = self.c["contact"].get("slug", "contact"); self.noindex = set()   # every CTA button points at the primary lead page
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
    def rel_links(self, cur, html_):
        """Site-relative links written in config HTML (href="/pricing/") work in both preview and live builds."""
        return re.sub(r'href="/(?!/)([^"#?]*)', lambda m: 'href="' + self.href(cur, m.group(1).strip("/")), html_)
    def alt_btn(self, cur, label=True):
        """Secondary button beside the main CTA: the phone number, or (no phone) labels.alt_cta = (label, slug), else the email."""
        if self.has_phone:
            return f'<a class="btn btn-ghost" href="{self.rh}">{(esc(self.L["phone_prefix"]) + " ") if label else ""}{self.rt}</a>'
        if self.L.get("alt_cta") and self.L["alt_cta"][1] == cur:
            return ""   # never link a page to itself
        if self.L.get("alt_cta"):
            return f'<a class="btn btn-ghost" href="{self.href(cur, self.L["alt_cta"][1])}">{esc(self.L["alt_cta"][0])}</a>'
        return f'<a class="btn btn-ghost" href="{self.rh}">{esc(self.rt)}</a>'
    def canon(self, path): return self.D + "/" + (path + "/" if path else "")

    # ---------- theme
    def theme_css(self):
        t = self.c["theme"]; col = t["colors"]
        disp, body = t["fonts"]["display"], t["fonts"]["body"]
        for f in (disp, body):
            if f not in FONT_FILES: raise SystemExit(f"Font '{f}' not in core/fonts. Options: {sorted(FONT_FILES)}")
        radius = {"sharp": ("4px", "6px"), "soft": ("14px", "999px"), "round": ("22px", "999px")}[t.get("radius", "soft")]
        tex = TEXTURES.get(t.get("texture", "ripples"))
        sec = col.get("texture", col["secondary"]).replace("#", "%23")   # colors.texture: optional line color for the hero texture
        tex_css = f"url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240' viewBox='0 0 240 240'%3E%3Cpath d='{tex}' fill='none' stroke='{sec}' stroke-width='2'/%3E%3C/svg%3E\")" if tex else "none"
        dark = col.get("accent_text", "#121c35").replace("#", "%23")
        faces = "".join(f'@font-face{{font-family:"{FONT_FAMILY[f]}";src:url(fonts/{f}.woff2) format("woff2");font-weight:100 900;font-display:swap}}\n' for f in sorted({disp, body}))
        return faces + f''':root{{
--c-primary:{col["primary"]};--c-primary-deep:{col["primary_deep"]};--c-secondary:{col["secondary"]};--c-secondary-deep:{col["secondary_deep"]};
--c-secondary-wash:{col["secondary_wash"]};--c-accent:{col["accent"]};--c-highlight:{col.get("highlight", col["accent"])};--c-accent-text:{col.get("accent_text","#121c35")};
--c-surface:{col["surface"]};--c-ink:{col.get("ink","#16213a")};--c-muted:{col.get("muted","#4a5674")};--c-line:#dfe3ea;--c-white:#fff;
--radius:{radius[0]};--btn-radius:{radius[1]};--shadow:0 10px 30px rgba(18,28,53,.12);
--display:"{FONT_FAMILY[disp]}",system-ui,sans-serif;--body:"{FONT_FAMILY[body]}",system-ui,-apple-system,"Segoe UI",sans-serif;
--heading-case:{t.get("heading_case","none")};--wrap:1180px;--texture:{tex_css};
--chk-white:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M4 8.5l2.5 2.5L12 5.5' fill='none' stroke='white' stroke-width='2'/%3E%3C/svg%3E");
--chk-dark:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M4 8.5l2.5 2.5L12 5.5' fill='none' stroke='{dark}' stroke-width='2'/%3E%3C/svg%3E");
}}
'''

    # ---------- logo
    def logo(self, cur, where="header"):
        lg = self.c["logo"]
        if lg["type"] == "svg": return lg.get("footer_svg", lg["svg"]) if where == "footer" else lg["svg"]
        # logo.footer_file: a version for the dark footer (e.g. full-color logo on a light header + a knockout in the footer)
        if lg["type"] == "image": return f'<img src="{self.asset(cur, lg.get("footer_file", lg["file"]) if where == "footer" else lg["file"])}" alt="{esc(self.b["name"])}" width="{lg.get("width",160)}" height="{lg.get("height",58)}">'
        return '<span class="logo-text">' + "<br>".join(esc(x) for x in lg["lines"]) + "</span>"

    # ---------- schema
    def business_schema(self):
        b = self.b
        addr = {"@type": "PostalAddress", "addressLocality": b["address"]["locality"], "addressRegion": b["address"]["region"], "addressCountry": "US"}
        if b["address"].get("street"): addr["streetAddress"] = b["address"]["street"]
        if b["address"].get("zip"): addr["postalCode"] = b["address"]["zip"]
        s = {"@type": b["schema_type"], "@id": self.D + "/#business", "name": b["legal_name"], "alternateName": b["name"],
             "url": self.D + "/", **({"telephone": b["tel"]} if b.get("tel") else {}), "description": b["description"], "address": addr,
             **({"openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": d, "opens": o, "closes": c} for d, o, c in b["hours"]]} if b.get("hours") else {}),
             "sameAs": [u for u in b.get("social", {}).values() if u]}
        logo = self.c["logo"].get("schema_file") or self.c["logo"].get("file") or "logo.svg"   # schema_file: a version for light backgrounds (Google shows logos on white)
        s["logo"] = s["image"] = self.D + "/assets/" + logo
        if b.get("geo"): s["geo"] = {"@type": "GeoCoordinates", "latitude": b["geo"][0], "longitude": b["geo"][1]}
        if b.get("price_range"): s["priceRange"] = b["price_range"]
        if b.get("email"): s["email"] = b["email"]
        if b.get("legal_entity"): s["legalName"] = b["legal_entity"]
        if b.get("founder"): s["founder"] = {"@type": "Person", "name": b["founder"]}
        if b.get("slogan"): s["slogan"] = b["slogan"]
        if b.get("knows_about"): s["knowsAbout"] = b["knows_about"]
        served = [{"@type": "AdministrativeArea", "name": x} for x in b.get("counties", [])]
        if self.areas: served += [{"@type": "City", "name": f'{a["city"]}, {b["address"]["region"]}'} for a in self.areas["pages"]]
        if self.areas: served += [{"@type": "City", "name": f'{t}, {b["address"]["region"]}'} for g in self.areas["groups"] for t in g.get("also", [])]
        if served: s["areaServed"] = served
        if self.tiers:
            s["hasOfferCatalog"] = {"@type": "OfferCatalog", "name": self.tiers["nav_label"], "itemListElement": [
                self.tier_offer(t) for t in self.tiers["items"]]}
        return s
    def tier_offer(self, t):
        o = {"@type": "Offer", "itemOffered": {"@type": "Service", "name": t["name"], "description": t["for"]}}
        if t.get("price_amount"):   # numeric price, e.g. "497": adds price + monthly unit to the structured data
            o.update({"price": t["price_amount"], "priceCurrency": t.get("currency", "USD"),
                      "priceSpecification": {"@type": "UnitPriceSpecification", "price": t["price_amount"], "priceCurrency": t.get("currency", "USD"),
                                             "unitText": t.get("price_unit", "MONTH"), "referenceQuantity": {"@type": "QuantitativeValue", "value": 1, "unitCode": "MON"}}})
        return o
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
        # .dd-all: hub link shown only in the mobile accordion (on phones, tapping the parent opens the list instead of navigating)
        items.append(f'<li><a class="nl" href="{self.href(cur,sh["slug"])}"{ca(sh["slug"])}>{esc(sh["nav_label"])} ▾</a><ul class="dropdown"><li class="dd-all"><a href="{self.href(cur,sh["slug"])}">{esc(sh["nav_label"])} overview →</a></li>{svc}</ul></li>')
        if self.areas:
            dd = ""
            for g in self.areas["groups"]:
                dd += f'<li class="sep">{esc(g["name"])}</li>' + "".join(f'<li><a href="{self.href(cur,a["slug"])}">{esc(a["city"])}</a></li>' for a in self.areas["pages"] if a["slug"] in g["slugs"])
            items.append(f'<li><a class="nl" href="{self.href(cur,self.areas["hub_slug"])}"{ca(self.areas["hub_slug"])}>{esc(self.areas["nav_label"])} ▾</a><ul class="dropdown"><li class="dd-all"><a href="{self.href(cur,self.areas["hub_slug"])}">{esc(self.areas["nav_label"])} overview →</a></li>{dd}</ul></li>')
        G = self.c.get("gallery_page")
        if G and G.get("in_nav", True): items.append(f'<li><a class="nl" href="{self.href(cur,G["slug"])}"{ca(G["slug"])}>{esc(G["nav_label"])}</a></li>')
        if self.resource: items.append(f'<li><a class="nl" href="{self.href(cur,self.resource["slug"])}"{ca(self.resource["slug"])}>{esc(self.resource["nav_label"])}</a></li>')
        if self.blog: items.append(f'<li><a class="nl" href="{self.href(cur,self.blog["index_slug"])}"{ca(self.blog["index_slug"])}>{esc(self.blog["nav_label"])}</a></li>')
        items.append(f'<li><a class="nl" href="{self.href(cur,"about")}"{ca("about")}>About</a></li>')
        promise = f'<span class="promise"><span class="dot"></span><span>{esc(L["topbar_promise"])}</span></span>' if L.get("topbar_promise") else "<span></span>"
        return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">{promise}<span><span class="hide-sm">{esc(b["hours_text"])} · </span><a href="{self.rh}">{esc(L["phone_prefix"])} {esc(self.rt)}</a></span></div></div>
<header class="site-header"><div class="wrap">
<a class="logo" href="{self.href(cur,"")}" aria-label="{esc(b["name"])} home">{self.logo(cur)}</a>
<nav class="nav" id="nav" aria-label="Main"><ul>{"".join(items)}</ul></nav>
<div class="header-cta"><a class="btn btn-gold" href="{self.href(cur,self.cta)}">{esc(L["cta"])}</a>
<button class="menu-toggle" aria-label="Open menu" aria-controls="nav" aria-expanded="false">{icon("menu")}</button></div>
</div></header>'''

    def footer(self, cur):
        b, L = self.b, self.L
        svc = "".join(f'<li><a href="{self.href(cur,self.svc_path(s))}">{esc(s["name"])}</a></li>' for s in self.c["services"])
        if self.tiers: svc = f'<li><a href="{self.href(cur,self.tiers["slug"])}">{esc(self.tiers["nav_label"])}</a></li>' + svc
        col3 = ""
        if self.areas:
            # Footer service areas are ALWAYS compact (Steelclad standard, Nov 2026): a few plain town names + "All service areas",
            # never a "<Service> <City>, ST" link for every city page (reads as keyword stuffing).
            # areas.footer_slugs picks the towns (default: the first footer_count pages, 5); areas.footer_note adds one line under them.
            # areas.footer "compact" shows the towns as one wrapping line (optional footer_lead above it) instead of a short list.
            A = self.areas; names = {a["slug"]: a["city"] for a in A["pages"]}
            fs = A.get("footer_slugs") or [a["slug"] for a in A["pages"]][:A.get("footer_count", 5)]
            bad = [sl for sl in fs if sl not in names]
            if bad: sys.exit(f"[{self.client}] areas.footer_slugs has slug(s) with no area page: {', '.join(bad)}")
            allx = f'<a class="footer-areas-all" href="{self.href(cur,A["hub_slug"])}">All service areas →</a>'
            note = f'<p style="margin-top:10px;font-size:.88rem;opacity:.8">{esc(A["footer_note"])}</p>' if A.get("footer_note") else ""
            if A.get("footer") == "compact":   # each town keeps its trailing dot on the same line, so no line starts with "·"
                towns = " ".join(f'<span class="fa-item"><a href="{self.href(cur,sl)}">{esc(names[sl])}</a>{"<span aria-hidden=" + chr(34) + "true" + chr(34) + "> ·</span>" if i < len(fs) - 1 else ""}</span>' for i, sl in enumerate(fs))
                lead = f'<p class="footer-areas-lead">{esc(A["footer_lead"])}</p>' if A.get("footer_lead") else ""
                col3 = f'<div><h4>Service Areas</h4>{lead}<p class="footer-areas">{towns}</p><p>{allx}</p>{note}</div>'
            else:
                col3 = ('<div><h4>Service Areas</h4><ul>' + "".join(f'<li><a href="{self.href(cur,sl)}">{esc(names[sl])}</a></li>' for sl in fs)
                        + f'<li>{allx}</li></ul>{note}</div>')
        else:
            addr = b["address"]; street = f'{esc(addr["street"])}<br>' if addr.get("street") else ""
            col3 = f'<div><h4>Visit</h4><p>{street}{esc(addr["locality"])}, {addr["region"]} {addr.get("zip","")}</p><p>{esc(b["hours_text"])}</p></div>'
        social = "".join(f'<a href="{u}" aria-label="{k.title()}">{icon("fb" if k=="facebook" else "ig")}</a>' for k, u in b.get("social", {}).items() if u and k in ("facebook", "instagram"))
        company = [("about", "About Us"), (self.cta, L["cta"])]
        if self.resource: company.insert(1, (self.resource["slug"], self.resource["nav_label"]))
        if self.c.get("gallery_page"): company.insert(1, (self.c["gallery_page"]["slug"], self.c["gallery_page"]["nav_label"]))
        if self.blog: company.insert(1, (self.blog["index_slug"], self.blog["nav_label"]))
        comp = "".join(f'<li><a href="{self.href(cur,p)}">{esc(n)}</a></li>' for p, n in company)
        wr = self.c.get("integrations", {}).get("google_review_write_url")
        if wr: comp += f'<li><a href="{wr}" rel="noopener" target="_blank">Leave a Google Review</a></li>'
        legal = " · ".join(f'<a href="{self.href(cur,s)}">{esc(n)}</a>' for s, n in self.c.get("legal_pages", []))
        return f'''<footer class="site-footer"><div class="wrap"><div class="cols">
<div><a class="logo" href="{self.href(cur,"")}">{self.logo(cur, "footer")}</a><p style="margin-top:16px">{esc(L["footer_blurb"])}</p>
<p><a href="{self.rh}"><strong>{esc(self.rt)}</strong></a><br>{esc(b["hours_text"])}</p><div class="social">{social}</div></div>
<div><h4>{esc(L.get("footer_services_title","Services"))}</h4><ul>{svc}</ul></div>{col3}
<div><h4>Company</h4><ul>{comp}</ul></div>
</div><div class="legal"><span>© {date.today().year} {esc(b["legal_name"])}. All rights reserved.</span><span>{legal}</span></div></div></footer>
<nav class="mbar" aria-label="Quick actions"><a href="{self.rh}">{icon("phone" if self.has_phone else "mail")}{"Call" if self.has_phone else "Email"}</a><a href="{L.get("mbar_second_href") or (self.href(cur, L["mbar_second_slug"]) if L.get("mbar_second_slug") else ("sms:" + b["tel"] if self.has_phone else self.href(cur, self.c["services_hub"]["slug"])))}">{icon(L.get("mbar_second_icon","chat"))}{esc(L.get("mbar_second_label","Text"))}</a><a class="go" href="{self.href(cur,self.cta)}">{icon("calendar")}{esc(L["cta_short"])}</a></nav>'''

    def page(self, cur, title, meta, body, schema=None, trail=None, noindex=False, og_override=None, og_type="website"):
        brand = self.b["name"]; base = title.split(" | ")[0]
        title = f"{base} | {brand}" if len(base) + 3 + len(brand) <= 60 else base   # keep the full <title> within 60 chars
        if noindex: self.noindex.add(cur)
        ig = self.c.get("integrations", {})
        graph = [self.business_schema(), {"@type": "WebPage", "@id": self.canon(cur) + "#webpage", "url": self.canon(cur), "name": title, "description": meta,
                 "isPartOf": {"@type": "WebSite", "@id": self.D + "/#website", "url": self.D + "/", "name": brand}, "about": {"@id": self.D + "/#business"}, "dateModified": TODAY}]
        if trail: graph.append(self.crumbs_schema(trail))
        graph += schema or []
        ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
        gtm = f"<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{ig['gtm_id']}');</script>" if ig.get("gtm_id") else "<!-- GTM: set integrations.gtm_id -->"
        chat = f'<script src="https://widgets.leadconnectorhq.com/loader.js" data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" data-widget-id="{ig["ghl_chat_widget_id"]}"></script>' if ig.get("ghl_chat_widget_id") else "<!-- GHL chat: set integrations.ghl_chat_widget_id -->"
        if ig.get("chat_snippet") and not self.preview: chat = "\n" + ig["chat_snippet"].strip()   # any other chat widget (e.g. tawk.to), live build only
        snip = ig.get("ghl_tracking_snippet", "").strip()
        track = ("\n" + snip) if snip and not self.preview else "<!-- GHL external tracking: set integrations.ghl_tracking_snippet -->"
        if ig.get("form_mode") == "web3forms":   # GHL-free site: no GHL placeholders in the HTML
            if not ig.get("ghl_chat_widget_id") and not ig.get("chat_snippet"): chat = ""
            if not snip: track = ""
        fonts = sorted({self.c["theme"]["fonts"]["display"], self.c["theme"]["fonts"]["body"]})
        pre = "".join(f'<link rel="preload" href="{self.asset(cur,"fonts/"+f+".woff2")}" as="font" type="font/woff2" crossorigin>' for f in fonts)
        og = og_override or self.c.get("og_image", "og-image.jpg")
        rss = f'<link rel="alternate" type="application/rss+xml" title="{esc(brand)}" href="{self.D}/{self.blog["index_slug"]}/rss.xml">' if self.blog and self.posts else ""
        return f'''<!DOCTYPE html>
<html lang="en-US"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(meta)}">
<link rel="canonical" href="{self.canon(cur)}"><meta name="robots" content="{'noindex' if noindex else ('index, follow, max-image-preview:large' if self.c.get("launched") else 'noindex, nofollow')}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{esc(brand)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(meta)}">
<meta property="og:url" content="{self.canon(cur)}"><meta property="og:image" content="{self.D}/assets/{og}"><meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="US-{self.b["address"]["region"]}"><meta name="geo.placename" content="{esc(self.b["address"]["locality"])}">
<meta name="theme-color" content="{self.c["theme"]["colors"]["primary"]}"><link rel="icon" href="{self.asset(cur,"favicon.svg")}" type="image/svg+xml">{f'<link rel="apple-touch-icon" href="{self.asset(cur,"apple-touch-icon.png")}">' if os.path.exists(os.path.join(self.client_assets, "apple-touch-icon.png")) else ""}
{pre}<link rel="stylesheet" href="{self.asset(cur,"theme.css")}"><link rel="stylesheet" href="{self.asset(cur,"site.css")}">
<script type="application/ld+json">{ld}</script>{gtm}{rss}
</head><body{' class="hdr-light"' if self.c["theme"].get("header") == "light" else ""}>
{self.header(cur)}
<main id="main">
{body}
</main>
{self.footer(cur)}
<script src="{self.asset(cur,"site.js")}" defer></script>{chat}{track}
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
        btns = f'<div class="btn-row" style="margin-top:22px"><a class="btn btn-gold" href="{self.href(cur,self.cta)}">{esc(self.L["cta_long"])}</a>{self.alt_btn(cur)}</div>' if ctas else ""
        lead_html = f'<p class="lead">{lead}</p>' if lead else ""
        return f'''<section class="hero page-hero on-dark">{self.texture()}<div class="wrap"><div><nav class="crumbs" aria-label="Breadcrumb">{bc}</nav><h1>{h1}</h1>{lead_html}{btns}</div></div>{self.divider(sand)}</section>'''

    def tier_cards(self, cur):
        T = self.tiers; out = []
        for p in T["items"]:
            items = "".join(f'<li class="plus">{esc(i)}</li>' if i.endswith(":") else f"<li>{esc(i)}</li>" for i in p["items"])
            price = p.get("price") or T["price_label"]
            out.append(f'''<article class="plan{' featured' if p.get('featured') else ''}" id="plan-{p["slug"]}"><span class="badge">{esc(p["tag"])}</span>
<h3>{esc(p["name"])}</h3><p class="for">{esc(p["for"])}</p><div class="price{' num' if re.match(r"^[$€£\d]", price or "") else ''}">{esc(price)}<small>{esc(p.get("price_note") or T["price_note"])}</small></div>
<ul>{items}</ul><a class="btn {'btn-gold' if p.get('featured') else 'btn-outline'}" href="{self.href(cur,self.cta)}#plan-{p["slug"]}">{esc(T["card_cta"].format(name=p["name"]))}</a></article>''')
        return f'<div class="plans{" n2" if len(out) == 2 else ""}">{"".join(out)}</div>'

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
        return f'<form class="quiz" id="plan-finder" data-tiers="{data}" onsubmit="return false">{sets}<div class="quiz-result" id="quiz-result" aria-live="polite"><h3></h3><p></p><a class="btn btn-gold" href="{self.href(cur,self.cta)}">{esc(self.L["cta_long"])}</a></div></form>'

    def reviews_block(self):
        cards = "".join(f'<figure class="review"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><blockquote>“{esc(t)}”</blockquote><figcaption><cite>{esc(n)}<span>{esc(c)}</span></cite></figcaption></figure>' for n, c, t in self.c["reviews"])
        ig = self.c.get("integrations", {})
        url = ig.get("google_reviews_url")            # link that SHOWS the reviews (Maps / search)
        write = ig.get("google_review_write_url")     # GBP "ask for reviews" link (g.page/r/.../review) that OPENS the write-a-review box
        btns = (f'<a class="btn btn-outline" href="{url}" rel="noopener" target="_blank">Read more reviews on Google</a>' if url else "") + \
               (f'<a class="btn btn-outline" href="{write}" rel="noopener" target="_blank"><span class="rv-stars" aria-hidden="true">★★★★★</span> Leave us a Google review</a>' if write else "")
        more = f'<p class="btn-row" style="justify-content:center;margin-top:28px">{btns}</p>' if btns else ""
        return f'<div class="reviews">{cards}</div>{more}'

    @staticmethod
    def faq_block(faqs): return '<div class="faq">' + "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs) + "</div>"

    def cta_band(self, cur, h=None, p=None):
        h = h or self.L["cta_band_title"]; p = p or self.L["cta_band_text"]
        return f'''<section><div class="wrap"><div class="cta-band"><div><h2>{h}</h2><p>{p}</p></div>
<div class="btn-row"><a class="btn btn-gold" href="{self.href(cur,self.cta)}">{esc(self.L["cta"])}</a>{self.alt_btn(cur, label=False)}</div></div></div></section>'''

    def svc_path(self, s):   # services_hub.flat_urls: service pages at /<slug>/ (keeps old top-level URLs like /lawn-care-lexington-sc)
        return s["slug"] if self.c["services_hub"].get("flat_urls") else f'{self.c["services_hub"]["slug"]}/{s["slug"]}'
    def service_cards(self, cur, exclude=None, limit=None):
        svcs = [s for s in self.c["services"] if s["slug"] != exclude][:limit]
        return '<div class="grid-3">' + "".join(
            f'<a class="card" href="{self.href(cur,self.svc_path(s))}"><span class="ic">{icon(s["icon"])}</span><h3>{esc(s["name"])}</h3><p>{esc(s["short"])}</p><span class="more">Learn more →</span></a>'
            for s in svcs) + "</div>"

    def area_block(self, cur):
        A = self.areas; cols = ""
        for g in A["groups"]:
            links = "".join(f'<li><a href="{self.href(cur,a["slug"])}">{esc(a["city"])}</a></li>' for a in A["pages"] if a["slug"] in g["slugs"])
            also = (f'<p class="also-served">{esc(g.get("also_label", "Also serving"))} {esc(", ".join(g["also"]))}{esc(g.get("also_tail", ""))}</p>') if g.get("also") else ""   # groups[].also: towns served without their own page
            cols += f'<div class="county"><h3>{esc(g["name"])} <small>{esc(g.get("note",""))}</small></h3><ul class="city-links">{links}</ul>{also}</div>'
        return f'<div class="grid-2">{cols}</div><p style="text-align:center;margin-top:24px;color:var(--c-muted)">{esc(A["outside_note"])} <a href="{self.rh}">{esc(self.rt)}</a></p>'

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
{f'<div class="readings">{stats}</div>' if stats else ""}{f'<ul class="checks">{checks}</ul>' if checks else ""}{f'<p class="note">{esc(k["note"])}</p>' if k.get("note") else ""}{f'<a class="hanger-link" href="{self.href(cur, k["link"][1])}{k["link"][2] if len(k["link"]) > 2 else ""}">{esc(k["link"][0])} →</a>' if k.get("link") else ""}</aside>'''
        return ""

    def trail(self, *parts): return [("Home", "")] + list(parts)

    # ============================================================== pages
    def home(self):
        cur = ""; h = self.c["home"]; L = self.L
        lay = self.c["theme"].get("hero_layout", "card"); vis = self.hero_visual(cur)
        if not vis: lay = "centered"
        proof = "".join(f"<span>{icon('check')}{esc(x)}</span>" for x in h.get("proof", []))
        sec2 = f'<a class="btn btn-ghost" href="{self.href(cur,h["secondary_cta"][1])}">{esc(h["secondary_cta"][0])}</a>' if h.get("secondary_cta") else ""
        ho = h.get("hero_owner")   # home.hero_owner: a small "who you'll deal with" chip under the hero (owner photo, name, one line)
        owner_chip = (f'<div class="owner-chip"><img src="{self.asset(cur, ho["photo"])}" alt="{esc(ho.get("alt", ho["name"]))}" width="56" height="56">'
                      f'<p><b>{esc(ho["name"])}</b><span>{esc(ho.get("text",""))}</span></p></div>') if ho else ""
        hero = f'''<section class="hero on-dark layout-{lay}">{self.texture()}<div class="wrap"><div>
<span class="eyebrow">{esc(h["eyebrow"])}</span><h1>{h["h1"]}</h1><p class="lead">{esc(h["lead"])}</p>
<div class="btn-row" style="margin-top:26px"><a class="btn btn-gold" href="{self.href(cur,self.cta)}">{esc(L["cta_long"])}</a>{sec2}</div>
<div class="hero-proof">{proof}</div>{owner_chip}</div>{vis}</div>{self.divider()}</section>'''
        S = {}
        o = h.get("owner")   # home.owner: owner's story on the home page (photo, story, signature, links) -> "owner" in home.order
        if o:
            ph = o.get("photo")
            fig = (f'<figure class="owner-photo"><img src="{self.asset(cur, ph["file"])}" alt="{esc(ph["alt"])}" width="{ph.get("w",600)}" height="{ph.get("h",760)}" loading="lazy">'
                   + (f'<figcaption>{esc(ph["caption"])}</figcaption>' if ph.get("caption") else "") + '</figure>') if ph else ""
            links = "".join(f'<a class="btn {"btn-navy" if i == 0 else "btn-outline"}" href="{self.href(cur, s)}">{esc(t)}</a>' for i, (t, s) in enumerate(o.get("links", [])))
            S["owner"] = (f'<section class="owner-sec"><div class="wrap owner-grid">{fig}<div class="prose"><span class="eyebrow">{esc(o.get("eyebrow","Meet the owner"))}</span>'
                          f'<h2>{esc(o["title"])}</h2>{o["story_html"]}'
                          + (f'<p class="signature">{esc(o["signature"])}<small>{esc(o.get("signature_role",""))}</small></p>' if o.get("signature") else "")
                          + (f'<div class="btn-row" style="margin-top:22px">{links}</div>' if links else "") + '</div></div></section>')
        cd = h.get("cards")   # home.cards: a row of icon cards (e.g. local conditions), each optionally linking to a page -> "cards" in home.order
        if cd:
            items = ""
            for it in cd["items"]:   # (icon, title, text[, (link_label, slug)])
                lk = it[3] if len(it) > 3 else None
                inner = f'<span class="card-icon">{icon(it[0])}</span><h3>{esc(it[1])}</h3><p>{esc(it[2])}</p>'
                items += (f'<a class="card local-card" href="{self.href(cur, lk[1])}">{inner}<span class="more">{esc(lk[0])} →</span></a>' if lk
                          else f'<div class="card local-card">{inner}</div>')
            S["cards"] = (f'<section class="{cd.get("bg","")}"><div class="wrap"><div class="section-head"><span class="eyebrow">{esc(cd.get("eyebrow",""))}</span><h2>{esc(cd["title"])}</h2>'
                          + (f'<p class="lead">{esc(cd["lead"])}</p>' if cd.get("lead") else "") + f'</div><div class="grid-4">{items}</div></div></section>')
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
        n_svc = len(self.c["services"]); hc = sh.get("home_count")   # services_hub.home_count: feature the first N services on the home page, link the rest
        more_svc = f'<p style="margin-top:28px"><a class="btn btn-outline" href="{self.href(cur, sh["slug"])}">See all {n_svc} services →</a></p>' if hc and hc < n_svc else ""
        S["services"] = f'<section><div class="wrap"><div class="section-head"><span class="eyebrow">{esc(sh["nav_label"])}</span><h2>{esc(sh["home_title"])}</h2><p class="lead">{esc(sh["home_lead"])}</p></div>{self.service_cards(cur, limit=sh.get("home_count"))}{more_svc}</div></section>'
        g = h.get("gallery")
        S["gallery"] = (f'<section><div class="wrap"><div class="section-head"><span class="eyebrow">{esc(g.get("eyebrow","Our work"))}</span><h2>{esc(g["title"])}</h2>'
                        + (f'<p>{esc(g["lead"])}</p>' if g.get("lead") else "") + '</div>' + self.photo_grid(cur, g["photos"]) + '</div></section>') if g else ""
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
        if h.get("form"):
            hf = h["form"]; pts = "".join(f"<li>{esc(x)}</li>" for x in hf.get("points", []))
            S["form"] = (f'<section class="bg-sand" id="get-started"><div class="wrap grid-2"><div><span class="eyebrow">{esc(hf.get("eyebrow",""))}</span><h2>{esc(hf["title"])}</h2>'
                         f'<p class="lead">{esc(hf.get("lead",""))}</p>{f"<ul class=checklist>{pts}</ul>" if pts else ""}</div>'
                         f'<div>{self.lead_form(cur, {**self.c["contact"], **hf.get("form", {}), "form_name": "home"}, fid="h")}</div></div></section>')
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
<a class="btn btn-navy" href="{self.href(cur,self.cta)}">{esc(self.L["cta_long"])}</a></div><div><h3>{esc(pe["factors_title"])}</h3><ul class="checklist">{"".join("<li>"+esc(f)+"</li>" for f in pe["factors"])}</ul></div></div></section>''' if pe else ""
        quiz = f'<section><div class="wrap"><div class="section-head center"><span class="eyebrow">{esc(T["quiz"]["eyebrow"])}</span><h2>{esc(T["quiz"]["title"])}</h2></div>{self.quiz(cur)}</div></section>' if T.get("quiz") else ""
        compare = f'<section class="bg-sand"><div class="wrap"><div class="section-head"><span class="eyebrow">Side by side</span><h2>Compare what\'s included</h2><p class="lead">{esc(T["compare_lead"])}</p></div>{self.compare_table()}</div></section>' if T.get("compare") else ""
        ad = T.get("addons")
        addons = (f'<section style="padding-top:0"><div class="wrap"><div class="section-head"><span class="eyebrow">{esc(ad.get("eyebrow","Add-ons"))}</span><h2>{esc(ad["title"])}</h2><p class="lead">{esc(ad.get("lead",""))}</p></div><div class="addons">'
                  + "".join(f'<div class="addon"><div><h3>{esc(n)}</h3><p>{esc(d)}</p></div><b>{esc(p)}</b></div>' for n, p, d in ad["items"])
                  + "</div>" + (f'<p class="form-note" style="margin-top:18px">{esc(ad["note"])}</p>' if ad.get("note") else "") + "</div></section>") if ad else ""
        body = self.page_hero(cur, trail, T["h1"], esc(T["lead"])) + f'<section><div class="wrap"><div class="section-head center"><h2>{esc(T["home_title"])}</h2></div>{self.tier_cards(cur)}</div></section>{addons}{compare}{quiz}{pricing}' + \
            f'<section><div class="wrap"><div class="section-head center"><span class="eyebrow">FAQ</span><h2>{esc(T["nav_label"])} questions</h2></div>{self.faq_block(T["faqs"])}</div></section>{self.cta_band(cur)}'
        self.pages[cur] = self.page(cur, T["title"], T["meta"], body, [self.faq_schema(T["faqs"]), self.service_schema(T["nav_label"], T["meta"], cur)], trail)

    def gallery_page(self):
        """gallery_page: a standalone photo gallery (portfolio) page: {slug, nav_label, title, meta, h1, lead, photos, in_nav, cta_title, cta_text}."""
        G = self.c["gallery_page"]; cur = G["slug"]; trail = self.trail((G["nav_label"], cur))
        body = (self.page_hero(cur, trail, G["h1"], esc(G.get("lead", "")))
                + f'<section><div class="wrap">{self.photo_grid(cur, G["photos"])}</div></section>{self.cta_band(cur, G.get("cta_title"), G.get("cta_text"))}')
        img = [{"@type": "ImageObject", "contentUrl": f'{self.D}/assets/{ph["file"]}', "caption": ph.get("caption") or ph["alt"]} for ph in G["photos"]]
        sch = [{"@type": "ImageGallery", "@id": self.canon(cur) + "#gallery", "name": G["h1"], "url": self.canon(cur), "image": img}]
        self.pages[cur] = self.page(cur, G["title"], G["meta"], body, sch, trail)

    def services_hub(self):
        sh = self.c["services_hub"]; cur = sh["slug"]; trail = self.trail((sh["nav_label"], cur))
        extra = f'<section class="bg-sand"><div class="wrap"><div class="section-head center"><span class="eyebrow">{esc(self.tiers["nav_label"])}</span><h2>{esc(self.tiers["home_title"])}</h2></div>{self.tier_cards(cur)}</div></section>' if self.tiers else ""
        body = self.page_hero(cur, trail, sh["h1"], esc(sh["lead"])) + f'<section><div class="wrap"><div class="section-head"><h2>{esc(sh["home_title"])}</h2></div>{self.service_cards(cur)}</div></section>{extra}{self.cta_band(cur)}'
        self.pages[cur] = self.page(cur, sh["title"], sh["meta"], body, None, trail)

    def photo_grid(self, cur, photos):
        """Real job photos: [{"file": "photos/x.webp", "alt": "...", "caption": "...", "w": 1200, "h": 900}] from clients/<client>/assets/."""
        figs = "".join(f'<figure{" class=contain" if ph.get("contain") else ""}><img src="{self.asset(cur, ph["file"])}" alt="{esc(ph["alt"])}" width="{ph.get("w",1200)}" height="{ph.get("h",900)}" loading="lazy" decoding="async">'
                       f'{"<figcaption>" + esc(ph["caption"]) + "</figcaption>" if ph.get("caption") else ""}</figure>' for ph in photos)
        return f'<div class="photo-grid">{figs}</div>'
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
{f'<h2 id="photos">{esc(s.get("photos_title","Recent work"))}</h2>' + self.photo_grid(cur, s["photos"]) if s.get("photos") else ""}
{f'<h2>{esc(s["signs_title"])}</h2><ul class="checklist">{signs}</ul>' if signs else ""}{faq_html}{where}</div>
<aside class="aside"><h3>{esc(self.L["aside_title"])}</h3><p>{esc(self.L["aside_text"])}</p><a class="phone{"" if self.has_phone else " is-email"}" href="{self.rh}">{esc(self.rt)}</a>
<a class="btn btn-gold" href="{self.href(cur,self.cta)}">{esc(self.L["cta"])}</a>{alt}<p style="margin:12px 0 0;font-size:.85rem">{esc(self.L["aside_badges"])}</p></aside></div></section>
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
<aside class="aside"><h3>{f(A["aside_title"])}</h3><p>{esc(self.L["aside_text"])}</p><a class="phone{"" if self.has_phone else " is-email"}" href="{self.rh}">{esc(self.rt)}</a>
<a class="btn btn-gold" href="{self.href(cur,self.cta)}">{esc(self.L["cta"])}</a><p style="margin:14px 0 6px;font-weight:700;color:#fff">Also serving</p><ul class="city-links" style="grid-template-columns:1fr">{nearby}</ul></aside></div></section>
{self.related_posts_block(cur, "areas", a["slug"], self.blog.get("area_related_title", "Tips for {city}").format(city=a["city"])) if self.blog else ""}{f'<section class="bg-sand"><div class="wrap"><div class="section-head center"><span class="eyebrow">Reviews</span><h2>What our neighbors say</h2></div>{self.reviews_block()}</div></section>' if self.c["reviews"] else ""}{self.cta_band(cur)}'''
        sch = [self.service_schema(f(A["page_title"]), a["intro"], cur, [a["city"]]), self.faq_schema(faqs)]
        self.pages[cur] = self.page(cur, f(A["page_title"]), f(A["page_meta"]), body, sch, trail)

    def resource_page(self):
        R = self.resource; cur = R["slug"]; trail = self.trail((R["nav_label"], cur))
        cards = "".join(f'<article class="month"><small>{esc(k)}</small><h3>{esc(t)}</h3><ul>{"".join("<li>"+esc(i)+"</li>" for i in items)}</ul></article>' for k, t, items in R["cards"])
        body = self.page_hero(cur, trail, R["h1"], esc(R["lead"]), sand=True) + f'''<section class="bg-sand" style="padding-top:40px"><div class="wrap"><h2 class="skip">{esc(R["nav_label"])}</h2><div class="cal">{cards}</div></div></section>
{f'<section><div class="wrap"><div class="prose" style="max-width:860px">{self.rel_links(cur, R["body_html"])}</div></div></section>' if R.get("body_html") else ""}
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

    def cat_info(self, name):
        B = self.blog; v = (B.get("categories") or {}).get(name)
        if isinstance(v, dict): return {"slug": v["slug"], **v}
        return {"slug": v or re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")}
    def cat_path(self, name): return f'{self.blog["category_prefix"]}/{self.cat_info(name)["slug"]}' if self.blog.get("category_prefix") else None
    def chip(self, cur, name):
        p = self.cat_path(name)
        return f'<a class="chip" href="{self.href(cur,p)}">{esc(name)}</a>' if p else f'<span class="chip">{esc(name)}</span>'

    def category_pages(self):
        """One archive page per category at <category_prefix>/<slug> (keeps old GHL /blog/c/<slug> URLs alive)."""
        B = self.blog
        if not B.get("category_prefix"): return
        for name in sorted({p.get("category") for p in self.posts if p.get("category")}):
            ci = self.cat_info(name); cur = self.cat_path(name); posts = [p for p in self.posts if p.get("category") == name]
            trail = self.trail((B["nav_label"], B["index_slug"]), (name, cur))
            h1 = ci.get("h1") or f"{name}: {B['nav_label']} articles"
            body = (self.page_hero(cur, trail, esc(h1), esc(ci.get("lead", "")), ctas=False)
                    + f'<section><div class="wrap"><div class="section-head"><h2>{len(posts)} article{"s" if len(posts)!=1 else ""}</h2></div>{self.post_cards(cur, posts)}</div></section>' + self.cta_band(cur))
            sch = [{"@type": "CollectionPage", "@id": self.canon(cur) + "#collection", "name": h1, "url": self.canon(cur), "isPartOf": {"@id": self.canon(B["index_slug"]) + "#blog"},
                    "hasPart": [{"@type": "BlogPosting", "headline": p["title"], "url": self.canon(self.post_path(p))} for p in posts]}]
            self.pages[cur] = self.page(cur, ci.get("title") or h1, ci.get("meta") or f"{name} articles from the {self.b['name']} {B['nav_label'].lower()}.", body, sch, trail)

    def blog_index(self):
        B = self.blog; cur = B["index_slug"]; trail = self.trail((B["nav_label"], cur))
        cats = sorted({p.get("category") for p in self.posts if p.get("category")})
        chips = "".join(self.chip(cur, c) for c in cats)
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
                f'<span class="eyebrow">{(f'<a href="{self.href(cur, self.cat_path(p["category"]))}">{esc(p["category"])}</a>' if p.get("category") and self.cat_path(p["category"]) else esc(p.get("category", B["nav_label"])))}</span><h1>{esc(p["title"])}</h1>'
                f'<p class="lead">{esc(p.get("description",""))}</p>{meta_line}</div></div>{self.divider()}</section>'
                f'<section><div class="wrap layout-side"><article class="prose post-body">{hero_img}{body_html}</article>'
                f'<aside class="aside"><h2 class="h3">{esc(self.L["aside_title"])}</h2><p>{esc(self.L["aside_text"])}</p>'
                f'<a class="phone{"" if self.has_phone else " is-email"}" href="{self.rh}">{esc(self.rt)}</a>'
                f'<a class="btn btn-gold" href="{self.href(cur,self.cta)}">{esc(self.L["cta"])}</a>{aside_links}</aside></div></section>'
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
        ph = A.get("photo")   # about.photo: owner/team photo beside the story; about.photos: a work gallery section
        photo_html = (f'<figure class="about-photo"><img src="{self.asset(cur, ph["file"])}" alt="{esc(ph["alt"])}" width="{ph.get("w",600)}" height="{ph.get("h",800)}" loading="lazy">'
                      + (f'<figcaption>{esc(ph["caption"])}</figcaption>' if ph.get("caption") else "") + '</figure>') if ph else ""
        gallery = (f'<section class="bg-sand"><div class="wrap"><div class="section-head"><h2>{esc(A.get("photos_title", "Our work"))}</h2></div>'
                   + self.photo_grid(cur, A["photos"]) + '</div></section>') if A.get("photos") else ""
        tm = A.get("team")   # about.team: [{name, role, bio, photo?, alt?}] -> "Meet the team" cards (initials when no photo)
        if tm:
            def person(p):
                pic = (f'<img src="{self.asset(cur, p["photo"])}" alt="{esc(p.get("alt", p["name"]))}" width="160" height="160" loading="lazy">' if p.get("photo")
                       else f'<span class="initials" aria-hidden="true">{esc("".join(w[0] for w in p["name"].split()[:2]))}</span>')
                return f'<div class="person">{pic}<h3>{esc(p["name"])}</h3><p class="role">{esc(p.get("role",""))}</p><p>{esc(p.get("bio",""))}</p></div>'
            gallery = (f'<section><div class="wrap"><div class="section-head center"><span class="eyebrow">{esc(A.get("team_eyebrow","The people"))}</span><h2>{esc(A.get("team_title","Meet the team"))}</h2></div>'
                       f'<div class="team">{"".join(person(p) for p in tm)}</div></div></section>') + gallery
        body = self.page_hero(cur, trail, A["h1"], esc(A["lead"])) + f'''<section><div class="wrap grid-2"><div class="prose"><span class="eyebrow">Our story</span><h2>{esc(A["story_title"])}</h2>{A["story_html"]}</div>
<div>{photo_html}<h3>{esc(A["list_title"])}</h3><ul class="checklist">{"".join("<li>"+esc(x)+"</li>" for x in A["list"])}</ul></div></div></section>
{gallery}{f'<section class="bg-sand"><div class="wrap"><div class="section-head center"><span class="eyebrow">Reviews</span><h2>What our customers say</h2></div>{self.reviews_block()}</div></section>' if self.c["reviews"] else ""}{self.cta_band(cur)}'''
        self.pages[cur] = self.page(cur, A["title"], A["meta"], body, None, trail)

    # ---------- lead forms (contact page, extra lead pages, optional home-page section)
    def lead_form(self, cur, C, fid="f"):
        """The site's lead form in whichever integrations.form_mode is active:
        ghl_embed (GHL iframe) | native (own form, captured by the GHL tracking script) |
        web3forms (own form, posted to api.web3forms.com, which emails the owner; no CRM needed) | demo."""
        b = self.b; ig = self.c.get("integrations", {}); mode = self.form_mode()
        if mode == "ghl_embed":
            gid = ig["ghl_form_id"]
            return f'<div class="form-card"><iframe src="https://api.leadconnectorhq.com/widget/form/{gid}" style="width:100%;height:{C.get("ghl_height",760)}px;border:none;border-radius:4px" id="inline-{gid}" data-layout="{{\'id\':\'INLINE\'}}" data-form-id="{gid}" title="{esc(self.L["cta"])}"></iframe><script src="https://link.msgsndr.com/js/form_embed.js"></script></div>'
        selects = ""
        names = C.get("select_names", {})
        for i, (lbl, opts) in enumerate(C.get("selects", [])):
            selects += (f'<div class="full"><label for="{fid}-s{i}">{esc(lbl)}</label><select id="{fid}-s{i}" name="{esc(names.get(lbl, "s%d" % i))}"{" required" if lbl in C.get("required_selects", []) else ""}>'
                        + "".join(f'<option value="">{esc(C.get("select_placeholder", "Choose one"))}</option>' if o == "" else f"<option>{esc(o)}</option>" for o in opts) + "</select></div>")
        if self.areas and C.get("city_select", True):
            selects = (f'<div class="full"><label for="{fid}-city">{esc(C.get("city_label", "City"))}</label><select id="{fid}-city" name="city">'
                       + (f'<option value="">{esc(C["city_placeholder"])}</option>' if C.get("city_placeholder") else "")   # contact.city_placeholder / city_first: e.g. home town first
                       + "".join(f"<option>{esc(x)}</option>" for x in C.get("city_first", []))
                       + "".join(f"<option>{esc(a['city'])}</option>" for a in self.areas["pages"]) + "<option>Other / not sure</option></select></div>" + selects)
        if self.tiers and C.get("plan_select", True):
            # contact.plan_label / plan_placeholder / plan_extra_options: relabel the tier select and add non-tier choices
            selects += (f'<div class="full"><label for="{fid}-plan">{esc(C.get("plan_label", "Interested in"))}</label><select id="{fid}-plan" class="plan-select" name="plan"><option value="">{esc(C.get("plan_placeholder", "Not sure yet"))}</option>'
                        + "".join(f'<option value="{t["slug"]}">{esc(t["name"])}</option>' for t in self.tiers["items"])
                        + "".join(f"<option>{esc(o)}</option>" for o in C.get("plan_extra_options", [])) + "</select></div>")
        # extra_inputs: (name, label, autocomplete, required, full_width[, input_type[, placeholder]]), e.g. type "date", "url", "number"
        def _inp(n, lbl, ac, req, full, typ="text", ph=""):
            return (f'<div{" class=full" if full else ""}><label for="{fid}-{n}">{esc(lbl)}</label><input id="{fid}-{n}" name="{n}" type="{typ}" autocomplete="{ac}"'
                    + (f' placeholder="{esc(ph)}"' if ph else "") + (" required" if req else "") + "></div>")
        extra_inputs = "".join(_inp(*x) for x in C.get("extra_inputs", []))
        # extra_textareas: (name, label, placeholder) shown after the main message box
        extra_tas = "".join(f'<div class="full"><label for="{fid}-{n}">{esc(lbl)}</label><textarea id="{fid}-{n}" name="{n}" rows="3"' + (f' placeholder="{esc(ph)}"' if ph else "") + "></textarea></div>"
                            for n, lbl, ph in C.get("extra_textareas", []))
        after_inputs = "".join(_inp(*x) for x in C.get("after_inputs", []))   # inputs placed after the message, e.g. "How did you hear about us?"
        consent = (f'<div class="full consent"><label><input type="checkbox" name="sms_consent" value="yes"> <span>{esc(C["consent_text"])}</span></label></div>'
                   if C.get("consent_text") else "")
        ok = (f'<div class="form-msg" role="status">{esc(C.get("success", "Thanks! We got your request and will reach out shortly."))} '
              f'Need us sooner? {esc(self.reach_verb)} <a href="{self.rh}">{esc(self.rt)}</a>.</div>')
        err = f'<div class="form-err" role="alert">Something went wrong sending the form. Please {esc(self.reach_verb.lower())} <a href="{self.rh}">{esc(self.rt)}</a> so we don\'t miss you.</div>'
        hp = f'<div class="hp" aria-hidden="true"><label for="{fid}-website">Leave this empty</label><input id="{fid}-website" name="website" tabindex="-1" autocomplete="off"></div>'
        hidden = ""
        if mode == "native":
            attrs, note, msg = 'data-native-ghl name="website-lead"', "<!-- LIVE FORM: captured into GoHighLevel by the External Tracking script (integrations.ghl_tracking_snippet) -->", ok + err
        elif mode == "web3forms":
            subject = ig.get("web3forms_subject") or f'New website lead: {b["name"]}'
            thanks_abs = (self.D + "/" + ig["thank_you_slug"] + "/") if ig.get("thank_you_slug") else ""
            attrs = 'data-web3forms action="https://api.web3forms.com/submit" method="POST"' + (f' data-thanks="{self.href(cur, ig["thank_you_slug"])}"' if thanks_abs else "")
            note = "<!-- LIVE FORM: posts to Web3Forms, which emails each submission (integrations.web3forms_access_key). Works without JavaScript too. -->"
            track = ("page", "landing_page", "referrer", "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "fbclid")
            hidden = (f'<input type="hidden" name="access_key" value="{esc(ig["web3forms_access_key"])}">'
                      f'<input type="hidden" name="subject" value="{esc(subject)}">'
                      f'<input type="hidden" name="from_name" value="{esc(ig.get("web3forms_from_name") or b["name"] + " website")}">'
                      + (f'<input type="hidden" name="ccemail" value="{esc(ig["web3forms_cc"])}">' if ig.get("web3forms_cc") else "")
                      + (f'<input type="hidden" name="redirect" value="{esc(thanks_abs)}">' if thanks_abs else "")
                      + f'<input type="hidden" name="form" value="{esc(C.get("form_name") or cur or "home")}">'
                      + "".join(f'<input type="hidden" name="{k}" value="" data-track="{k}">' for k in track)
                      + '<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">')
            hp = ""   # Web3Forms' own botcheck field replaces the generic honeypot
            msg = ok + err
        else:
            attrs = "data-demo"
            note = "<!-- DEMO FORM: set integrations.form_mode (web3forms + web3forms_access_key, ghl_embed + ghl_form_id, or native + ghl_tracking_snippet) to go live -->"
            msg = '<div class="form-msg" role="status">Preview only: this form goes live once a form connection (Web3Forms or GoHighLevel) is set in the site config.</div>'
        email_req = " required" if C.get("email_required") else ""
        return (f'<form class="form-card" {attrs}>{note}{hidden}\n{hp}'
                f'<div class="form-grid"><div><label for="{fid}-name">Name</label><input id="{fid}-name" name="name" autocomplete="name" required></div>\n'
                f'<div><label for="{fid}-phone">{esc(C.get("phone_label", "Mobile phone"))}</label><input id="{fid}-phone" name="phone" type="tel" autocomplete="tel" required></div>\n'
                f'<div class="full"><label for="{fid}-email">Email</label><input id="{fid}-email" name="email" type="email" autocomplete="email"{email_req}></div>{extra_inputs}{selects}\n'
                f'<div class="full"><label for="{fid}-msg">{esc(C["message_label"])}</label><textarea id="{fid}-msg" name="message" rows="4"></textarea></div>{extra_tas}{after_inputs}{consent}</div>\n'
                f'<button class="btn btn-gold" type="submit" style="width:100%;margin-top:16px">{esc(C["submit"])}</button><p class="form-note">{esc(C["note"])}</p>\n'
                f'{msg}</form>')

    def contact_page(self, C=None):
        """Primary lead page (contact.slug, default "contact"). Each entry in `lead_pages` is built the same way,
        inheriting form settings from `contact`, so an old /contact or /quote URL can stay a real page."""
        C = {**self.c["contact"], **(C or {})}
        cur = C.get("slug", "contact"); b = self.b
        trail = self.trail((C.get("crumb") or (self.L["cta"] if cur == self.cta else C["h1"]), cur))
        form = self.lead_form(cur, C)
        nxt = "".join(f"<li>{esc(x)}</li>" for x in C["next_steps"])
        email = f'<p><a href="mailto:{b["email"]}" style="color:#fff">{esc(b["email"])}</a></p>' if b.get("email") and C.get("show_email", True) else ""
        aside = (f'<aside class="aside"><h2 class="h3">{esc(self.L["phone_prefix"])}</h2><a class="phone{"" if self.has_phone else " is-email"}" href="{self.rh}">{esc(self.rt)}</a><p>{esc(b["hours_text"])}</p>{email if self.has_phone else ""}'
                 f'<h2 class="h3" style="margin-top:20px">{esc(C.get("next_title", "What happens next"))}</h2><ul class="checklist" style="color:rgba(255,255,255,.86)">{nxt}</ul></aside>')
        extra, sch = "", []
        if C.get("steps"):
            st = C["steps"]
            extra += (f'<section><div class="wrap"><div class="section-head"><span class="eyebrow">{esc(st["eyebrow"])}</span><h2>{esc(st["title"])}</h2></div><div class="steps">'
                      + "".join(f'<div class="step"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in st["items"]) + "</div></div></section>")
        if C.get("body_html"):
            extra += f'<section class="bg-sand"><div class="wrap prose">{self.rel_links(cur, C["body_html"])}</div></section>'
        if C.get("faqs"):
            extra += f'<section><div class="wrap"><div class="section-head center"><span class="eyebrow">FAQ</span><h2>{esc(C.get("faq_title", "Common questions"))}</h2></div>{self.faq_block(C["faqs"])}</div></section>'
            sch.append(self.faq_schema(C["faqs"]))
        if C.get("page_type"):
            sch.append({"@type": C["page_type"], "@id": self.canon(cur) + "#page", "url": self.canon(cur), "name": C["h1"], "about": {"@id": self.D + "/#business"}})
        body = (self.page_hero(cur, trail, C["h1"], esc(C["lead"]), ctas=False, sand=True)
                + f'<section class="bg-sand" style="padding-top:40px"><div class="wrap layout-side"><div>{form}</div>\n{aside}</div></section>{extra}')
        self.pages[cur] = self.page(cur, C["title"], C["meta"], body, sch or None, trail)

    def thank_you_page(self):
        """Optional /thank-you/ page (integrations.thank_you_slug): Web3Forms forms land here after a send,
        so GA4 / Google Ads can count a lead as a page view. Never indexed."""
        slug = self.c.get("integrations", {}).get("thank_you_slug")
        if not slug: return
        T = self.c.get("thank_you", {}); b = self.b
        more = f'<p><a href="{self.href(slug, self.blog["index_slug"])}">Read the {esc(self.blog["nav_label"].lower())} while you wait →</a></p>' if self.blog else ""
        body = (self.page_hero(slug, self.trail(("Thank you", slug)), esc(T.get("h1", "Thanks, we got it.")), esc(T.get("lead", "We'll be in touch shortly.")), ctas=False)
                + f'<section><div class="wrap prose"><p>{esc(T.get("text", "Need us sooner?"))} {esc(self.reach_verb)} <a href="{self.rh}">{esc(self.rt)}</a>.</p>{more}</div></section>')
        self.pages[slug] = self.page(slug, T.get("title", "Thank you"), "Thanks for reaching out.", body, noindex=True)

    def legal_pages(self):
        for slug, name in self.c.get("legal_pages", []):
            f = os.path.join(ROOT, "clients", self.client, "legal", slug + ".md")
            if os.path.exists(f):
                inner = markdown(open(f, encoding="utf-8").read(), self.post_link(slug) if self.blog else (lambda u: u))
            else:
                inner = f'<!-- TODO before launch: create clients/{self.client}/legal/{slug}.md --><p>[Paste the {esc(name)} text here before launch.]</p>'
            self.pages[slug] = self.page(slug, name, f'{name} for {self.b["legal_name"]}.',
                self.page_hero(slug, self.trail((name, slug)), esc(name), "", ctas=False) +
                f'<section><div class="wrap prose">{inner}</div></section>')

    def form_mode(self):
        ig = self.c.get("integrations", {})
        mode = ig.get("form_mode") or ("ghl_embed" if ig.get("ghl_form_id") else "demo")
        if mode == "ghl_embed" and not ig.get("ghl_form_id"): mode = "demo"
        if mode == "native" and not ig.get("ghl_tracking_snippet"): mode = "demo"
        if mode == "web3forms" and not ig.get("web3forms_access_key"): mode = "demo"
        return mode

    # ============================================================== launch check
    def launch_check(self):
        """Returns (blockers, warnings). Blockers = things that lose leads, break URLs or show placeholder text."""
        ig = self.c.get("integrations", {}); B, W = [], []
        mode = self.form_mode()
        want = ig.get("form_mode")
        if mode == "demo":
            hint = {"web3forms": "Set integrations.web3forms_access_key (web3forms.com > create an access key for the owner's email).",
                    "native": "Set integrations.ghl_tracking_snippet."}.get(want, "Set form_mode 'web3forms' + web3forms_access_key, or ghl_form_id, or form_mode 'native' + ghl_tracking_snippet.")
            B.append("Contact form is the DEMO form, so leads go nowhere. " + hint)
        if want != "web3forms" and not ig.get("ghl_tracking_snippet"):
            B.append("GHL External Tracking script not set (integrations.ghl_tracking_snippet): no UTM/source attribution or page-view tracking in GHL.")
        if want == "web3forms":
            W.append("Web3Forms: send one real test submission from the live domain and confirm the email arrives (check spam the first time) with the page and UTM fields filled in.")
            if ig.get("web3forms_cc"): W.append("Web3Forms ccemail needs a paid Web3Forms plan; on the free plan, set a forwarding rule in the owner's inbox instead.")
            if not ig.get("gtm_id"):
                if ig.get("no_analytics"):   # integrations.no_analytics: client opted out of GTM/GA4; leads are counted from the Web3Forms inbox
                    W.append("No analytics by choice (integrations.no_analytics): count leads from the Web3Forms emails / dashboard.")
                else:
                    B.append("Web3Forms mode has no CRM tracking script, so integrations.gtm_id (GA4 + lead conversions) is required to measure leads. (Set integrations.no_analytics: True if the client opts out.)")
        if mode == "native":
            W.append("Native form mode: send one real test submission after launch and confirm it appears in GHL > Contacts and fires the owner-notification workflow.")
        if mode == "ghl_embed":
            W.append("Send one real test submission after launch and confirm the owner-notification workflow fires.")
        if not ig.get("gtm_id") and want != "web3forms": W.append("No Google Tag Manager ID (integrations.gtm_id): GA4 / conversion tracking not installed.")
        if not ig.get("google_reviews_url"): W.append("No google_reviews_url: the 'Read more reviews on Google' button is hidden.")
        for slug, name in self.c.get("legal_pages", []):
            if not os.path.exists(os.path.join(ROOT, "clients", self.client, "legal", slug + ".md")):
                B.append(f"{name} page is placeholder text. Create clients/{self.client}/legal/{slug}.md.")
        pdir = os.path.join(ROOT, "clients", self.client, "posts")
        if self.blog and os.path.isdir(pdir):
            for f in sorted(os.listdir(pdir)):
                if f.endswith(".md"):
                    p = parse_post(os.path.join(pdir, f))
                    if p["draft"] and p.get("migrate_from"):
                        B.append(f"Blog post not migrated (old URL will 404): /{self.blog['post_prefix']}/{p['slug']}/ (posts/{f})")
                    elif p["draft"]:
                        W.append(f"Draft post not published: posts/{f}")
        og = self.c.get("og_image", "og-image.jpg")
        if not os.path.exists(os.path.join(self.client_assets, og)):
            W.append(f"No assets/{og} committed: social share image will be missing on Cloudflare builds.")
        if self.c["logo"]["type"] == "text": W.append("Logo is a text placeholder; add the real logo to assets/.")
        if any("placeholder" in (t or "").lower() for _, _, t in self.c.get("reviews", [])): B.append("Reviews contain placeholder text.")
        if "example.com" in self.D: B.append("business.domain is still example.com.")
        return B, W

    # ============================================================== write
    def build(self):
        self.home(); self.services_hub(); self.about_page(); self.contact_page(); self.legal_pages(); self.thank_you_page()
        for lp in self.c.get("lead_pages", []): self.contact_page(lp)
        if self.c.get("gallery_page"): self.gallery_page()
        for s in self.c["services"]: self.service_page(s)
        if self.tiers: self.tiers_page()
        if self.areas:
            self.areas_hub()
            for a in self.areas["pages"]: self.area_page(a)
        if self.resource: self.resource_page()
        if self.blog:
            self.blog_index(); self.category_pages()
            for p in self.posts: self.post_page(p)
        if os.path.exists(self.out): shutil.rmtree(self.out)
        for path, h in self.pages.items():
            d = os.path.join(self.out, path); os.makedirs(d, exist_ok=True)
            open(os.path.join(d, "index.html"), "w").write(h)
        A = os.path.join(self.out, "assets"); os.makedirs(os.path.join(A, "fonts"))
        for f in ("site.css", "site.js"): shutil.copy(os.path.join(ROOT, "core", f), A)
        # site.js carries GHL-only code between //@@GHL markers: keep it (markers removed) for GHL sites, drop it for GHL-free (web3forms) sites
        js = open(os.path.join(A, "site.js"), encoding="utf-8").read()
        if self.c["integrations"].get("form_mode") == "web3forms":
            js = re.sub(r"  //@@GHL-START\n.*?  //@@GHL-END\n", "", js, flags=re.S)
            js = js.replace("  //@@GHL-LINE demo form (no GHL connection yet): never pretends to send", "  // demo form (no form connection yet): never pretends to send")
        else:
            js = js.replace("  //@@GHL-START\n", "").replace("  //@@GHL-END\n", "").replace("  //@@GHL-LINE demo form", "  // demo form")
        open(os.path.join(A, "site.js"), "w", encoding="utf-8").write(js)
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
            urls = "".join(f"<url><loc>{self.canon(p)}</loc><lastmod>{post_dates.get(p, TODAY)}</lastmod></url>" for p in self.pages if p != "404" and p not in self.noindex)
            if self.blog and self.posts:
                open(os.path.join(self.out, self.blog["index_slug"], "rss.xml"), "w").write(self.rss())
            open(os.path.join(self.out, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
            open(os.path.join(self.out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {self.D}/sitemap.xml\n")
            # Cloudflare matches the exact path, so "/old" and "/old/" are different URLs: emit both (unless the rule is a wildcard or already ends in "/")
            lines = []; given = {r[0] for r in self.c.get("redirects", [])}
            for r in self.c.get("redirects", []):
                code = r[2] if len(r) > 2 else 301
                lines.append(f"{r[0]}  {r[1]}  {code}\n")
                if not r[0].endswith(("/", "*")) and "." not in r[0].rsplit("/", 1)[-1] and r[0] + "/" not in given:
                    lines.append(f"{r[0]}/  {r[1]}  {code}\n")
            open(os.path.join(self.out, "_redirects"), "w").write("".join(lines))
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
        d.text((80, 500), f'{self.rt}  ·  {self.b["domain"].split("//")[-1]}', font=load(34), fill=hx(col["accent"]))
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
    failed = False
    for c in targets:
        site = Site(c, "--preview" in sys.argv)
        blockers, warnings = site.launch_check()
        launched = site.c.get("launched", False)
        if "--check" in sys.argv:
            print(f"\n=== Launch check: {c} ({'LIVE' if launched else 'not launched'}) ===")
            print(f"BLOCKERS ({len(blockers)}):" if blockers else "BLOCKERS: none")
            for x in blockers: print("  [X] " + x)
            print(f"TO VERIFY / NICE TO HAVE ({len(warnings)}):" if warnings else "")
            for x in warnings: print("  [ ] " + x)
            print("READY TO LAUNCH" if not blockers else "NOT READY: fix blockers before setting launched: True / pointing the domain")
            failed |= bool(blockers)
            continue
        if launched and blockers and "--preview" not in sys.argv:
            print(f"[{c}] BUILD STOPPED: site is marked launched but has launch blockers:")
            for x in blockers: print("  [X] " + x)
            sys.exit(1)
        if blockers and not launched:
            print(f"[{c}] note: {len(blockers)} launch blocker(s); run `python3 build.py {c} --check`")
        site.build()
    if "--check" in sys.argv and failed: sys.exit(1)
