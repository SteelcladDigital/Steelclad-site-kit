# Steelclad Site Kit

Steelclad Digital's master template for fast, SEO-first local business websites. One repo holds every client. Each client is a single config file, and the kit generates the pages, structured data, sitemap and GoHighLevel hooks.

## Quick start

```bash
python3 build.py --list                   # show clients
python3 build.py palmetto-pool --preview  # preview build -> preview/palmetto-pool/ (open index.html)
python3 build.py palmetto-pool            # deploy build  -> dist/palmetto-pool/
python3 build.py all                      # build every client (folders starting with _ are skipped)
```

Needs only Python 3. No npm, no database, no page builder.

## How it's organized

```
build.py                 the generator (shared by every client)
core/site.css, site.js   shared layout + components (colors come from each client's theme)
core/fonts/              12 self-hosted fonts (no Google Fonts calls)
clients/<client>/site.py ALL content + design choices for one business
clients/<client>/assets/ optional: logo.png, photos, og-image.jpg (copied to /assets/)
```

## Making each site different

Everything about a site's look and structure lives in that client's `site.py`.

**Theme**
- `colors`: primary, primary_deep, secondary, secondary_deep, secondary_wash, accent, accent_text, surface
- `fonts`: display and body. Choose from: oswald, inter, fraunces, playfair-display, outfit, space-grotesk, dm-sans, archivo, nunito-sans, manrope, bricolage-grotesque, source-serif-4
- `radius`: sharp, soft or round
- `heading_case`: none or uppercase
- `divider`: wave, angle or none
- `texture`: ripples, lines, grid or none
- `hero_layout`:
  - `card`: info card beside the headline
  - `image`: photo, set `home.hero_image`
  - `centered`

**Logo**
- `svg`: inline SVG
- `image`: a file in the client's `assets/` folder
- `text`: wordmark lines

**Optional sections**
- `tiers`: plans, packages, memberships or subscriptions, with an optional comparison table and plan-finder quiz
- `areas`: city and service-area pages, for service-area businesses
- `resource`: a guide or calendar page that earns links
- Storefronts: add `address.street` and `hours_table` to get a "Visit us" block with directions instead of area pages

**Home page order:** `home.order` sets which sections appear and in what order.

**Structured data:** `business.schema_type` takes any schema.org type, such as Plumber, HVACBusiness, RoofingContractor, CafeOrCoffeeShop, Dentist, AutoRepair or HomeAndConstructionBusiness.

Two reference clients:
- `clients/palmetto-pool/`: a service-area business (maintenance plans, 8 city pages, seasonal guide)
- `clients/_demo-coffee/`: a fictional storefront with a totally different look (serif type, warm palette, subscriptions, hours and directions, no area pages)

## Starting a new client

1. Copy whichever reference client is closer: `cp -r clients/palmetto-pool clients/new-client`
2. Rewrite `site.py`: business info, theme, copy, services, areas and FAQs. Keep URL slugs that already rank on the old site, and add old-to-new 301s in `redirects`.
3. Put the logo and photos in `clients/new-client/assets/`.
4. Run `python3 build.py new-client --preview` and review.

## GoHighLevel and tracking

Set these in `integrations`, then rebuild:
- `ghl_form_id`: replaces the demo form on `/contact/` with the live GHL form
- `ghl_chat_widget_id`: adds the chat widget to every page
- `gtm_id`: Google Tag Manager. Load GA4, pixels and call tracking inside GTM.
- `google_reviews_url`: adds a "Read more reviews on Google" button

## Deploying (Netlify, one Netlify site per client, all from this repo)

1. In Netlify, choose **Add new site → Import from Git** and pick this repo.
2. Set the build command to `python3 build.py palmetto-pool` and the publish directory to `dist/palmetto-pool`.
3. Add the client's custom domain and update DNS.
4. Submit `https://domain/sitemap.xml` in Google Search Console.

Every push to `main` rebuilds the live sites. Cloudflare Pages works the same way.

## Pre-launch checklist (per client)

- [ ] Client confirmed every fact: services, plans and pricing, hours, service areas, certifications
- [ ] Legal pages filled in (they're placeholders)
- [ ] Old URLs either kept or 301-redirected; blog posts migrated
- [ ] Real logo and photos in `assets/`; `og-image.jpg` added (1200×630)
- [ ] GHL form, chat and GTM IDs set
- [ ] Mobile check, form test, Search Console and sitemap submitted
