# Palmetto Pool Solutions: client notes

## Before launch: blog migration (blocker)

The 8 existing posts keep their exact URLs (`/post/<slug>`). Each has a stub in `posts/` with its title, date, description, category, author and service/area tags already filled in, and `draft: true`. For each one, copy the article text from the live URL (listed as `migrate_from` in the file), paste it as Markdown, and remove `draft: true`. Drafts aren't built, so an unmigrated post would 404 after launch.

New post (needs Mike's approval): `2026-11-11-saltwater-pool-maintenance-lexington-sc.md` targets the salt-cell and saltwater-maintenance keywords that no existing post or page covers. It links to Salt Cell & Filter Cleaning, Equipment Upgrades, the plans page and 4 city pages.

## Before launch: confirm with Mike

1. **Plan names and inclusions** (Balance / Full Service / Full Service Plus) are a *proposal*, built only from services already on his site. Confirm what each plan includes, and whether chemicals are included in the monthly rate.
2. **Consider publishing "starting at" prices.** Neither competitor (Poolman360, All Clear) shows pricing. Even "from $X/mo" on the plans page would beat both of them on conversion and give the page more to rank on.
3. **Legal pages:** paste the current Privacy, Terms and Accessibility text into the placeholder pages.
4. **Blog:** the live site has `/blog`. Migrate any posts that get traffic, or keep the blog on a subdomain. Don't let those URLs 404.
5. **Photos:** the design works without them, but 4–6 real job photos (before/after green pools, Mike on a route, the door hanger itself) would strengthen trust and image search. Add them to `src/assets/` and reference them in `site.py` (assets folder).
6. **Logo:** the header uses an SVG redraw of the wordmark and palmetto. Swap in the original vector logo if he has one.
7. **City facts:** each city page has unique local content. Have Mike sanity-check the neighborhood mentions.

## Old site vs. new site

| | Current GHL site | New build |
|---|---|---|
| Structured data | Meta tag only; no JSON-LD | Full JSON-LD on every page: LocalBusiness, Service, FAQPage, BreadcrumbList, OfferCatalog with plans, areaServed by city and county |
| H1 | Duplicated on the homepage | One unique, keyword-targeted H1 per page |
| Maintenance plans | "Custom pricing," no plan page | Dedicated `/pool-maintenance-plans/` money page: 3 tiers, comparison table, plan-finder quiz, pricing explainer, FAQ |
| City pages | 5 | 8 (added Cayce, Forest Acres, Blythewood), each with unique local copy, local FAQ and FAQ schema |
| Content assets | Blog | Midlands Pool Care Calendar: a month-by-month guide built to earn links and rank for seasonal searches |
| Internal linking | Menus only | Services ↔ cities ↔ plans cross-linked on every page; breadcrumbs |
| URLs | — | **All existing URLs kept**, so current rankings carry over. Broken `pool-service-columbia-sc2` and `/contact-page` are 301-redirected. |
| Speed | GHL builder JS + stock hero image | Static HTML, about 24 KB CSS/JS, self-hosted fonts, no render-blocking third parties |
| Mobile | Standard | Sticky Call / Text / Free Evaluation bar; tap-to-text link |
| Differentiators | Listed in text | Shown visually: the door-hanger visit report becomes the hero, "We answer our phone" sits in the top bar site-wide |

