# Teal Outdoor Services: rebuild notes

Owner: Billy Lander · Lexington, SC · (803) 240-8356 · tealoutdoorservices@gmail.com
Domain registrar: Namecheap · Email: personal Gmail (no email on the domain) · No GoHighLevel items kept.

- Build: `python3 build.py teal-outdoor` → `dist/teal-outdoor`
- Preview: `python3 build.py teal-outdoor --preview`
- Status: **approved by Billy (Nov 17, 2026)**, merged to `main`, `launched: True`. Goes live when tealoutdoorservices.com is added to the `teal-outdoor` Cloudflare Pages project.

## Billy's answers (Nov 17, 2026): applied

- **Visit documentation:** yes, before-and-after photos and notes after every commercial/pond visit. The copy now says "every visit".
- **Ponds:** he also does dredging, structural/erosion repairs and aquatic weed control. These were added to the pond page, the checklist page and the Aiken County page. The copy no longer says he refers this work out.
- **License:** SC pesticide applicator license #C0035614, Category 5 (Aquatic) and Category 6 (Right-of-Way). It now shows in the home trust bar, the hero proof line, the sidebar badges, the pond, ROW and weed control pages, the general FAQ and the About list.
- **Contracts:** service agreements are optional, and commercial accounts are preferred on one. The FAQs and the commercial blog post's closing line ("No contracts") were updated.
- **Aiken County:** added `/property-maintenance-aiken-county-sc/` (county-level page), plus Aiken in the hub group, schema areaServed and the general FAQ. Confirm how far he goes (e.g. North Augusta).
- **Customer email (Greg Boling, Holtzman Propane | Valley Ice):** NOT published. Get Greg's permission first, then use it as "Greg B., Holtzman Propane" (no phone number), or ask Greg for a Google review.

## Photos (Nov 17, 2026)

These are 8 real photos from Billy, stored in `assets/photos/*.webp` (resized to 1200px, about 200–360 KB each).
- **Blurred:** the customer's signs (Edisto Recycling) on the roadside planting photo and the house number on the residential bed.
- **Where they're used:**
  - Home page: "Recent jobs" gallery
  - Commercial page: before/after pair plus two installs
  - Landscaping page
  - Fence page
  - About page: Billy's portrait and the equipment shot
- **Still wanted:** pond and right-of-way photos, the two growth services with no pictures yet. Before-and-after pond banks would be ideal.

## Before launch: still open (original list; items 3–6 resolved above)

1. **The old site is losing leads right now.** The GHL form shows "Unable to find form" on the contact page and every service page, and the header "Get a Free Estimate" button links to `#`. The new site posts to Web3Forms, which emails tealoutdoorservices@gmail.com. After launch, send one test from the live domain and check spam the first time.
2. **Fake testimonials removed.** The old /about and /contact pages show three software/analytics "testimonials" (Ashwin Santiago, Kaden Scott, unnamed). They're template filler, so they were not carried over. Only the three real homepage reviews (Jim B., Ashley W., Sean L) are used.
3. **Visit documentation.** The hero card (labeled "Example") and pond/commercial copy say we send before-and-after photos and notes. The old site says this both as standard and as "available on request". Confirm which it is. If it's standard, it's the strongest selling point on the site.
4. **Pond scope.** The copy says Teal handles routine pond work (mowing banks, woody growth, shoreline vegetation, debris on inlets, outlets and trash racks, documentation). It also says sediment removal and structural repairs get flagged and referred out. Confirm both, and whether he removes trees from dams himself.
5. **Licensing.** The site says "licensed for chemical weed and vegetation control" (as the old site did). Get the SC Department of Pesticide Regulation license category and number. Showing it on the ROW and pond pages would be a real trust boost for municipal bids.
6. **"No contracts" vs. recurring contracts.** The migrated commercial blog post ends "No contracts. No runaround." The old commercial page says most commercial clients are on recurring contracts. Pick one message.
7. **Response time.** The old site said both "same business day" and "within 1 business day". The new site uses "typically within one business day, often the same day".
8. **City pages (new).** There are 12 new pages, each with distinct local copy. Have Billy check the place references (Sunset Blvd/US-378, 12th Street Extension, Knox Abbott Dr, St. Andrews/Lake Murray Blvd, peach country in Gilbert, US-1 in Batesburg-Leesville, US-321 in Gaston/Swansea). Confirm that he really takes Newberry and Prosperity work.
9. **Pond checklist page (new).** `/pond-maintenance-checklist/` is built from Lexington County's 2025 pond maintenance requirements, the county's annual inspection checklist, and Richland County's Private Pond Inspection Program (sources linked on the page). It's the link-worthy asset: send it to HOA managers and property management companies.
10. **Privacy policy.** The policy was rewritten for the new stack (Web3Forms, GTM/GA, Cloudflare). Billy should read it, and compare it with the old /privacy text if he had it professionally written.
11. **Photos.** The old gallery images are AI-generated (`funnel-ai-production/image-generation`), so none were used. 6–10 real job photos would add trust and image-search traffic: pond banks before and after, a crew on a ROW, a commercial site, a fence. Good targets are an `hero_layout: "image"` option or post images.
12. **Google Business Profile.** Add the GBP "read reviews" URL (`integrations.google_reviews_url`). Point the GBP website link at the home page (or at /commercial-property-maintenance-lexington-sc/ as a test).
13. **Social.** No Facebook or Instagram links were found. Add them to `business.social` if they exist.

## Tracking

- GTM `GTM-W3KKNTH5` is in the **client's own** Tag Manager account and on every page.
- Every form submit pushes `generate_lead` to the dataLayer and lands on `/thank-you/` (noindex).
- In GTM, add a GA4 event tag on `generate_lead` (mark it as a key event), or count `/thank-you/` page views.
- Form emails include the page, landing page, referrer, UTM, gclid and fbclid.

## Design decisions

- **Colors are sampled from the logo.** Teal is `#0a7376` (header text, hero, footer). Orange is `#f1592a` (hero stripes, logo). Buttons use a one-step-deeper orange, `#cf4418`, so white button text passes WCAG AA. The logo orange on white text is only 3.4:1.
- **White header, as on the old site,** so the full-color logo reads. The footer uses a knockout version (white TEAL, orange duck). Both are cut from the supplied JPG. Ask for the vector (SVG/EPS/AI) to get crisper edges.
- **Hero visual:** an example pond visit report, which turns "communication and follow-through" into something a property manager can picture.
- **Kit additions** (generic, for every client):
  - `theme.header: "light"`
  - `logo.footer_file`
  - `colors.highlight` (accent text and icons on dark sections)
  - `services_hub.flat_urls` (service pages at the root, keeping old GHL URLs)
  - `services_hub.home_count` (feature the first N services, then "See all")
  - `resource.body_html`

## Old site vs. new site

| | Current GHL site | New build |
|---|---|---|
| Lead form | **Broken** ("Unable to find form"); header CTA links to `#` | Working Web3Forms form on /contact/ and the home page, with a no-JS fallback, attribution fields, a thank-you page and a GTM `generate_lead` event |
| Structured data | None (meta tags only) | JSON-LD on every page: LocalBusiness, Service, FAQPage, BreadcrumbList, BlogPosting, Article |
| H1s / titles | Titles over 60 chars on several pages; homepage H1 doesn't name a service | One keyword-targeted H1 per page, clean H1 → H2 → H3, titles ≤ 60 and metas ≤ 155 |
| Positioning | Generic "outdoor services" homepage | Leads with the top three growth services (commercial, retention pond, right-of-way); lawn care and landscaping are next in line |
| City pages | 0 (one list page) | 12 city pages with unique local copy, plus the /service-area/ hub |
| Content asset | 2 blog posts | 2 migrated posts + the Midlands Stormwater Pond Maintenance Checklist (cites county sources) |
| Reviews | 3 real + 3 fake software testimonials | 3 real reviews only |
| FAQs | Homeowner FAQs repeated on commercial and ROW pages | Service-specific FAQs on each page |
| URLs | — | All kept: every service URL, /about, /services, /service-area, /blog, /post/*, /blog/category/*, /contact, /privacy. 301s for /index-home, /home, the malformed /tealoutdoorservices.com, /commercial-lawn-care-lexington-sc, /privacy-policy, /blog/tag/*, /blog/author/* |
| Speed | GHL builder JS, remote webp images, Google Maps embed | Static HTML, self-hosted fonts, about 25 KB of CSS/JS, no map iframe |
| Mobile | Standard | Sticky Call / Text / Free Estimate bar |
| Tracking | GHL | Client-owned GTM, no GHL |

## Monthly blog ideas (one each, tag to services + cities)

- "How often should an HOA retention pond be mowed in South Carolina?"
- "What Lexington County's annual stormwater pond inspection looks for"
- "Pre-emergent timing for Midlands lawns: when to apply in Lexington, SC"
- "Commercial landscaping bids: what to put in the scope so you can compare apples to apples"
- "After the storm: a right-of-way clearing checklist for municipalities"
