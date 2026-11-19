# Harvest Moon Realty: build notes

New site for Barry Keith's brokerage (no previous website). Domain: **harvestmoonrealty.com** (registered at GoDaddy, not live yet).
Built Nov 19, 2026 from Barry's onboarding notes, his Google Business Profile, his Facebook page and the GHL preview he liked.

## Canonical NAP (use exactly this everywhere)

**Harvest Moon Realty** · 411 N Lake Dr, Lexington, SC 29072 · (803) 309-9521 · barry@harvestmoonrealty.com
Agent: Barry Keith, SC real estate license #43236. GBP primary category: Real estate agency → schema `RealEstateAgent`.

## Launch blockers (`python3 build.py harvest-moon-realty --check`)

1. **GHL form**: create the "Harvest Moon contact" form in his sub-account, set `integrations.ghl_form_id`.
2. **GHL tracking script**: set `integrations.ghl_tracking_snippet`.
3. **IDX search** for `/search-homes/` and `/search-land/`: paste the vendor's embed code into `search.pages[].embed_html` (plan below).
4. (Recommended) GTM container → `integrations.gtm_id`.

## Confirm with Barry before launch

- [ ] **Hours**: the site says "Open 7 days, 8 AM – 8 PM" (Google shows "closes 8 PM"; the GHL preview said Mon–Sun 8–8). Confirm, or give real hours.
- [ ] **barry@harvestmoonrealty.com** is set up and receiving mail (it's in the footer, contact page and privacy policy).
- [ ] License wording: "SC real estate license #43236". Is he the broker-in-charge of Harvest Moon Realty? If so, we can say "Broker" on the About page.
- [ ] REALTOR® association memberships: the GHL preview claimed Columbia/Central Carolina REALTORS® and SC REALTORS®. Not confirmed, so **left off** the site. Add them if true.
- [ ] Buyer's-agent compensation FAQ wording (Buying a Home page) is general and post-2024-settlement safe; he may want his own wording.
- [ ] Community-page facts (school districts, county lines) are deliberately general and tell buyers to confirm schools with the district. Ask him to skim them.
- [ ] **Buying a Home** and **Buying Land** pages are drafted from his intake answers. He's sending his own process copy for both; swap it into `SERVICES[0]` and `SERVICES[1]` (`included`, `signs`, `faqs`) when it arrives.

## Do NOT carry over from the GHL preview (it has invented content)

The GHL preview Barry liked has the right *look* but several made-up facts. If that preview is shown to anyone, fix these too:
- Testimonials from "Sarah & Marcus Miller", "David Holbrook" and "Elena Vance" are **fictional**. The site uses his three real Google reviews instead.
- License "#48192": his license is **#43236**.
- Email "barry@harvestmoon.cc": that domain is **Harvest Moon Construction's** website (same street address). Use barry@harvestmoonrealty.com.
- "Schedule a Chat" button dials **(803) 555-0192**, a fake number.
- Timeline items "2002 Land Advisory" and "2015 Harvest Moon established", "hundreds of Midlands families", "off-market alerts", "timber cruise" and "soil" services, and "500 miles of shoreline" are not from Barry. Only 1989 (investing) and 2003 (licensed) are confirmed.
- Social icons link to the bare facebook.com / instagram.com / linkedin.com / youtube.com homepages.

## Listing search (IDX) plan: no forced registration

Barry is in the **Consolidated MLS (CMLS, the Columbia/Midlands MLS)**. The site already has the two pages, the nav, the home-page section, a "No sign-up. No email required." badge and FAQs, waiting for the embed.

1. **Pick a vendor that covers CMLS and embeds in a static site** (no WordPress needed): IDX Broker (hosted subdomain such as `search.harvestmoonrealty.com` plus JavaScript widgets) or iHomefinder (embeddable search). Diverse Solutions and PeakIDX also list CMLS coverage. Showcase IDX and AgentFire are WordPress-based, so skip them.
2. Barry signs the CMLS IDX agreement and approves the vendor (CMLS lets each member approve up to 20 vendors). Expect a vendor setup fee and monthly fee.
3. **Turn registration OFF**: IDX Broker: uncheck *Force Registration* and *Request Registration* for all five page types (search, map search, results, details, photo galleries). Diverse Solutions: Registration Level → *Never*. Whatever the vendor, also check there's no "soft" pop-up after X views.
4. Paste the homes search embed into `/search-homes/` and a land-filtered search (property type Land/Lots/Acreage) into `/search-land/`. Optional: add `quick_links` (deep links like Lake Murray waterfront, acreage 5+, under $300k).
5. Replace `search.disclaimer_html` with the exact attribution wording CMLS and the vendor require. The listing brokerage's name must show on each listing.
6. Leads: the vendor's optional "Request a showing / Ask a question" form should be optional only, and routed into GHL (vendor email → GHL, or Zapier/webhook) with an owner notification.
7. Test in a private window: search, open listings, use the map and photos without ever seeing a sign-up wall.

## Design brief (benchmark)

Sites reviewed: the **GHL preview** Barry likes (warm sunset farmland hero, cream backgrounds, serif headings with a highlighted word, yellow buttons, two "paths": homes and land); **Whitetail Properties** (national land brokerage: search box is the hero, browse by land type, a knowledge center, clear land disclaimers); and the Lexington market in search results: most local agents only have franchise profile pages (C21, ERA, EXIT, NextHome, KW), and the typical IDX sites (e.g. Real Geeks) put a sign-in wall in front of listings. Land specialists in SC are national franchises (Mossy Oak Properties, Whitetail) with no local home-buying focus.

1. **Search in the first screen.** Top brokerages put search up front, so "Search Homes & Land" is the hero's second button, the first nav item and the phone's bottom-bar button.
2. **Make "no sign-up" the headline differentiator.** Badge, hero proof point, FAQs and the privacy policy all say it.
3. **Two paths, one standard** (from the GHL preview): homes and land side by side in the search section and the services.
4. **The GHL look in the kit:** brand brown, sunset gradient and yellow buttons, Fraunces serif headings, a highlighted phrase in the H1, cream sections, rounded cards, wave dividers. The hero art is an original moon-over-fields illustration built from his logo (no stock photos).
5. **Real proof only:** 1989 / 2003 / 5.0★ Google card, three real Google reviews, his own words quoted.
6. **Land expertise as content:** the SC Land Buying Checklist is built from his own list, a link-worthy page none of the local agents have.
7. **Community pages** for the six places buyers ask about most, each with different, practical local notes (no copy-swapped doorway pages).

## Photo shot list (ask Barry)

People hire people. The site has no photos of Barry yet; the About page and hero card are ready for them.
- [ ] Clear, smiling headshot (vertical, good light) → About page and hero card
- [ ] Barry out on a property or walking land (tract, pasture or timber)
- [ ] Barry at the office sign / 411 N Lake Dr
- [ ] Local shots: Lake Murray, downtown Lexington, farmland and timber he's sold
- [ ] (With permission) closing-day photos with happy buyers, especially first-timers
Send originals (full size). Phone photos are fine in good light.

## Logo

Client-supplied `HMR_Logo2.svg` (source/logo-original.svg). Header: full color on white. Footer: knockout version (brown → cream). Favicon: the moon-and-fields mark. The logo reads "Realty Co."; the business name on Google and everywhere else is "Harvest Moon Realty". Keep "Harvest Moon Realty" on citations.

## Citation clean-up list (send to the client / do in our listings work)

| Where | Problem | Fix |
|---|---|---|
| Homes.com agent profile | Phone shows **(803) 770-4672** | Change to (803) 309-9521 |
| Realtor.com agent profile | Address **1224 Huger St, Columbia, SC 29201** | Change to 411 N Lake Dr, Lexington, SC 29072 |
| Facebook page | Email **Barry@harvestmoon.cc**; address written "411 N Lake Drive" | Use barry@harvestmoonrealty.com and "411 N Lake Dr"; add website |
| Facebook page | Reviews show "Not yet rated (0 reviews)" | Ask a few clients for Facebook recommendations |
| Google Business Profile | No website | Add https://harvestmoonrealty.com after launch |
| Instagram | Could not verify (login wall) | Check bio: name, phone, website |
| Harvest Moon Construction (harvestmoon.cc) | Same street address, different business | Keep the two listings clearly separate; don't share the email domain |

Barry thinks he has no reviews, but his Google profile has **11 reviews, 5.0 stars**. Send him the review link (https://g.page/r/CQxe66N9ozaoEBM/review) to keep them coming. The footer and reviews section already link to it.

## Kit changes made for this client (generic, off by default)

- `search` block: IDX listing-search pages with nav dropdown, home-page section, placeholder until `embed_html` is set, MLS disclaimer, and a launch blocker when the embed is missing.
- `theme.hero_bg` (+ `_position`, `_overlay`, `_mobile` variants): background art for the home hero.
- `labels.footer_note_html` (license / Equal Housing / disclaimer line), `labels.footer_email`, `labels.footer_areas_title`, `labels.footer_areas_all`.
- Footer shows the office street address when a site has both city pages and a street address.
- `labels.mbar_second_href: "page:<slug>"` links a site page from the mobile bottom bar.
- Icons: `key`, `tree`.
