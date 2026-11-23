# Veritas Investigative Group: rebuild notes

Owner: Mark Henson · Lexington, SC (service area, address hidden) · (803) 904-1755 · mark@veritaspigroup.com
Domain: veritaspigroup.com (GoDaddy, not live, not connected) · SLED License No. 4362

- Build: `python3 build.py veritas-pi` → `dist/veritas-pi` · Preview: `python3 build.py veritas-pi --preview`
- Branch: `veritas-pi-group` (not merged). `launched` is off. `--check`: no blockers.
- Source: 14 GHL preview pages (never live). **All body copy is verbatim from GHL and client-approved.** Only titles, meta descriptions, alt text, schema and links were added.

## Page map (same pages and order as GHL)

| # | GHL page | New URL |
|---|---|---|
| 1 | Home | `/` |
| 2 | Services | `/services/` |
| 3 | About | `/about/` |
| 4 | Founder | `/about/founder/` |
| 5 | Contact | `/contact/` |
| 6 | Private Investigations & Surveillance | `/services/private-investigations-surveillance/` |
| 7 | Attorney & Litigation Support | `/services/attorney-litigation-support/` |
| 8 | Insurance Investigations | `/services/insurance-investigations/` |
| 9 | Corporate & Business Investigations | `/services/corporate-business-investigations/` |
| 10 | Polygraph Services | `/services/polygraph-services/` |
| 11 | Critical Investigative Response | `/services/critical-investigative-response/` |
| 12 | International Investigative Services | `/services/international-investigative-services/` |
| 13 | Background & Due Diligence | `/services/background-due-diligence/` |
| 14 | Security Consulting & Risk Management | `/services/security-consulting-risk-management/` |

No redirects, because nothing was live or indexed.

## Before launch: must confirm

1. **Lead inbox.** The Web3Forms key (e088f1a2-…) sends to whatever email it was created with. If that's mark@veritaspigroup.com, check that the mailbox exists. The domain isn't live, so email on it may not be set up at GoDaddy yet. If it isn't, leads will bounce. Send a test from the preview once the inbox works. Network limits meant no test submission could be sent from the build environment.
2. **Hero photo.** GHL uses a dark skyscraper photo behind every service hero. It couldn't be exported (GHL serves it as a CSS background), so the preview uses a navy/gold CSS background instead. Download it from the GHL media library and save it as `clients/veritas-pi/assets/hero.jpg` (about 1920px wide). The build picks it up automatically. Also confirm it's a licensed stock image and not a GHL AI/template image.
3. **Logo.** The only file supplied is the 470×160 LinkedIn cover (`source/logo-original.png`). It was trimmed to `assets/logo.png`, but it's soft on retina screens. Get a transparent PNG at 1000px+ or an SVG (Mark said there are other versions). The favicon and touch icon are cropped from the shield.
4. **FCRA.** The Background FAQ says screening is "compliant with ... the FCRA". If Veritas supplies background reports to employers for hiring decisions, it may count as a consumer reporting agency under the FCRA, with its own obligations. Mark should confirm this with counsel.
5. **Polygraph.** The page says "Veritas examiners each bring 25+ years". Confirm there is more than one examiner, and get their credentials (e.g. APA membership, federal polygraph school) if Mark wants to show them.
6. **License, bond and insurance.** SLED No. 4362 and "Licensed, Bonded & Insured" appear site-wide. Verify the license number on SLED's lookup and that the bond and insurance are current.
7. **"© 2026" is hard-coded** (verbatim from GHL). It goes stale in January. Approve a switch to an auto year.
8. **About submenu label.** The GHL About dropdown's child label wasn't visible, so it's shown as "Founder" (the GHL page title).

## Placeholder / template content flagged

- The phone placeholder `+1 (555) 000-0000` in the contact form is the GHL default. It's only a placeholder, not shown as a number, and was kept.
- The Services page lead says "**Veritas Group** provides…"; everywhere else says "Veritas Investigative Group". Kept verbatim.
- No fake testimonials, stock team names or lorem ipsum were found. The phone number and SLED number are consistent on every page.
- No GHL code, form, chat widget or tracking was carried over.

## What changed vs. GHL (markup and UX only, no copy)

- **One H1 per page.** GHL's home hero was three separate H1s; it's now one H1 on three lines. FAQ questions moved from H4 to accordion buttons, so there are no skipped heading levels.
- **Links added on existing words:**
  - Services-page "Learn More" and the home discipline tiles were plain text in GHL; they now link to their pages.
  - "Our Philosophy", "Critical Investigative Response" and "Background & Due Diligence" link where the copy mentions them.
- **Contact form** posts to Web3Forms with the same fields: First/Last optional; Phone, Email and Nature of Request required. Each submission carries first-touch UTM/gclid attribution and pushes `generate_lead` to GTM. The success and error messages are kit wording ("Thanks! We got your request…" / "please call…").
- **Header and footer** match GHL. The nav dropdown is navy with gold hover instead of GHL's white box. The mobile hamburger menu is new, and so is a fixed **Call / Contact bar** on phones.
- **Removed GHL scroll animations,** which hid text until scrolled into view, and the GHL load weight. Fonts are self-hosted: Instrument Serif (synthetic bold, as GHL renders it) and Work Sans.
- **Not added:** privacy policy, thank-you page, breadcrumbs (schema only), reviews. A privacy policy is recommended because the form collects personal data. Add `legal_pages` + `legal/privacy-policy.md` once the client approves the text.

## SEO added

- Unique titles (≤ 60 chars) and metas (≤ 155) per page, targeting "<service> + South Carolina / Lexington SC".
- Schema:
  - ProfessionalService business with areaServed (Lexington, Columbia, South Carolina), the SLED license as `hasCredential` + `identifier`, founder, slogan and knowsAbout.
  - Every page: WebPage + BreadcrumbList.
  - Service pages: Service with an OfferCatalog of sub-services, plus FAQPage from the existing Q&As.
  - Founder page: Person (Mark Henson, memberOf the 5 associations).
  - About, Contact and Services hub: AboutPage, ContactPage and CollectionPage + ItemList.
- Sitemap, robots and canonical tags on veritaspigroup.com. Share image: `assets/og-image.jpg` (logo on navy).

## Suggested copy changes (NOT applied: for Mark's approval)

1. **No local wording in the body copy.** "Lexington" and "Columbia" never appear on the site; only "South Carolina". This is the biggest ranking gap for "private investigator Lexington SC / Columbia SC". Even one line on the home page and the PI page ("based in Lexington, serving Columbia and the Midlands") would help.
2. **The home "Confidential Consultation" card repeats the H2 and lead word for word** right beside them. Suggest card text like "Free, confidential first conversation. Call (803) 904-1755."
3. **Reviews:** none yet. Once GBP is set up, add 2–3 real reviews (attorneys/adjusters especially).
4. **Small wording fixes:**
   - Hero and card copy use " - " where the rest of the site uses "—".
   - "conducted objectively" repeats "objective" in Internal & Workplace Investigations.
   - Nav label "Critical Invest Response" is abbreviated.
   - "Veritas Group" on Services (see above).
5. **Photo of Mark** on the Founder page. PI clients hire the person; a professional headshot builds trust.
6. **Response-time promise** (e.g. "calls returned same business day") if Mark can commit to it.

## Tracking

- GTM `GTM-KF4BGX7C` (client's own account) is on every page.
- Web3Forms submits push `generate_lead`. In GTM, add the GA4 tag + a `generate_lead` event (key event) + a `tel:` click trigger (`phone_click`), per the project's GTM/GA4 guide.

## Kit additions (generic, every client can use them)

- `layout: "sections"`: pages built from ordered content sections in `CONFIG["pages"]` (hero, text with creds/list, audience cards, service grid, items, steps, bullets, faq, numbered, split_cta, cta, contact form). The nav and footer come from config. Intended for client-approved copy that must be used word for word.
- Fonts `instrument-serif` and `work-sans`, with italic files (`<font>-italic.woff2`). Single-weight fonts get synthetic bold.
- Lead form options:
  - `name_split` (first/last), `name_required`, `first_label`/`last_label`, `email_label`
  - `placeholders`, `message_required`, `submit_class`; `note` is now optional
- `business.area_served`, `business.schema_extra`, and `exact_title` on pages.
- All reference clients still build unchanged.
