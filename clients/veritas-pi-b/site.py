# Veritas Investigative Group: DESIGN OPTION B (alternate look for the client to choose from).
# Pages, copy, SEO and integrations are imported unchanged from clients/veritas-pi/site.py (option A), so
# the wording can never drift between the two. Only the theme, stylesheet and layout options differ.
# Whichever option the client picks becomes the live site; the other is deleted before launch.
import copy, importlib.util, os
_a = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "veritas-pi", "site.py")
_spec = importlib.util.spec_from_file_location("veritas_a", _a); _m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)

CONFIG = copy.deepcopy(_m.CONFIG)
CONFIG["theme"] = {
    # light, document-like "case brief": white pages, navy bands, gold kept to rules and accents
    "colors": {"primary": "#0b1424", "primary_deep": "#060c18", "secondary": "#13203a", "secondary_deep": "#0b1424", "secondary_wash": "#f1ede4",
               "accent": "#c5a059", "highlight": "#d9b877", "accent_text": "#0b1424", "surface": "#ffffff", "ink": "#121a2b", "muted": "#566074"},
    "fonts": {"display": "source-serif-4", "body": "inter"},
    "radius": "soft", "heading_case": "none", "divider": "none", "texture": "none",
    "sections_css": "sections-brief.css",
}
CONFIG["logo"] = {**CONFIG["logo"], "file": "logo-light.png", "footer_file": "logo-dark.png"}   # light header, navy footer
CONFIG["sx_options"] = {
    "utility_bar": "SLED License #4362. Licensed, Bonded & Insured.",   # repeats the existing footer line above the fold
    "hero_mark": "hero-shield.png",   # the client's shield (from 04_shield_v_icon) in the home hero
    "subnav": True, "contact_split": True,
    "highlight_edits": True,   # preview only: shows the Lexington/Columbia wording below in a highlight
}

# ---------------------------------------------------------------- Option B only: local wording (Lexington / Columbia)
# Proposed for client review, NOT client-approved copy. Each insertion is wrapped in ==...== so the preview highlights it
# (sx_options.highlight_edits). Before launch: if approved, set highlight_edits False; if not, delete LOCAL_EDITS.
LOCAL_EDITS = {
    # home
    "based in South Carolina, with investigative experience that extends into international matters.":
        "based in ==Lexington, serving Columbia and all of== South Carolina, with investigative experience that extends into international matters.",
    "Veritas works directly with the people and organizations who need answers.":
        "Veritas works directly with the people and organizations ==in Lexington, Columbia and across South Carolina== who need answers.",
    # services hub
    "Veritas offers nine investigative services for individuals, attorneys, insurers, businesses and government clients.":
        "Veritas offers nine investigative services for individuals, attorneys, insurers, businesses and government clients ==in Lexington, Columbia and throughout South Carolina==.",
    # about
    "to private investigative work throughout South Carolina":
        "to private investigative work ==in Lexington, Columbia and== throughout South Carolina",
    # service pages (hero leads)
    "Veritas provides thorough investigation and surveillance handled with discretion.":
        "Veritas provides thorough investigation and surveillance ==in Lexington, Columbia and across South Carolina,== handled with discretion.",
    "Veritas supports attorneys and legal teams with investigative research that holds up under scrutiny, backed":
        "Veritas supports attorneys and legal teams ==in Columbia, Lexington and across South Carolina== with investigative research that holds up under scrutiny, backed",
    "Veritas helps insurance carriers and adjusters verify claims":
        "Veritas helps insurance carriers and adjusters ==in Columbia, Lexington and statewide== verify claims",
    "to help business leaders make informed decisions":
        "to help business leaders ==in Lexington, Columbia and across South Carolina== make informed decisions",
    "Veritas provides professional polygraph examinations for government agencies":
        "Veritas provides professional polygraph examinations ==in Lexington, Columbia and across South Carolina== for government agencies",
    "Veritas provides the background research individuals and organizations need":
        "Veritas provides the background research individuals and organizations ==in Lexington, Columbia and across South Carolina== need",
    "to help organizations identify vulnerabilities":
        "to help organizations ==in Columbia, Lexington and across South Carolina== identify vulnerabilities",
    # contact
    "We'll help you understand your options and determine how Veritas can best assist.":
        "We'll help you understand your options and determine how Veritas can best assist. ==Based in Lexington, serving Columbia and all of South Carolina.==",
}
LOCAL_TITLES = {   # Option B only: <title>/meta with city names (no highlight possible; listed in NOTES.md)
    "services": ("Private Investigators in Lexington & Columbia, SC", None),
    "about": ("About Veritas | Lexington & Columbia, SC Investigators", None),
    "contact": ("Contact a Lexington & Columbia, SC Private Investigator", None),
}
SVC_TITLES = {
    "Private Investigations & Surveillance": "Private Investigator & Surveillance | Columbia, SC",
    "Attorney & Litigation Support": "Litigation Support Investigator | Columbia & Lexington",
    "Insurance Investigations": "Insurance Investigations | Columbia & Lexington, SC",
    "Corporate & Business Investigations": "Workplace Investigations | Columbia & Lexington, SC",
    "Polygraph Services": "Polygraph Examinations | Columbia & Lexington, SC",
    "Background & Due Diligence": "Background Checks | Columbia & Lexington, SC",
    "Security Consulting & Risk Management": "Security Consulting | Columbia & Lexington, SC",
}
_used = set()
def _localize(o):
    if isinstance(o, str):
        for a, b in LOCAL_EDITS.items():
            if a in o: o = o.replace(a, b); _used.add(a)
        return o
    if isinstance(o, list): return [_localize(x) for x in o]
    if isinstance(o, tuple): return tuple(_localize(x) for x in o)
    if isinstance(o, dict): return {k: (v if k in ("slug", "title", "meta", "schema", "trail", "icon", "type", "id") else _localize(v)) for k, v in o.items()}
    return o
CONFIG["pages"] = _localize(CONFIG["pages"])
assert _used == set(LOCAL_EDITS), f"LOCAL_EDITS not found in A's copy: {set(LOCAL_EDITS) - _used}"
for P in CONFIG["pages"]:
    if P["slug"] in LOCAL_TITLES: P["title"] = LOCAL_TITLES[P["slug"]][0]; P["exact_title"] = True
    if P.get("service") in SVC_TITLES: P["title"] = SVC_TITLES[P["service"]]; P["exact_title"] = True
CONFIG["legal_from"] = "veritas-pi"   # same Privacy Policy draft as Option A
