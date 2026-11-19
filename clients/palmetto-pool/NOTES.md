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

## Before launch: confirm with Mike

1. **Family and crew, by name, with photos.** The site says "family-owned" and reviews mention "Mike and his crew", but no names are confirmed. `about.team` is ready (name, role, short bio, photo). Wanted: crew/family names, Mike or the crew on a pool, the truck(s), and before/after green pools. Until then, Mike is the only person named.
2. **His phone number vs. GHL.** His SMS terms say "text STOP to (803) 394-0765". **If that number is a GHL/LeadConnector number, port it out before GHL is cancelled.** Otherwise the number printed on his banner, truck and every page dies with the account.
3. **Reviews from other towns.** All three real reviews are from Lexington. Ask 3–5 customers in Columbia, Irmo and Chapin for Google reviews, then add them to `REVIEWS` with their town. Add the GBP "read reviews" link (`integrations.google_reviews_url`).
4. **Plan names and inclusions** (Balance / Full Service / Full Service Plus) are still a *proposal*. Confirm them, and whether chemicals are included.
5. **Publish "starting at" prices?** Every strong national and top independent site shows plans with a starting price or a clear price range. Even "from $X/mo" would beat Poolman360 and All Clear, which show none.
6. **A real guarantee?** National brands lead with one (no-contract satisfaction, an algae-free promise). Mike's promises today are "we answer our phone", "callback within the hour" and the door hanger. If he'll stand behind something more (for example, "pool not clear after a visit, we come back free"), it belongs in the hero proof line. Not added without his OK.
7. **Gilbert.** Several posts list Gilbert as served, but there's no Gilbert page or area entry. Confirm, then add it to the posts' sign-offs or remove it.
8. **One factual check in a migrated post:** the October closing post says cracked return lines are "a five-to-six figure surprise". That's likely high; Mike may want "four-figure".
9. **City facts:** he should sanity-check the neighborhood mentions on the 8 city pages (unchanged from the first build).
10. **GTM setup** (per the GTM + GA4 doc): GA4 tag, a `generate_lead` GA4 event tag on the Custom Event trigger, phone-click tag, Preview test, publish. Then mark `generate_lead` and `phone_click` as key events.
11. **Web3Forms:** Mike confirms the key's email, sends one test from the `pages.dev` preview, and marks the Web3Forms sender as safe. Leave the domain restriction off until launch.

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
- Web3Forms mode emits no GHL comments or hooks.
- The `generate_lead` push uses GTM's `eventCallback` before going to the thank-you page.

## Old site vs. new site

| | Current GHL site | New build |
|---|---|---|
| Structured data | Meta tag only; no JSON-LD | JSON-LD on every page: LocalBusiness (with founder), Service, FAQPage, BreadcrumbList, OfferCatalog, BlogPosting, CollectionPage |
| H1 | Duplicated on the homepage | One keyword-targeted H1 per page, with a clean H1 → H2 → H3 hierarchy (script-checked on all 41 pages) |
| Forms | GHL form + chat widget | Web3Forms to Mike's Gmail, a thank-you page, `generate_lead` to his own GTM, first-touch UTM/gclid on every lead |
| Owner / people | Owner story on /about only | Mike's photo and story on the home page (hero chip + owner section) and the About page |
| Maintenance plans | "Custom pricing," no plan page | `/pool-maintenance-plans/`: 3 plans, comparison table, plan finder, pricing explainer, FAQ |
| City pages | 5 | 8, each with unique local copy and FAQ |
| Blog | 8 posts, internal links to 404s | 8 posts migrated at the same URLs, cross-linked with service and city pages, category pages kept, RSS |
| URLs | — | All existing URLs kept (pages, `/post/`, `/posts/category/`, legal). `/contact-page`, `/posts`, `/terms`, `/home`, `/sitemap`, author and tag pages, the broken `-sc2` URL and the old in-post link targets all 301 |
| Speed | GHL builder JS + chat widget | Static HTML, self-hosted fonts, no render-blocking third parties (GTM loads async) |
| Mobile | Standard | Sticky Call / Text / Free Evaluation bar |
