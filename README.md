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

## Blog

Turn it on with the `blog` block in a client's `site.py`. Set `index_slug` (usually `blog`) and `post_prefix`, which is the URL folder for posts. Match the old site's pattern so existing URLs keep ranking: `post` gives `/post/<slug>/` (GHL style), and `blog` gives `/blog/<slug>/`.

Each post is one file at `clients/<client>/posts/YYYY-MM-DD-slug.md`:

```markdown
---
title: Saltwater Pool Maintenance in Lexington, SC: What Your Salt Cell Needs
seo_title: Saltwater Pool Maintenance in Lexington, SC     # optional, shorter <title>
slug: saltwater-pool-maintenance-lexington-sc              # optional, defaults to the filename
date: 2026-11-11
updated: 2026-12-01                                         # optional
description: One or two sentences. Used as the meta description and the card text.
category: Pool Equipment
author: Mike Brazell, owner                                # a person's name gets Person author markup
services: specialized-pool-cleaning, weekly-pool-maintenance  # service slugs, cross-linked both ways
areas: pool-service-lexington-sc, pool-service-irmo-sc        # area slugs, cross-linked both ways
image: blog/salt-cell.jpg                                  # optional, from clients/<client>/assets/
image_alt: Technician cleaning a salt cell
draft: false                                               # true = not built
---

Body in Markdown: ## and ### headings, - lists, 1. lists, **bold**, *italic*,
[links](/services/specialized-pool-cleaning/), > callouts, ![images](/assets/blog/x.jpg).
Internal links start with "/" and work in both preview and live builds.
```

What the build does with each post:
- Creates the post page (BlogPosting markup, breadcrumbs, author, read time, sidebar call to action, related services and areas, "keep reading")
- Adds it to the `/blog/` index (Blog markup, category chips) and the homepage "latest articles" section (add `"blog"` to `home.order`)
- Lists it under "Related articles" on every service page and city page it's tagged with
- Adds it to `/blog/rss.xml` and `sitemap.xml`, with the post date as `lastmod`

Keyword strategy for posts: each post targets one question or informational keyword that a service or city page can't rank for on its own. Tag the posts so they pass authority to the money pages. Never write a post that targets the same keyword as an existing service or city page, because the two pages would compete with each other.

## GoHighLevel integration

GHL stays the lead inbox, automation engine, chat, reviews and Social Planner. The website just feeds it. Everything lives in `integrations` in the client's `site.py`.

| Setting | Where to get it in GHL | What it does |
|---|---|---|
| `ghl_tracking_snippet` | Settings → External Tracking → Copy Script (paste the whole `<script …></script>`) | Added to every page of the live build (never the preview). Gives source/UTM attribution and page views in GHL, and captures the native form. **Required to launch.** |
| `form_mode: "ghl_embed"` + `ghl_form_id` | Sites → Forms → your form → Integrate | Contact page shows the GHL form (iframe). The most proven option, and the default. |
| `form_mode: "native"` | (uses the tracking snippet) | Contact page shows the site's own styled form. The tracking script captures submissions into GHL Contacts and Form Submissions. If the script didn't load (ad blocker or outage), the visitor sees "please call or text" instead of a false "sent". Includes a hidden spam trap. |
| `ghl_chat_widget_id` | Sites → Chat Widget | Chat bubble on every page |
| `gtm_id` | Google Tag Manager | GA4 and conversion tags |
| `google_reviews_url` | Google Business Profile | "Read more reviews on Google" button |

Without a form ID or native mode, the contact page shows a **demo form** that clearly says it's a preview. The launch check blocks it.

**In GHL, for every client:**
- A workflow on the form submission (embed) or on "External form submitted" (native) → notify the owner by SMS and email, plus your normal follow-up.
- Social Planner → New Post → RSS Post → `https://<domain>/blog/rss.xml`, so new blog posts auto-share to Facebook, Instagram and GBP.

## Launch check (nothing falls through the cracks)

```bash
python3 build.py palmetto-pool --check
```

**Blockers** (any one stops a launch):
- Demo form still in place
- Missing GHL tracking script
- Placeholder legal pages: write them to `clients/<client>/legal/<slug>.md`
- Blog posts not yet migrated from the old site, since their URLs would 404
- Placeholder reviews
- `example.com` domain

**Warnings** (things to verify by hand):
- Send a real test lead and confirm it lands in GHL and the owner gets notified
- GTM, the Google reviews link, the share image, and a text placeholder logo

Set `"launched": True` in the client's `site.py` when the domain points to Cloudflare. From then on, any blocker **stops the Cloudflare build**, so the live site keeps serving its last good version instead of shipping a broken form or a 404.

## Deploying (Cloudflare Pages, free)

Each client is its own Cloudflare Pages project, and every project builds from this one repo. The free plan covers unlimited bandwidth, up to 100 projects and free SSL.

**First time only:** create a free account at dash.cloudflare.com, then go to **Workers & Pages → Create → Pages → Connect to Git** and authorize GitHub for the `SteelcladDigital` account.

**For each client:**
1. Go to **Workers & Pages → Create → Pages → Connect to Git** and pick `Steelclad-site-kit`.
2. Name the project after the client, for example `palmetto-pool`. That gives a free preview address like `palmetto-pool.pages.dev`.
3. Build settings:
   - Framework preset: **None**
   - Build command: `python3 build.py palmetto-pool`
   - Build output directory: `dist/palmetto-pool`
   - Production branch: `main`
4. Click **Save and Deploy**, then review the `*.pages.dev` link with the client.
5. When the client approves, go to **Custom domains → Set up a custom domain** and follow the DNS steps. SSL is automatic.
6. Submit `https://domain/sitemap.xml` in Google Search Console.

How it behaves:
- Every push to `main` rebuilds all client sites, which is harmless because each one only changes if its files did.
- Pushes to any other branch create a private preview URL, which is handy for showing a client changes before they go live.
- `_redirects` (old URLs → new) and `404.html` work on Cloudflare Pages as-is.

**Social share image:** the build creates `og-image.jpg` automatically when Pillow is installed. Cloudflare's build environment doesn't have Pillow, so run one local build per client and commit the result to `clients/<client>/assets/og-image.jpg`. Better still, add a real 1200×630 photo there.

## Pre-launch checklist (per client)

1. `python3 build.py <client> --check` shows **READY TO LAUNCH**.
2. Client approved the preview, including every fact: services, plans and prices, hours, areas, certifications.
3. Cloudflare Pages project created and reviewed on `<project>.pages.dev`.
4. Custom domain added. Set `"launched": True` and push.
5. Live test: submit the form, confirm the GHL contact and owner notification arrive, and check the chat widget.
6. Search Console: verify the site and submit `sitemap.xml`. Then update the GBP website link and the Social Planner RSS feed.
