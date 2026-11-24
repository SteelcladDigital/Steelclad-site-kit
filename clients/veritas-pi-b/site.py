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
}
