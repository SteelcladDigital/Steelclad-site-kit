# Carolina Outdoor Services: rebuild notes

Owner: Nicky Waters · Carolina Outdoor Services, LLC · 1318 Peach Festival Road, Gilbert, SC 29054 · (803) 518-2787 · csas2787@gmail.com
Domain: cosstormwater.com (registrar GoDaddy) · Email: Gmail · No GoHighLevel items kept (forms, tracking, chat all off GHL).

- Build: `python3 build.py carolina-outdoor` → `dist/carolina-outdoor`
- Preview: `python3 build.py carolina-outdoor --preview`
- Forms: Web3Forms key `9b342499-…445c` (client's Gmail) → `/thank-you/`, pushes `generate_lead` to the dataLayer
- Tracking: GTM `GTM-578PKL83` (GA4 goes inside GTM, see claude/gtm-ga4-client-setup.md)
- Status: **preview only** (branch `carolina-outdoor`). `launched` is off. Not connected to Cloudflare yet.

## Before launch: must do (blockers)

1. **Migrate 15 blog posts.** Two are migrated (`how-often-should-a-retention-pond-be-inspected`, `what-is-sustainable-stormwater-management`). The other 15 are draft stubs in `posts/` with `migrate_from` links, and `--check` blocks launch until each is filled in (their URLs would 404). Copy each body, set the real date, tag `services:` and `areas:`.
2. **Confirm the testimonials.** The old site shows 15 five-star "reviews" with first name + last initial and town, but none appear on Google, and several read like template copy (e.g. "game-changer for our industrial property", lawn and tree-trimming reviews for a stormwater-only company). Only 6 stormwater-relevant ones are used. **Ask Nicky if each is a real client.** If not, remove them and use Google reviews instead. Don't launch with unverified reviews.
3. **Master Pond Manager.** The site says Nicky is a "Clemson Extension Certified Master Pond Manager" (full certificate track). Confirm he completed the full certificate (with exam), not the Letter of Completion track, and the year.
4. **Sustain SC.** Confirm the membership is current and under the company name, and ask whether Sustain SC lists members (a link back from their Member Network page would be a strong local citation).
5. **SC contractor license.** The old site shows an "SC Contractor Licensed" badge but no number. Get the license type and number if he has one; otherwise the site only says "licensed and insured".
6. **Web3Forms:** confirm the key is verified in csas2787@gmail.com, send a test from the preview, and add a Gmail filter so Web3Forms mail never goes to spam.

## To confirm with Nicky (facts the copy relies on)

- 2004 founding, "12+ years" stormwater-focused, owner name Nicky Waters (taken from the old area pages)
- Hours Mon–Fri 7–5; response "within one business day"
- Free site assessment; no travel surcharge for Greater Columbia (from the old Columbia page)
- Forestry mulching capacity: trees up to ~6–8" diameter, 2–4" mulch layer (old site)
- Area pages (11 new): Gilbert, Blythewood, Aiken, North Augusta, Greenville, Spartanburg, Anderson, York County, Midlands, Upstate, North Carolina. Each has distinct local copy built on cited county rules (Lexington annual checklist, Richland 30-day NOV, Greenville County maintenance plans, Fort Mill HOA handbook, NC annual SCM reports). Have him confirm he takes work in each, and how far into NC he goes.
- Photos: the 13 gallery photos were pulled at the size GHL served them (~700px). **Ask for the full-size originals**, plus before/after pond photos and a photo of Nicky or the crew for the About page.
- The old "Asset vs Liability" before/after sliders were AI-generated images. They were not carried over.
- Google Business Profile: send the Maps link (`google_reviews_url`) and the "ask for reviews" link (`google_review_write_url`).

## Nice to have later

- LinkedIn (Nicky's profile) in `business.social` if he wants it in schema sameAs
- A Master Pond Manager / credentials badge image from Clemson, if they provide one
- A NC-specific blog post on annual SCM inspection reports (Charlotte, Gastonia), to support the NC page

## Design brief (niche benchmark)

**Local competitors reviewed:**
- **Aqueous Environmental** (aqueousenv.com, Lexington SC, Wix). 100+ Google reviews shown as a badge only, Post-Construction BMP + EPSC certs, Master Pond Manager listed as *pending*. No city pages, FAQs, blog or prices; nav links broken; phone number mismatch.
- **Dragonfly Pond Works** (multi-state, since 2006). Strong "one partner" hero, consultation form under the hero, association logos (CAI, BOMA, Southeast Stormwater Assn). No reviews, no certifications, no visible FAQ or blog.
- **Carolina Storm Water Services** (carolinastormwater.com, Chapin). 2008-era PHP site with a placeholder H1 ("H1 text here"), dead CTA, phone only in the footer, no form. Ranks on its exact-match domain and age, not its content.

**National benchmark (best-in-class pond/stormwater operators):** SOLitude Lake Management (stormwater inspection & maintenance pages, HOA-specific landing pages, deep FAQs and education content), Dragonfly Pond Works (single-partner positioning, association proof), and municipal/extension guides (Clemson HGIC, Greenville County, Fort Mill) that rank for "who maintains a stormwater pond".

Patterns they share, and how they're applied here through COS's own brand:
1. **Lead with the deliverable, not the mowing.** Top operators sell the inspection report and compliance record. → The hero card is an (Example-labeled) inspection report: outlet, forebay, berm, photos, "fix now · monitor · plan".
2. **Credentials as proof, linked to the issuer.** → New "Certified for stormwater, not just mowing" section with linked cards for Master Pond Manager (Clemson), SC BMP inspector, plan reviewer, NC State SCM, Sustain SC. Also in schema (`hasCredential`, `memberOf`), the trust bar, hero proof and every sidebar. None of the local competitors do this; Aqueous's MPM is still pending.
3. **Education that ranks.** → A cited SC pond owner's guide (`/stormwater-pond-guide/`) covering Lexington, Richland, Greenville, York, Aiken and NC rules, plus a season checklist.
4. **Location pages with real local substance.** → 14 area pages (3 kept + 11 new) grouped Midlands / Aiken / Upstate / York & NC, each citing that county's program. No competitor has any.
5. **Clear, repeated path to one offer.** → "Free Site Assessment" everywhere, sticky mobile Call/Text/Assessment bar, form on the home page, 4-step process.
6. **Real photos, no stock.** → 13 job photos from his gallery across home, services, gallery and about.

**Kept from the current site (to avoid change anxiety):** slate header (#333946), green buttons, sky-blue accent from the logo, round logo, uppercase headings, "asset or liability" message, FAQs, testimonials, same nav order and every URL.

**Bolder visual ideas for later:** a full-width photo hero (needs a high-res pond photo), a drone shot of a maintained pond, and a downloadable PDF version of the pond checklist for HOA boards.

## Old vs. new

| | Old (GHL) | New (Site Kit) |
|---|---|---|
| Schema | None useful | LocalBusiness + HomeAndConstructionBusiness, credentials, memberOf, areaServed, Service, FAQPage, BreadcrumbList, BlogPosting, ImageGallery |
| H1s | Home H1 + duplicate uppercase/title-case sections; blog posts with body text marked up as H3s | One keyword H1 per page, clean H1→H2→H3 |
| OG tags | Service pages carried the About page's OG title | Page-specific titles, metas, OG image |
| Pages | ~16 + blog | 36 built (7 services, 14 areas, guide, gallery, blog, legal) |
| Area pages | 3 (Lexington, Columbia, Rock Hill; Columbia's ditch section was a copy of the mulching text) | 14, each with distinct local content |
| Credentials | 2 badges, both with alt text "SC Contractor Licensed" | 4 certifications + Sustain SC, linked and in schema |
| Master Pond Manager / Sustain SC | Not mentioned | Home, About, trust bar, sidebars, FAQ, guide, schema |
| Forms | GHL form | Web3Forms (to the client's Gmail) + thank-you page + `generate_lead` |
| Tracking | GHL | GTM-578PKL83 |
| Speed | GHL page builder, external image CDN | Static HTML on Cloudflare, self-hosted fonts, WebP photos |
| CTAs | Mixed ("Get Inspection Now", "Mulching Estimate", header phone only) | One offer (Free Site Assessment), header button, sticky mobile bar |
| URLs | — | All kept: /services/<slug>, /lexington-sc, /columbia-sc, /rock-hill-sc, /gallery, /blog, /post/<slug>, /blog/category/<slug>, /privacy-policy, /about, /contact. Duplicate top-level service URLs 301 to /services/<slug>/; /blog/author/* and /blog/tag/* 301 to /blog/ |

## Kit changes made for this client (generic, all clients benefit)

- `areas.pages[]` can set `region` (e.g. "NC"), `title`, `meta`, `h1`, `crumb`, `place_type`, `place_name` for regional/out-of-state pages; `zips` optional.
- `business.credentials` → `hasCredential`; `business.member_of` → `memberOf` in schema.
- `home.credentials` section (linked credential cards; add `"credentials"` to `home.order`).
- Verified: palmetto-pool, teal-outdoor and steelclad-digital build byte-identical apart from dates.
