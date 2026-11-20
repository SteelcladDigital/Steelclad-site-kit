# Sweet & Cinnful: site rebuild notes

**Client:** Cinnamon Larkin, Founder & CBO · Lexington, SC home bakery · cinnamonrlarkin@gmail.com
**Old site:** GoHighLevel funnel at sweetandcinnful.com (4 pages, 3 legal pages)
**Build:** `python3 build.py sweet-and-cinnful [--preview | --check]`
**Status:** preview built. Not launched (`launched` is off). One blocker: the GHL tracking script.

## Confirm with Cinnamon before launch

1. **Delivery radius and fee.** Her order form offers "Pickup or Delivery?", but no radius or fee is published. The site says "delivery available in some areas, ask on your order" and has town pages for Irmo, Chapin, West Columbia, Cayce and Gilbert. Confirm which towns she actually delivers to, and drop or reword any she doesn't.
2. **Lead time.** No minimum notice is published. The FAQs say "as early as you can". If she has a rule (for example 1 week for cakes), add it to the FAQs and the order steps.
3. **Cheesecakes and cottage food law.** Her menu lists Cheesecake ($45) and Mini Cheesecakes ($30 / 6). South Carolina's Home-Based Food Production (cottage food) law does not cover baked goods that need refrigeration. Cheesecakes, and possibly cream-cheese frostings, may need a retail food permit from SC Dept. of Agriculture. Ask her to confirm her status. Remove them from `tiers.addons` if they shouldn't be sold online. *(We are not giving legal advice; she should check with SCDA or Clemson Extension: sccottagefood@clemson.edu.)*
4. **Prices.** Taken from her current menu image: cake pops $24/12, cupcakes $30/12 or $50/24, cookies $30/12, brownies $30/12, cakes $55 & up, cookie cakes $45 & up, bundt $45, cheesecake $45, mini cheesecakes $30/6. The old homepage said cookies were sold "by the half-dozen and up", which conflicts with the menu. Confirm the minimum.
5. **Gluten-free.** The site says gluten-free *requests are welcome* (based on a real review and her form's Dietary Needs field). It never promises allergen-free. Confirm the wording.
6. **Pickup details.** The site says "Pickup by arrangement" and doesn't show her address. Confirm she wants it that way.
7. **Photo of Cinnamon.** The About page has no photo. A real photo of her (with permission) would be the single biggest trust upgrade. Add it as `about.photo`.
8. **Story copy.** The About story uses only known facts: solo home baker, her tagline, her reviews. Ask for 2–3 sentences in her own words (why she started, favorite thing to bake) and replace it.
9. **Legal pages** were migrated word-for-word from the old site. The template blanks (company name, email, governing state) were filled with Sweet & Cinnful / her email / South Carolina, and "appointment" wording in the SMS terms was lightly adapted to orders. Have her review them.
10. **Photos** are her 8 gallery photos, cropped to remove a child and a person in the background. Brand names in the old alt text (a snack-cake brand) were removed from captions.

## Launch setup

- `integrations.ghl_tracking_snippet`: paste from GHL > Settings > External Tracking. **This is the only launch blocker.**
- The order form embed uses the existing GHL form `iOW0QPcEwExTKLMCqQi5` (Custom Bakery Order Form: date, order details, flavor, pickup/delivery, dietary, inspiration uploads). Height is set to 1950px. Check it on mobile after launch and adjust `contact.ghl_height` if it scrolls inside.
- Optional: GTM ID, `google_reviews_url` / `google_review_write_url` from her Google Business Profile. Her old site doesn't link to one. If she doesn't have one, **set it up as a service-area business**, since it's the biggest local-search lever for a home bakery.
- `og-image.jpg` is committed (generated).

## Kit changes made for this client (generic, all clients benefit)

- **Optional phone.** If `business.phone` is empty, every phone link becomes an email link. The hero and CTA-band secondary button uses `labels.alt_cta = (label, slug)`, which is never linked from its own page. The mobile bar shows Email + `labels.mbar_second_slug`. `labels.reach_verb` controls "Call or text" / "Email" wording, and the schema omits `telephone`.
- **`gallery_page`:** a standalone portfolio page with ImageGallery schema (kept `/favorites`).
- **Optional `business.hours`:** no empty `openingHoursSpecification` in the schema.
- New icons: `cake`, `cookie`, `cupcake`, `gift`, `mail`.
- Existing clients' output was verified byte-identical apart from one new CSS rule.

## Design brief (benchmark)

Benchmarked: **Magnolia Bakery**, **Levain Bakery**, **Ista Bake Studio** (custom cookie/cake studio), plus local **Nothing Bundt Cakes Lexington** and **Crumbl Lexington**. Local custom/home bakers (Buds & Roses Couture Cakes, Cruz 'N Cakes, BabyCakes, Four Little Loaves, etc.) mostly live on Zola, WeddingWire, Bakesy, Facebook or Jotform, with no real website.

1. **Real product photo as the hero** (Levain leads with a cookie filling the screen). Her mermaid cake is the hero.
2. **Three clear doors: Cakes / Cookies / Cupcakes** (Ista's three-tile home). These are the three money pages.
3. **Prices posted up front** (Magnolia and Levain show prices; local home bakers hide them). This is the main gap, and every card shows a starting price.
4. **Visible ordering process** (Magnolia's "order now / plan ahead" flow): a 4-step "How ordering works" section.
5. **Maker story** (Levain's founders, Ista's family business): the "Meet the baker" band and About page, built on her own tagline.
6. **Occasion framing** (Levain's "for every occasion"): event batches, holiday trays, party favors.
7. **Brand refresh:** the old logo was an image on a stock-photo background. The new wordmark is in Fraunces with her teal + pink kept from the old logo. Bolder idea for later: a custom illustrated logo mark.

## Old vs new

| | Old (GHL funnel) | New (Site Kit) |
|---|---|---|
| Pages | 4 + 3 legal | 19 (3 money pages, menu, gallery, guide, 5 town pages, about, order, hub pages, legal) |
| H1s | Home H1 was "Cinnamon Larkin"; empty duplicate H1 on menu page | One keyword-targeted H1 per page |
| Title / meta | Home only; inner pages had none | Unique title ≤60 and meta ≤155 on every page |
| Schema | None | Bakery (founder, slogan, sameAs, area served), Service, FAQPage, BreadcrumbList, ImageGallery |
| Menu & prices | One image, unreadable to Google | Real text and prices, 3 cards + 6 extras |
| Photos | 8, no captions | 8, cropped, descriptive alt and captions, used on service pages |
| City pages | 0 | 5 (Irmo, Chapin, West Columbia, Cayce, Gilbert) |
| Link-earning content | None | Party dessert planning guide (servings by headcount, SC heat tips) |
| Reviews | 4 in a carousel | Same 4 real reviews, on home, about and town pages |
| CTAs | Order Now | Order CTA in header, hero, every page, sticky mobile bar |
| Speed | GHL funnel JS | Static HTML, self-hosted fonts, no page builder |

**URLs kept:** `/menu-pricing-page/`, `/place-custom-order/`, `/favorites/`, `/termsofservice/`, `/privacy-page/`, `/accessibility/`.
**Redirects:** `/privacy-policy` → `/privacy-page/`, `/order-now` → `/place-custom-order/`, `/menu` → `/menu-pricing-page/`, `/home` → `/`.
