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

## Before launch: status (updated Nov 24)

1. **Lead inbox:** confirmed working (mark@veritaspigroup.com). Still send one test lead from the live domain at launch.
2. **Hero photo (Option A):** on hold. The team likes it without the photo, so the CSS navy/gold background stays. Drop a photo in `assets/hero.jpg` only if that changes.
3. **Logo:** a transparent cut of `02_horizontal_logo` is in use (see below). Better source files are still to be discussed with Mark.
4. **FCRA wording** on the Background FAQ: still open. Undecided whether counsel should review.
5. **Polygraph "examiners" (plural):** confirmed correct per Mark's master content document.
6. **SLED License #4362:** confirmed current and correct.
7. **Copyright year:** now automatic. The footer uses `{year}`: the build fills the current year and `site.js` updates it on every visit.
8. **About > Founder** label: approved.
9. **Email added for Mark's review:** mark@veritaspigroup.com in the footer contact block and as a button beside "Call Veritas" on the Contact page (`footer.show_email`, contact section `show_email`).
10. **Privacy Policy: DRAFT for Mark's approval** at `/privacy-policy/` (`legal/privacy-policy.md`), linked in the footer. It covers the contact form (Web3Forms), Cloudflare hosting logs, Google Tag Manager/Analytics, campaign attribution stored in the browser, no selling of data, legal-process disclosure, retention, security, children and contact details. Not legal advice; Mark (or his attorney) should approve it before launch. Update "Last updated" when approved.

**Copy changes applied Nov 24 (client rules, both options):**
- Name pattern: "Veritas Investigative Group" or "Veritas" only. The Services page lead "Veritas Group provides…" is now "Veritas Investigative Group provides…".
- Short dash: every em dash (—) in site content is now a short dash (-).

## Placeholder / template content flagged

- The phone placeholder `+1 (555) 000-0000` in the contact form is the GHL default. It's only a placeholder, not shown as a number, and was kept.
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
- **Not added:** thank-you page, visible breadcrumbs (schema only), reviews. The Privacy Policy draft was added Nov 24 (see above).

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

1. **No local wording in the body copy** (Option B now shows Lexington/Columbia wording, highlighted, for Mark to compare). "Lexington" and "Columbia" never appear on the site; only "South Carolina". This is the biggest ranking gap for "private investigator Lexington SC / Columbia SC". Even one line on the home page and the PI page ("based in Lexington, serving Columbia and the Midlands") would help.
2. **The home "Confidential Consultation" card repeats the H2 and lead word for word** right beside them. Suggest card text like "Free, confidential first conversation. Call (803) 904-1755."
3. **Reviews:** none yet. Once GBP is set up, add 2–3 real reviews (attorneys/adjusters especially).
4. **Small wording fixes:**
   - "conducted objectively" repeats "objective" in Internal & Workplace Investigations.
   - Nav label "Critical Invest Response" is abbreviated.
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

## Cloudflare previews (Nov 24)
- Both options get their own Pages project, built from branch `veritas-pi-group`. Option A: `veritas-pi` → `dist/veritas-pi`. Option B: `veritas-pi-b` → `dist/veritas-pi-b`.
- `preview_noindex: True`: while `launched` is off, each `pages.dev` preview sends `X-Robots-Tag: noindex` and a disallow-all robots.txt. This clears itself when `launched: True` is set.
- At launch: merge `veritas-pi-group` into main, switch the chosen project's production branch to `main`, delete the other project and client folder, then add the custom domain.
