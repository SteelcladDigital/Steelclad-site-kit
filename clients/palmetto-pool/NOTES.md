# Palmetto Pool Solutions: client notes

Owner: Mike Brazell · Lexington, SC · (803) 394-0765 · palmettopoolsolutions@gmail.com
Build: `python3 build.py palmetto-pool` → `dist/palmetto-pool` · Preview: `python3 build.py palmetto-pool --preview`
Status (Nov 19, 2026): **refreshed to the current process, not launched.** Branch `palmetto-refresh-nov-2026`, not merged to `main`. `launched` stays `False`.

## What changed in the Nov 19 refresh

- **Forms → Web3Forms.** The access key `e088f1a2-…-3e348ce9e112` was created with palmettopoolsolutions@gmail.com, so leads go straight to Mike. Successful sends go to `/thank-you/` (noindex). The form has an optional SMS-consent checkbox to match his existing SMS terms.
- **Tracking → GTM-K3752MP5** in Mike's own Tag Manager account, on every page.
  - Verified in a headless test: a successful submit pushes `{event: "generate_lead", form_name, lead_source}` to the dataLayer.
  - It fires only after Web3Forms confirms the send. The page waits for GTM's eventCallback (1.5 s cap) before going to the thank-you page.
  - Failed sends push nothing and show "please call or text".
- **GHL removed.** There's no GHL form, chat or tracking script, and no GHL comments in the HTML. The kit now drops all GHL hooks in Web3Forms mode.
- **Blog migrated.** All 8 posts carry their full text at their exact `/post/<slug>` URLs (draft flags removed).
  - Links inside the posts pointed at URLs that 404 on the old site (`/weekly-pool-maintenance`, `/pump-filter-services`, `/green-to-clean`, `/contact`). They now point at the real pages, and those old paths 301 too.
  - Light fixes only: one typo ("At Palmetto Pool Solutions, CPO certified" → "we're CPO certified"), H4s changed to H2s, and the repeated sign-off kept.
  - The authors match the live site (Mike on 4 posts, "Palmetto Pool Solutions" on 3, plus the new salt post).
  - Post images were not carried over (the old ones are GHL-hosted). Add real photos via `image:` when available.
- **Category URLs kept** as real pages at `/posts/category/<slug>` (5 categories). `/posts/author/*` 301s to `/about/` and `/posts/tag/*` to `/blog/`.
- **Legal pages done** in `legal/`:
  - Terms: migrated from the live page. The SMS section was kept and tied to the new consent checkbox, and the email link was fixed (it pointed at contact@).
  - Accessibility: migrated, with the known limitations updated.
  - Privacy: rewritten for the new stack (Web3Forms, Google Tag Manager/Analytics, Cloudflare), keeping the SMS no-sharing clause. **Mike should read all three.**
- **Real logo** (white knockout cut from his JPG) on a header in his exact logo navy, `#1b227d`. The SVG redraw is gone.
- **Real photo of Mike** (parade float) in the hero chip, the homepage owner story, the About page and the share image (`og-image.jpg`).

## Decisions from Steelclad (Nov 19, 2026)

- **No GHL anywhere.** Each page's HTML has no GHL scripts, forms, chat, comments or links. The built site.js no longer ships the GHL native-form handler (kit now strips it unless `form_mode` is `native`). The only outside hosts in the HTML are Web3Forms, Google Tag Manager, Mike's Google review link, Facebook, Instagram and schema.org. Every old GHL-era URL is kept or 301-redirected, so nothing breaks.
- **(803) 394-0765 is Mike's own number.** Nothing needs porting.
- **Google reviews link:** https://g.page/r/CSSJuhDXidrPEBM/review. The button reads "Read or leave a review on Google", because that link opens his reviews with the write-a-review box.
- **Plans stay, with no prices.** Mike does not want prices on the website. Watch his reaction to having the plans themselves on the site; they can be removed.
- **Meet the team: spring 2027.** `about.team` is ready when names and photos come in.
- **Service area = all of Lexington County, plus Richland routes.**
  - New city pages for Gilbert (29054) and Batesburg-Leesville (29006, 29070), each with its own local copy.
  - The Lexington County box also lists Swansea, Pelion, Gaston, Pine Ridge, South Congaree, Springdale, Summit, Red Bank, Oak Grove and Seven Oaks, "and every other community in Lexington County". These are in the schema areaServed too, but they have no pages, to avoid thin doorway pages.
  - Add a page for any of them later if Mike has real work or local detail there.
- **Door hanger:** now matches Mike's real hanger.
  - The hero card mirrors its checklist, service comments and "date of next service". The old example "readings" (chlorine/pH numbers) were removed, since the real hanger doesn't record them.
  - Every "your readings" claim on the site was corrected.
  - The real hanger image is on the Weekly Pool Maintenance page.

## Before launch: still open

1. **Reviews from other towns:** all three real reviews are from Lexington. Ask Columbia, Irmo, Chapin and Gilbert customers for Google reviews (his review link makes it easy), then add them to `REVIEWS` with their town.
2. **Plan names and inclusions** (Balance / Full Service / Full Service Plus) are still a proposal for Mike to react to.
3. **A formal guarantee?** Only if Mike wants one. Today the site uses his real promises only.
4. **One factual check in a migrated post:** the October closing post says cracked return lines are "a five-to-six figure surprise". That's likely high.
5. **City facts:** Mike should sanity-check the neighborhood and local mentions on the 10 city pages, especially the new Gilbert (Peach Festival, well water) and Batesburg-Leesville pages.
6. **Legal pages:** Mike reads Privacy, Terms and Accessibility.
7. **GTM setup** (per the GTM + GA4 doc): GA4 tag, a `generate_lead` GA4 event tag, phone-click tag, Preview test on pages.dev, publish. Mark `generate_lead` and `phone_click` as key events.
8. **Web3Forms:** one test lead from the pages.dev preview, and mark the sender as safe in his Gmail. (The claude.ai preview can't send forms; its host blocks outside requests.)

## Design brief: national polish, local heart (Nov 19, 2026)

**Benchmarks reviewed:**
- National brands: ASP – America's Swimming Pool Co. (its homepage is behind a bot check, so its location and maintenance-plan pages were reviewed), Poolwerx, and Pool Scouts.
- Top-rated independents: Endless Blue Pools (Round Rock/Austin, TX), The Pool Police (Austin, TX), The Good Pool Company (Scottsdale, AZ), Aqua Burst Pools (Orlando, FL), Aquatec Pool Service (Tampa, FL) and Diamond Pool Service (San Diego, CA), reviewed through their sites and directory listings.

| National pattern | How the franchises do it | How Palmetto does it (made local) |
|---|---|---|
| Proof in the first screen | Pool Scouts: a "thousands of 5-star reviews" banner; independents: rating and licence chips | Eyebrow "Family-owned in Lexington County, SC". The proof line leads with "Serving Lexington & Richland counties", and the trust bar opens with "Family-Owned · Lexington County". No made-up review counts. |
| Named plans plus a comparison | Poolwerx Gold/Silver/Bronze; ASP maintenance plans | Three plans with a comparison table and plan-finder quiz, still built only from services Mike already sells, with one flat monthly rate after a free evaluation. |
| Visit reports | ASP's app-based digital reports; Pool Scouts' post-service reports | Mike's paper **door hanger** is the hero visual (labeled "Example"), with Midlands notes like "pine pollen heavy this week". It's personal, not an app. |
| Guarantee and promise block | Scout Guarantee, Algae-Free Guarantee, "no contract, satisfaction guaranteed" | His real promises, in his own voice: we answer our phone, callback within the hour, same route day, a door hanger every visit. A formal guarantee is held for Mike's approval (item 6). |
| Real technicians, not stock | Franchises show generic smiling families and techs; the best independents put the owner in the hero | A **hero owner chip** (Mike's photo, "Mike Brazell, owner · CPO certified · Lifelong Lexington County resident"), plus a **homepage owner story** in Mike's own words, with his photo and signature. No stock photography anywhere. |
| Reviews tied to a place | Poolwerx tags each review with its franchise location | Each review carries the customer's town ("Lexington, SC"); the heading is "What our Lexington County neighbors are saying". More towns as real reviews come in. |
| "Find a location near you" | ZIP locator, location-swap pages | **Not used.** There's one service area, shown as the two real counties (Lexington is the home base) and 8 city pages with distinct local copy. |
| Seasonal and expert content | Poolwerx winter promos and tips | A "Built for Midlands pools" row on the homepage (pine pollen, summer thunderstorms, "Famously Hot" August, a long swim season), linking to the Pool Care Calendar and Mike's own posts. |
| One-tap call or book | Phone in the header, sticky request button | The topbar reads "Family-owned in Lexington County. We answer our phone…". There's a phone in the header, a sticky Call / Text / Free Evaluation bar on mobile, and a 3-field form with plan and pool type. |

**Look:** everything comes from Palmetto's own brand: the logo navy `#1b227d` (header, footer, hero), pool teal for links and icons, and a warm gold for buttons. Oswald matches the condensed capitals of his logo. Nothing was copied from any benchmark's layout, wording, photos or branding.

**Avoided on purpose:** stock "happy family" photos, "America's #1" style claims, 1-800 numbers, ZIP locators, franchise/careers blocks and doorway "near me" pages.

**Later upgrades (need Mike's photos):** a truck photo in the hero or trust bar, a "Meet the family" row on the home page (`about.team` can feed it), and before/after green-pool pairs on the Green to Clean page.

## Kit additions (generic, any client)

- `home.hero_owner`: an owner chip under the hero (photo, name, one line).
- `home.owner`: an owner-story section on the home page (photo with caption, story, signature, two buttons). Add `"owner"` to `home.order`.
- `home.cards`: an icon-card row, each card optionally linking to a page. Add `"cards"` to `home.order`.
- `about.team`: "Meet the team" cards (photo or initials, name, role, bio).
- Web3Forms mode emits no GHL comments or hooks, and the GHL native-form JS is stripped from site.js unless `form_mode` is `native`.
- `areas.groups[].also`: towns served without their own page (shown in the county box and added to areaServed).
- `integrations.google_reviews_label`: button text for the Google reviews link.
- `photos[].contain`: a photo shown whole, not cropped (documents, tall images).
- The `generate_lead` push uses GTM's `eventCallback` before going to the thank-you page.

## Old site vs. new site

| | Current GHL site | New build |
|---|---|---|
| Structured data | Meta tag only; no JSON-LD | JSON-LD on every page: LocalBusiness (with founder), Service, FAQPage, BreadcrumbList, OfferCatalog, BlogPosting, CollectionPage |
| H1 | Duplicated on the homepage | One keyword-targeted H1 per page, with a clean H1 → H2 → H3 hierarchy (script-checked on all 43 pages) |
| Forms | GHL form + chat widget | Web3Forms to Mike's Gmail, a thank-you page, `generate_lead` to his own GTM, first-touch UTM/gclid on every lead |
| Owner / people | Owner story on /about only | Mike's photo and story on the home page (hero chip + owner section) and the About page |
| Maintenance plans | "Custom pricing," no plan page | `/pool-maintenance-plans/`: 3 plans, comparison table, plan finder, pricing explainer, FAQ |
| City pages | 5 | 10 (added Cayce, Forest Acres, Blythewood, Gilbert, Batesburg-Leesville), each with unique local copy and FAQ; 10 more Lexington County towns listed |
| Blog | 8 posts, internal links to 404s | 8 posts migrated at the same URLs, cross-linked with service and city pages, category pages kept, RSS |
| URLs | — | All existing URLs kept (pages, `/post/`, `/posts/category/`, legal). `/contact-page`, `/posts`, `/terms`, `/home`, `/sitemap`, author and tag pages, the broken `-sc2` URL and the old in-post link targets all 301 |
| Speed | GHL builder JS + chat widget | Static HTML, self-hosted fonts, no render-blocking third parties (GTM loads async) |
| Mobile | Standard | Sticky Call / Text / Free Evaluation bar |
