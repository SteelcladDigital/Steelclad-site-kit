# Steelclad Digital (steelcladdigital.com): rebuild notes

The agency's own site, and the first site off GoHighLevel. Built Nov 15, 2026 from the live GHL site, its Terms of Service and Privacy Policy.

- Build: `python3 build.py steelclad-digital` → `dist/steelclad-digital/`
- Forms: **Web3Forms** (`form_mode: "web3forms"`), no GHL anywhere on the site.
- Positioning: the only Lexington-area agency we found that **publishes its prices**, focuses only on home services, and is owner-operated and month-to-month. The site is built around that.

## Before launch: decisions and facts to confirm

**Blockers (the build will refuse to launch without these):**
1. ~~**Web3Forms access key**~~ Done (Nov 16). The key was created with **steelcladdigital@gmail.com**, so every lead is emailed there. To send leads to team@ instead, create a new key with that address and swap it in `integrations.web3forms_access_key`.
2. ~~**GTM container ID**~~ Done (Nov 16): `GTM-KP9LD8WV` (Steelclad-owned account; replaces GTM-MKD488Q8, which sat under the TruePoint client account). GA4 property 564521555, Measurement ID `G-6JBYXY9Z86` (Steelclad-owned), configured inside GTM, not in the site config. In GTM: GA4 config tag, a GA4 event tag on the `generate_lead` dataLayer event (mark it as a key event in GA4), or count page views of `/thank-you/`.

**Facts to confirm:**
3. **Exit fee conflict.** The old /pricing page says a one-time **$500 exit fee**. Your Terms of Service (Section 8) say **no cancellation fee**, with migration help quoted only if you ask. The new site follows the Terms. If the $500 fee is real, the Terms need updating too.
4. **Call length.** The old site said both 20 and 30 minutes. The new site says **30 minutes** everywhere.
5. **"Lead capture and automated follow-up"** is listed in Foundation (from the old pricing page). That was GHL. Confirm what delivers automated follow-up for clients after you leave GHL, or reword it.
6. **Setup fee amount** isn't published (it wasn't on the old site either). Publishing it would make the pricing page even stronger; nobody local does.
7. **Owner name.** The old About page's photo alt text says "Founder Marcus Vance" on what looks like a stock photo. If that's the owner, add `"founder"` in `business` plus a real photo and a short bio (big trust and E-E-A-T win for an owner-operated agency). If not, nothing on the new site uses it.
8. **City pages** (Lexington, Columbia, West Columbia, Cayce, Irmo, Chapin) assume you take clients in all six. The local notes are general market observations, not stats. Remove any city you don't want work from.
9. **"Do you only work with businesses in South Carolina?"** The answer on the new strategy-call page is a proposal ("Midlands and across SC, reach out anyway"). The old answer wasn't readable.
10. **Phone number (803) 205-2732.** If it's a GHL/LeadConnector number, **port it out before cancelling GHL**, and re-register A2P texting with the new provider. The SMS consent text on the form was kept from the old form.
11. **Privacy Policy**: migrated as-is, plus one sentence naming Web3Forms as the form processor, and a new Last Updated date (Nov 15, 2026). Review it.
12. **Logo** was redrawn as SVG from the live header. Drop the original file in `assets/` and switch `logo.type` to `image` if you prefer.

**Reviews (you can't solicit Google reviews under your current contract):** the site has no reviews section and no review markup, and nothing invented. It earns trust with published prices, month-to-month terms, ownership of everything, direct owner access, a free checklist and a transparent process instead. Options that don't involve asking for Google reviews (check your contract first): written client testimonials or short case studies on-site with permission; a portfolio of sites you've built (only with each client's OK).

## Old vs new

| | Old (GHL) | New (Site Kit) |
|---|---|---|
| Platform | GoHighLevel page builder | Static HTML on Cloudflare Pages, self-hosted fonts |
| Home page weight | Page-builder scripts + large hero images | ~139 KB total (HTML 8.7 KB gzipped, CSS, JS, 2 fonts), no third-party scripts until GTM |
| Indexable pages | 15 pages + 6 posts + 3 category pages | 32 (+ noindex thank-you page) |
| City pages | 0 | 6, each with its own local copy and FAQ |
| Free resource | none | Local Visibility Checklist (link bait + lead magnet) |
| Schema | Blog type on /blog (others not verified) | LocalBusiness + ProfessionalService with **priced monthly offers**, Service per service page, FAQPage, BreadcrumbList, BlogPosting, CollectionPage, ContactPage |
| H1s | Paid Advertising page had its H1 three times | Exactly one H1 per page, no skipped heading levels |
| Titles | Several over 60 chars | All ≤ 60, metas ≤ 155 |
| Pricing | Plans published, but not in structured data | Plans + add-ons + comparison table + plan finder quiz; prices in schema |
| CTAs | Mixed targets (/strategy-call vs /contact), 20 vs 30 min | Every CTA → /strategy-call/; lead form on the home page; sticky Call/Text/Book bar on mobile |
| Lead capture | GHL form | Web3Forms email + first-touch attribution (landing page, referrer, UTMs, gclid, fbclid), `generate_lead` event, /thank-you/ page |
| Internal linking | Footer/nav only, posts linked to /contact | Posts ↔ services ↔ city pages cross-linked; category archives; related posts |
| Copy issues | Internal editing notes visible on Paid Advertising page ("No changes needed... keep it exactly as is") | Removed |

## URLs

All old URLs are kept as real pages (Cloudflare serves `/about` → `/about/`, a single permanent hop):
`/`, `/about`, `/services`, `/services/website-design`, `/services/local-seo`, `/services/google-business-profile`, `/services/social-media`, `/services/review-management`, `/services/paid-advertising`, `/pricing`, `/strategy-call`, `/contact`, `/blog`, `/blog/b/<6 posts>`, `/blog/c/reviews`, `/blog/c/local-seo`, `/blog/c/lead-generation`, `/privacy-page`, `/terms-of-service`.

New: `/areas-we-serve/` + 6 city pages, `/local-visibility-checklist/`, `/thank-you/` (noindex).
301s (`_redirects`): `/blog/b` and `/blog/c` → `/blog/`; `/privacy`, `/privacy-policy` → `/privacy-page/`; `/terms` → `/terms-of-service/`.

## Blog migration

All 6 posts migrated at their exact URLs with their original text, plus light edits: em-dash punctuation, CTAs now point to /strategy-call/, cross-links between related posts, rewritten meta descriptions (≤ 155), category "local SEO" displayed as "Local SEO" (URL unchanged). One unsourced stat ("over 70% of local searches happen on mobile") was softened to "most local searches happen on a phone".

Next posts should target questions the service and city pages can't (e.g. "how much does SEO cost for a contractor in SC", "Google Business Profile suspended: what to do"), tagged with `services:` and `areas:`.

## Launch steps

1. Fill the two blockers above, then `python3 build.py steelclad-digital --check` → READY TO LAUNCH.
2. Cloudflare: Workers & Pages → Create → Pages → Connect to Git → `Steelclad-site-kit`. Project `steelclad-digital`, framework None, build `python3 build.py steelclad-digital`, output `dist/steelclad-digital`. Review on `steelclad-digital.pages.dev`.
3. Send a test lead from the pages.dev URL; confirm it arrives at steelcladdigital@gmail.com (check spam once) with page + UTM fields.
4. Custom domain: add `steelcladdigital.com` in the Pages project. **Copy the existing MX/TXT records first** so team@ email keeps working when DNS moves off GHL.
5. Set `"launched": True`, push, and resubmit `https://steelcladdigital.com/sitemap.xml` in Search Console.
6. Point your social scheduler's RSS feature (if it has one) at `/blog/rss.xml`.
