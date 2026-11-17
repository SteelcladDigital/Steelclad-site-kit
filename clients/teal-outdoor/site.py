"""Teal Outdoor Services — client config for Steelclad Site Kit.
Service-area business (Lexington, SC; no storefront). Build: python3 build.py teal-outdoor
Forms: Web3Forms (owner's Gmail). Tracking: client's own GTM. No GoHighLevel.
Every URL on the old GHL site is kept (service pages stay at the top level via services_hub.flat_urls)."""

LICENSE = "SC pesticide applicator license #C0035614 (Category 5 Aquatic, Category 6 Right-of-Way)"   # confirmed by Billy, Nov 2026

FAVICON_SVG = open(__file__.replace("site.py", "source/favicon.svg")).read()

# ---------------------------------------------------------------- SERVICES
# Slugs = the CURRENT live URLs. Order = growth priority (the first five also list on every city page).
SERVICES = [
    {
        "slug": "commercial-property-maintenance-lexington-sc",
        "name": "Commercial Property Maintenance",
        "short": "Scheduled grounds care for business parks, retail, HOAs and investment properties, with one point of contact.",
        "icon": "badge",
        "title": "Commercial Property Maintenance in Lexington, SC",
        "meta": "Commercial grounds maintenance in Lexington & the Midlands: mowing, weed control, pond banks and cleanups on a set schedule. Free written estimates.",
        "h1": "Commercial Property Maintenance in Lexington, SC",
        "lead": "Your property manager shouldn't have to chase the lawn crew. We put your grounds on a set schedule, tell you when we're coming and what we found, and fix problems without an argument.",
        "included_title": "What a commercial grounds program covers",
        "included": [
            ("Scheduled mowing & edging", "Large-area and detail mowing, string trimming and edging on a fixed cycle, so the property looks the same on Friday as it did on Monday."),
            ("Licensed weed control", "Large-area spraying for parking lots, curb lines, fence lines and common areas, applied by a licensed applicator."),
            ("Retention & holding ponds", "Bank mowing, shoreline vegetation control and debris removal folded into the same visit, with no second vendor to manage."),
            ("Seasonal & storm cleanups", "Leaf removal, storm debris and seasonal bed work, scheduled before tenants start calling."),
            ("Investment property cleanup", "Overgrown lots, neglected landscaping and debris cleared before you list or lease."),
            ("Reporting you can forward", "What was done, what we noticed and photos when you need them for owners, boards or inspectors."),
        ],
        "signs_title": "Built for properties like these",
        "signs": [
            "Office parks, strip centers and retail pads",
            "HOA common areas, entrances and amenity grounds",
            "Industrial sites with fence lines and access roads",
            "Rental portfolios and investment properties between tenants",
            "Multi-site accounts that want one contractor and one point of contact",
        ],
        "faqs": [
            ("Do you require a contract?", "It's your choice. Service agreements are optional, but most commercial accounts prefer one: you get a set schedule and consistent pricing, built around the property's size, the services needed and the budget."),
            ("Can you handle several properties at once?", "Yes. Multi-site clients get one point of contact, consistent service across every location and a single conversation when something needs attention."),
            ("Can you provide proof of insurance?", "Yes. Teal Outdoor Services, LLC carries insurance, and we send a certificate on request, which most property managers need before the first visit."),
            ("How quickly can you start?", "After a walkthrough and a written estimate, we set the schedule with you. Tell us your deadline when you reach out and we'll be straight with you about whether we can meet it."),
        ],
    },
    {
        "slug": "retention-pond-maintenance-lexington-sc",
        "name": "Retention Pond Maintenance",
        "short": "Bank mowing, aquatic weed control, debris removal, dredging and repairs for HOA, commercial and municipal stormwater ponds.",
        "icon": "drop",
        "title": "Retention Pond Maintenance in Lexington, SC",
        "meta": "Retention pond maintenance in Lexington & Columbia, SC: bank mowing, aquatic weed control, outlet clearing, dredging and repairs, with visit records.",
        "h1": "Retention &amp; Detention Pond Maintenance in Lexington, SC",
        "lead": "Stormwater ponds are infrastructure, and the county expects them maintained. We keep banks mowed, woody growth off the embankments, weeds out of the water and outlets clear, handle dredging and repairs when they're needed, and document every visit so you're ready when the inspection letter arrives.",
        "included_title": "Pond services, start to finish",
        "included": [
            ("Bank & slope mowing", "Embankments, side slopes and access areas mowed and trimmed, including the steep, wet ground a standard mowing crew skips."),
            ("Woody growth removal", "Saplings, brush and vines cut back from embankments and around pipes and structures, where county maintenance requirements call for it."),
            ("Aquatic weed control", "Licensed control of aquatic weeds, algae and invasive plants in the water and along the shoreline. We hold SC Category 5 (Aquatic) certification."),
            ("Inlets, outlets & trash racks", "Litter, limbs and debris removed from inlets, outlet structures and trash racks so water keeps moving."),
            ("Fence lines & access", "Perimeter fence lines sprayed and cleared, and access paths kept open for maintenance and inspections."),
            ("Dredging & sediment removal", "Built-up sediment removed to restore the pond's capacity and keep outlets working."),
            ("Structural & erosion repairs", "Washouts, eroded slopes, headwalls and outlet structures repaired and stabilized."),
            ("Visit documentation", "Before-and-after photos and notes after every visit, ready for your HOA board, property owner or county inspector."),
        ],
        "signs_title": "Your pond needs attention if…",
        "signs": [
            "Trees or brush are growing on the dam or embankment",
            "Grass on the banks hasn't been cut this season",
            "The outlet structure or trash rack is clogged with debris",
            "You've received an inspection notice from the county",
            "Algae or weeds are taking over the water surface",
            "Residents are complaining about odor, mosquitoes or an overgrown eyesore",
        ],
        "faqs": [
            ("How often does a retention pond need to be maintained?", "Most commercial and HOA ponds in the Midlands do well with monthly or every-other-month visits during the growing season, with more frequent service for high-visibility or regulated sites. We set the schedule after looking at the pond."),
            ("Are you licensed for aquatic weed control?", "Yes. We hold a South Carolina pesticide applicator license (#C0035614) with Category 5 (Aquatic) certification, so we can treat weeds and algae in the water as well as on the banks."),
            ("Can you take care of multiple ponds across several properties?", "Yes. HOAs and property managers with several ponds get one point of contact and the same standard of service at every site."),
            ("Do you provide documentation after visits?", "Yes, after every visit. You get before-and-after photos and notes you can use for HOA reporting, property owners or county inspections."),
            ("Do you do dredging or structural repairs?", "Yes. Beyond routine maintenance, we handle dredging and sediment removal, erosion and washout repairs, and outlet and headwall repairs. If your permit or the county requires an engineer's inspection or sign-off, we'll work alongside your engineer."),
        ],
    },
    {
        "slug": "right-of-way-maintenance-lexington-sc",
        "name": "Right-of-Way Maintenance",
        "short": "Roadside, utility corridor and ditch vegetation control for municipalities, utilities and large properties.",
        "icon": "truck",
        "title": "Right-of-Way Maintenance in Lexington, SC",
        "meta": "Right-of-way mowing, brush clearing and licensed vegetation control for municipalities, utilities and commercial owners in Lexington County & the Midlands.",
        "h1": "Right-of-Way Maintenance in Lexington County &amp; the Midlands",
        "lead": "Mowing, brush clearing and licensed vegetation control on a schedule built around your cycle and your compliance requirements. You get records of the work, and you talk directly to the owner, not a dispatcher.",
        "included_title": "Right-of-way services",
        "included": [
            ("Roadside mowing & trimming", "Roadsides, shoulders, fence lines and access roads mowed and trimmed on a recurring cycle."),
            ("Utility corridor clearing", "Vegetation control along power line, telecom and pipeline easements."),
            ("Brush & invasive removal", "Heavy overgrowth, brush and invasive species cleared back to the easement line."),
            ("Licensed vegetation control", "Herbicide application under our SC Category 6 (Right-of-Way) certification to keep regrowth down between mowing cycles."),
            ("Ditch & drainage ROW", "Drainage ditches and swales kept clear so water moves where it's designed to."),
            ("Post-storm clearing", "Downed limbs and debris cleared from rights-of-way after storms, for clients in our service area."),
        ],
        "signs_title": "Who we work with",
        "signs": [
            "City and county road, public works and parks departments",
            "Electric cooperatives and utility operators",
            "Telecom and pipeline easement holders",
            "SCDOT contractors and subcontractors",
            "Commercial and industrial owners with fence lines and access roads",
        ],
        "faqs": [
            ("Are you licensed for chemical vegetation control?", "Yes. We hold a South Carolina pesticide applicator license (#C0035614) with Category 6 (Right-of-Way) certification, covering roadside, utility corridor and easement applications."),
            ("Do you offer ongoing right-of-way contracts?", "Yes. We run recurring programs under a service agreement on monthly, seasonal or custom cycles, set around your growth season and compliance requirements."),
            ("Do you provide records for compliance reporting?", "Yes. We provide records of completed work for municipal reporting and utility compliance programs."),
            ("Can you handle emergency storm clearing?", "Yes. We respond to post-storm right-of-way clearing in our service area. Call (803) 240-8356."),
        ],
    },
    {
        "slug": "lawn-care-lexington-sc",
        "name": "Lawn Care & Maintenance",
        "short": "Weekly or bi-weekly mowing, edging, trimming and cleanup for homes and commercial properties.",
        "icon": "leaf",
        "title": "Lawn Care & Mowing in Lexington, SC",
        "meta": "Weekly and bi-weekly lawn care in Lexington, SC: mowing, edging, trimming and cleanup for homes and businesses. Written estimates. Call (803) 240-8356.",
        "h1": "Lawn Care in Lexington, SC That Keeps Your Yard Sharp Every Week",
        "lead": "Mowing, edging, trimming and a clean blow-off on a schedule you can count on. You'll know when we're coming, and if something isn't right, we come back and fix it.",
        "included_title": "Every lawn visit includes",
        "included": [
            ("Mowing", "Cut at the right height for the season and your grass, on a weekly or bi-weekly schedule."),
            ("Edging", "Clean lines along driveways, walks and curbs."),
            ("String trimming", "Around beds, fences, trees and structures, where the mower can't reach."),
            ("Blow-off & cleanup", "Clippings blown off hard surfaces before we leave, every visit."),
            ("Add-ons when you want them", "Weed control, shrub trimming and seasonal cleanups added to the same visit."),
        ],
        "signs_title": "A good fit if…",
        "signs": [
            "Your last lawn service stopped showing up or calling back",
            "You'd rather spend Saturdays doing anything else",
            "You manage a rental or commercial property that has to look kept",
            "You want one company for the lawn, beds, weeds and cleanups",
        ],
        "faqs": [
            ("How often will you mow my lawn?", "Most residential clients are on a weekly or bi-weekly schedule, depending on the season and how fast the yard grows."),
            ("Do I have to sign a contract?", "No. Service agreements are optional. We offer one-time cuts and cleanups as well as recurring plans, with or without an agreement."),
            ("Do you mow commercial properties too?", "Yes. We work with property managers, landlords and commercial owners across Lexington County, including multi-unit and multi-location properties."),
        ],
    },
    {
        "slug": "landscaping-lexington-sc",
        "name": "Landscaping",
        "short": "Design, installation, bed renovation, mulch and planting that holds up in the Midlands.",
        "icon": "sparkle",
        "title": "Landscaping in Lexington, SC: Design & Install",
        "meta": "Landscape design and installation in Lexington, SC: new beds, bed renovation, mulch and planting for homes and businesses. Free written estimates.",
        "h1": "Landscaping in Lexington, SC: Curb Appeal That Lasts",
        "lead": "We walk the property with you, build a plan that fits it and your budget, and give you a written estimate before anything goes in the ground. No surprises.",
        "included_title": "Landscaping services",
        "included": [
            ("Design & installation", "A plan built around your property, sun, soil and budget, then installed by the same crew."),
            ("Bed creation & edging", "New beds cut in with clean, lasting edges."),
            ("Mulching", "Fresh mulch for color, moisture and weed suppression."),
            ("Planting", "Trees, shrubs and perennials chosen to handle Midlands heat and humidity."),
            ("Bed renovation", "Overgrown or dated beds cleared, reworked and replanted."),
            ("Hardscape coordination", "Walkways, borders and other hardscape elements planned to fit the landscape."),
        ],
        "signs_title": "Common landscaping projects",
        "signs": [
            "Refreshing a front yard before you sell",
            "Replacing overgrown shrubs that swallowed the windows",
            "Entrance and sign beds for HOAs and businesses",
            "Turning a bare new-construction yard into a finished one",
        ],
        "faqs": [
            ("Do you do landscape design or just installation?", "Both. We build a plan that fits the property and the budget, then handle the full installation."),
            ("Can you redo an existing landscape that's overgrown or dated?", "Yes, and it's one of our most common requests. We assess what's there, remove or relocate what needs to move, and rebuild the beds."),
            ("Do you landscape commercial properties?", "Yes. We work with commercial owners and managers throughout Lexington County."),
        ],
    },
    {
        "slug": "weed-control-lexington-sc",
        "name": "Chemical Weed Control",
        "short": "Licensed pre- and post-emergent treatments for lawns, lots, fence lines and parking areas.",
        "icon": "shield",
        "title": "Weed Control in Lexington, SC | Licensed Applicator",
        "meta": "Licensed weed control in Lexington, SC: pre-emergent and post-emergent treatments for lawns, commercial lots, fence lines and large areas. Free estimates.",
        "h1": "Licensed Weed Control in Lexington, SC",
        "lead": "Licensed chemical treatments (SC pesticide applicator license #C0035614) that hit weeds at the root and stop new ones before they start. We'll tell you exactly what we're applying and what to expect.",
        "included_title": "Weed control services",
        "included": [
            ("Pre-emergent treatments", "Applied ahead of the season to stop new weeds before they come up."),
            ("Post-emergent treatments", "Targeted treatment for weeds that are already growing."),
            ("Residential lawn programs", "Scheduled treatments matched to your grass type."),
            ("Commercial & large-area spraying", "Parking lots, curb lines, fence lines, vacant lots and common areas."),
        ],
        "signs_title": "Where we treat",
        "signs": [
            "Lawns and landscape beds",
            "Parking lot cracks and curb lines",
            "Fence lines and building perimeters",
            "Vacant lots, pond banks and rights-of-way",
        ],
        "faqs": [
            ("How long until I see results?", "Post-emergent treatments usually show visible results in 7–14 days. Pre-emergent results show up as weeds that never come up."),
            ("Is chemical weed control safe for my lawn and plants?", "When a licensed applicator applies it correctly, yes. We match products to your grass and plants and tell you about any precautions after treatment."),
            ("Do you treat large commercial properties?", "Yes, including large-area and lot spraying for property managers, developers and commercial owners across the Midlands."),
        ],
    },
    {
        "slug": "tree-trimming-removal-lexington-sc",
        "name": "Tree Trimming & Removal",
        "short": "Trimming, removal and hazardous limbs, with every branch hauled off.",
        "icon": "tool",
        "title": "Tree Trimming & Removal in Lexington, SC",
        "meta": "Tree trimming, tree removal and hazardous limb removal in Lexington, SC. We haul everything off and leave the property clean. Free written estimates.",
        "h1": "Tree Trimming &amp; Removal in Lexington, SC",
        "lead": "Dead wood down, property cleaned up. We trim and remove trees safely, then haul off every branch, log and leaf, so you're not left with a mess.",
        "included_title": "Tree services",
        "included": [
            ("Trimming & shaping", "Crown thinning, raising and shaping for health, clearance and looks."),
            ("Tree removal", "Removal of trees of all sizes with the crew and equipment the job needs."),
            ("Hazardous limbs", "Dead, cracked or overhanging limbs taken down before they fall."),
            ("Full cleanup & hauling", "Branches, wood and leaves hauled away. No separate pickup to arrange."),
            ("Stump grinding & lot clearing", "Available on many jobs. Ask when you request your estimate."),
        ],
        "signs_title": "Call us if you notice",
        "signs": [
            "Dead or hanging limbs over the house, drive or parking lot",
            "Branches rubbing the roof or touching service lines",
            "A tree leaning more than it used to after a storm",
            "Limbs blocking signs, lights or sight lines on a commercial property",
        ],
        "faqs": [
            ("Do you handle large trees?", "Yes. We take on trees of all sizes with the right crew and equipment for the job."),
            ("Do you remove the stump?", "Stump grinding is available on many jobs. Ask about it when you request your estimate."),
            ("Will you clean up the debris?", "Yes. Branches, wood and leaves are all hauled off."),
        ],
    },
    {
        "slug": "yard-cleanup-lexington-sc",
        "name": "Yard & Property Cleanup",
        "short": "One-time or recurring cleanup for overgrown yards, rentals and post-storm debris, all hauled away.",
        "icon": "wrench",
        "title": "Yard Cleanup in Lexington, SC | Overgrown & Storm",
        "meta": "Overgrown yard, rental turnover or storm debris? One-time or recurring yard cleanup in Lexington, SC, with everything hauled away. Free written estimates.",
        "h1": "Yard Cleanup in Lexington, SC: Overgrown? We Fix That.",
        "lead": "No yard is too far gone. We clear overgrowth, leaves, brush and storm debris and haul it all away, as a one-time job or on a recurring schedule.",
        "included_title": "Cleanup services",
        "included": [
            ("Overgrown yards & lots", "Tall grass, brush and briars cut back and cleared."),
            ("Leaves & seasonal debris", "Fall leaf removal and seasonal cleanups."),
            ("Post-storm cleanup", "Limbs and storm debris cleared and hauled."),
            ("Bed cleanup", "Weeds and overgrowth pulled, beds reset."),
            ("Rental & investment turnovers", "Neglected rentals cleaned up before listing or leasing."),
        ],
        "signs_title": "Typical cleanup jobs",
        "signs": [
            "A rental that sat empty all summer",
            "An estate or inherited property getting ready to sell",
            "Limbs everywhere after a storm",
            "Beds that disappeared under weeds and vines",
        ],
        "faqs": [
            ("Do you haul everything away?", "Yes. Leaves, brush and debris leave with our crew, so you don't need to arrange a separate pickup."),
            ("Can I book a one-time cleanup?", "Yes. One-time cleanups carry no ongoing obligation. Recurring plans are there if you want them."),
        ],
    },
    {
        "slug": "fence-installation-lexington-sc",
        "name": "Fence Installation & Repair",
        "short": "Wood and vinyl privacy fences, gates and repairs for homes and commercial properties.",
        "icon": "layers",
        "title": "Fence Installation & Repair in Lexington, SC",
        "meta": "Wood and vinyl privacy fence installation, gates and fence repair in Lexington, SC, for homes and commercial properties. Free written estimates.",
        "h1": "Fence Installation &amp; Repair in Lexington, SC",
        "lead": "Privacy, security and a clean property line. We install wood and vinyl privacy fences and gates, repair what's already there, and clean up completely when we're done.",
        "included_title": "Fence services",
        "included": [
            ("Wood privacy fences", "New wood privacy fence installation."),
            ("Vinyl privacy fences", "Low-maintenance vinyl privacy fencing."),
            ("Gates", "New gates installed and old gates rehung."),
            ("Repairs", "Panel replacement, post correction and section replacement."),
            ("Commercial fencing", "Fencing for commercial properties."),
        ],
        "signs_title": "Repair or replace?",
        "signs": [
            "A few leaning posts or broken boards: usually a repair",
            "A sagging gate: usually a rehang or new hardware",
            "Widespread rot or storm damage: often a section or full replacement",
            "We'll tell you which makes more sense, and why",
        ],
        "faqs": [
            ("What types of fencing do you install?", "Wood and vinyl privacy fences for residential and commercial properties, plus gates, post reinforcement and repairs. We go over options during the estimate visit."),
            ("How long does fence installation take?", "Most residential projects take one to two days, depending on footage and site conditions. You'll get a timeline after we look at the property."),
        ],
    },
    {
        "slug": "outdoor-lighting-lexington-sc",
        "name": "Outdoor Lighting",
        "short": "Low-voltage landscape, pathway and accent lighting for homes and commercial properties.",
        "icon": "bolt",
        "title": "Outdoor Lighting & Lightscaping in Lexington, SC",
        "meta": "Low-voltage outdoor lighting in Lexington, SC: pathway, accent and landscape lighting for homes and commercial properties, timer and smart-control ready.",
        "h1": "Outdoor Lighting in Lexington, SC: Your Property, After Dark",
        "lead": "Low-voltage lightscaping that shows off the landscape, lights the way and makes a property look cared for after dark.",
        "included_title": "Lighting services",
        "included": [
            ("Design & installation", "Low-voltage (12V) lighting systems designed around your property."),
            ("Pathway & walkway lighting", "Safer, better-looking walks and entries."),
            ("Accent & uplighting", "Trees, beds and architecture highlighted at night."),
            ("Entertainment areas", "Patios and outdoor living spaces you can actually use after sunset."),
            ("Commercial & storefront", "Lighting for storefronts, entrances and office properties."),
            ("Timers & smart controls", "Systems compatible with timers and most smart-lighting controllers."),
        ],
        "signs_title": "Why low-voltage",
        "signs": [
            "Runs on 12V instead of 120V, so it's safer around the yard",
            "Energy-efficient to run",
            "Easy to adjust or add fixtures later",
            "Works with timers and smart controls",
        ],
        "faqs": [
            ("Can the lights run on a timer or smart app?", "Yes. Our systems work with timers and most smart-lighting controllers."),
            ("Do you light commercial properties?", "Yes. We light storefronts, office complexes and other commercial properties in Lexington County."),
        ],
    },
]

# ---------------------------------------------------------------- AREAS
# NEW pages (the old site had one /service-area page with no city pages). Slugs: property-maintenance-<city>-sc.
# Facts kept conservative and verifiable; have Billy sanity-check them (NOTES.md).
AREAS = [
    {
        "slug": "property-maintenance-lexington-sc", "city": "Lexington", "county": "Lexington County",
        "zips": "29072, 29073",
        "intro": "Lexington is home base. We live and work here, and the town has grown fast: new subdivisions, shopping centers along Sunset Boulevard and US-378, and business parks that all need grounds kept up. Most of our routes start a few minutes from your property.",
        "local": [
            ("Growth means more stormwater ponds", "Nearly every newer subdivision and commercial site around Lexington drains to a retention or detention pond. Lexington County asks private pond owners to keep them maintained and inspected every year, and we handle the routine work."),
            ("HOAs and shopping centers", "Entrances, common areas, parking lot edges and pond banks on one schedule, with one point of contact."),
            ("Homeowners, too", "Weekly mowing, beds, weed control, fences and tree work for Lexington homes."),
        ],
        "faqs": [
            ("Are you based in Lexington, SC?", "Yes. Teal Outdoor Services is a Lexington, SC company, and Lexington is the center of our service area. Call or text (803) 240-8356."),
        ],
    },
    {
        "slug": "property-maintenance-west-columbia-sc", "city": "West Columbia", "county": "Lexington County",
        "zips": "29169, 29170, 29172",
        "intro": "West Columbia mixes established neighborhoods near the Congaree River, commercial corridors and industrial parks around the airport and 12th Street Extension. That's a lot of fence line, roadside and pond bank to keep under control.",
        "local": [
            ("Industrial and flex properties", "Large mowing areas, fence lines and access roads where weed control and right-of-way style clearing matter more than flower beds."),
            ("Established neighborhoods", "Mature trees mean hazardous limbs, leaf cleanup and overgrown beds. We handle all three."),
            ("Rental turnovers", "Overgrown rentals cleaned up and kept up between tenants."),
        ],
        "faqs": [
            ("Do you serve all of West Columbia?", "Yes. We cover West Columbia (29169, 29170 and 29172), just minutes from our Lexington base."),
        ],
    },
    {
        "slug": "property-maintenance-cayce-sc", "city": "Cayce", "county": "Lexington County",
        "zips": "29033",
        "intro": "Cayce sits along the Congaree River across from downtown Columbia, with older neighborhoods, commercial strips along Knox Abbott Drive and industrial sites to the south. Properties here need dependable, no-drama upkeep.",
        "local": [
            ("Commercial strips & small businesses", "Mowing, edging, litter pickup and weed control along curb lines and parking lots, so the storefront looks open for business."),
            ("Older trees, older lots", "Tree trimming, hazardous limb removal and overgrowth cleanup on established lots."),
            ("Low-lying ground near the river", "Drainage swales and ditches kept clear so water keeps moving after heavy rain."),
        ],
        "faqs": [
            ("Do you offer lawn care and property maintenance in Cayce, SC?", "Yes. Cayce (29033) is part of our regular Lexington County service area."),
        ],
    },
    {
        "slug": "property-maintenance-irmo-sc", "city": "Irmo", "county": "Lexington & Richland Counties",
        "zips": "29063",
        "intro": "Irmo straddles the Lexington and Richland county line between Lake Murray and Harbison. Neighborhoods, HOA amenities and busy commercial corridors along St. Andrews and Lake Murray Boulevard all need regular, reliable grounds care.",
        "local": [
            ("Two counties, one crew", "Whether the property falls in Lexington or Richland County, we keep the same schedule and the same standard."),
            ("HOA communities", "Entrances, common areas, amenity grounds and stormwater ponds handled in one program."),
            ("Wooded lots near the lake", "Leaf cleanup, tree trimming and bed renovation for heavily shaded properties."),
        ],
        "faqs": [
            ("Is Irmo in your service area?", "Yes. We serve Irmo (29063) on both the Lexington County and Richland County sides."),
        ],
    },
    {
        "slug": "property-maintenance-chapin-sc", "city": "Chapin", "county": "Lexington County",
        "zips": "29036",
        "intro": "Chapin calls itself the Capital of Lake Murray, and plenty of properties here are lake homes, larger wooded lots and newer subdivisions off I-26. Owners want the place kept up whether they're there that weekend or not.",
        "local": [
            ("Lake homes & second homes", "Recurring mowing and cleanups so the property looks kept when you arrive."),
            ("Larger and wooded lots", "Tree work, brush clearing and overgrowth cleanup beyond what a standard mowing crew takes on."),
            ("New subdivisions", "HOA common areas and stormwater pond banks maintained on a schedule."),
        ],
        "faqs": [
            ("Do you serve Chapin and the Lake Murray area?", "Yes. Chapin (29036) and the surrounding Lake Murray communities are in our service area."),
        ],
    },
    {
        "slug": "property-maintenance-columbia-sc", "city": "Columbia", "county": "Richland County",
        "zips": "29201–29229",
        "intro": "Columbia has the Midlands' biggest concentration of office parks, apartment communities, retail centers and institutional grounds, and plenty of stormwater ponds behind them. Richland County runs a Private Pond Inspection Program, so owners need ponds that pass.",
        "local": [
            ("Commercial and multifamily grounds", "Recurring mowing, weed control, cleanups and bed care across large properties, with one point of contact."),
            ("Richland County pond inspections", "Richland County inspects private detention and retention ponds and gives owners 30 days to correct violations. We keep banks, vegetation and outlets in shape and document the work."),
            ("Right-of-way and corridors", "Roadside, ditch and easement vegetation control for public and private clients."),
        ],
        "faqs": [
            ("Do you serve Columbia and Richland County?", "Yes. We serve Columbia and surrounding Richland County communities, especially commercial, HOA and pond maintenance clients."),
        ],
    },
    {
        "slug": "property-maintenance-gilbert-sc", "city": "Gilbert", "county": "Lexington County",
        "zips": "29054",
        "intro": "Gilbert is rural Lexington County: farms, peach country, pastures and homes on several acres. Properties here need more than a quick mow-and-go, including fence lines, field edges, brush and big trees.",
        "local": [
            ("Acreage & large lots", "Large-area mowing, field edges and brush clearing."),
            ("Fence lines & driveways", "Long fence lines and private drives cleared and sprayed so they stay open."),
            ("Tree work & storm cleanup", "Hazardous limbs and storm debris on wooded properties."),
        ],
        "faqs": [
            ("Do you work on rural properties around Gilbert?", "Yes. We serve Gilbert (29054) and handle larger rural properties, fence lines and brush."),
        ],
    },
    {
        "slug": "property-maintenance-batesburg-leesville-sc", "city": "Batesburg-Leesville", "county": "Lexington County",
        "zips": "29006, 29070",
        "intro": "Batesburg-Leesville anchors western Lexington County along US-1, with an industrial park, small-town commercial properties and rural acreage around it. We bring the same scheduled, documented service to the west end of the county.",
        "local": [
            ("Industrial & commercial sites", "Large-area mowing, weed control and fence line clearing on industrial and commercial properties."),
            ("Rural roads & easements", "Right-of-way mowing and brush clearing along roadsides and private access roads."),
            ("Homes & small businesses", "Lawn care, cleanups and landscaping in town."),
        ],
        "faqs": [
            ("Do you travel to Batesburg-Leesville?", "Yes. Batesburg-Leesville (29006 and 29070) is in our regular service area."),
        ],
    },
    {
        "slug": "property-maintenance-gaston-sc", "city": "Gaston", "county": "Lexington County",
        "zips": "29053",
        "intro": "Gaston is a small, rural town in southern Lexington County along US-321. Homes sit on bigger lots, and roadsides and fence lines grow fast through a long Midlands summer.",
        "local": [
            ("Large lots & acreage", "Mowing, brush clearing and overgrowth cleanup for larger properties."),
            ("Fence lines & ditches", "Fence lines sprayed and ditches kept clear so water drains."),
            ("Tree & storm work", "Hazardous limbs and storm debris removed and hauled."),
        ],
        "faqs": [
            ("Do you serve Gaston, SC?", "Yes. Gaston (29053) is part of our southern Lexington County service area."),
        ],
    },
    {
        "slug": "property-maintenance-swansea-sc", "city": "Swansea", "county": "Lexington County",
        "zips": "29160",
        "intro": "Swansea is a small town in southern Lexington County with rural homesites, farms and small businesses. It's the kind of area where one dependable crew for mowing, brush, weeds and trees saves a lot of phone calls.",
        "local": [
            ("Rural homes & acreage", "Large-area mowing, field edges and brush clearing."),
            ("Small businesses & churches", "Recurring grounds care and weed control on a set schedule."),
            ("Overgrowth cleanup", "Properties that got away from their owners, cleared and hauled."),
        ],
        "faqs": [
            ("Do you serve Swansea, SC?", "Yes. Swansea (29160) is in our southern Lexington County service area."),
        ],
    },
    {
        "slug": "property-maintenance-newberry-sc", "city": "Newberry", "county": "Newberry County",
        "zips": "29108",
        "intro": "Newberry, the Newberry County seat up I-26, has a historic downtown, a college campus, commercial corridors and plenty of rural land around it. We bring Midlands commercial and right-of-way service up the interstate.",
        "local": [
            ("Commercial & institutional grounds", "Recurring mowing, weed control and cleanups for commercial and institutional properties."),
            ("Roadsides & easements", "Right-of-way mowing and vegetation control for public and private clients."),
            ("Rural properties", "Brush clearing, fence lines and tree work on larger lots."),
        ],
        "faqs": [
            ("Do you serve Newberry County?", "Yes. We serve Newberry (29108) and nearby Newberry County communities, especially commercial and right-of-way clients."),
        ],
    },
    {
        "slug": "property-maintenance-prosperity-sc", "city": "Prosperity", "county": "Newberry County",
        "zips": "29127",
        "intro": "Prosperity is a small Newberry County town near the upper end of Lake Murray, with lake properties, farmland and rural homesites around it.",
        "local": [
            ("Lake & weekend properties", "Recurring mowing and cleanups so the place is ready when you are."),
            ("Rural acreage", "Field edges, fence lines and brush cleared and kept back."),
            ("Tree work", "Trimming, removals and storm cleanup on wooded lots."),
        ],
        "faqs": [
            ("Is Prosperity in your service area?", "Yes. Prosperity (29127) and the upper Lake Murray area are part of our service area."),
        ],
    },
    {
        "slug": "property-maintenance-aiken-county-sc", "city": "Aiken County", "county": "South Carolina",
        "zips": "29801, 29803 (Aiken), 29841 (North Augusta), 29164 (Wagener) and the rest of the county",
        "intro": "Aiken County borders western Lexington County, just past Batesburg-Leesville. It We serve all of it, from Wagener to the county seat of Aiken and on to North Augusta, with commercial properties, subdivisions, horse farms and plenty of rural acreage.",
        "local": [
            ("Commercial & HOA ponds", "Retention pond maintenance, aquatic weed control, dredging and repairs for commercial sites and neighborhoods, with photos after every visit."),
            ("Roadsides & easements", "Right-of-way mowing and licensed vegetation control for public and private clients."),
            ("Farms & acreage", "Large-area mowing, fence lines, field edges and brush clearing."),
            ("Commercial grounds", "Recurring mowing, weed control and cleanups on a set schedule."),
        ],
        "faqs": [
            ("Do you serve all of Aiken County?", "Yes. We serve the whole county, including Aiken, North Augusta, Wagener and the communities in between, for commercial, retention pond, right-of-way and residential work."),
            ("Do you serve North Augusta?", "Yes. North Augusta is part of our Aiken County service area. Call or text (803) 240-8356 for a free estimate."),
        ],
    },
]

# Real reviews from the current site only (homepage). The three software/analytics "testimonials" on the old
# /about and /contact pages are template filler and were NOT carried over.
REVIEWS = [
    ("Jim B.", "Commercial weed control", "Billy takes great care of the weed control at our commercial property. Very reliable and professional."),
    ("Ashley W.", "Lawn care & landscaping", "Our lawn and landscaping has never looked better. I'd highly recommend Teal Outdoor Services to anyone!"),
    ("Sean L", "Fence installation", "Billy did a great job on my fence work. Very professional and got the work done really quickly. I would highly recommend him to anyone."),
]

GENERAL_FAQS = [
    ("How do your free estimates work?", "Tell us about the property and the work you need by form, call or text. Many jobs can be ballpark-priced from photos; larger projects get an on-site walkthrough. Either way, you get a written estimate before any work starts."),
    ("What areas do you serve?", "We're based in Lexington, SC and serve Lexington County and the Midlands: Lexington, West Columbia, Cayce, Irmo, Chapin, Gilbert, Batesburg-Leesville, Gaston, Swansea, Columbia, Newberry, Prosperity and Aiken County. Not on the list? Ask. We may already be nearby."),
    ("Do you work with commercial properties, HOAs and municipalities?", "Yes. Commercial property maintenance, retention pond maintenance and right-of-way work are our focus, and we provide documentation for boards, owners and compliance reporting."),
    ("Are you licensed and insured?", "Yes. We hold a South Carolina pesticide applicator license (#C0035614) with Category 5 (Aquatic) and Category 6 (Right-of-Way) certifications. Teal Outdoor Services, LLC carries insurance, and we send a certificate on request."),
    ("Do you offer ongoing maintenance plans? Do I need a contract?", "Yes, and contracts are optional. Homes are usually on weekly or bi-weekly plans. Commercial accounts usually prefer a service agreement. Commercial, pond and right-of-way clients get recurring schedules (monthly, seasonal or custom) built around the property."),
    ("How fast will I hear back?", "We typically respond within one business day, and often the same day. Hours are Monday to Friday, 8 AM to 6 PM."),
]

# ---------------------------------------------------------------- RESOURCE (link-worthy guide)
POND_CHECKLIST = [
    ("Every visit", "Routine bank care", ["Mow embankments, side slopes and access areas", "Trim around pipes, headwalls and the outlet structure", "Pick up litter and floating debris", "Note anything new: washouts, slumping, leaks, animal burrows"]),
    ("Growing season · monthly", "Keep vegetation in check", ["Mow often enough that woody growth never gets established", "Treat shoreline overgrowth and invasive plants", "Spray the perimeter fence line for vines and brush", "Keep the access path open for inspectors and equipment"]),
    ("After heavy rain", "Storm check", ["Clear limbs and trash from inlets, the outlet and the trash rack", "Look for new erosion on the banks and around headwalls", "Check that swales and channels into the pond are flowing", "Photograph damage before it's repaired"]),
    ("Fall & winter", "Woody growth season", ["Cut saplings and brush off fill embankments and dams", "Clear woody growth within 30 feet of pipes and structures", "Remove leaf and limb build-up around the outlet", "Plan repairs before spring storms"]),
    ("Once a year", "Annual inspection", ["Lexington County: complete the annual stormwater pond (BMP) inspection checklist", "Richland County: expect the Private Pond Inspection Program to check private ponds", "Keep dated records and photos of the maintenance you've done", "Schedule dredging or repairs for sediment build-up and structural damage"]),
    ("What inspectors flag", "Common failure points", ["Trees or brush on the dam or embankment", "Clogged orifices, outlet structures or trash racks", "Eroded slopes, headwalls or washouts", "Sediment build-up and blocked swales, plus mowing that's fallen behind"]),
]

POND_BODY = """
<h2>Who is responsible for a stormwater pond?</h2>
<p>In South Carolina, the stormwater ponds behind subdivisions, shopping centers and office parks are usually private. When a development is permitted, the owner signs a permanent maintenance agreement, and that responsibility passes to whoever owns the property next. That's often an HOA, a property owner or a management company. The state's own guide for homeowner associations says plainly that all stormwater ponds require maintenance.</p>
<h2>What Lexington County asks pond owners to do</h2>
<p>Lexington County's post-construction pond maintenance requirements cover the same items over and over: <strong>no woody vegetation on fill embankments</strong> or within 30 feet of any structure or pipe; sediment and debris kept clear around the outlet structure and pipes; trash racks clear and secure; eroded slopes and headwalls repaired and stabilized; perimeter fence lines kept free of trees, vines and shrubs; and swales and channels kept flowing. Owners of private stormwater ponds are also asked to complete an annual inspection checklist.</p>
<h2>What Richland County does</h2>
<p>Richland County's Private Pond Inspection Program inspects privately owned detention and retention ponds. It names poor maintenance as the leading cause of pond failure. Owners who receive a Notice of Violation get 30 days to make corrections before daily penalties can apply.</p>
<h2>What we handle</h2>
<p>Teal Outdoor Services handles everything on this checklist: mowing banks and slopes, removing woody growth, aquatic and shoreline weed control, fence-line vegetation control, clearing debris from inlets, outlets and trash racks, dredging and sediment removal, and erosion and structure repairs. We document every visit with photos and notes. Our herbicide work is done under South Carolina pesticide applicator license #C0035614, with Category 5 (Aquatic) and Category 6 (Right-of-Way) certifications. If your permit calls for an engineer's inspection or sign-off, we work alongside your engineer. See <a href="/retention-pond-maintenance-lexington-sc/">retention pond maintenance</a> or <a href="/contact/">request a free pond walkthrough</a>.</p>
<p style="font-size:.9rem;color:var(--c-muted)">Sources: <a href="https://lex-co.sc.gov/sites/lexco/files/Documents/Lexington%20County/Departments/Community%20Dev/Land%20Development/LexCo%20Pond%20maintenance%20requirements%202025v1.pdf" rel="noopener">Lexington County post-construction pond maintenance requirements (2025)</a> ·
<a href="https://lex-co.sc.gov/sites/lexco/files/Documents/Lexington%20County/Departments/Community%20Dev/Land%20Development/Pond-Inspection-Form-LDM-rev-2025.pdf" rel="noopener">Lexington County annual pond inspection checklist</a> ·
<a href="https://richlandcountysc.gov/Portals/0/Departments/PublicWorks/StormDocs/Private%20Pond%20Inspection%202024.pdf" rel="noopener">Richland County Private Pond Inspection Program</a> ·
<a href="https://www.des.sc.gov/sites/des/files/docs/HomeAndEnvironment/Docs/ponds.pdf" rel="noopener">SC Department of Environmental Services stormwater pond guide</a>.
This page is a general guide, not legal or engineering advice. Your pond's approved plans and maintenance agreement govern.</p>
"""

CONFIG = {
  "business": {
    "name": "Teal Outdoor Services", "legal_name": "Teal Outdoor Services, LLC",
    "domain": "https://tealoutdoorservices.com",
    "phone": "(803) 240-8356", "tel": "+18032408356",
    "email": "tealoutdoorservices@gmail.com",
    "schema_type": ["LocalBusiness", "HomeAndConstructionBusiness"],
    "description": "Lexington, SC outdoor services company for commercial property maintenance, retention pond maintenance, right-of-way vegetation control, lawn care and landscaping across Lexington County and the Midlands.",
    "address": {"locality": "Lexington", "region": "SC"},     # service-area business: no street address published
    "geo": (33.9815, -81.2362),
    "hours": [(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "08:00", "18:00")],
    "hours_text": "Mon–Fri 8 AM – 6 PM",
    "counties": ["Lexington County, SC", "Richland County, SC", "Newberry County, SC", "Aiken County, SC"],
    "knows_about": ["Commercial grounds maintenance", "Stormwater retention pond maintenance", "Right-of-way vegetation management", "Chemical weed control", "Lawn care", "Landscaping"],
    "founder": "Billy Lander",
    "slogan": "We do what we say. When we say we'll do it.",
    "social": {},
  },
  "theme": {
    # Brand colors sampled from the logo: teal #0a7376, orange #f1592a.
    # Buttons use a one-step-deeper orange (#cf4418) so white button text passes WCAG AA contrast.
    "colors": {"primary": "#0a7376", "primary_deep": "#06504f", "secondary": "#6fd0c7", "secondary_deep": "#0a7376",
               "secondary_wash": "#e7f5f4", "accent": "#cf4418", "accent_text": "#ffffff", "surface": "#f4f8f7",
               "ink": "#14302f", "muted": "#4a5f5e", "texture": "#f1592a", "highlight": "#ffb08f"},   # highlight: light orange for accents on dark teal
    "fonts": {"display": "archivo", "body": "inter"},
    "radius": "soft", "heading_case": "none", "divider": "angle", "texture": "lines", "hero_layout": "card",
    "header": "light",   # white header so the full-color logo reads, as on the original site
  },
  "logo": {"type": "image", "file": "logo.webp", "footer_file": "logo-footer.webp", "schema_file": "logo-light-bg.png", "width": 142, "height": 64},
  "favicon_svg": FAVICON_SVG,
  "integrations": {
    "form_mode": "web3forms",
    "web3forms_access_key": "ef0d9cca-cbe0-4e7e-8695-2de2ca8ed9a3",   # created with tealoutdoorservices@gmail.com (public by design)
    "web3forms_subject": "New estimate request from tealoutdoorservices.com",
    "web3forms_from_name": "Teal Outdoor Services website",
    "thank_you_slug": "thank-you",
    "gtm_id": "GTM-W3KKNTH5",          # client's OWN Tag Manager account
    "google_reviews_url": "",           # TODO: GBP "read reviews" link once confirmed
  },
  "launched": False,                   # set True only after client approval + clean --check, when DNS points to Cloudflare
  "labels": {
    "cta": "Get a Free Estimate", "cta_short": "Free Estimate", "cta_long": "Get Your Free Estimate",
    "phone_prefix": "Call or text", "topbar_promise": "We do what we say. When we say we'll do it.",
    "footer_blurb": "Commercial property, retention pond and right-of-way maintenance, plus lawn care and landscaping, from a Lexington, SC company that shows up and follows through.",
    "footer_services_title": "Services",
    "reviews_title": "What our customers say",
    "cta_band_title": "Ready to stop chasing your grounds crew?",
    "cta_band_text": "Get a free, no-obligation estimate. We'll look at your property and give you a straight answer in writing, with no pressure and no runaround.",
    "aside_title": "Get a free estimate", "aside_text": "Talk directly to the owner. We typically respond within one business day.",
    "aside_badges": "✓ SC pesticide license #C0035614 · ✓ Insured · ✓ Written estimates",
  },
  "home": {
    "title": "Commercial Property & Pond Maintenance, Lexington SC",
    "meta": "Commercial grounds, retention pond and right-of-way maintenance plus lawn care and landscaping in Lexington & the Midlands. Free written estimates.",
    "eyebrow": "Lexington County & the Midlands",
    "h1": "Commercial property, pond &amp; right-of-way maintenance from a crew that <em>shows up and follows through</em>",
    "lead": "Teal Outdoor Services keeps commercial grounds, HOA retention ponds and rights-of-way across the Midlands on schedule, and tells you what we did and what we found. Lawn care and landscaping for homeowners, too.",
    "secondary_cta": ("See Our Services", "services"),
    "proof": ["SC licensed: aquatic & right-of-way", "Before & after photos every visit", "Talk directly to the owner"],
    "hero_card": {"label": "Visit report", "title": "Retention pond · HOA common area", "sub": "What you get after a maintenance visit", "badge": "Example", "hanger": False,
                  "checks": ["Banks & slopes mowed", "Woody growth cut back", "Outlet & trash rack cleared", "Litter & debris removed", "Fence line sprayed", "Before & after photos"],
                  "note": "Noted: small washout on the north bank by the inlet pipe. Photos attached. We can repair it before the next heavy rain. Want a quote?"},
    "trust": [("doc", "Written estimates", "Before any work starts"), ("shield", "SC licensed #C0035614", "Aquatic & right-of-way categories"),
              ("check", "Documented visits", "Photos & notes for boards and inspectors"), ("phone", "Owner-run", "Billy oversees every job")],
    "why": {"eyebrow": "Why Teal",
            "quote_html": "We do what we say. <em>When we say we'll do it.</em>",
            "body": "That sounds simple. But if you've hired an outdoor services company before, you know it's rare. Billy Lander built Teal Outdoor Services on communication and follow-through: no surprises, no ghosting, and no chasing us down for an update.",
            "items": [("phone", "You'll always know what's happening.", "We communicate before, during and after every job."),
                      ("doc", "You'll have the paperwork.", "Visit notes and before-and-after photos when your board, owner or inspector asks."),
                      ("check", "Quality that actually shows.", "The job isn't done until it looks right and the site is cleaned up. If it's not right, we fix it."),
                      ("home", "Local. Invested. Accountable.", "We live and work in Lexington County. Your property is our reputation, driving down your street.")]},
    "steps": {"eyebrow": "Getting started", "title": "From first call to a set schedule",
              "items": [("Call, text or send the form", "(803) 240-8356. Tell us about the property and what it needs."),
                        ("Photos or a walkthrough", "Many jobs can be priced from photos. Larger properties get an on-site walkthrough."),
                        ("Written estimate", "You see the scope and price in writing before anything starts."),
                        ("We show up and report back", "On schedule, with a heads-up before we come and a summary after.")]},
    "form": {"eyebrow": "Free estimate", "title": "Tell us about your property",
             "lead": "Commercial, HOA, municipal or residential: send the basics and we'll get back to you, typically within one business day.",
             "points": ["Written estimate before any work", "Photo pricing for many jobs", "One point of contact: the owner"]},
    "order": ["trust", "services", "why", "reviews", "steps", "areas", "form", "blog", "faq", "cta"],
  },
  "services_hub": {"slug": "services", "flat_urls": True, "home_count": 6, "nav_label": "Services",
    "title": "Outdoor & Grounds Services in Lexington, SC",
    "meta": "Commercial grounds, retention ponds, right-of-way, lawn care, landscaping, weed control, tree work, cleanups, fences & lighting in Lexington, SC.",
    "h1": "Outdoor Services in Lexington &amp; the Midlands",
    "lead": "One crew for the whole property: commercial grounds, stormwater ponds and rights-of-way, plus lawn care, landscaping, weed control, tree work, cleanups, fences and lighting.",
    "home_title": "Everything your property needs. One crew, no excuses.",
    "home_lead": "From commercial grounds programs and HOA pond banks to weekly mowing and privacy fences, we handle it so you don't have to manage three different contractors."},
  "services": SERVICES,
  "areas": {
    "enabled": True, "hub_slug": "service-area", "nav_label": "Service Area", "link_prefix": "Property Maintenance",
    "hub_title": "Service Area: Lexington County & the Midlands, SC",
    "hub_meta": "Teal Outdoor Services serves Lexington County, Columbia, Irmo, Chapin, Batesburg-Leesville, Swansea, Newberry, Prosperity and Aiken County, SC.",
    "hub_h1": "Local Service for Lexington County &amp; the Midlands",
    "hub_lead": "Based in Lexington, SC, we cover Lexington County and reach into Richland, Newberry and Aiken counties for commercial, pond and right-of-way clients.",
    "home_title": "Proudly serving Lexington County & beyond",
    "groups": [{"name": "Lexington County", "note": "Home base", "slugs": ["property-maintenance-lexington-sc", "property-maintenance-west-columbia-sc", "property-maintenance-cayce-sc", "property-maintenance-irmo-sc", "property-maintenance-chapin-sc", "property-maintenance-gilbert-sc", "property-maintenance-batesburg-leesville-sc", "property-maintenance-gaston-sc", "property-maintenance-swansea-sc"]},
               {"name": "Richland, Newberry & Aiken Counties", "note": "Commercial, pond & ROW", "slugs": ["property-maintenance-columbia-sc", "property-maintenance-irmo-sc", "property-maintenance-newberry-sc", "property-maintenance-prosperity-sc", "property-maintenance-aiken-county-sc"]}],
    "outside_note": "Don't see your town? Call or text. Chances are we cover it.",
    "service_where_text": "We serve properties throughout Lexington County and the Midlands, including",
    "page_title": "Property Maintenance & Lawn Care in {city}, {region}",
    "page_meta": "Commercial property, retention pond and right-of-way maintenance plus lawn care in {city}, {region}. Free written estimates: (803) 240-8356.",
    "page_h1": "Property Maintenance &amp; Lawn Care in {city}, {region}",
    "local_title": "Outdoor services in {city}", "aside_title": "Service in {city}",
    "shared_faqs": [("How much does property maintenance cost in {city}?", "It depends on the size of the property, the services and how often. Many jobs can be priced from photos; larger properties get a walkthrough. Either way, you get a written estimate before any work starts.")],
    "pages": AREAS,
  },
  "resource": {
    "enabled": True, "slug": "pond-maintenance-checklist", "nav_label": "Pond Checklist",
    "title": "Stormwater Pond Maintenance Checklist: Lexington SC",
    "meta": "What Lexington & Richland County expect from private stormwater pond owners, plus a season-by-season checklist for HOAs and property managers.",
    "h1": "The Midlands Stormwater Pond Maintenance Checklist",
    "lead": "A plain-English checklist for HOAs, property managers and business owners with a retention or detention pond in Lexington or Richland County: what to do, when, and what county inspectors look for.",
    "cards": POND_CHECKLIST, "body_html": POND_BODY, "faq_title": "Stormwater pond questions",
    "faqs": [("Who has to maintain a retention pond on private property?", "Usually the property owner, such as the HOA, business owner or property manager, under the permanent maintenance agreement signed when the site was developed. That responsibility transfers with the property."),
             ("Why can't trees grow on a pond embankment?", "Roots can open paths for water through the fill and weaken the embankment. Lexington County's requirements call for woody vegetation to be removed from fill embankments and from within 30 feet of structures and pipes."),
             ("How often should a stormwater pond be inspected?", "Lexington County asks private pond owners to complete an annual inspection checklist, and Richland County inspects private ponds through its Private Pond Inspection Program. Routine maintenance visits in between catch problems early."),
             ("What happens if a pond fails a county inspection in Richland County?", "Richland County gives owners 30 days after a Notice of Violation to make corrections, after which daily penalties may be assessed.")],
    "cta_title": "Want this checklist handled for you?", "cta_text": "We'll walk your pond, tell you what needs attention, and put it on a documented maintenance schedule.",
  },
  "blog": {
    "enabled": True, "index_slug": "blog", "post_prefix": "post",     # keeps the old GHL URLs: /blog and /post/<slug>
    "category_prefix": "blog/category",                                # keeps /blog/category/<slug>
    "categories": {"Right of Way Maintenance": "right-of-way-maintenance", "Commercial Property Maintenance": "commercial-property-maintenance"},
    "nav_label": "Blog", "title": "Grounds & Property Maintenance Tips, Lexington SC",
    "meta": "Practical advice on commercial grounds, retention ponds, right-of-way and lawn care for Lexington County & Midlands property owners and managers.",
    "h1": "Property maintenance advice for Lexington County",
    "lead": "Straight answers for property managers, HOAs, municipalities and homeowners in the Midlands.",
    "default_author": "Billy Lander, owner", "home_title": "From the blog",
    "area_related_title": "Advice for {city} property owners",
  },
  "about": {"title": "About Teal Outdoor Services | Lexington, SC",
    "meta": "Meet Billy Lander, owner of Teal Outdoor Services: a Lexington, SC outdoor services company built on communication, follow-through and quality work.",
    "h1": "Built on a Handshake. Run on Follow-Through.",
    "lead": "Teal Outdoor Services is owner-run and Lexington-based. Billy Lander oversees every job and stays in touch with every client.",
    "story_title": "Why Billy started Teal",
    "story_html": "<p>Teal Outdoor Services didn't start in a boardroom. Billy Lander spent about a decade in corporate sales and customer relationships, and he watched businesses succeed or fail mostly on how they treated their customers.</p><p>When a downsizing opened the door, he started an outdoor services company built the way he'd always wanted to be treated as a customer: crews that arrive when promised, calls that get returned, work that's done right, and a follow-up afterward.</p><p><strong>That's not a tagline. It's how we've operated from day one.</strong> You work directly with the owner, from the first estimate to the last cleanup.</p>",
    "list_title": "How we work",
    "list": ["Communication first: when we're coming, what we'll do, what we found", "No shortcuts: done right, or redone", "Relationships over transactions", "Written estimates before any work starts", "SC pesticide applicator license #C0035614: Category 5 (Aquatic) & Category 6 (Right-of-Way)", "Insured, with certificates on request"]},
  "contact": {"title": "Free Estimate | Teal Outdoor Services, Lexington SC",
    "meta": "Request a free, no-obligation estimate for commercial, pond, right-of-way, lawn or landscaping work in Lexington County & the Midlands. (803) 240-8356.",
    "h1": "Let's Talk About Your Property",
    "lead": "Tell us what you need and we'll follow up, typically within one business day. Prefer to talk? Call or text (803) 240-8356.",
    "extra_inputs": [("company", "Company / HOA (optional)", "organization", False, True), ("address", "Property address or nearest cross street", "street-address", False, True)],
    "selects": [("Property type", ["", "Commercial (office, retail, industrial)", "HOA or community", "Municipal, utility or right-of-way", "Residential", "Rental or investment property"]),
                ("Service needed", ["", "Commercial property maintenance", "Retention pond maintenance", "Right-of-way maintenance", "Lawn care & maintenance", "Landscaping", "Chemical weed control", "Tree trimming & removal", "Yard or property cleanup", "Fence installation or repair", "Outdoor lighting", "Not sure / several"])],
    "select_names": {"Property type": "property_type", "Service needed": "service"},
    "select_placeholder": "Choose one",
    "message_label": "Tell us about the property (size, number of ponds, frequency, deadline, photos available?)",
    "submit": "Request my free estimate", "note": "No pressure, no obligation. You'll get a written estimate before any work starts.",
    "success": "Thanks! We got your request and will follow up, typically within one business day.",
    "next_steps": ["We reply, typically within one business day", "Photo pricing or an on-site walkthrough", "Written estimate before any work starts"],
    "faqs": GENERAL_FAQS[:2] + GENERAL_FAQS[3:4], "page_type": "ContactPage"},
  "thank_you": {"title": "Thank you", "h1": "Thanks, we got your request.", "lead": "We'll follow up, typically within one business day.", "text": "Need us sooner?"},
  "reviews": REVIEWS,
  "faqs": GENERAL_FAQS,
  "legal_pages": [("privacy", "Privacy Policy")],
  "redirects": [("/index-home", "/"), ("/home", "/"), ("/tealoutdoorservices.com", "/"),
                ("/commercial-lawn-care-lexington-sc", "/commercial-property-maintenance-lexington-sc/"),   # old internal link on the tree page
                ("/privacy-policy", "/privacy/"), ("/blog/tag/*", "/blog/"), ("/blog/author/*", "/blog/")],
}
