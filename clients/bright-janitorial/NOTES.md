# Bright Janitorial Services: rebuild notes (Nov 19, 2026)

Static Site Kit rebuild of brightjs.net (GHL). Not live. `"launched"` is off.
Build: `python3 build.py bright-janitorial` → `dist/bright-janitorial`. Config: `site.py` (+ `services.py`, `areas.py`).
Forms: Web3Forms key `dab4b782-…431b` (vasylb@brightjs.net). Tracking: GTM `GTM-TP8G6H5L` (client's own account; GA4 `G-JQ13XPG8GG` lives inside GTM only). No GHL.

## Confirm with Vasyl before launch
1. **City pages (19).** Each has local facts (corridors, institutions, nearby employers like Scout Motors, BMW, Boeing, Volvo). Confirm he really takes recurring work in the Upstate, York County, Pee Dee and Lowcountry, and sanity-check each page. Remove any city he doesn't want calls from.
2. **Columbia has no city page on purpose** (the home page targets Columbia). Mount Pleasant appeared on the old site but isn't on his list, so it was left out. Add it back if he wants it.
3. **Hot-water carpet extraction** was added to the Floor Care page (the old site lists it; the approved .md didn't). Same for epoxy rejuvenation: not used. Confirm.
4. **Daycare & Education and Auto Dealerships** tiles were added to Facilities We Serve (from the current home page). The old "non-toxic, eco-safe sanitization **certified**" claim was softened, since no certifying body is named. Add the certification if there is one.
5. **Medical page:** written from the current page only. No OSHA/bloodborne-pathogen or HIPAA training claims were made. Add them if his team is trained.
6. **Hours / 24/7 emergency response / office address** (1931 Assembly St., 2nd Floor) carried over. Confirm the address matches the Google Business Profile exactly.
7. **Hero card** is a labeled *Example* of a written cleaning plan. Confirm he does put scope in writing after a walk-through (the old "custom documented plan" language suggests yes).
8. **Owner name and photo:** none published. A photo of Vasyl or the team would be the strongest trust upgrade available.
9. **Photos:** the six before/after photos are small (320–640px). Higher-resolution originals, and any jobsite/team photos, would help.
10. **Testimonials:** the three on the old site, kept with names and titles. Add the Google reviews link (`google_reviews_url`).
11. **Privacy policy:** rewritten for the new stack (Web3Forms, GTM, Cloudflare, SMS consent). It replaces the GHL-era policy at the same URL.
12. **Post-construction .md** linked to `/services/window-cleaning`, which doesn't exist. Swapped for Day Porter. Build a window cleaning page later if he wants that keyword.
13. The .md files' JSON-LD blocks are **not pasted**; the kit generates equivalent LocalBusiness + Service + FAQPage + BreadcrumbList on every page.

## Lead tracking (confirmed in a headless browser, Nov 19)
- On a **successful** Web3Forms submit, the form pushes `{event: 'generate_lead', form_name, lead_source}` to `dataLayer`, waits for GTM (`eventCallback`, 2 s timeout), then redirects to `/thank-you/` (noindex).
- On a failed submit: **no** event, a visible error with the phone number, and the button re-enables.
- Each submission also carries the page, landing page, referrer, UTMs, gclid and fbclid.
- In GTM: Custom Event trigger `generate_lead` → GA4 Event tag `generate_lead`, plus `phone_click` on `tel:` links (see the project's GTM guide).

## Design brief (niche benchmark)
Reviewed nationally: City Wide Facility Solutions (Nashville), Executive Cleaning Services (Columbia location page), Maintenance Resources Inc. (Denver, CIMS-GB), Anago (Austin/Denver), Jani-King, JAN-PRO, Vanguard. Locally: ServiceMaster Building Maintenance (Midlands), Jani-King Columbia, JAN-PRO Columbia, Enviro-Master, Palmetto Commercial Services, Carolina Cleaning Dynamics, C&W Janitorial.

Patterns the leaders share, and how this site applies them:
1. **City + service H1 with a trust row directly under it** (Executive, City Wide) → keyword H1, bonded/insured, 18 years, 90% referrals in the first screen.
2. **Two-path CTA everywhere** (quote + click-to-call) → yellow quote button in the header and every hero, phone in the top bar, sticky Call / Text / Quote bar on phones.
3. **Itemized "what's included" task lists** (City Wide) → every service page lists the tasks done each visit.
4. **Industries grid that links to service pages** (City Wide, Executive) → Facilities We Serve with 10 facility types, each linking to the matching service.
5. **Quote form that qualifies the lead** (Executive's frequency dropdown) → facility type, service and frequency selects, on the home page and the contact page.
6. **Named QA/process** (MRI's walkthroughs) → a four-step "How we work" (listen, written plan, same team, accountability).
7. **FAQs on every page** → FAQPage markup throughout.

Where local competitors are weak (the gap): franchise pages with generic copy, stock photos (ServiceMaster's Columbia page uses an image labeled "Lakeland"), no named testimonials, no visible process, few or no city pages, broken text. Bright now has **real before/after photos, named commercial testimonials, named products and equipment (Diversey, Kärcher, Pro-Team HEPA), 19 city pages, a link-worthy cleaning checklist, and full schema**.

**Brand:** the client's teal `#4d9db5` header is kept. White nav text on that teal fails contrast, so the nav uses deep navy text, and the logo sits on a white plate so its royal blue `#0700b2` and sun yellow `#fed91b` read at full strength (the issue from the GHL build). Dark sections use a deep royal navy drawn from the logo; buttons use the logo yellow with navy text. Fonts: Outfit + Inter.

**Later upgrade ideas:** a team/owner photo hero (`hero_layout: image`) once there's a good photo; an inspection/QA report sample; case-study pages per facility type; a blog targeting question keywords (e.g., "how much does office cleaning cost in Columbia SC").

## Old site vs new site
| | Old (GHL) | New (Site Kit) |
|---|---|---|
| Structured data | `meta-schema:type` tag only, no JSON-LD | JSON-LD on every page: LocalBusiness/ProfessionalService, Service, FAQPage, BreadcrumbList, ContactPage, Article |
| H1s | Duplicates (home had 2; About, Retail, Medical each had a second "Office Cleaning" H1) | Exactly one keyword H1 per page; clean H1→H2→H3 |
| Titles/metas | Medical page's title was about office cleaning; metas over length | Unique title ≤60 and meta ≤155 on all 36 pages |
| Pages | 12 | 36: same 12 + contact, thank-you, service-area hub, 19 city pages, cleaning checklist |
| City pages | 0 | 19 |
| Forms | GHL form | Web3Forms → vasylb@brightjs.net, with spam trap, error fallback, attribution and `generate_lead` |
| Tracking | GHL | Client's own GTM |
| URLs | — | All 12 kept; misspelled `/services/commecial-retail-spaces` 301'd; plus `/home`, `/index`, `/contact-us`, `/quote` |
| Mixed www/non-www links | Yes | One canonical (`https://brightjs.net`); set www → apex redirect in Cloudflare |
| Speed | GHL builder JS, stock hero photo | Static HTML, self-hosted fonts, small CSS/JS, lazy-loaded photos |
| Mobile | Standard | Sticky Call / Text / Free Quote bar |

## Launch steps
1. Vasyl approves the preview → `python3 build.py bright-janitorial --check` shows READY.
2. Cloudflare Pages project `bright-janitorial`: build `python3 build.py bright-janitorial`, output `dist/bright-janitorial`. Test a lead on `*.pages.dev` (Web3Forms domain restriction off until launch).
3. Domain: registrar is GoDaddy (email is also GoDaddy). **Keep the GoDaddy MX/email DNS records** when moving DNS to Cloudflare, or only point the web records. Add `www` → apex redirect.
4. Set `"launched": True`, push. Live test lead + GTM Preview. Search Console: verify, submit sitemap, request indexing. Update the GBP website link.
