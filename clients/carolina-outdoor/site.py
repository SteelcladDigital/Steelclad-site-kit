"""Carolina Outdoor Services, LLC: client config for Steelclad Site Kit.
Service-area business based in Gilbert, SC (Lexington County), serving SC statewide and North Carolina.
Build: python3 build.py carolina-outdoor
Forms: Web3Forms (owner's Gmail). Tracking: GTM-578PKL83 (GA4 inside GTM). No GoHighLevel.
Every URL on the old GHL site is kept: /services/<slug>, /lexington-sc, /columbia-sc, /rock-hill-sc, /gallery,
/blog, /post/<slug>, /blog/category/<slug>, /privacy-policy. The old duplicate top-level service URLs 301 to /services/<slug>/."""

FAVICON_SVG = open(__file__.replace("site.py", "source/favicon.svg")).read()

PHONE = "(803) 518-2787"
CLEMSON_MPM = "https://www.clemson.edu/extension/water/programs/mpm/"
CLEMSON_BMP = "https://www.clemson.edu/extension/water/programs/bmp/index.html"
NCSU_SCM = "https://bae.ncsu.edu/workshops-conferences/stormwater-bmp/"
SUSTAIN_SC = "https://www.sustainsouthcarolina.org"

# ---------------------------------------------------------------- PHOTOS (real job photos from the old site's gallery)
# Pulled at the size the old site served them (about 700px wide). Ask Nicky for the full-size originals (NOTES.md).
# The old site's before/after "Asset vs Liability" sliders were AI-generated images, so they are NOT used.
def P(f, alt, caption="", w=694, h=520): return {"file": "photos/" + f + ".webp", "alt": alt, "caption": caption, "w": w, "h": h}
PH = {
    "outlet": P("detention-basin-outlet-riser", "Dry detention basin with a concrete outlet riser and trash rack behind an industrial warehouse", "Detention basin and outlet riser at an industrial site"),
    "wetpond": P("commercial-wet-pond-outlet", "Wet stormwater pond with a concrete outlet structure and rock ring in front of a commercial office building", "Wet pond and outlet structure, commercial site", 520, 346),
    "mowedpond": P("retention-pond-mowed-banks", "Retention pond with freshly mowed banks and a tree line behind it", "Retention pond banks after a maintenance visit", 554, 414),
    "fenced": P("fenced-retention-pond", "Fenced dry retention basin with mowed slopes and a small outlet structure", "Fenced retention basin, mowed and trimmed"),
    "tractor": P("tractor-mowing-basin", "Tractor mowing a large stormwater basin next to a commercial building and parking lot", "Basin mowing at a commercial property"),
    "mowers": P("slope-mowers-embankment", "Two slope mowers cutting tall grass on a stormwater embankment", "Slope mowers on a stormwater embankment", 554, 414),
    "slope": P("mowed-stormwater-slope", "Long mowed stormwater channel and embankment beside a field", "Stormwater channel and slopes after mowing", 833, 616),
    "riprap": P("basin-riprap-channel", "Large mowed stormwater basin with a riprap channel across the bottom", "Large basin mowed, riprap channel clear"),
    "mulcher": P("mulcher-clearing-basin", "Compact track loader with a mulching head clearing an overgrown stormwater basin by a commercial park", "Forestry mulching inside a stormwater basin"),
    "excavator": P("excavator-mulching-slope", "Mini excavator with a mulching head clearing brush from a steep slope beside a parking lot", "Clearing a steep slope above a parking lot"),
    "woods": P("cleared-understory-mulching", "Wooded lot after forestry mulching removed the underbrush and kept the larger trees", "Selective clearing: underbrush mulched, trees kept", 520, 346),
    "hoabank": P("hoa-pond-bank-cleared", "Stormwater pond bank in a residential subdivision after brush clearing", "HOA pond bank cleared of brush"),
    "stabilized": P("basin-slopes-stabilized", "Stormwater basin slopes after clearing, with bare areas covered for stabilization", "Basin slopes cleared and stabilized"),
}

# ---------------------------------------------------------------- SERVICES
# Slugs = the CURRENT live URLs (/services/<slug>). Order = growth priority (the first five list on every area page).
SERVICES = [
    {
        "slug": "retention-pond-maintenance",
        "name": "Retention Pond Maintenance",
        "short": "Scheduled care for retention and detention ponds: vegetation, debris, inlets and outlets, with a documented record of every visit.",
        "icon": "drop",
        "title": "Retention Pond Maintenance in SC & NC",
        "meta": "Retention and detention pond maintenance for HOAs, commercial and industrial sites in SC & NC: vegetation, debris, outlets and documented visits.",
        "h1": "Retention Pond Maintenance for Commercial Properties & HOAs in SC & NC",
        "lead": "A retention pond is a permitted stormwater structure, and someone has to keep it working the way it was designed. We keep the banks, berms, inlets and outlets in shape on a set schedule, and we document every visit so you have the records when an inspector asks.",
        "included_title": "What a maintenance program includes",
        "included": [
            ("Vegetation management", "Mowing and trimming on banks, slopes and berms, with woody growth kept off embankments and away from pipes and structures."),
            ("Debris & litter removal", "Inlets, outlets, trash racks and the pond edge cleared on every visit so water keeps moving."),
            ("Condition monitoring", "A look at the outlet, inlets, forebay, slopes and berm on every visit, so a soft spot or washout gets caught while it's small."),
            ("Planting & stabilization", "Bare or eroding slopes replanted or seeded before they turn into a repair."),
            ("Wildlife & mosquito control", "Nuisance animal activity and standing-water problems managed around the pond."),
            ("Minor repairs on the spot", "Small fixes handled during routine visits instead of waiting for a separate work order."),
            ("Visit documentation", "Dated notes and photos you can hand to an HOA board, property owner or county inspector."),
        ],
        "photos_title": "Recent pond maintenance", "photos": [PH["mowedpond"], PH["fenced"], PH["tractor"], PH["mowers"]],
        "signs_title": "Your pond needs attention if…",
        "signs": [
            "Saplings or brush are growing on the berm or embankment",
            "The outlet structure or trash rack is clogged with debris",
            "Banks are bare, slumping or washing out after heavy rain",
            "Sediment is building up in the forebay or around inlets",
            "Water is standing longer than it should in a dry basin",
            "You've received an inspection letter or Notice of Violation",
        ],
        "faqs": [
            ("How often does a retention pond need maintenance?", "Most commercial and HOA ponds need regular visits through the growing season, plus a check after major storms. Your permit or maintenance agreement may set a minimum. We set the schedule after we walk the pond and read what your agreement requires."),
            ("Who is responsible for maintaining a stormwater pond?", "Usually the property owner: the HOA, business or property management company that signed (or inherited) the stormwater maintenance agreement when the site was developed. The county or city can inspect it and require repairs."),
            ("Do you document each visit?", "Yes. You get dated notes and photos after every visit. Those records are what you show a regulator to prove the pond has been maintained."),
            ("Can you take over several ponds across different properties?", "Yes. Property managers and HOAs with multiple ponds get one point of contact and the same standard at every site, across South Carolina and North Carolina."),
        ],
    },
    {
        "slug": "stormwater-inspections",
        "name": "Stormwater Inspections",
        "short": "Certified BMP / SCM inspections with a written report, photos and a prioritized list of what to fix now, monitor and plan for.",
        "icon": "doc",
        "title": "Stormwater & BMP Inspections in SC & NC",
        "meta": "Certified stormwater pond and BMP inspections in SC & NC: written report, photos, compliance summary and prioritized fixes. Free site assessment.",
        "h1": "Stormwater & BMP Inspections for South Carolina & North Carolina Properties",
        "lead": "Regulators inspect stormwater systems, and when they find violations, the owner pays. We get there first: a certified inspection of every component, a written report with photos, and a clear plan for anything that needs attention.",
        "included_title": "What we inspect",
        "included": [
            ("Retention & detention ponds", "Berm, slopes, forebay, basin, outlet structure, sediment levels, vegetation and invasive growth, erosion and a visual water-quality check."),
            ("Outlet & inlet structures", "Risers, weirs, trash racks, orifices and control devices, checked for blockages, damage and proper function."),
            ("Banks, slopes & berms", "Bare soil, rills, early slope failures, soft spots and overall berm integrity."),
            ("Ditches & conveyances", "Vegetation encroachment, debris, flow capacity and channel bank erosion or undercutting."),
            ("Catch basins & inlets", "Sediment, debris, structural condition and drainage function."),
            ("Bioretention & other BMPs", "Vegetation health, sediment, outlet function and overall performance of alternative practices."),
            ("Underground systems", "Pipe condition, blockages and structural integrity where they can be safely accessed."),
        ],
        "photos_title": "What we look at", "photos": [PH["outlet"], PH["wetpond"], PH["riprap"]],
        "signs_title": "What you receive after every inspection",
        "signs": [
            "A full written inspection report covering every component we checked",
            "Photo documentation of existing conditions, flagged issues and key structures",
            "A plain-language compliance summary against typical permit requirements",
            "Prioritized recommendations: address now, monitor, and plan for later",
            "Inspection by an inspector certified in both SC (post-construction BMP) and NC (SCM)",
        ],
        "faqs": [
            ("How often does a stormwater pond need to be inspected?", "It depends on your permit and the local program. Many permits call for one to four inspections a year, and some counties ask owners for an annual inspection report. If you're not sure what yours requires, we'll help you find out during a free site assessment."),
            ("Are you certified to inspect stormwater BMPs?", "Yes. We are a certified SC post-construction BMP inspector, hold NC State's SCM Inspection & Maintenance certification, are a Clemson-certified stormwater plan reviewer and a Clemson Extension Certified Master Pond Manager."),
            ("What if the inspection finds problems?", "You get a prioritized list and a written proposal for the repairs. We handle the work with our own crew and equipment, and you decide what gets done and when. We don't inflate findings to win a bigger job."),
            ("Can you inspect ponds in North Carolina?", "Yes. Many NC cities and counties require an annual SCM inspection report. Some require a professional engineer or landscape architect to certify it; in those cases we work alongside your engineer."),
        ],
    },
    {
        "slug": "stormwater-pond-repairs",
        "name": "Stormwater Pond Repairs",
        "short": "Sediment removal, slope and berm repair, sinkholes, outlet structures and pipe repair, done by our own crew.",
        "icon": "wrench",
        "title": "Stormwater Pond Repair in SC & NC",
        "meta": "Stormwater and retention pond repair in SC & NC: sediment removal, berm and slope repair, sinkholes, outlet structures and pipes. Own crew, no subs.",
        "h1": "Stormwater Pond & Retention Basin Repair in South Carolina & North Carolina",
        "lead": "Eroding slopes, damaged outlet structures and sediment build-up don't fix themselves, and they move up a regulator's list the longer they wait. We find the root cause, repair it properly with our own crew and equipment, and document the work.",
        "included_title": "What we repair",
        "included": [
            ("Sediment removal & cleanout", "Accumulated sediment excavated to restore the pond's design capacity and keep outlets working."),
            ("Slope & berm erosion repair", "Banks, slopes and berms rebuilt and stabilized with proper fill, grading and vegetative cover."),
            ("Sinkhole detection & repair", "Subsidence near structures traced to its source, usually internal erosion or a failing pipe, and repaired."),
            ("Outlet structure repair & replacement", "Damaged risers, clogged trash racks, failed weirs and worn control devices, handled in-house."),
            ("Stormwater pipe repair & installation", "Cracked, collapsed or blocked conveyance pipes inspected, repaired or replaced."),
            ("Brush cutting & heavy clearing", "Overgrown and woody vegetation removed from banks and access areas so routine maintenance can resume."),
            ("Hydroseeding", "Fast vegetative cover on repaired berms, disturbed slopes and newly graded areas."),
        ],
        "photos_title": "Repair and clearing work", "photos": [PH["hoabank"], PH["stabilized"], PH["outlet"]],
        "signs_title": "How a repair works",
        "signs": [
            "Site assessment: we walk the property and find the cause, not just the symptom",
            "Written proposal: scope, approach and price, with no add-ons after work starts",
            "Repair: our own crew and equipment; we don't hand BMP work to general contractors",
            "Documentation: photos, a scope summary and recommendations to keep it from coming back",
        ],
        "faqs": [
            ("How do I know if my pond needs a repair or just maintenance?", "Maintenance keeps a working pond working. Repairs are for things that have already failed or are failing: a slumping berm, a sinkhole, a damaged riser, or so much sediment the pond can't hold its design volume. An inspection tells you which you're dealing with."),
            ("Do you subcontract repair work?", "No. Repairs are done by our own crew with our own equipment. If your permit requires an engineer's design or sign-off, we work alongside your engineer."),
            ("How often does a pond need sediment removed?", "It varies with the drainage area and how well upstream erosion is controlled. South Carolina's guide for HOAs suggests planning on dredging roughly every ten years. Checking forebay sediment during inspections tells you when it's coming."),
        ],
    },
    {
        "slug": "forestry-mulching",
        "name": "Forestry Mulching",
        "short": "One pass, clean finish: brush, briars and small trees ground in place. No burning, no hauling.",
        "icon": "leaf",
        "title": "Forestry Mulching in South Carolina & NC",
        "meta": "Forestry mulching for commercial lots, pond banks, buffers and rights-of-way in SC & NC. One pass, no burning, no hauling, mulch left to protect the soil.",
        "h1": "Forestry Mulching for Commercial Land, Pond Banks & Rights-of-Way in SC & NC",
        "lead": "Forestry mulching turns overgrown land into usable property in a single pass. One machine grinds brush, briars, saplings and stumps where they stand and leaves a layer of mulch that protects the soil. No burn piles, no haul-off, no debris to deal with.",
        "included_title": "What we can handle",
        "included": [
            ("Dense brush & briars", "Thickets and undergrowth cleared down to ground level."),
            ("Small to mid-size trees", "Trees up to about 6–8 inches in diameter, depending on species, ground in place."),
            ("Overgrown pond banks & slopes", "Woody growth removed from stormwater pond banks ahead of maintenance or an inspection."),
            ("Invasive species", "Privet, kudzu, Chinese tallow and other invasives cut back to reclaim the ground."),
            ("Rights-of-way & easements", "Utility corridors, access roads and drainage easements opened back up."),
            ("Lots, buffers & acreage", "Overgrown commercial lots, wooded buffers and large tracts cleared for access, sale or development."),
        ],
        "photos_title": "Forestry mulching jobs", "photos": [PH["mulcher"], PH["excavator"], PH["woods"]],
        "signs_title": "Forestry mulching vs. traditional clearing",
        "signs": [
            "Speed: one machine, one pass, instead of several pieces of equipment",
            "Waste: the mulch stays on site, so there are no haul-off, burning or disposal fees",
            "Erosion: a 2–4 inch mulch layer covers the soil instead of leaving bare ground",
            "Disturbance: minimal compared with dozer clearing",
            "Ready to use: the land can be mowed, accessed or prepped for the next step right away",
        ],
        "faqs": [
            ("What size trees can a forestry mulcher handle?", "Brush, briars and small to mid-size trees, typically up to about 6–8 inches in diameter depending on the species. Larger trees can be removed separately or left in place."),
            ("What happens to the mulch?", "It stays on site as a 2–4 inch layer that settles quickly, holds the soil in place, and breaks down over time. Nothing is burned or hauled away."),
            ("Can you clear around trees we want to keep?", "Yes. Forestry mulching is selective. We can clear the underbrush and leave the larger trees, or clear everything inside a marked area."),
            ("Is forestry mulching good for pond banks?", "Yes, it's one of the best uses. Woody growth on a stormwater embankment is a common inspection finding, and mulching removes it without tearing up the slope."),
        ],
    },
    {
        "slug": "land-clearing",
        "name": "Land Clearing",
        "short": "Tree and brush removal, site prep, right-of-way clearing and overgrown acreage, from small lots to large tracts.",
        "icon": "truck",
        "title": "Commercial Land Clearing in SC & NC",
        "meta": "Commercial land clearing in SC & NC: tree and brush removal, site prep, right-of-way and easement clearing, and overgrown lot reclamation.",
        "h1": "Commercial Land Clearing in South Carolina & North Carolina",
        "lead": "From an overgrown lot to a large commercial tract, we clear what needs to go, keep what you want to keep, and leave the site ready for its next use with as little ground disturbance as possible.",
        "included_title": "Land clearing services",
        "included": [
            ("Tree & brush removal", "Single trees to densely wooded acreage: trees, stumps, brush and undergrowth."),
            ("Forestry mulching", "The most efficient method for most commercial properties: vegetation ground in place, nothing hauled or burned."),
            ("Site preparation clearing", "Clearing and debris removal for sites headed to grading or construction."),
            ("Right-of-way & easement clearing", "Utility corridors, access roads and drainage easements, on a recurring or as-needed basis."),
            ("Overgrown lot & acreage reclamation", "Years of overgrowth removed from commercial lots, industrial buffers and large acreage."),
        ],
        "photos_title": "Clearing work", "photos": [PH["excavator"], PH["woods"], PH["mulcher"]],
        "signs_title": "Who we clear land for",
        "signs": [
            "Commercial and industrial property owners and managers",
            "Developers preparing sites for construction",
            "HOAs with overgrown common areas and pond banks",
            "Municipalities and institutional facilities",
            "Owners getting land ready to sell",
        ],
        "faqs": [
            ("Do you haul away the debris?", "With forestry mulching there's nothing to haul: vegetation is ground in place. For other clearing, we'll explain how debris is handled in your proposal."),
            ("Can you clear land that's steep or near a pond?", "Yes. Steep slopes and pond banks are where we work every day, and we clear them without causing the erosion that brings an inspector back."),
            ("Do I need a permit to clear my land?", "Sometimes. Larger disturbances can trigger land disturbance or stormwater permit requirements. We'll flag it during the site assessment so you can check with your county or engineer before work starts."),
        ],
    },
    {
        "slug": "erosion-repair",
        "name": "Erosion Repair",
        "short": "Slope stabilization, berm restoration, bank remediation, hydroseeding and outlet scour repair.",
        "icon": "layers",
        "title": "Erosion Repair & Slope Stabilization in SC",
        "meta": "Erosion repair for pond banks, slopes, berms, ditches and outlets in SC & NC: regrading, stabilization and hydroseeding. Free erosion assessment.",
        "h1": "Erosion Repair & Slope Stabilization for Ponds, Berms and Ditches in SC & NC",
        "lead": "Erosion starts small: a rill, a bare patch, a soft spot near an outlet. Left alone it becomes a failed berm, a collapsed bank or a pond full of sediment after one big storm. We catch it early, or fix it properly once it's already a problem.",
        "included_title": "Erosion repair services",
        "included": [
            ("Slope stabilization", "Eroding graded slopes on pond banks, berms and cut areas restored with grading, proper fill and vegetative cover."),
            ("Berm repair & restoration", "We find why a berm is eroding or failing, then repair it to proper function and stability."),
            ("Bank erosion remediation", "Pond banks, ditch banks and channel edges repaired with vegetative or structural protection so it doesn't come back."),
            ("Rill, gully & sheet erosion", "Early-stage erosion regraded and seeded before it grows."),
            ("Hydroseeding", "Fast cover for disturbed slopes, repaired berms and newly graded areas, as part of a repair or on its own."),
            ("Outlet erosion repair", "Scour and erosion at outlet structures and pipe discharges, where moving water does the most damage."),
        ],
        "photos_title": "Erosion and stabilization work", "photos": [PH["stabilized"], PH["hoabank"], PH["slope"]],
        "signs_title": "Early signs of erosion",
        "signs": [
            "Small channels (rills) cut into a graded slope",
            "Bare patches on pond banks that never fill in",
            "Soft or sunken ground near an outlet structure or pipe",
            "Undercut banks along a ditch or channel",
            "Muddy water or new sediment in the pond after every rain",
        ],
        "faqs": [
            ("Why does erosion matter on a stormwater pond?", "Sediment from eroding slopes fills the pond and cuts its capacity, and erosion around a berm or outlet can lead to structural failure. Both are common inspection findings."),
            ("What's the fastest way to stop erosion on a slope?", "It depends on the cause and the slope. Often it's regrading plus hydroseeding or another vegetative cover; steeper or high-flow areas may need structural protection. We'll recommend the fix that will last."),
            ("Can you repair erosion around an outlet pipe?", "Yes. Outlet scour is one of the most common and most damaging erosion problems on a pond, and we repair it as part of our stormwater repair work."),
        ],
    },
    {
        "slug": "drainage-ditch-maintenance",
        "name": "Drainage Ditch Maintenance",
        "short": "Ditches and channels cleared, regraded and stabilized so water keeps moving and stays off your property.",
        "icon": "tool",
        "title": "Drainage Ditch Maintenance in SC & NC",
        "meta": "Drainage ditch clearing and maintenance for commercial and industrial properties in SC & NC: vegetation, sediment, regrading, culverts and bank repair.",
        "h1": "Drainage Ditch Maintenance for Commercial & Industrial Properties in SC & NC",
        "lead": "A clogged or overgrown ditch is a flooding risk, a compliance problem and a repair that gets bigger every season. We clear, restore and maintain your ditches and channels so water moves the way the site was designed.",
        "included_title": "Ditch maintenance services",
        "included": [
            ("Vegetation clearing & management", "Mowing, cutting and growth control in channels and along banks, so vegetation holds the bank without blocking flow."),
            ("Debris & sediment removal", "Leaves, sediment and other build-up removed to restore channel capacity."),
            ("Bank stabilization & erosion repair", "Eroded banks regraded and revegetated so sediment stops washing into ponds and downstream structures."),
            ("Ditch regrading", "Silted-in channels restored to their designed cross-section and grade."),
            ("Outlet & culvert clearing", "Culverts and outlets cleared, inspected and restored so water doesn't back up upstream."),
        ],
        "photos_title": "Channel and ditch work", "photos": [PH["slope"], PH["riprap"]],
        "signs_title": "Signs your ditch needs work",
        "signs": [
            "Standing water days after a rain",
            "Water backing up at a culvert or pipe",
            "Brush, trees or cattails filling the channel",
            "Banks caving in or undercut",
            "Parking lots or buildings taking on water in heavy storms",
        ],
        "faqs": [
            ("How often should a drainage ditch be cleaned?", "Most commercial ditches need vegetation control during the growing season and a check after major storms, with sediment removal as needed. We'll recommend a schedule after we see the site."),
            ("Is ditch maintenance part of stormwater compliance?", "Often, yes. Ditches and swales that convey runoff to a pond are usually part of the permitted stormwater system, and they're one of the most overlooked parts of it."),
        ],
    },
]

# ---------------------------------------------------------------- AREAS
# /lexington-sc, /columbia-sc and /rock-hill-sc are the CURRENT live URLs; the rest are new, same <place>-sc pattern.
# Copy is local and conservative; the county facts are sourced on the pond guide page. Have Nicky check them (NOTES.md).
AREAS = [
    {
        "slug": "gilbert-sc", "city": "Gilbert", "county": "Lexington County", "zips": "29054",
        "intro": "Gilbert is home. Our office and equipment are on Peach Festival Road in western Lexington County, so Gilbert, Lexington and the rest of the county get the fastest response we have.",
        "local": [
            ("Home-base response", "When a storm takes out a slope or clogs an outlet, the properties closest to our yard are the first ones we can reach."),
            ("Rural acreage & pond banks", "Farm ponds, wooded buffers and overgrown acreage around Gilbert are a natural fit for forestry mulching: no burn piles, no hauling."),
            ("Lake Murray side of the county", "Commercial sites and neighborhoods between Gilbert, Lexington and the lake are growing, and nearly every new one drains to a stormwater pond."),
        ],
        "faqs": [("Where is Carolina Outdoor Services located?", "Our office is at 1318 Peach Festival Road, Gilbert, SC 29054, in Lexington County. We serve the Midlands every day and travel statewide and into North Carolina for commercial work.")],
    },
    {
        "slug": "lexington-sc", "city": "Lexington", "county": "Lexington County", "zips": "29072, 29073",
        "intro": "Lexington has grown fast along US-378, I-20 and the US-1 corridor, and nearly every new subdivision, shopping center and business park comes with a retention pond or other stormwater BMP that someone has to maintain. We're based minutes away in Gilbert.",
        "local": [
            ("Lexington County pond rules", "Lexington County asks private pond owners to complete an annual inspection checklist, and its maintenance requirements call for no woody vegetation on fill embankments or within 30 feet of pipes and structures. We keep you ahead of both."),
            ("HOAs and commercial centers", "Pond banks, outlets and ditches handled on one documented schedule, so the board or property manager has records ready."),
            ("Nearby towns we cover", "Gilbert, Batesburg-Leesville, Swansea, Gaston, Pelion, Chapin, Irmo, West Columbia and Cayce, plus the rest of the county."),
        ],
        "faqs": [("Are you a local Lexington County company?", f"Yes. We're based in Gilbert, SC, in Lexington County, and have served the area since 2004. Call or text {PHONE}.")],
    },
    {
        "slug": "columbia-sc", "city": "Columbia", "county": "Richland & Lexington Counties", "zips": "29201–29229",
        "intro": "From Harbison to Fort Jackson and Forest Acres to the Vista, Columbia's office parks, apartment communities, retail centers and industrial sites along I-20, I-26 and I-77 almost all drain to a stormwater pond or BMP. We're just west of the metro in Gilbert, with no travel surcharge for Greater Columbia.",
        "local": [
            ("Richland County's Private Pond Inspection Program", "Richland County inspects privately owned detention and retention ponds. Owners who get a Notice of Violation have 30 days to make corrections before penalties can apply. We help you pass the first time."),
            ("Commercial & multifamily sites", "Documented pond maintenance, inspections and repairs for property managers running several Columbia-area sites."),
            ("Areas we cover", "Columbia, Forest Acres, Cayce, West Columbia, Irmo, Chapin, Blythewood, Lugoff, Elgin and Hopkins. Not listed? Ask."),
        ],
        "faqs": [
            ("Do you charge extra to travel to Columbia?", "No. Greater Columbia is part of our home service area, and there's no travel surcharge."),
            ("What happens if my pond fails a Richland County inspection?", "Richland County gives owners 30 days after a Notice of Violation to make corrections before daily penalties may be assessed. Call us as soon as you get the notice; we'll inspect, prioritize the fixes and document the work."),
        ],
    },
    {
        "slug": "blythewood-sc", "city": "Blythewood", "county": "Richland & Fairfield Counties", "zips": "29016",
        "intro": "Blythewood sits on I-77 north of Columbia, and it's changing quickly: new neighborhoods, schools and some of the largest industrial projects in the Midlands. Large sites mean large stormwater systems, and those systems need inspection and maintenance from day one.",
        "local": [
            ("New development, new BMPs", "Newer sites often have ponds and BMPs still settling in, when erosion and vegetation problems show up fastest. Early inspections catch them while they're cheap to fix."),
            ("Industrial & commercial grounds", "Forestry mulching and land clearing for buffers, easements and overgrown acreage along the I-77 corridor."),
            ("HOA communities", "Pond bank mowing, woody growth removal and outlet clearing on a documented schedule."),
        ],
        "faqs": [("Do you serve Blythewood and northern Richland County?", "Yes. Blythewood and the I-77 corridor north of Columbia are part of our Midlands service area.")],
    },
    {
        "slug": "aiken-sc", "city": "Aiken", "county": "Aiken County", "zips": "29801, 29803, 29805",
        "intro": "Aiken County runs its own stormwater program through Public Works & Engineering, and the county seat's mix of commercial corridors, subdivisions and wooded acreage gives us a steady list of ponds, ditches and clearing work.",
        "local": [
            ("Commercial & HOA ponds", "Inspections, maintenance and repairs for retention and detention ponds across Aiken, Graniteville and the surrounding county."),
            ("Wooded lots & buffers", "Forestry mulching clears overgrown land and pond banks without burning or hauling, a good fit for Aiken's sandy, erosion-prone soils."),
            ("Drainage & ditches", "Ditch clearing, regrading and bank stabilization to keep water off parking lots and buildings."),
        ],
        "faqs": [("Do you serve all of Aiken County?", "Yes, including Aiken, North Augusta, Graniteville and the communities in between, for stormwater, pond and land clearing work.")],
    },
    {
        "slug": "north-augusta-sc", "city": "North Augusta", "county": "Aiken & Edgefield Counties", "zips": "29841, 29842, 29860",
        "intro": "North Augusta sits on the Savannah River across from Augusta, Georgia, with riverfront redevelopment, busy commercial corridors along I-20 and plenty of newer neighborhoods. All of it sends stormwater somewhere, usually a pond someone has to maintain.",
        "local": [
            ("River-adjacent sites", "Sites close to the Savannah River and its tributaries need erosion under control, because sediment leaving the site is exactly what regulators look for."),
            ("Neighborhood ponds", "Pond bank maintenance, outlet clearing and erosion repair for HOAs, with records the board can keep."),
            ("Clearing & mulching", "Overgrown lots and buffers cleared in a single pass with forestry mulching."),
        ],
        "faqs": [("Do you work in North Augusta?", "Yes. North Augusta is part of our Aiken County service area for pond maintenance, inspections, repairs and forestry mulching.")],
    },
    {
        "slug": "greenville-sc", "city": "Greenville", "county": "Greenville County", "zips": "29601–29617",
        "intro": "Greenville County's Land Development Division inspects detention ponds and reviews their maintenance, and in most cases the HOA or commercial owner is solely responsible for keeping them working. With the Upstate's growth along I-85 and I-385, that's a lot of ponds.",
        "local": [
            ("Greenville County maintenance agreements", "Subdivisions permitted after 2008 should have a stormwater maintenance plan, and the county's detention basin record calls for routine checks monthly and after large rain events. We do the work and keep the record."),
            ("City, county & Greer", "The City of Greenville and the City of Greer run their own stormwater programs separate from the county. We'll work to whichever one covers your site."),
            ("Upstate towns we cover", "Greenville, Greer, Simpsonville, Mauldin, Fountain Inn, Taylors, Travelers Rest and Easley."),
        ],
        "faqs": [("Who maintains a detention pond in Greenville County?", "In most cases the HOA or commercial property owner is solely responsible, and Greenville County's Land Development Division inspects and reviews the maintenance. We can take the routine work and documentation off your plate.")],
    },
    {
        "slug": "spartanburg-sc", "city": "Spartanburg", "county": "Spartanburg County", "zips": "29301–29307",
        "intro": "Spartanburg County sits where I-85 and I-26 meet, and its manufacturing plants, distribution centers and business parks come with big stormwater systems: wet ponds, dry basins, long ditches and plenty of slope to keep stable.",
        "local": [
            ("Industrial & distribution sites", "Large basins and conveyance ditches inspected, mowed, cleared and repaired on a schedule that fits a 24/7 operation."),
            ("Storm response", "After a major storm, debris in a pond or a blocked outlet needs attention fast. We clear it, repair the damage and document it."),
            ("Buffers & easements", "Forestry mulching keeps wooded buffers, fence lines and easements open without hauling debris off site."),
        ],
        "faqs": [("Do you serve Spartanburg County industrial sites?", "Yes. We inspect, maintain and repair stormwater systems for industrial, distribution and commercial properties across Spartanburg County and the I-85 corridor.")],
    },
    {
        "slug": "anderson-sc", "city": "Anderson", "county": "Anderson County", "zips": "29621, 29624, 29625, 29626",
        "intro": "Anderson County runs along I-85 between Greenville and the Georgia line, with industrial parks, retail along the US-76 and SC-28 corridors, and neighborhoods spreading toward Lake Hartwell. Each new site adds stormwater infrastructure that has to keep working.",
        "local": [
            ("Industrial & retail ponds", "Detention and retention ponds kept mowed, clear and documented for owners and property managers."),
            ("Erosion on Upstate slopes", "Red clay slopes erode quickly once they're bare. We stabilize banks and berms before they fail."),
            ("Clemson & surrounding areas", "We also serve Clemson, Pendleton, Easley and Powdersville."),
        ],
        "faqs": [("Is Anderson County in your service area?", "Yes. Anderson and the surrounding Upstate communities are part of our regular service area for stormwater, pond and clearing work.")],
    },
    {
        "slug": "rock-hill-sc", "city": "Rock Hill", "county": "York County", "zips": "29730, 29732, 29733",
        "intro": "Rock Hill is one of the fastest-growing cities in the Southeast, about 30 minutes south of Charlotte. Business parks like Waterford, Legacy Park, Antrim, TechPark and Southway Industrial, plus the Dave Lyle Boulevard and I-77 corridors, all rely on stormwater systems that need regular care.",
        "local": [
            ("Business park ponds", "Inspections and maintenance for retention ponds at Rock Hill's business and industrial parks, with reports for your files."),
            ("Charlotte-fringe development", "Forestry mulching and land clearing for sites being prepared along the I-77 corridor."),
            ("Rock Hill area towns", "Fort Mill, Tega Cay, Clover, Lake Wylie, York, Catawba and Indian Land, plus Gastonia and Belmont, NC."),
        ],
        "faqs": [("Do you travel to Rock Hill regularly?", "Yes. We work in Rock Hill and York County regularly and serve the Charlotte side of the line in North Carolina too.")],
    },
    {
        "slug": "york-county-sc", "city": "York County", "county": "South Carolina", "zips": "29708, 29715, 29710, 29745 and Rock Hill",
        "intro": "York County is the South Carolina side of the Charlotte metro: Fort Mill, Tega Cay, Clover, Lake Wylie and York, along with Rock Hill. Neighborhood growth here means hundreds of HOA stormwater ponds, and Fort Mill even publishes a stormwater pond maintenance handbook for neighborhood HOAs.",
        "local": [
            ("HOA stormwater ponds", "Routine pond care, inspections and a maintenance log your board can keep up to date."),
            ("Lake Wylie & Catawba River sites", "Erosion control and stabilization matter even more near the lake and river."),
            ("Land clearing for growth", "Forestry mulching for lots, buffers and easements as the county keeps building out."),
        ],
        "faqs": [("Do you work with HOAs in Fort Mill and Tega Cay?", "Yes. We maintain and inspect neighborhood stormwater ponds across York County, including Fort Mill, Tega Cay, Clover and Lake Wylie.")],
        "place_type": "AdministrativeArea", "place_name": "York County, SC",
        "title": "Stormwater Pond Services in York County, SC",
        "meta": "Retention pond maintenance, stormwater inspections and forestry mulching for HOAs and businesses in Fort Mill, Tega Cay, Clover, Lake Wylie & York, SC.",
        "h1": "Stormwater &amp; Retention Pond Services in York County, SC",
    },
    {
        "slug": "midlands-sc", "city": "Midlands of SC", "county": "Lexington, Richland, Kershaw, Fairfield & Newberry Counties", "zips": "",
        "intro": "The Midlands is our home territory. From our base in Gilbert we cover Lexington and Richland counties every day, and reach Kershaw, Fairfield, Newberry and Calhoun counties for commercial pond, inspection and clearing work.",
        "local": [
            ("Two county pond programs", "Lexington County asks private pond owners for an annual inspection checklist; Richland County runs a Private Pond Inspection Program with 30-day correction deadlines. We know both."),
            ("Fastest response", "Midlands properties are closest to our crew and equipment, so storm damage and urgent repairs get handled quickly."),
            ("Towns we cover", "Columbia, Lexington, Gilbert, Irmo, Chapin, Cayce, West Columbia, Blythewood, Forest Acres, Lugoff, Elgin, Batesburg-Leesville and more."),
        ],
        "faqs": [("What counties do you cover in the Midlands?", "Lexington and Richland counties every day, plus Kershaw, Fairfield, Newberry and Calhoun counties for commercial stormwater and clearing work.")],
        "place_type": "AdministrativeArea", "place_name": "Midlands of South Carolina", 
        "title": "Stormwater & Pond Maintenance, Midlands of SC",
        "meta": "Stormwater inspections, retention pond maintenance, erosion repair and forestry mulching across the Midlands of South Carolina, from a Gilbert, SC crew.",
        "h1": "Stormwater &amp; Retention Pond Services in the Midlands of South Carolina",
    },
    {
        "slug": "upstate-sc", "city": "Upstate SC", "county": "Greenville, Spartanburg, Anderson, Pickens & Oconee Counties", "zips": "",
        "intro": "The Upstate's growth along I-85, I-26 and I-385 has added thousands of stormwater ponds behind neighborhoods, plants and distribution centers. We bring certified inspections, maintenance, repairs and forestry mulching to properties across the region.",
        "local": [
            ("Different rules by jurisdiction", "Greenville County, the City of Greenville and Greer each run their own stormwater program, and Spartanburg and Anderson counties have theirs. We work to the one that covers your site."),
            ("Red clay & steep slopes", "Upstate slopes erode fast once they're bare, so stabilization and early repair matter more here."),
            ("Towns we cover", "Greenville, Spartanburg, Anderson, Greer, Simpsonville, Mauldin, Fountain Inn, Taylors, Easley, Clemson and more."),
        ],
        "faqs": [("Do you have crews in the Upstate?", "We travel to the Upstate from our Gilbert base for commercial and HOA stormwater work, and schedule visits so Upstate clients get the same standard as the Midlands.")],
        "place_type": "AdministrativeArea", "place_name": "Upstate South Carolina", 
        "title": "Stormwater & Pond Maintenance, Upstate SC",
        "meta": "Stormwater pond inspections, maintenance, repairs and forestry mulching for HOAs and commercial sites in Greenville, Spartanburg, Anderson & the Upstate.",
        "h1": "Stormwater &amp; Retention Pond Services in Upstate South Carolina",
    },
    {
        "slug": "north-carolina", "city": "North Carolina", "region": "NC", "county": "Charlotte metro, Gaston, Union & surrounding counties", "zips": "",
        "intro": "We hold NC State's SCM Inspection & Maintenance certification and work across the state line, mostly in the Charlotte metro: Charlotte, Pineville, Matthews, Gastonia, Belmont and the surrounding counties.",
        "local": [
            ("Annual SCM inspections", "Many North Carolina cities and counties require an annual inspection report on stormwater control measures (SCMs) by a qualified inspector. Some, like Durham, require a professional engineer or landscape architect to certify it; we work alongside yours."),
            ("Maintenance & repairs", "Wet ponds, dry basins, bioretention and other SCMs kept to their maintenance plan, with repairs handled by our own crew."),
            ("Forestry mulching", "Clearing for lots, buffers, pond banks and easements across the Charlotte region."),
        ],
        "faqs": [
            ("Are you certified to inspect SCMs in North Carolina?", "Yes. We hold NC State's Stormwater SCM Inspection & Maintenance certification, along with SC post-construction BMP inspector certification."),
            ("Which parts of North Carolina do you serve?", "Mostly the Charlotte metro and southern Piedmont: Mecklenburg, Gaston, Union and nearby counties. Call about other areas."),
        ],
        "place_type": "State", "place_name": "North Carolina", "crumb": "North Carolina",
        "title": "Stormwater SCM Inspection & Maintenance, NC",
        "meta": "NC State-certified SCM inspections, stormwater pond maintenance, repairs and forestry mulching in Charlotte, Gastonia, Pineville & the NC Piedmont.",
        "h1": "Stormwater SCM Inspections &amp; Pond Maintenance in North Carolina",
    },
]

# Google reviews from the Carolina Outdoor Services LLC Business Profile (5.0, 7 reviews), copied Nov 25, 2026.
# The 5 reviews with written text are used word for word; 2 are star-only. The old site's testimonials were removed.
REVIEWS = [
    ("Frank M.", "Google review · forestry mulching", "Great overall experience with Nicky and his son Austin. From initial communication to on-site estimate, to final mulching, working with Nicky was a 1st class experience. I highly recommend giving him a call for your forest mulching needs."),
    ("Jim R.", "Google review · land clearing", "Thorough discussion before job scope was agreed to. We agreed to use two tree grinders in tandem for eight hour job covering 3 plus acres of mostly thickly dispersed trees of six inch diameter and smaller with plenty of underbrush and vines. Very pleased with results. Allowed me about thirty minutes after they finished the scope of work asking if I had any extra items to tackle. I will use Nick's services next year. Well done."),
    ("Steve T.", "Google review · lot clearing", "Reached out to the crew at Carolina Outdoor Services to clean/mulch a two acre lot and what a job they did!! From overgrown to clear! Thanks guys for the professional work, punctuality, and price! It's greatly appreciated!"),
    ("Rylan W.", "Google review", "The entire crew at Carolina Outdoor services were professional and courteous. They worked with me through some delays and explained everything along the way. I will using them for future projects and recommend that others do the same"),
    ("Angela M.", "Google review", "Great experience 👍 Free estimate, prompt responses, quick scheduling. Luke who came out and spent the day working on my property did a great job and was very polite :) Very happy with the whole interaction."),
]

GENERAL_FAQS = [
    ("What areas do you serve?", "We're based in Gilbert, SC and serve all of South Carolina: the Midlands (Lexington, Columbia, Blythewood), Aiken County and North Augusta, the Upstate (Greenville, Spartanburg, Anderson) and York County and Rock Hill, plus North Carolina, mostly the Charlotte metro."),
    ("What is a Master Pond Manager?", "Master Pond Manager is Clemson Extension's pond management certification. It covers stormwater pond design, inspection and maintenance, water quality, aquatic plant management and best management practices for stormwater ponds, with online coursework, field days and an exam."),
    ("How often should a retention pond be inspected?", "It depends on your permit and local program, but many permits call for one to four inspections a year, and some counties ask owners for an annual report. Routine maintenance visits in between catch problems early."),
    ("Who do you work with?", "Commercial and industrial property owners and managers, HOA boards and community managers, developers with permitted stormwater features, and municipal and institutional facilities."),
    ("Are you licensed and insured?", "Yes. Carolina Outdoor Services, LLC is licensed and insured, and we provide a certificate of insurance on request. Our inspector certifications are listed on our About page."),
    ("How do I get started?", f"Request a free site assessment online or call or text {PHONE}. We'll walk the property, tell you plainly what we see, and give you a written proposal. No obligation and no pressure."),
]

# ---------------------------------------------------------------- RESOURCE (link-worthy guide)
POND_CARDS = [
    ("Every visit", "Routine care", ["Mow banks, side slopes and access areas", "Trim around pipes, headwalls and the outlet", "Remove litter and floating debris", "Note anything new: washouts, slumping, soft spots, burrows"]),
    ("Growing season", "Keep vegetation in check", ["Mow often enough that woody growth never takes hold", "Keep shoreline overgrowth and invasives under control", "Clear the perimeter fence line of vines and brush", "Keep the access path open for inspectors and equipment"]),
    ("After heavy rain", "Storm check", ["Clear limbs and trash from inlets, outlet and trash rack", "Look for new erosion on banks and around headwalls", "Check that swales and ditches into the pond are flowing", "Photograph damage before it's repaired"]),
    ("Fall & winter", "Woody growth season", ["Cut saplings and brush off fill embankments", "Clear woody growth away from pipes and structures", "Clean leaf and limb build-up around the outlet", "Plan repairs before spring storms"]),
    ("Once a year", "Inspection & records", ["Have the full system inspected and get a written report", "Lexington County: complete the annual pond inspection checklist", "Keep dated maintenance records and photos", "Budget for sediment removal when the forebay fills"]),
    ("What inspectors flag", "Common failure points", ["Trees or brush on the berm or embankment", "Clogged orifices, risers or trash racks", "Eroded slopes, headwalls or washouts", "Sediment build-up and blocked swales"]),
]

POND_BODY = f"""
<h2>Who is responsible for a stormwater pond in South Carolina?</h2>
<p>Usually the property owner. The ponds behind subdivisions, shopping centers, office parks and industrial sites are generally private. When the site was permitted, the owner signed a maintenance agreement, and that responsibility passes to whoever owns the property next: often an HOA, a business owner or a property management company. South Carolina's guide for homeowner associations says plainly that all stormwater ponds require maintenance, and suggests planning on dredging roughly every ten years.</p>
<h2>What the counties ask</h2>
<p><strong>Lexington County</strong> asks private pond owners to complete an annual inspection checklist. Its maintenance requirements call for no woody vegetation on fill embankments or within 30 feet of structures and pipes, sediment and debris kept clear of outlets, trash racks clear, and eroded slopes and headwalls repaired.</p>
<p><strong>Richland County</strong> runs a Private Pond Inspection Program for privately owned detention and retention ponds. Owners who receive a Notice of Violation have 30 days to make corrections before daily penalties may apply.</p>
<p><strong>Greenville County</strong>'s Land Development Division inspects and reviews detention pond maintenance. In most cases the HOA or commercial owner is solely responsible, subdivisions permitted after 2008 should have a maintenance plan, and the county's detention basin record calls for routine checks monthly and after large rain events. The City of Greenville and the City of Greer run their own programs.</p>
<p><strong>York County</strong>: the Town of Fort Mill publishes a neighborhood HOA stormwater pond maintenance handbook with a maintenance log, a good model for any HOA. <strong>Aiken County</strong> runs its stormwater program through Public Works &amp; Engineering.</p>
<h2>And in North Carolina</h2>
<p>Many North Carolina cities and counties require an annual inspection report for stormwater control measures (SCMs) by a qualified inspector. Some, such as Durham County, require a registered professional engineer or landscape architect to certify the report.</p>
<h2>How we can help</h2>
<p>Carolina Outdoor Services handles everything on this checklist: <a href="/services/stormwater-inspections/">certified inspections</a> with written reports, <a href="/services/retention-pond-maintenance/">routine pond maintenance</a>, <a href="/services/stormwater-pond-repairs/">repairs and sediment removal</a>, <a href="/services/erosion-repair/">erosion repair</a> and <a href="/services/forestry-mulching/">forestry mulching</a> for overgrown banks. We're a Clemson Extension Certified Master Pond Manager, a certified SC post-construction BMP inspector and NC State SCM-certified. <a href="/contact/">Request a free site assessment</a>.</p>
<p style="font-size:.9rem;color:var(--c-muted)">Sources:
<a href="https://lex-co.sc.gov/sites/lexco/files/Documents/Lexington%20County/Departments/Community%20Dev/Land%20Development/LexCo%20Pond%20maintenance%20requirements%202025v1.pdf" rel="noopener">Lexington County pond maintenance requirements</a> ·
<a href="https://richlandcountysc.gov/Portals/0/Departments/PublicWorks/StormDocs/Private%20Pond%20Inspection%202024.pdf" rel="noopener">Richland County Private Pond Inspection Program</a> ·
<a href="https://greenvillecountysc.gov/LandDevelopment/DetentionPonds.aspx" rel="noopener">Greenville County detention ponds</a> ·
<a href="https://www.greenvillecounty.org/LandDevelopment/pdf/GCHOAStormWaterGuideFinal.pdf" rel="noopener">Greenville County HOA stormwater guide</a> ·
<a href="https://www.fortmillsc.gov/DocumentCenter/View/1930/Neighborhood-HOA-Stormwater-Pond-Maintenance-Handbook" rel="noopener">Fort Mill HOA pond handbook</a> ·
<a href="https://www.des.sc.gov/sites/des/files/docs/HomeAndEnvironment/Docs/ponds.pdf" rel="noopener">SC DES stormwater pond guide</a> ·
<a href="https://raleighnc.gov/stormwater/services/submit-stormwater-device-inspection-report" rel="noopener">Raleigh annual device inspections</a> ·
<a href="{CLEMSON_MPM}" rel="noopener">Clemson Extension Master Pond Manager</a>.
This page is a general guide, not legal or engineering advice. Your pond's approved plans, permit and maintenance agreement govern.</p>
"""

ABOUT_STORY = f"""<p>Carolina Outdoor Services started in 2004 as a full-service commercial landscaping company. Over our first decade we kept getting called to the same problems: neglected retention ponds, eroding slopes and outlet structures that hadn't been looked at in years.</p>
<p>About twelve years ago we narrowed the business to the work that kept finding us: stormwater maintenance, inspection and repair. Today that's all we do, along with the forestry mulching and land clearing that keep pond banks and commercial land usable. We're not a landscaping company that dabbles in stormwater.</p>
<p>We report what we actually find. If a pond needs a $400 fix, we say so. We don't inflate findings to win a bigger job, and you'll know what it costs and when we're coming before we show up.</p>
<p>Our credentials include <a href="{CLEMSON_MPM}" rel="noopener">Clemson Extension Certified Master Pond Manager</a>, certified SC post-construction BMP inspector, NC State SCM Inspection &amp; Maintenance certification and Clemson-certified stormwater plan reviewer. Carolina Outdoor Services is also a member of <a href="{SUSTAIN_SC}" rel="noopener">Sustain SC</a>, the Columbia-based nonprofit that connects South Carolina businesses' sustainability goals with local solutions where commerce and conservation meet.</p>"""

CONFIG = {
  "business": {
    "name": "Carolina Outdoor Services", "legal_name": "Carolina Outdoor Services, LLC",
    "domain": "https://cosstormwater.com",
    "phone": PHONE, "tel": "+18035182787",
    "schema_type": ["LocalBusiness", "HomeAndConstructionBusiness"],
    "description": "Gilbert, SC stormwater company providing certified stormwater inspections, retention pond maintenance and repair, erosion repair, forestry mulching and land clearing for commercial, industrial and HOA properties across South Carolina and North Carolina since 2004.",
    "address": {"street": "1318 Peach Festival Road", "locality": "Gilbert", "region": "SC", "zip": "29054"},
    "geo": (33.9246, -81.3937),
    "hours": [(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "07:00", "17:00")],
    "hours_text": "Mon–Fri 7 AM – 5 PM",
    "counties": ["South Carolina", "North Carolina", "Lexington County, SC", "Richland County, SC", "Aiken County, SC", "Greenville County, SC", "Spartanburg County, SC", "Anderson County, SC", "York County, SC"],
    "knows_about": ["Stormwater management", "Retention pond maintenance", "Detention pond maintenance", "Stormwater BMP inspection", "Stormwater control measure (SCM) inspection", "Erosion control", "Forestry mulching", "Land clearing", "Drainage ditch maintenance"],
    "legal_entity": "Carolina Outdoor Services, LLC",
    "slogan": "Stormwater Management You Can Count On.",
    "credentials": [
        ("Certified Master Pond Manager", "Clemson Cooperative Extension", CLEMSON_MPM),
        ("Certified SC Post-Construction BMP Inspector", "Clemson Cooperative Extension", CLEMSON_BMP),
        ("Certified Stormwater Plan Reviewer", "Clemson Cooperative Extension", CLEMSON_BMP),
        ("SCM Inspection & Maintenance Certification", "NC State University, Biological & Agricultural Engineering", NCSU_SCM),
    ],
    "member_of": [("Sustain SC", SUSTAIN_SC)],
    "social": {"facebook": "https://www.facebook.com/profile.php?id=61561802767388", "instagram": "https://www.instagram.com/carolinaoutdoorservices/"},
  },
  "theme": {
    # Kept from the current site: slate header (#333946), green buttons, navy headings, sky blue from the logo.
    # Button green deepened one step (#4c7a2e) so white text passes WCAG AA.
    "colors": {"primary": "#333946", "primary_deep": "#242833", "secondary": "#72c4d6", "secondary_deep": "#0f3b5f",
               "secondary_wash": "#eaf6f9", "accent": "#4c7a2e", "accent_text": "#ffffff", "surface": "#f6f8fa",
               "ink": "#152033", "muted": "#4a5568", "texture": "#72c4d6", "highlight": "#9ed36a"},
    "fonts": {"display": "inter", "body": "outfit"},
    "radius": "soft", "heading_case": "uppercase", "divider": "none", "texture": "none", "hero_layout": "centered",
  },
  "logo": {"type": "image", "file": "logo.webp", "schema_file": "logo-light-bg.png", "width": 96, "height": 96},
  "favicon_svg": FAVICON_SVG,
  "integrations": {
    "form_mode": "web3forms",
    "web3forms_access_key": "9b342499-7e94-4d37-b2a9-e7b7bb17445c",   # created with the client's email csas2787@gmail.com (public by design)
    "web3forms_subject": "New site assessment request from cosstormwater.com",
    "web3forms_from_name": "Carolina Outdoor Services website",
    "thank_you_slug": "thank-you",
    "gtm_id": "GTM-578PKL83",
    "google_reviews_url": "https://maps.google.com/?cid=12341557194562310408",   # GBP listing (5.0, 7 reviews)
    "google_review_write_url": "https://g.page/r/CQiRDU3hBEarEBM/review",   # GBP "Ask for reviews" link
  },
  "labels": {
    "cta": "Free Site Assessment", "cta_short": "Free Assessment", "cta_long": "Schedule a Free Site Assessment",
    "phone_prefix": "Call or text", "topbar_promise": "Stormwater Management You Can Count On.",
    "footer_blurb": "Certified stormwater inspections, retention pond maintenance and repair, erosion repair and forestry mulching for commercial, industrial and HOA properties across South Carolina and North Carolina. Since 2004.",
    "footer_services_title": "Services",
    "reviews_title": "What our clients say on Google",
    "cta_band_title": "Ready to stop worrying about your stormwater system?",
    "cta_band_text": "Let's do a free site assessment. We'll look, tell you exactly what we see, and give you a clear recommendation. No obligation, no pressure.",
    "aside_title": "Free site assessment", "aside_text": "Talk directly with a certified inspector. We respond within one business day.",
    "aside_badges": "✓ Clemson Master Pond Manager · ✓ SC BMP & NC SCM certified · ✓ Licensed & insured",
  },
  "home": {
    "title": "Stormwater & Retention Pond Maintenance, SC & NC",
    "meta": "Certified stormwater inspections, retention pond maintenance and repair, erosion repair and forestry mulching across SC and NC since 2004.",
    "eyebrow": "Your pond is either an asset or a liability",
    "h1": "Stormwater management &amp; retention pond maintenance <em>across South Carolina</em>",
    "lead": "Certified inspections, pond maintenance and repairs, erosion repair and forestry mulching for commercial, industrial and HOA properties, from a Gilbert, SC team with 20+ years in the field. We treat compliance as the starting point, not the scramble.",
    "secondary_cta": ("See Our Work", "gallery"),
    "proof": ["Clemson Certified Master Pond Manager", "SC BMP & NC SCM certified inspector", "Serving the Carolinas since 2004"],
    "trust": [("badge", "Master Pond Manager", "Clemson Extension certified"), ("shield", "SC BMP · NC SCM", "Certified stormwater inspector"),
              ("doc", "Written reports", "Photos + prioritized fixes"), ("leaf", "Sustain SC member", "Sustainability network, Columbia")],
    "why": {"eyebrow": "Why property managers trust us",
            "quote_html": "Your retention pond is either an asset or a liability. <em>Let's make it an asset.</em>",
            "body": "Stormwater systems don't fail dramatically. They fail slowly: a little erosion, some overgrowth, a clogged outlet. Then after one heavy rain you're facing a Notice of Violation and a repair bill that could have been a fraction of the cost. Catching it early is what we do.",
            "items": [("check", "20+ years, still showing up.", "Two decades in outdoor services, the last twelve focused entirely on stormwater."),
                      ("doc", "We inspect before they do.", "We find the issues first and give you the chance to fix them on your timeline, not a regulator's."),
                      ("phone", "Direct, no drama.", "You'll know what we found, what it costs and when we're coming. No upsells, no surprise invoices."),
                      ("pin", "All of SC and into NC.", "From Gilbert and Lexington to the Upstate, Aiken, York County and Charlotte.")]},
    "credentials": {"eyebrow": "Credentials", "title": "Certified for stormwater, not just mowing",
                    "lead": "Most pond crews are landscapers. These are the certifications behind our inspections and maintenance plans.",
                    "items": [("badge", "Certified Master Pond Manager", "Clemson Extension", CLEMSON_MPM, "Clemson's pond management certification: stormwater pond design, inspection and maintenance, water quality and aquatic plant management."),
                              ("shield", "SC Post-Construction BMP Inspector", "Clemson Extension", CLEMSON_BMP, "Certified to inspect permanent stormwater BMPs such as ponds, basins and outlet structures in South Carolina."),
                              ("doc", "Stormwater Plan Reviewer", "Clemson Extension", CLEMSON_BMP, "Trained to read and review stormwater plans, so we maintain your pond the way it was designed."),
                              ("check", "NC SCM Inspection & Maintenance", "NC State University", NCSU_SCM, "Certified in North Carolina stormwater control measure (SCM) inspection and maintenance."),
                              ("leaf", "Member, Sustain SC", "Sustain SC · Columbia", SUSTAIN_SC, "A statewide nonprofit connecting South Carolina businesses' sustainability goals with local land and water solutions."),
                              ("users", "Licensed & insured", "Carolina Outdoor Services, LLC", "", "In business since 2004, with certificates of insurance available on request.")]},
    "steps": {"eyebrow": "How it works", "title": "From first call to a compliant pond",
              "items": [("Call, text or send the form", f"{PHONE}. Tell us about the property and the system."),
                        ("Free site assessment", "We walk the site and tell you plainly what we see. No obligation."),
                        ("Written proposal", "Scope, timeline and price in plain language, with no add-ons after work starts."),
                        ("Work, then records", "Our own crew does the work, and you get photos and a written summary.")]},
    "form": {"eyebrow": "Free site assessment", "title": "Tell us about your stormwater system",
             "lead": "Commercial, industrial, HOA or municipal: send the basics and we'll get back to you within one business day.",
             "points": ["Certified inspector walks the site", "Plain-language findings", "Written proposal before any work"]},
    "gallery": {"eyebrow": "Our work", "title": "Recent stormwater & clearing jobs",
                "lead": "Real photos from real job sites across the Carolinas.",
                "photos": [PH["outlet"], PH["mowedpond"], PH["mulcher"], PH["tractor"], PH["excavator"], PH["fenced"]]},
    "order": ["trust", "services", "why", "credentials", "gallery", "reviews", "steps", "areas", "form", "blog", "faq", "cta"],
  },
  "services_hub": {"slug": "services", "flat_urls": False, "home_count": 6, "nav_label": "Services",
    "title": "Stormwater Management Services in SC & NC",
    "meta": "Stormwater management for SC & NC properties: certified inspections, retention pond maintenance and repair, erosion repair, ditches, forestry mulching.",
    "h1": "Stormwater Management Services for South Carolina &amp; North Carolina",
    "lead": "Everything a permitted stormwater system needs, from one certified team: inspections, routine pond maintenance, repairs, erosion control and ditch work, plus forestry mulching and land clearing.",
    "home_title": "Everything your stormwater system needs",
    "home_lead": "Inspections, maintenance and repairs that keep ponds compliant, plus forestry mulching and land clearing that keep the land around them usable."},
  "services": SERVICES,
  "areas": {
    "enabled": True, "hub_slug": "service-areas", "nav_label": "Areas We Serve", "link_prefix": "Stormwater Services",
    "footer": "compact", "footer_lead": "Stormwater & pond services in:", "services_listed": 7,
    "hub_title": "Areas We Serve: South Carolina & North Carolina",
    "hub_meta": "Carolina Outdoor Services serves the Midlands, Aiken, the Upstate, York County & Rock Hill, SC and the Charlotte area of NC from Gilbert, SC.",
    "hub_h1": "Stormwater Services Across South Carolina &amp; North Carolina",
    "hub_lead": "Based in Gilbert, SC, we cover the Midlands every day and travel statewide and into North Carolina for commercial, industrial and HOA stormwater work.",
    "home_title": "Serving South Carolina & North Carolina",
    "groups": [{"name": "The Midlands", "note": "Home base", "slugs": ["gilbert-sc", "lexington-sc", "columbia-sc", "blythewood-sc", "midlands-sc"]},
               {"name": "Aiken County", "note": "CSRA", "slugs": ["aiken-sc", "north-augusta-sc"]},
               {"name": "The Upstate", "note": "I-85 corridor", "slugs": ["greenville-sc", "spartanburg-sc", "anderson-sc", "upstate-sc"]},
               {"name": "York County & North Carolina", "note": "Charlotte region", "slugs": ["rock-hill-sc", "york-county-sc", "north-carolina"]}],
    "outside_note": "Don't see your area? We work statewide in SC and into NC. Call or text",
    "service_where_text": "We serve commercial, industrial and HOA properties across South Carolina and North Carolina, including",
    "page_title": "Retention Pond & Stormwater, {city}, {region}",
    "page_meta": "Retention pond maintenance, stormwater inspections, pond repair and forestry mulching in {city}, {region}. Certified inspector. Call (803) 518-2787.",
    "page_h1": "Retention Pond &amp; Stormwater Services in {city}, {region}",
    "local_title": "Stormwater work in {city}", "aside_title": "Free assessment in {city}",
    "shared_faqs": [("How much does retention pond maintenance cost in {city}?", "It depends on the size of the pond, its condition, and how often it needs service. We price after a free site assessment, and you get a written proposal before any work starts.")],
    "pages": AREAS,
  },
  "gallery_page": {"slug": "gallery", "nav_label": "Gallery", "in_nav": True,
    "title": "Stormwater & Retention Pond Work: Gallery",
    "meta": "Photos of stormwater pond maintenance, inspections, repairs, forestry mulching and land clearing by Carolina Outdoor Services across SC & NC.",
    "h1": "The Work Speaks for Itself",
    "lead": "Pond maintenance, basin mowing, slope clearing and forestry mulching from real job sites across the Carolinas.",
    "photos": [PH[k] for k in ["outlet", "wetpond", "mowedpond", "fenced", "tractor", "mowers", "slope", "riprap", "mulcher", "excavator", "woods", "hoabank", "stabilized"]],
    "cta_title": "Want your pond looking like this?", "cta_text": "Start with a free site assessment. We'll tell you exactly what we see."},
  "resource": {
    "enabled": True, "slug": "stormwater-pond-guide", "nav_label": "Pond Guide",
    "title": "SC Stormwater Pond Maintenance Guide & Checklist",
    "meta": "Who is responsible for a stormwater pond in SC, what Lexington, Richland, Greenville & York counties ask, plus a season-by-season checklist.",
    "h1": "The South Carolina Stormwater Pond Owner's Guide &amp; Checklist",
    "lead": "A plain-English guide for HOAs, property managers and business owners with a retention or detention pond: who's responsible, what your county expects, and what to do each season.",
    "cards": POND_CARDS, "body_html": POND_BODY, "faq_title": "Stormwater pond questions",
    "faqs": [("Who has to maintain a stormwater pond on private property?", "Usually the property owner, such as the HOA, business owner or property manager, under the maintenance agreement signed when the site was developed. That responsibility transfers with the property."),
             ("Why can't trees grow on a pond embankment?", "Roots can open paths for water through the fill and weaken the embankment. Lexington County's requirements, for example, call for woody vegetation to be removed from fill embankments and from within 30 feet of structures and pipes."),
             ("How often should a stormwater pond be dredged?", "South Carolina's stormwater pond guide for HOAs suggests roughly every ten years, but it depends on the drainage area and upstream erosion. Checking forebay sediment at each inspection tells you when."),
             ("What happens if my pond fails a Richland County inspection?", "Richland County gives owners 30 days after a Notice of Violation to make corrections, after which daily penalties may be assessed.")],
    "cta_title": "Want this checklist handled for you?", "cta_text": "We'll inspect your pond, tell you what needs attention, and put it on a documented maintenance schedule.",
  },
  "blog": {
    "enabled": True, "index_slug": "blog", "post_prefix": "post",     # keeps the old GHL URLs: /blog and /post/<slug>
    "category_prefix": "blog/category",                                # keeps /blog/category/<slug>
    "categories": {"Pond Maintenance": "pond-maintenance", "Stormwater Management": "stormwater-management",
                   "Forestry Mulching": "forestry-mulching", "Land Clearing": "land-clearing", "Seasonal": "seasonal",
                   "Sustainability": "sustainability", "Environmental Sustainability": "environmental-sustainability",
                   "South Carolina & North Carolina Resources": "south-carolina-north-carolina-resources", "Rock Hill, SC": "rock-hill-sc"},
    "nav_label": "Blog", "title": "Stormwater & Pond Maintenance Blog, SC & NC",
    "meta": "Practical advice on retention pond maintenance, stormwater inspections, erosion and forestry mulching for SC & NC property managers and HOAs.",
    "h1": "Stormwater advice for South Carolina property managers",
    "lead": "Straight answers on pond maintenance, inspections, compliance and land clearing for commercial, industrial and HOA properties.",
    "default_author": "Carolina Outdoor Services", "home_title": "From the blog",
    "area_related_title": "Advice for {city} property managers",
  },
  "about": {"title": "About Us: Stormwater Specialists Since 2004",
    "meta": "Carolina Outdoor Services: in business since 2004, stormwater-focused for 12+ years. Clemson Master Pond Manager and certified SC & NC inspectors.",
    "h1": "Over 20 Years of Showing Up. 12+ Years of Stormwater Focus.",
    "lead": "Carolina Outdoor Services is based in Gilbert, SC and serves commercial, industrial and HOA properties across South Carolina and North Carolina. We do stormwater work, and we do it right.",
    "story_title": "How we got here",
    "story_html": ABOUT_STORY,
    "photos_title": "On the job", "photos": [PH["outlet"], PH["mulcher"], PH["mowedpond"]],
    "list_title": "Credentials & commitments",
    "list": ["Clemson Extension Certified Master Pond Manager", "Certified SC Post-Construction BMP Inspector", "NC State SCM Inspection & Maintenance Certification",
             "Clemson Certified Stormwater Plan Reviewer", "Member, Sustain SC", "Licensed & insured, certificates on request",
             "Our own crew and equipment: no subcontracting of BMP work", "Plain-language reports, no inflated findings"]},
  "contact": {"title": "Free Site Assessment",
    "meta": "Request a free stormwater site assessment for your retention pond, BMP, ditch or overgrown land in SC or NC. Call or text (803) 518-2787.",
    "h1": "Schedule Your Free Site Assessment",
    "lead": f"Tell us about the property and what's going on, and we'll follow up within one business day. Prefer to talk? Call or text {PHONE}, Monday to Friday, 7 AM to 5 PM.",
    "extra_inputs": [("company", "Company / HOA / property (optional)", "organization", False, True), ("address", "Property address or city", "street-address", False, True)],
    "selects": [("Property type", ["", "Commercial / retail", "Industrial / distribution", "HOA or community association", "Municipal or institutional", "Developer / construction site", "Other"]),
                ("Service needed", ["", "Stormwater / pond inspection", "Retention pond maintenance", "Pond repair", "Erosion repair", "Drainage ditch maintenance", "Forestry mulching", "Land clearing", "Not sure / several"])],
    "select_names": {"Property type": "property_type", "Service needed": "service"},
    "select_placeholder": "Choose one", "city_select": False,
    "message_label": "Tell us about the site (number of ponds, problem you're seeing, inspection notice, deadline)",
    "submit": "Request my free assessment", "note": "No obligation. You'll get a written proposal before any work starts.",
    "success": "Thanks! We got your request and will follow up within one business day.",
    "next_steps": ["We reply within one business day", "A free on-site assessment", "Written proposal before any work"],
    "faqs": [GENERAL_FAQS[0], GENERAL_FAQS[5], GENERAL_FAQS[4]], "page_type": "ContactPage"},
  "thank_you": {"title": "Thank you", "h1": "Thanks, we got your request.", "lead": "We'll follow up within one business day.", "text": "Need us sooner?"},
  "reviews": REVIEWS, "reviews_display": "carousel", "reviews_interval": 6000,   # 3 across, rotates every 6s
  "faqs": GENERAL_FAQS,
  "legal_pages": [("privacy-policy", "Privacy Policy")],
  "redirects": [("/home", "/"), ("/index", "/"),
                # the old site had a second, duplicate copy of every service page at the top level; /services/<slug> was canonical
                ("/retention-pond-maintenance", "/services/retention-pond-maintenance/"), ("/stormwater-inspections", "/services/stormwater-inspections/"),
                ("/stormwater-pond-repairs", "/services/stormwater-pond-repairs/"), ("/forestry-mulching", "/services/forestry-mulching/"),
                ("/land-clearing", "/services/land-clearing/"), ("/drainage-ditch-maintenance", "/services/drainage-ditch-maintenance/"),
                ("/erosion-repair", "/services/erosion-repair/"),
                ("/blog/author/*", "/blog/"), ("/blog/tag/*", "/blog/"), ("/areas-we-serve", "/service-areas/")],
}
