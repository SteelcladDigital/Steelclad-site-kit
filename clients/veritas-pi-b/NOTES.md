# Veritas Investigative Group: Design Option B ("Brief")

A second look for Mark to choose from. **Pages, copy, SEO and integrations are imported from `clients/veritas-pi/site.py` (Option A) at build time**, so the wording is identical by construction (except the highlighted Lexington/Columbia proposals below). A script also compared the text inside `<main>` on all 14 pages of A and B: 0 differences. Only the theme, stylesheet (`core/sections-brief.css`) and four layout options differ.

Build: `python3 build.py veritas-pi-b` → `dist/veritas-pi-b`. Same URLs, same canonical domain (veritaspigroup.com). **Only one option ever goes live:** after Mark chooses, delete the other client folder (or, if B wins, move B's theme/options into `veritas-pi/site.py` and delete `veritas-pi-b`).

## Design direction and how it follows the voice rules
- **Light, document-like ("a well-set case brief")** instead of A's dark, cinematic skyscraper look. White pages, navy bands for the hero, calls to action and footer, gold only for rules, icons and accent words. It reads professional without being sterile, and it avoids the dark/noir and luxury-gold PI clichés.
- **Type:** Source Serif 4 headings with a real italic for the gold accent words; Inter body. Calmer and more legible than A's condensed display face, which suits "simple and direct".
- **Left-aligned section heads with a short gold rule**, like headings in a report. Confident without decoration.
- The home hero shows his actual shield (from `04_shield_v_icon`, upscaled to `assets/hero-shield.png`) beside the headline. No stock imagery, so no hero photo is needed (A still needs the GHL photo).

## UX improvements over A (no copy changes)
1. **Trust line above the fold:** a slim utility bar on every page reads "SLED License #4362. Licensed, Bonded & Insured." plus the phone. This **repeats** the existing footer line; it is not new copy, but flag it to Mark.
2. **Sticky "on this page" sub-nav on the 9 service pages.** The labels are the page's own H2s (What This Covers, How Veritas Works, …), and the link for the section in view is highlighted. Long service pages become scannable for attorneys and adjusters.
3. **Contact page split:** the form and "What Happens Next?" sit side by side, so people see the process while filling in the form (A stacks the process below the form).
4. **Whole audience cards are clickable** (A: only the small button). The nine-discipline index is a clean link list with arrows.
5. **Services hub as an index:** one row per service (name + link | summary | sub-services), which is easier to scan than A's card grid.
6. **"How Veritas Works" as a numbered timeline** (horizontal on desktop, vertical on phones); FAQs sit beside their heading on desktop.
7. Header call button and mobile Call / Contact bar kept; the mobile menu is white and full-height, with larger tap targets.

## Same as A
Form (Web3Forms, same fields, `generate_lead`), GTM-KF4BGX7C, schema, titles and metas, sitemap, and every before-launch item and copy suggestion in `clients/veritas-pi/NOTES.md` (FCRA, polygraph examiners, logo file, © year, local wording, privacy policy).

## Kit additions (generic)
- `theme.sections_css`: choose a sections stylesheet (`sections.css` default, `sections-brief.css` new).
- `sx_options`: `utility_bar` (text), `hero_mark` (True for a line-drawn shield, or an image file), `subnav` (service pages), `contact_split`.
- `source-serif-4` now ships an italic file. `site.js` adds the sub-nav scroll highlight (inert unless a sub-nav exists).
- Option A and all other clients build the same as before (verified by diff; only site.js gained the sub-nav block).

## Lexington / Columbia wording (Option B only, proposed Nov 24)
Mark's approved copy never names Lexington or Columbia, which limits local rankings. Option B mixes the cities in so he can compare. **This is proposed wording, not approved copy.** In the preview every insertion is **highlighted in gold** (`sx_options.highlight_edits`), and `--check` blocks launch while the highlight is on.

Body copy (12 short insertions, in `LOCAL_EDITS` in `site.py`):
- Home hero: "based in **Lexington, serving Columbia and all of** South Carolina"
- Home services lead: "people and organizations **in Lexington, Columbia and across South Carolina** who need answers"
- Services hub lead: "…government clients **in Lexington, Columbia and throughout South Carolina**"
- About: "private investigative work **in Lexington, Columbia and** throughout South Carolina"
- Hero leads on 7 service pages (Private Investigations, Attorney, Insurance, Corporate, Polygraph, Background, Security): "**in Lexington, Columbia and across South Carolina**" or similar. Critical Response and International are left alone because they aren't local services.
- Contact: added the sentence "**Based in Lexington, serving Columbia and all of South Carolina.**"

Page titles (not visible on the page, shown in Google results):
- Services: "Private Investigators in Lexington & Columbia, SC"
- About: "About Veritas | Lexington & Columbia, SC Investigators"
- Contact: "Contact a Lexington & Columbia, SC Private Investigator"
- 7 service pages: "<Service> | Columbia & Lexington, SC" (e.g. "Insurance Investigations | Columbia & Lexington, SC")

If Mark approves: set `highlight_edits` to False (and, if he picks Option A's design, move `LOCAL_EDITS`/titles into A). If he declines: delete `LOCAL_EDITS`, `LOCAL_TITLES` and `SVC_TITLES` and B is word-for-word A again.

## Other Nov 24 changes (shared with A)
Auto-updating © year, email in the footer and on Contact, draft Privacy Policy (`legal_from: "veritas-pi"`), "Veritas Group" → "Veritas Investigative Group", em dashes → short dashes. See `clients/veritas-pi/NOTES.md`.
