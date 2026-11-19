"""Harvest Moon Realty: client config for Steelclad Site Kit.
Real estate brokerage, office at 411 N Lake Dr, Lexington, SC. Barry Keith, SC real estate license #43236.
New site (no previous website). Build: python3 build.py harvest-moon-realty
Forms: GoHighLevel (form id + tracking script still to add). Listing search: CMLS IDX embed, NO forced registration.
Facts come from Barry's onboarding notes (Nov 2026), his Google Business Profile and Facebook page. See NOTES.md
for everything still to confirm, and the placeholders the Buying a Home / Buying Land pages hold until his own copy arrives."""

LICENSE = "SC real estate license #43236"
FAVICON_SVG = open(__file__.replace("site.py", "source/favicon.svg")).read()
PHONE = "(803) 309-9521"

# ---------------------------------------------------------------- SERVICES (money pages)
# Buying a Home and Buying Land are drafted from Barry's onboarding answers. He is sending his own process copy for
# both pages; when it arrives, it replaces "included" / "signs" below (NOTES.md).
SERVICES = [
    {
        "slug": "buying-a-home-lexington-sc",
        "name": "Buying a Home",
        "short": "From your first question to the closing table, with someone who points out the pitfalls and the advantages.",
        "icon": "key",
        "title": "Buying a Home in Lexington, SC | Buyer's Agent",
        "meta": "Buying a home in Lexington or Richland County? Barry Keith walks you through every step, low-pressure, with 35+ years in SC real estate. (803) 309-9521.",
        "h1": "Buying a Home in Lexington, SC",
        "lead": "Buying with me means you'll understand what's happening at every step. I'll point out the potential pitfalls I see, and the potential advantages too, and I'll stick up for you from the first showing to the closing table.",
        "included_title": "How we'll buy your home, step by step",
        "included": [
            ("1. Sit down and talk it through", "What you need, what you'd like, where you want to be and what you want to spend. No pressure, and no obligation to keep going."),
            ("2. Get your financing lined up", "A pre-approval from a lender tells you what you can comfortably buy and shows sellers you're serious. I can point you to local lenders I trust."),
            ("3. Search, then tour the right homes", "Search the MLS on this site without signing up, and I'll set up showings for the ones worth seeing. I'll tell you what I notice in each house, good and bad."),
            ("4. Write a strong offer", "When you find the one, we move. The #1 mistake I see is buyers being scared to write a contract and losing the house they wanted. I'll help you decide with confidence."),
            ("5. Inspections & due diligence", "Inspections, the appraisal, survey questions and repair negotiations. This is where experience protects you."),
            ("6. Close and get the keys", "In South Carolina an attorney handles the closing. I'll keep everyone on schedule and make sure nothing surprises you at the table."),
        ],
        "signs_title": "You'll get the most out of working with me if…",
        "signs": [
            "You're buying your first home and want someone to explain the process, not just open doors",
            "You've lost out on a house before and want to be ready to move next time",
            "You're relocating to Lexington or Richland County and don't know the area yet",
            "You want an agent who'll tell you the truth about a house, even when it's not what you hoped",
        ],
        "faqs": [
            ("Do I pay you to help me buy a home?", "How a buyer's agent is paid is agreed in writing before we tour homes, and in many sales the seller covers some or all of it. I'll explain your options plainly in our first conversation, before you sign anything."),
            ("How long does it take to buy a home?", "It depends on the market and your financing, but once you're under contract, closing commonly takes 30 to 45 days. The search itself can take a weekend or a few months. I'll go at your pace."),
            ("Can I search homes on your site without giving my email?", "Yes. That's on purpose. Search every listing on the Midlands MLS as long as you like, with no sign-up. When you're ready to see one, call or text me."),
            ("What areas do you cover?", "Mainly Lexington and Richland counties, including Lexington, Chapin, Irmo, West Columbia, Columbia and Gilbert. I've also helped buyers as far out as Johnston and Manning, so ask."),
        ],
    },
    {
        "slug": "buying-land-south-carolina",
        "name": "Buying Land",
        "short": "Farmland, timberland, home sites and large tracts anywhere in South Carolina, with the due diligence done right.",
        "icon": "tree",
        "title": "Buying Land in South Carolina | Farms, Timber, Acreage",
        "meta": "Buying land, farmland, timberland or acreage in South Carolina? Barry Keith checks easements, utilities, wetlands, timber and access with you. Statewide.",
        "h1": "Buying Land in South Carolina",
        "lead": "Land deals can be very simple for the recreational buyer, or extremely complicated for a developer. Either way, there's a lot to look at before you buy, and I work land sales across the entire state.",
        "included_title": "What I'll look at with you before you buy land",
        "included": [
            ("Easements & access", "Who else has a right to cross or use the property, and is there legal, year-round access to a public road?"),
            ("Utilities, septic & well", "Does it have power, water and sewer, or access to them? If not, will the ground support a septic system and a well?"),
            ("Topography & soils", "How the land lies, where water goes when it rains, and whether the soils fit what you want to do with it."),
            ("Wetlands & flood zones", "Wetlands and flood-prone areas can limit where and what you can build. We check before you're committed."),
            ("Timber & mineral value", "Merchantable timber can carry real value. Mineral rights matter too. Know what conveys with the sale and what doesn't."),
            ("What's around it", "Railroad tracks, noisy industry, flight paths, and how far it is to grocery stores, drug stores, schools and hospitals."),
            ("Future value", "What's happening around the property now, and what that likely means for its value later."),
        ],
        "signs_title": "Land I help buyers with",
        "signs": [
            "Farmland and pasture",
            "Timberland and recreational or hunting tracts",
            "Home sites and acreage to build on",
            "Large undeveloped tracts and investment land",
            "Waterfront lots, including Lake Murray",
        ],
        "faqs": [
            ("Do you sell land outside Lexington County?", "Yes. I work land sales across the entire state of South Carolina, not just the Midlands."),
            ("What's the biggest thing land buyers miss?", "That there's so much to check: easements, access, utilities or whether the land will support them, topography, wetlands, timber and mineral value, and what's around it. My land buying checklist covers all of it."),
            ("Can I search land listings on your site?", "Yes, with no sign-up. Search land and acreage on the Midlands MLS whenever you like, then call or text me about anything that catches your eye."),
            ("I'm just looking for a few acres to build a house. Is that a land deal or a home deal?", "Both, really, and that's where my background helps. A home site still needs the land checks: access, septic or sewer, a well or water, and what's next door."),
        ],
    },
    {
        "slug": "first-time-home-buyers-lexington-sc",
        "name": "First-Time Home Buyers",
        "short": "Patient, step-by-step help for first-time buyers, so the process makes sense before you sign anything.",
        "icon": "home",
        "title": "First-Time Home Buyers in Lexington, SC | Patient Help",
        "meta": "Buying your first home in Lexington or Columbia, SC? Barry Keith explains every step, answers every question and keeps the process simple. No pressure.",
        "h1": "First-Time Home Buyers in Lexington, SC",
        "lead": "First-time buyers are my favorite clients. I love to hold your hand from start to finish, helping you not only find a home but understand the process you're going through, because it can be overwhelming.",
        "included_title": "What first-time buyers get from me",
        "included": [
            ("Plain-English explanations", "Pre-approval, earnest money, inspections, appraisals, closing costs: I'll explain each one before you run into it."),
            ("Help with the money side", "I'll connect you with lenders who work with first-time buyers so you know your budget and your options before you shop."),
            ("Honest opinions on every house", "I've seen it all. I'll tell you what I notice about a house, the good and the not-so-good."),
            ("Confidence when it's time to offer", "Too many first-time buyers hesitate and lose the house they wanted. We'll be ready to move when the right one shows up."),
            ("Protection through closing", "I'll stand up for you through inspections and negotiations, professionally and respectfully, so you don't get taken advantage of."),
        ],
        "signs_title": "Questions first-time buyers ask me",
        "signs": [
            "How much house can I actually afford?",
            "How much do I need saved for the down payment and closing?",
            "What happens if the inspection finds problems?",
            "How fast do I need to make an offer?",
        ],
        "faqs": [
            ("I'm not sure I'm ready to buy. Can we still talk?", "Absolutely. A lot of my first-time buyers start with a conversation months before they buy. There's no pressure and no obligation."),
            ("Are there programs for first-time buyers in South Carolina?", "Yes. There are loan programs and down payment assistance options for qualifying buyers. A good lender will tell you which ones fit you, and I can connect you with lenders who use them."),
            ("Do your past clients actually recommend you?", "Read my Google reviews. Many of them come from first-time buyers, and that's how most of my business comes to me: referrals and repeat clients."),
        ],
    },
    {
        "slug": "lake-murray-homes-land",
        "name": "Lake Murray & Waterfront",
        "short": "Lake homes, waterfront lots and water-access neighborhoods around Lake Murray.",
        "icon": "drop",
        "title": "Lake Murray Homes & Waterfront Land | Local Realtor",
        "meta": "Buying a home or lot on Lake Murray? Barry Keith helps you check the dock, water depth, shoreline rules and access before you buy. Lexington to Chapin.",
        "h1": "Lake Murray Homes &amp; Waterfront Property",
        "lead": "A lake property is a home purchase and a land purchase at the same time. I'll help you look past the view at the things that decide whether the place works for you.",
        "included_title": "What to check on a Lake Murray property",
        "included": [
            ("The dock & the water", "Is there a dock, and is it permitted? How deep is the water at the dock, and does it stay usable when the lake is drawn down?"),
            ("Shoreline rules", "Dominion Energy manages the Lake Murray shoreline, and docks and shoreline work need its approval. We look at what's allowed before you count on it."),
            ("Main channel or cove", "Open-water views and boat traffic, or a quiet cove? Each has trade-offs for swimming, docking and resale."),
            ("Water access vs. waterfront", "Many neighborhoods offer a community dock, ramp or lake access without a private shoreline, often at a very different price."),
            ("Septic, slope & flood zones", "Lake lots often slope to the water and may rely on septic. Those details matter for building, renovating and insuring."),
        ],
        "signs_title": "Lake Murray communities I work in",
        "signs": [
            "Lexington and the south shore",
            "Chapin, the Capital of Lake Murray",
            "Irmo and the dam area",
            "Gilbert, Batesburg-Leesville and the quieter west end",
        ],
        "faqs": [
            ("Do you help with lake lots as well as lake homes?", "Yes. Waterfront lots are land purchases, so I bring the same land checks: access, septic, slope, flood zone and shoreline rules."),
            ("Can I search Lake Murray listings on your site?", "Yes, with no sign-up required. Search homes and land on the Midlands MLS and narrow it down to the lake."),
        ],
    },
    {
        "slug": "selling-a-home-lexington-sc",
        "name": "Selling Your Home",
        "short": "Pricing, preparation and negotiation from a broker who keeps the process simple and protects your interests.",
        "icon": "badge",
        "title": "Sell Your Home in Lexington, SC | Listing Agent",
        "meta": "Selling a home or land in Lexington or Richland County? Barry Keith prices it right, lists it on the MLS and negotiates for you. Honest, low-pressure.",
        "h1": "Selling Your Home in Lexington, SC",
        "lead": "Whether it's the house you raised a family in or a tract that's been in the family for generations, I'll keep the sale simple, keep you informed and keep your best interest at heart.",
        "included_title": "How I'll sell your property",
        "included": [
            ("An honest price", "A pricing opinion based on what's actually selling near you, not a number picked to win the listing."),
            ("Get it ready", "Advice on what's worth fixing, what isn't, and how to present the property for photos and showings."),
            ("On the MLS & beyond", "Your property goes on the Midlands MLS, where buyers' agents across the area see it."),
            ("Negotiation that protects you", "Offers, inspection requests and appraisal issues handled firmly, professionally and respectfully."),
            ("A clear path to closing", "I keep the buyer's agent, lender and closing attorney on schedule and keep you updated."),
        ],
        "signs_title": "Sellers I work with",
        "signs": [
            "Homeowners moving up, moving down or moving away",
            "Families selling a parent's home or an inherited property",
            "Landowners selling farmland, timberland or acreage",
            "Investors selling rental or investment property",
        ],
        "faqs": [
            ("What's my home worth?", "Call or text me. I'll look at what has sold near you recently and give you an honest opinion of value, with no obligation to list."),
            ("Do you also sell land?", "Yes. I sell land across South Carolina: farms, timberland, large tracts and home sites."),
        ],
    },
]

# ---------------------------------------------------------------- COMMUNITIES (city pages)
AREAS = [
    {
        "slug": "lexington-sc-real-estate", "city": "Lexington", "county": "Lexington County",
        "zips": "29072, 29073",
        "intro": "Lexington is home. My office is at 411 N Lake Dr, a few minutes from downtown, and I've been buying, selling and investing around here since 1989. It's grown fast, from the Sunset Boulevard and US-378 corridors to new neighborhoods heading toward Lake Murray, and I know which parts of town fit which buyers.",
        "local": [
            ("Lexington One schools", "Most of Lexington is served by Lexington County School District One, and the school zone is often the first filter families ask about. Always confirm a property's assigned schools with the district."),
            ("Downtown, subdivisions or acreage", "Walkable streets near Main Street and the Icehouse Amphitheater, established and newer subdivisions, or a few acres on the edge of town: Lexington has all three."),
            ("Close to the lake", "Lake Murray sits just north of town, so lake-access neighborhoods and waterfront homes are part of the Lexington market too."),
        ],
        "faqs": [
            ("Where is Harvest Moon Realty's office?", "411 N Lake Dr, Lexington, SC 29072. Call or text (803) 309-9521 to set a time to meet."),
            ("Can I search Lexington homes for sale on your site?", "Yes, with no sign-up required. Search homes and land on the Midlands MLS, then call or text me about the ones you want to see."),
        ],
    },
    {
        "slug": "chapin-sc-real-estate", "city": "Chapin", "county": "Lexington County",
        "zips": "29036",
        "intro": "Chapin calls itself the Capital of Lake Murray, and much of the market here is lake homes, water-access neighborhoods and larger wooded lots, with I-26 making the drive to Columbia easy.",
        "local": [
            ("Lake and lake-access living", "Waterfront homes and lots, and neighborhoods with community docks or ramps. I'll help you check the dock, the water and the shoreline rules."),
            ("Lexington-Richland Five schools", "Chapin is served by Lexington-Richland School District Five. Confirm a property's assigned schools with the district before you buy."),
            ("Room to spread out", "Bigger lots and acreage outside town for buyers who want space without being far from I-26."),
        ],
        "faqs": [
            ("Do you help buyers in Chapin and on the north side of Lake Murray?", "Yes. Chapin and the Lake Murray area are a regular part of my market, for homes and for waterfront land."),
        ],
    },
    {
        "slug": "irmo-sc-real-estate", "city": "Irmo", "county": "Lexington & Richland Counties",
        "zips": "29063",
        "intro": "Irmo sits right on the Lexington and Richland county line, between the Lake Murray dam and the Harbison shopping area. It's a settled, convenient part of the Midlands with a wide range of neighborhoods and price points.",
        "local": [
            ("Two counties", "Depending on the street, an Irmo home can be in Lexington County or Richland County. That affects property taxes and services, so we check it on every house."),
            ("Lexington-Richland Five schools", "Irmo is served by Lexington-Richland School District Five. Confirm the assigned schools for any specific address with the district."),
            ("Near the dam and the lake", "Quick access to Lake Murray, the dam walkway and Saluda Shoals Park, with I-26 close by."),
        ],
        "faqs": [
            ("Is Irmo in Lexington County or Richland County?", "Both. The town straddles the county line, so we confirm the county for every property you consider."),
        ],
    },
    {
        "slug": "west-columbia-sc-real-estate", "city": "West Columbia", "county": "Lexington County",
        "zips": "29169, 29170, 29172",
        "intro": "West Columbia sits across the Congaree River from downtown Columbia, so you get Lexington County living a few minutes from the city. It's a good fit for buyers who want older, established neighborhoods, newer homes farther out, or a shorter commute.",
        "local": [
            ("Close to the city", "Downtown Columbia, the riverwalk and the airport are all nearby, which makes West Columbia popular with commuters and first-time buyers."),
            ("Lexington Two schools", "Much of West Columbia is served by Lexington County School District Two. Confirm the assigned schools for any address with the district."),
            ("Older homes, careful inspections", "Established neighborhoods have charm and good locations, and older houses need a careful look at roofs, plumbing, electrical and foundations. I'll help you know what to look for."),
        ],
        "faqs": [
            ("Is West Columbia good for first-time buyers?", "It can be. You'll find a range of price points close to the city. Tell me your budget and commute and I'll show you what fits."),
        ],
    },
    {
        "slug": "columbia-sc-real-estate", "city": "Columbia", "county": "Richland County",
        "zips": "29201–29229",
        "intro": "Columbia is the state capital and the Richland County seat, home to the University of South Carolina and Fort Jackson. The market runs from historic in-town neighborhoods to suburbs in northeast Columbia and rural land toward the county's edges.",
        "local": [
            ("Many neighborhoods, many markets", "In-town historic homes, established suburbs and newer construction each price and sell differently. I'll help you compare them honestly."),
            ("Schools vary by address", "Richland County is served mainly by Richland One and Richland Two. Confirm the assigned schools for any specific address with the district."),
            ("Land in Richland County", "Lower Richland and the county's rural edges still have farmland, timber and acreage. I bring my land checks to those deals too."),
        ],
        "faqs": [
            ("Do you work in Columbia and Richland County, not just Lexington?", "Yes. Lexington and Richland counties are my primary market for home sales."),
        ],
    },
    {
        "slug": "gilbert-sc-real-estate", "city": "Gilbert", "county": "Lexington County",
        "zips": "29054",
        "intro": "Gilbert is rural Lexington County: peach orchards, farms, homes on acreage and roads that lead down to the south shore of Lake Murray. It's a favorite of buyers who want land, quiet and still a reasonable drive to Lexington.",
        "local": [
            ("Homes on acreage", "Many Gilbert properties come with land, so we check wells, septic, outbuildings, fencing and access along with the house."),
            ("Farmland & timber", "Working farms, pasture and timber tracts, where easements, soils and timber value all matter."),
            ("Lexington One schools", "Gilbert is served by Lexington County School District One. Confirm the assigned schools for any address with the district."),
        ],
        "faqs": [
            ("Do you help buyers find land and farms around Gilbert?", "Yes. Rural property is one of my favorite kinds of deal, and Gilbert has plenty of it."),
        ],
    },
]

# Real Google reviews (Barry's Google Business Profile, Nov 2026). Exact sentences, shortened, attributed to Google.
REVIEWS = [
    ("Claire M.", "Google review · bought two homes with Barry",
     "Barry is a family man at heart, and that really shows in the way he treats his clients. He was always quick to respond, patient, attentive, and so easy to work with."),
    ("Emily & Kevin H.", "Google review · sold and bought",
     "Barry kept us informed every step of the way, making a process with so many moving parts feel manageable. We always felt heard, supported, and confident that he understood our goals."),
    ("Elizabeth D.", "Google review",
     "He takes the time to answer questions, explain things clearly, and make the process as smooth and stress-free as possible."),
]

GENERAL_FAQS = [
    ("Do I have to sign up to search homes or land on your site?", "No, and that's on purpose. Most real estate sites make you hand over your email or phone number before you can look around. Here you can search the Midlands MLS as long as you like without signing up. When you're ready to talk, you reach out."),
    ("What areas do you serve?", "For homes, mainly Lexington and Richland counties: Lexington, Chapin, Irmo, West Columbia, Columbia, Gilbert and the communities around them, and I've sold homes as far away as Johnston and Manning. For land, I work the entire state of South Carolina."),
    ("How long have you been in real estate?", "I started investing in South Carolina real estate in 1989 and have been a licensed agent since 2003. Harvest Moon Realty is my brokerage."),
    ("Do you work with land buyers and investors?", "Yes. Farmland, timberland, large undeveloped tracts and investment properties are a big part of what I do."),
    ("Will you pressure me?", "No. I'm very low-pressure. Most of my business comes from repeat clients and referrals, and that only happens when people feel taken care of."),
    ("How do I get started?", "Call or text (803) 309-9521, or send a quick note through the contact page. We'll talk about what you're looking for, with no obligation."),
]

# ---------------------------------------------------------------- RESOURCE: land buying checklist (from Barry's own list)
LAND_CHECKLIST = [
    ("Access", "Can you get to it?", ["Legal, recorded access to a public road", "Driveway or road condition in wet weather", "Shared driveways and who maintains them", "Gates, locks and landlocked neighbors"]),
    ("Easements", "Who else has rights?", ["Power line, pipeline and utility easements", "Access easements across the property", "Conservation easements or restrictions", "Read the deed, the plat and the title commitment"]),
    ("Utilities", "Water, sewer, power", ["Is public water or sewer available, and how far away?", "If not: will the soil support a septic system?", "Well: depth and quality of nearby wells", "Power: distance to the nearest line and cost to bring it in"]),
    ("The ground", "Topography, soils & water", ["Slope, low spots and where rain runs", "Soil types for septic, building or farming", "Wetlands that limit where you can build", "Flood zone status on FEMA's flood maps"]),
    ("Value in the land", "Timber & minerals", ["Merchantable timber, and when it was last cut", "Whether timber rights convey with the sale", "Mineral rights and whether they were severed", "Current-use or agricultural tax status"]),
    ("The neighborhood", "What's around it", ["Railroad tracks, industry and noise", "Flight paths and air traffic", "Distance to grocery, drug stores, schools and hospitals", "Zoning on the property and next door"]),
    ("The future", "Where values are headed", ["New roads, subdivisions or industry planned nearby", "Comparable land sales in the area", "Zoning changes or rezoning requests", "How you'd resell it if plans change"]),
]

LAND_BODY = """
<h2>Why land needs a different checklist</h2>
<p>When you buy a house, a lot of the questions have already been answered: the power is on, the water runs and the septic or sewer works. With land, nothing is a given. Two tracts that look the same on a listing can be worth very different amounts once you know about the easement across the middle, the wetlands in the back or the cost of bringing power in.</p>
<p>Land deals can be very simple for the recreational buyer and extremely complicated for a developer. Either way, the checklist above is what I walk through with every land buyer before they're committed.</p>
<h2>Where to look things up</h2>
<p>Much of this can be researched before you ever walk the property:</p>
<ul>
<li><strong>Flood zones:</strong> <a href="https://msc.fema.gov/portal/home" rel="noopener">FEMA Flood Map Service Center</a></li>
<li><strong>Soils:</strong> <a href="https://websoilsurvey.nrcs.usda.gov/" rel="noopener">USDA Web Soil Survey</a></li>
<li><strong>Wetlands:</strong> <a href="https://www.fws.gov/program/national-wetlands-inventory/wetlands-mapper" rel="noopener">U.S. Fish &amp; Wildlife Service Wetlands Mapper</a> (a starting point; only a field delineation is definitive)</li>
<li><strong>Septic permits:</strong> the <a href="https://des.sc.gov/" rel="noopener">South Carolina Department of Environmental Services</a> handles onsite wastewater (septic) permits</li>
<li><strong>Parcels, deeds &amp; zoning:</strong> the county's GIS map, register of deeds and planning department</li>
</ul>
<h2>Get help before you sign</h2>
<p>Online maps are a start, not an answer. Surveys, soil evaluations, title work and a careful walk of the property tell you the rest. If you're looking at land anywhere in South Carolina, <a href="/contact/">call or text me</a> before you commit, or <a href="/search-land/">search land listings</a> on the Midlands MLS without signing up.</p>
<p style="font-size:.9rem;color:var(--c-muted)">This checklist is general information, not legal, survey or engineering advice. Rules vary by county and by property.</p>
"""

# ---------------------------------------------------------------- LISTING SEARCH (IDX from Consolidated MLS)
# embed_html stays empty until the IDX vendor is approved by CMLS and set up with registration OFF (NOTES.md).
SEARCH = {
    "enabled": True, "nav_label": "Search Listings",
    "badge": "No sign-up. No email required. Just search.",
    "home_eyebrow": "Search the Midlands MLS",
    "home_title": "Search homes and land on your own terms",
    "home_lead": "Most real estate sites make you hand over your email before you can look around. Not here. Browse every listing on the Midlands MLS as long as you like, and call when you're ready.",
    "preview_note": "Preview: the live Consolidated MLS search (homes and land, no sign-up) loads here once Barry's IDX feed is connected.",
    "fallback_text": "Our MLS search is being connected. In the meantime, call or text Barry and he'll send you current listings that match what you want, with no account needed.",
    "disclaimer_html": "Listing information is provided through the Consolidated Multiple Listing Service (CMLS) IDX program, is deemed reliable but not guaranteed and should be independently verified. Listings held by brokerages other than Harvest Moon Realty are marked with the listing brokerage's name.",
    "verify": "Listing search: confirm the IDX vendor has registration turned OFF (no forced or soft sign-up), and replace the MLS disclaimer with the exact wording CMLS and the vendor require.",
    "pages": [
        {
            "slug": "search-homes", "nav": "Search Homes for Sale", "icon": "home",
            "short": "Every house, townhome and condo for sale on the Midlands MLS, from Lexington and Chapin to Columbia.",
            "card_cta": "Search homes →",
            "title": "Search Homes for Sale in Lexington & Columbia, SC",
            "meta": "Search every home for sale on the Midlands MLS in Lexington, Columbia, Chapin & Irmo, SC. No sign-up, no email required. Questions? (803) 309-9521.",
            "h1": "Search Homes for Sale in Lexington &amp; the Midlands",
            "lead": "Every home on the Midlands MLS, searchable without handing over your email or phone number. When something catches your eye, call or text me.",
            "embed_html": "",
            "placeholder_title": "Midlands MLS home search",
            "tips_title": "Tips for searching smarter",
            "tips": [
                "Search by school zone as well as city: school assignments don't always follow town lines",
                "Check the county: some Irmo and Chapin-area homes are in Richland County, others in Lexington County",
                "Look at days on market: a home that has sat a while may have room to negotiate",
                "When a new listing fits, move quickly. The #1 mistake I see is waiting too long to write an offer",
            ],
            "aside_title": "Found one you like?", "aside_text": "Call or text and I'll set up a showing, usually the same week. No account needed.",
            "faq_title": "Searching on this site",
            "faqs": [
                ("Do I have to create an account to search?", "No. Search as much as you like without signing up or giving your email or phone number."),
                ("Will someone call me because I searched?", "No. We don't know who searches. You'll only hear from me if you reach out first."),
                ("Can I see homes listed by other brokerages?", "Yes. The search includes listings from brokerages across the Midlands MLS, and I can show you any of them."),
            ],
        },
        {
            "slug": "search-land", "nav": "Search Land & Acreage", "icon": "tree",
            "short": "Lots, farmland, timberland and large tracts on the Midlands MLS, including Lake Murray waterfront.",
            "card_cta": "Search land →",
            "title": "Search Land & Acreage for Sale in the SC Midlands",
            "meta": "Search land, lots, farms and timberland for sale on the Midlands MLS. No sign-up required. Land help from Barry Keith, statewide in SC: (803) 309-9521.",
            "h1": "Search Land &amp; Acreage for Sale",
            "lead": "Home sites, farmland, timberland and large tracts on the Midlands MLS. No sign-up wall. When you find a tract you like, I'll help you check what the listing doesn't tell you.",
            "embed_html": "",
            "placeholder_title": "Midlands MLS land search",
            "tips_title": "Before you fall in love with a tract",
            "tips": [
                "Look for recorded road access: \"no road frontage\" can mean an easement, or a problem",
                "Ask whether the land has passed a septic evaluation if you plan to build",
                "Check wetlands and flood zones before you plan where the house goes",
                "Ask what conveys: timber rights and mineral rights aren't always included",
            ],
            "body_html": '<p>Want the full list? Read my <a href="/land-buying-checklist-south-carolina/">South Carolina land buying checklist</a>.</p>',
            "aside_title": "Looking outside the Midlands?", "aside_text": "I work land sales across all of South Carolina. Tell me what you're after and I'll help you find it.",
            "faq_title": "Land search questions",
            "faqs": [
                ("Do I need to register to search land listings?", "No. Search freely, with no email or phone number required."),
                ("Do you handle land deals outside Lexington and Richland counties?", "Yes. I work land sales across the entire state of South Carolina."),
            ],
        },
    ],
}

CONFIG = {
  "business": {
    "name": "Harvest Moon Realty", "legal_name": "Harvest Moon Realty",
    "domain": "https://harvestmoonrealty.com",
    "phone": PHONE, "tel": "+18033099521",
    "email": "barry@harvestmoonrealty.com",            # new mailbox on the new domain (confirm it's set up before launch)
    "schema_type": "RealEstateAgent",
    "description": "Harvest Moon Realty is a Lexington, SC real estate brokerage. Barry Keith helps buyers and sellers of homes in Lexington and Richland counties and land buyers across South Carolina, with 35+ years in SC real estate.",
    "address": {"street": "411 N Lake Dr", "locality": "Lexington", "region": "SC", "zip": "29072"},
    "hours": [(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "08:00", "20:00")],
    "hours_text": "Open 7 days, 8 AM – 8 PM",
    "counties": ["Lexington County, SC", "Richland County, SC", "South Carolina"],
    "knows_about": ["Residential real estate", "First-time home buyers", "Land sales", "Farmland", "Timberland", "Lake Murray waterfront property", "Investment property"],
    "founder": "Barry Keith",
    "slogan": "Southern heritage. Modern comfort.",
    "social": {"facebook": "https://www.facebook.com/harvestmoonrealty", "instagram": "https://www.instagram.com/harvestmoonrealty/"},
  },
  "theme": {
    # Brand colors from the client's palette: Pantone 115 C #FDDA24, 150 C #FFB25B, 7610 C #683431, Warm Red C #F9423A.
    "colors": {"primary": "#683431", "primary_deep": "#3b1d1b", "secondary": "#ffb25b", "secondary_deep": "#a3461f",
               "secondary_wash": "#fff1dc", "accent": "#fdda24", "accent_text": "#3b1d1b", "surface": "#fff8ee",
               "ink": "#2e1a18", "muted": "#6b524d", "texture": "#ffb25b", "highlight": "#fdda24"},
    "fonts": {"display": "fraunces", "body": "dm-sans"},
    "radius": "round", "heading_case": "none", "divider": "wave", "texture": "none", "hero_layout": "card",
    "header": "light",
    "hero_bg": "hero-fields.svg",
    "hero_bg_position_mobile": "left bottom",              # phones: show the fields and the oak, not a giant moon behind the headline
    "hero_bg_overlay_mobile": "linear-gradient(180deg,rgba(43,20,18,.78),rgba(43,20,18,.55))",
    "hero_bg_overlay": "linear-gradient(90deg,rgba(43,20,18,.8) 0%,rgba(43,20,18,.45) 40%,rgba(43,20,18,.08) 62%,rgba(43,20,18,0) 100%)",
  },
  "logo": {"type": "image", "file": "logo.webp", "footer_file": "logo-footer.webp", "schema_file": "logo-light-bg.png", "width": 260, "height": 64, "footer_height": 80},   # footer: full-color logo on a cream badge
  "favicon_svg": FAVICON_SVG,
  "integrations": {
    "form_mode": "ghl_embed",
    "ghl_form_id": "",                 # TODO: Sites > Forms > "Harvest Moon contact" > Integrate (form id)
    "ghl_tracking_snippet": "",        # TODO: Settings > External Tracking > Copy Script (Harvest Moon sub-account)
    "ghl_chat_widget_id": "",
    "gtm_id": "",
    "google_reviews_url": "https://www.google.com/maps?cid=12121055207130619404",
    "google_review_write_url": "https://g.page/r/CQxe66N9ozaoEBM/review",
  },
  "labels": {
    "cta": "Let's Talk", "cta_short": "Let's Talk", "cta_long": "Start a Conversation",
    "phone_prefix": "Call or text", "topbar_promise": "No pressure. Just honest guidance.",
    "footer_blurb": "Homes in Lexington and Richland counties and land across South Carolina, with the calm, low-pressure help of a broker who has been around the block since 1989.",
    "footer_services_title": "Buy, Sell & Search",
    "footer_email": True,
    "footer_areas_title": "Communities", "footer_areas_all": "All Communities",
    "footer_note_html": "Barry Keith, SC real estate license #43236 · Harvest Moon Realty, 411 N Lake Dr, Lexington, SC 29072 · (803) 309-9521. Equal Housing Opportunity. Real estate advertising is subject to the federal Fair Housing Act. Listing information is deemed reliable but not guaranteed.",
    "reviews_title": "What clients say about working with Barry",
    "cta_band_title": "Let's talk, no pressure",
    "cta_band_text": "Whether you're buying your first home, looking for land or just thinking about selling, call or text. You'll get honest, local answers and nothing pushy.",
    "aside_title": "Talk with Barry", "aside_text": "Call or text and you'll talk with me directly. No call center, no pressure.",
    "aside_badges": "✓ Investing since 1989 · ✓ Licensed since 2003 · ✓ SC license #43236",
    "mbar_second_href": "page:search-homes", "mbar_second_icon": "search", "mbar_second_label": "Search",
  },
  "home": {
    "title": "Lexington, SC Realtor for Homes & Land",
    "meta": "Buy a home in Lexington or Richland County, or land anywhere in SC, with Barry Keith of Harvest Moon Realty. Search the MLS, no sign-up. (803) 309-9521.",
    "eyebrow": "Southern heritage. Modern comfort.",
    "h1": "Lexington, SC real estate for home &amp; land buyers, <em>without the pressure</em>",
    "lead": "Barry Keith has been buying, selling and investing in South Carolina real estate since 1989. Homes in Lexington and Richland counties, land anywhere in the state, and a search you can use without signing up.",
    "secondary_cta": ("Search Homes & Land", "search-homes"),
    "proof": ["Search the MLS with no sign-up", "35+ years in SC real estate", "5.0 stars on Google"],
    "hero_card": {"label": "Barry Keith · Harvest Moon Realty", "title": "Your guide for homes & land", "sub": "411 N Lake Dr, Lexington, SC", "hanger": False,
                  "stats": [("1989", "Investing since"), ("2003", "Licensed since"), ("5.0★", "On Google")],
                  "checks": ["Homes in Lexington & Richland counties", "Land, farms & timber statewide", "First-time buyers welcome", "Lake Murray homes & lots"],
                  "note": "“I'm going to be there for you from beginning to end. I'm not going to let you get taken advantage of.” Barry"},
    "trust": [("search", "Search with no sign-up", "Homes & land on the Midlands MLS"), ("clock", "Since 1989", "Investor first, licensed agent since 2003"),
              ("tree", "Land, statewide", "Farms, timber & large tracts"), ("star", "5.0 on Google", "Reviews from real clients")],
    "why": {"eyebrow": "Why Harvest Moon",
            "quote_html": "I'm going to stick up for you, <em>professionally and respectfully.</em>",
            "body": "At this point in my career, I rely on repeat business and referrals. My clients know I'll keep their best interest at heart, keep the process simple, and protect them from beginning to end.",
            "items": [("shield", "You won't get taken advantage of.", "I'll point out the potential pitfalls I see, and the potential advantages too."),
                      ("heart", "No pressure. Ever.", "I'm very low-pressure. Once you choose me as your agent, you'll feel taken care of."),
                      ("search", "Search on your terms.", "Browse the MLS here without giving up your email. Reach out when you're ready."),
                      ("tree", "Homes and land.", "From a first starter home to a timber tract, I've seen it all and know what to look for.")]},
    "steps": {"eyebrow": "How it works", "title": "From first question to closing day",
              "items": [("Search or call, your choice", "Browse homes and land here with no sign-up, or call or text (803) 309-9521."),
                        ("Talk it through", "What you want, where, and your budget. No pressure and no obligation."),
                        ("Tour, check & offer", "I'll show you the right properties, tell you what I see and help you write a strong offer."),
                        ("Close with confidence", "I keep the lender, inspector and closing attorney on track until you have the keys.")]},
    "order": ["trust", "search", "services", "why", "reviews", "steps", "areas", "faq", "cta"],
  },
  "services_hub": {"slug": "real-estate-services", "flat_urls": True, "nav_label": "Buy & Sell",
    "title": "Real Estate Services in Lexington, SC | Buy & Sell",
    "meta": "Buy a home, buy land, sell your home or find Lake Murray property with Barry Keith of Harvest Moon Realty in Lexington, SC. Low-pressure help since 1989.",
    "h1": "How I Can Help You Buy or Sell",
    "lead": "Homes in Lexington and Richland counties, land anywhere in South Carolina, and the experience to spot what others miss.",
    "home_title": "Homes, land and everything in between",
    "home_lead": "Whether you're settling into a neighborhood or buying a timber tract, you get the same steady, honest help."},
  "services": SERVICES,
  "areas": {
    "enabled": True, "hub_slug": "communities", "nav_label": "Communities", "link_prefix": "Real Estate in",
    "hub_title": "Lexington & Richland County Communities | Real Estate",
    "hub_meta": "Real estate in Lexington, Chapin, Irmo, West Columbia, Columbia and Gilbert, SC, from a broker who has worked the Midlands since 1989.",
    "hub_h1": "Communities I Know Well",
    "hub_lead": "If it's in Lexington or Richland County, I've probably been there. Here's a local's look at the places my clients ask about most.",
    "home_title": "Lexington & Richland counties, and land statewide",
    "groups": [{"name": "Lexington County", "note": "Home base", "slugs": ["lexington-sc-real-estate", "chapin-sc-real-estate", "west-columbia-sc-real-estate", "gilbert-sc-real-estate"]},
               {"name": "Richland County & the county line", "note": "", "slugs": ["columbia-sc-real-estate", "irmo-sc-real-estate"]}],
    "outside_note": "Looking somewhere else? I've sold homes as far as Johnston and Manning, and I work land deals statewide. Call or text",
    "service_where_text": "I help buyers and sellers throughout Lexington and Richland counties, including",
    "page_title": "{city}, {region} Real Estate | Homes & Land",
    "page_meta": "Buying or selling in {city}, {region}? Local help from Barry Keith of Harvest Moon Realty, plus a no-sign-up MLS search. Call or text (803) 309-9521.",
    "page_h1": "{city}, {region} Real Estate",
    "local_title": "Buying in {city}: what to know", "aside_title": "Buying in {city}?",
    "shared_faqs": [("Can I search {city} listings without signing up?", "Yes. Search homes and land on the Midlands MLS on this site with no sign-up, then call or text (803) 309-9521 about anything you'd like to see.")],
    "services_listed": 5,
    "pages": AREAS,
  },
  "resource": {
    "enabled": True, "slug": "land-buying-checklist-south-carolina", "nav_label": "Land Checklist",
    "title": "Land Buying Checklist for South Carolina Buyers",
    "meta": "Buying land in South Carolina? Check access, easements, utilities, septic, wetlands, flood zones, timber, minerals and what's nearby. A broker's checklist.",
    "h1": "The South Carolina Land Buying Checklist",
    "lead": "What most buyers don't know about buying land is how many things there are to be aware of. Here's the list I walk through with every land buyer, from easements and utilities to timber value and what's next door.",
    "cards": LAND_CHECKLIST, "body_html": LAND_BODY, "faq_title": "Land buying questions",
    "faqs": [("What should I check before buying land in South Carolina?", "Access and easements, utilities or whether the land will support a septic system and well, topography and soils, wetlands and flood zones, timber and mineral rights, what's around the property, and where values are headed."),
             ("Does raw land always need a septic evaluation?", "If you plan to build and public sewer isn't available, you'll need to know the soil can support a septic system. Find out before you're committed, not after."),
             ("Do timber and mineral rights come with the land?", "Not always. Timber and mineral rights can be sold or reserved separately, so confirm what conveys with the sale in the contract and title work.")],
    "cta_title": "Looking at a tract right now?", "cta_text": "Call or text before you commit. I'll help you check what the listing doesn't tell you, anywhere in South Carolina.",
  },
  "search": SEARCH,
  "about": {"title": "About Barry Keith | Harvest Moon Realty, Lexington SC",
    "meta": "Meet Barry Keith of Harvest Moon Realty: investing in SC real estate since 1989, licensed since 2003, helping home and land buyers in Lexington, SC.",
    "h1": "Meet Barry Keith",
    "lead": "Real estate investor since 1989, licensed agent since 2003, and the broker behind Harvest Moon Realty in Lexington, SC.",
    "story_title": "Been around the block a time or two",
    "story_html": "<p>I started investing in South Carolina real estate in 1989 and became a licensed agent in 2003. I've seen a lot of markets and a lot of houses, and I know the things to look for.</p>"
                  "<p>My two favorite kinds of clients are first-time home buyers and land buyers. I love to hold a first-time buyer's hand from start to finish and help them understand a process that can be overwhelming. And I love land deals because I get to see God's wonderful creation while I'm working.</p>"
                  "<p>At this point in my career, I rely heavily on repeat business and referrals. That only happens when people feel taken care of, so that's how I work: low-pressure, honest, and on your side. <strong>I'm going to stick up for you, but I'm going to do it while being professional and respectful to everyone involved.</strong></p>",
    "photo": {"file": "photos/barry-keith-and-wife.webp", "alt": "Barry Keith of Harvest Moon Realty with his wife, Beth", "caption": "Barry Keith and his wife, Beth", "w": 480, "h": 480},
    "list_title": "How I work",
    "list": ["Low-pressure, always", "I'll point out the pitfalls and the advantages I see", "Your best interest first, start to finish", "Homes in Lexington & Richland counties, land statewide", "Member of the Consolidated MLS (Midlands MLS)", "SC real estate license #43236 · Harvest Moon Realty"]},
  "contact": {"title": "Contact Barry Keith | Harvest Moon Realty, Lexington SC",
    "meta": "Call or text Barry Keith at (803) 309-9521, or send a note. Buying a home, buying land or selling in Lexington, Columbia or anywhere in SC. No pressure.",
    "h1": "Let's Talk",
    "lead": "Buying, selling, or just have a question? Send a quick note or call or text (803) 309-9521. There's no pressure and no obligation, and you don't need to fill this out to search listings.",
    "message_label": "What are you looking for? (home or land, area, budget, timing)",
    "submit": "Send to Barry", "note": "No pressure, no obligation. Barry will reply personally.",
    "success": "Thanks! Barry got your note and will reach out personally.",
    "next_steps": ["Barry replies personally", "A no-pressure conversation about what you want", "Showings or land visits when you're ready"],
    "faqs": GENERAL_FAQS[:3], "page_type": "ContactPage"},
  "reviews": REVIEWS,
  "faqs": GENERAL_FAQS,
  "legal_pages": [("privacy", "Privacy Policy")],
  "redirects": [],
}
