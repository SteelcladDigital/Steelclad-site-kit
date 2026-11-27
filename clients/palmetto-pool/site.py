"""Palmetto Pool Solutions — client config for Steelclad Site Kit.
Service-area business (no storefront). Build: python3 build.py palmetto-pool"""

# ---------------------------------------------------------------- PLANS
# NOTE: plan names/inclusions are a PROPOSAL built from services already on the
# current site. Confirm with Mike before launch. Prices intentionally omitted.
PLANS = [
    {
        "slug": "balance",
        "why": "You enjoy cleaning the pool yourself. Balance puts the chemistry in a CPO-certified pro's hands so the water stays safe and clear between your own skimming and vacuuming.",
        "name": "Balance",
        "tag": "Chemistry only",
        "for": "You like to skim and vacuum yourself, but want the water chemistry handled by a CPO-certified pro.",
        "items": [
            "Weekly water test & chemical balancing",
            "Skimmer & pump baskets emptied",
            "Quick look at pump, filter & equipment",
            "Door-hanger visit report every week",
        ],
    },
    {
        "slug": "full-service",
        "why": "You want a clean, balanced pool every week without doing the work. Full Service covers skimming, brushing, vacuuming, chemistry and equipment checks.",
        "name": "Full Service",
        "tag": "Most popular",
        "featured": True,
        "for": "You want to walk outside and find a clean, balanced pool every week, without lifting a brush.",
        "items": [
            "Everything in Balance, plus:",
            "Surface skimming",
            "Brushing walls, steps & tile line",
            "Vacuuming the floor",
            "Equipment check & small adjustments",
            "Priority scheduling for repairs",
        ],
    },
    {
        "slug": "full-service-plus",
        "why": "Your salt cell or cartridge filter needs scheduled cleaning to last. Full Service Plus builds that preventive work in, along with discounted openings and closings.",
        "name": "Full Service Plus",
        "tag": "Salt & cartridge pools",
        "for": "You have a saltwater system or cartridge filter and want the preventive work built in, not billed later.",
        "items": [
            "Everything in Full Service, plus:",
            "Salt cell cleaning twice a year",
            "Winter dummy-cell swap to protect your cell",
            "Cartridge filter cleaning every 90 days",
            "Discounted seasonal opening & closing",
        ],
    },
]

# ---------------------------------------------------------------- SERVICES
# Slugs match the CURRENT live site so existing rankings and links carry over.
SERVICES = [
    {
        "slug": "weekly-pool-maintenance",
        "name": "Weekly Pool Maintenance",
        "short": "Chemistry, cleaning and equipment checks on the same day every week.",
        "icon": "calendar",
        "title": "Weekly Pool Maintenance in Lexington, SC",
        "meta": "Weekly pool cleaning and chemical balancing in Lexington & Richland County, SC. CPO-certified, flat monthly rate, a visit report after every service.",
        "h1": "Weekly Pool Maintenance in Lexington & Richland County",
        "lead": "Same route day, same checklist, every week. We balance the water, clean the pool and check your equipment. Before we leave, you get a door hanger showing exactly what we did.",
        "included_title": "What happens on every weekly visit",
        "included": [
            ("Test & balance", "Chlorine, pH, alkalinity and stabilizer tested on site and adjusted to the right range for the season."),
            ("Skim & empty baskets", "Leaves, pollen and bugs off the surface; skimmer and pump baskets emptied."),
            ("Brush & vacuum", "Walls, steps and tile line brushed so algae can't get a foothold; floor vacuumed."),
            ("Equipment check", "Pump pressure, filter, heater and salt system looked over so small issues get caught early."),
            ("Deck & water level", "Deck blown off and water level checked. If your pool needs water, the door hanger tells you how many inches to add."),
            ("Door hanger", "Every service checked off on our door hanger, with service comments and the date of your next service, so you never have to wonder if we came."),
        ],
        "photos_title": "The door hanger you'll find after every visit",
        "photos": [{"file": "photos/palmetto-pool-door-hanger.jpg", "alt": "Palmetto Pool Solutions door hanger. Front: checklist of services performed, from water tested and baskets cleaned to pool brushed, vacuumed and chemically balanced. Back: service comments, water to add, date and time, and date of next service.",
                    "w": 896, "h": 1200, "contain": True, "caption": "Our actual door hanger: services checked off on the front, comments and your next service date on the back."}],
        "signs_title": "Weekly service is a good fit if…",
        "signs": [
            "You'd rather spend weekends in the pool than working on it",
            "Your last pool company stopped showing up or calling back",
            "Pollen, pine straw or oak leaves bury your pool every spring",
            "You travel and need the pool handled while you're gone",
        ],
        "faqs": [
            ("How much does weekly pool service cost in Lexington?", "It depends on your pool's size, type (in-ground, above-ground, salt or chlorine), tree cover and equipment. After a free evaluation we quote one flat monthly rate, with no teaser pricing that jumps after month one."),
            ("Do I need to be home for weekly service?", "No. Most customers aren't. We just need gate access and any pets kept inside on your service day. The door hanger tells you what was done."),
            ("Do you service above-ground pools?", "Yes. We care for above-ground pools as well as in-ground pools, including ones other companies turned down."),
        ],
    },
    {
        "slug": "green-to-clean-pool-recovery",
        "name": "Green to Clean Recovery",
        "short": "Algae recovery without draining, for pools that got away from you.",
        "icon": "leaf",
        "title": "Green Pool Cleaning & Algae Removal, Lexington SC",
        "meta": "Green pool? We clear algae without draining your pool in Lexington, Columbia and the Midlands. Most pools recover in 1–7 days. Free evaluation.",
        "h1": "Green Pool Recovery in Lexington & Columbia: No Draining Required",
        "lead": "A green pool is fixable, usually without draining a drop. We kill the algae, clear the water and get your filtration working, then set you up so it doesn't happen again.",
        "included_title": "How we turn a green pool blue",
        "included": [
            ("Assess", "We test the water and check the pump and filter. Most green pools have an equipment problem behind them."),
            ("Shock & treat", "A targeted chemical treatment matched to how heavy the algae is."),
            ("Brush, vacuum & filter", "Dead algae gets brushed loose, vacuumed out and filtered until the water clears."),
            ("Rebalance", "Once it's clear we bring the water back into balance so it stays that way."),
        ],
        "signs_title": "Typical timelines",
        "signs": [
            "Light green or cloudy: about 1–2 days",
            "Medium green, floor not visible: about 2–4 days",
            "Dark green or black \"swamp\": a week or more",
            "Every recovery ends with a plan to keep it from coming back",
        ],
        "faqs": [
            ("Do you have to drain my pool to fix green water?", "Almost never. We recover pools chemically and mechanically. Draining is rarely needed and can risk damage to liners and plaster."),
            ("Why did my pool turn green?", "Usually low chlorine, a filter or pump problem, heavy rain diluting the water, or phosphates from pollen and debris feeding algae. We'll tell you which one it was."),
        ],
    },
    {
        "slug": "specialized-pool-cleaning",
        "name": "Salt Cell & Filter Cleaning",
        "short": "Preventive salt cell and cartridge filter cleaning that extends equipment life.",
        "icon": "sparkle",
        "title": "Salt Cell & Filter Cleaning in Lexington, SC",
        "meta": "Professional salt cell cleaning, winter dummy-cell swaps and cartridge filter cleaning in Lexington & Richland County, SC.",
        "h1": "Salt Cell & Cartridge Filter Cleaning",
        "lead": "Scaled-up salt cells and clogged cartridges are the quiet reason pools go cloudy and equipment wears out early. Cleaning them on a schedule costs far less than replacing them.",
        "included_title": "What we clean and how often",
        "included": [
            ("Salt cell cleaning", "Twice a year, we descale your cell so it keeps making chlorine efficiently."),
            ("Winter dummy cell", "In cold months we swap in a dummy cell to protect your real one when it can't produce anyway."),
            ("Cartridge filter cleaning", "Every 90 days, cartridges are pulled, deep-cleaned and inspected for tears."),
            ("Condition report", "We let you know when a cell or cartridge is near the end of its life, before it fails."),
        ],
        "signs_title": "Signs your cell or filter needs attention",
        "signs": [
            "Salt system shows a \"check cell\" or low-output warning",
            "Filter pressure is 8–10 PSI above its clean reading",
            "Water stays cloudy even with good chemistry",
            "You can't remember the last time it was cleaned",
        ],
        "faqs": [
            ("Is salt cell cleaning included in a maintenance plan?", "It's built into our Full Service Plus plan, along with cartridge cleaning every 90 days. It's also available on its own."),
        ],
    },
    {
        "slug": "pool-pump-filter-repair",
        "name": "Pump & Filter Repair",
        "short": "Honest diagnosis, then repairs or replacement done right.",
        "icon": "wrench",
        "title": "Pool Pump & Filter Repair in Lexington, SC",
        "meta": "Pool pump not running? Filter leaking or losing pressure? Fast, honest pump and filter diagnosis and repair in Lexington & Columbia, SC.",
        "h1": "Pool Pump & Filter Repair in Lexington & Columbia",
        "lead": "When the pump quits, the clock starts on a green pool. We diagnose the real problem, explain your options in plain English, and quote it before we start.",
        "included_title": "What we fix",
        "included": [
            ("Pumps", "Won't prime, loud bearings, leaking seals, motor won't start or trips the breaker."),
            ("Filters", "Cartridge, sand and DE filters: leaks, high pressure, broken laterals or grids."),
            ("Plumbing at the pad", "Valves, unions and small leaks around your equipment."),
            ("Replace vs. repair", "If replacing makes more sense, we'll show you why, and what it saves."),
        ],
        "signs_title": "Call us if you notice",
        "signs": [
            "Screeching, grinding or humming from the pump",
            "Water leaking around the pump or filter",
            "Pressure gauge reading much higher or lower than normal",
            "Air bubbles blowing out of the return jets",
        ],
        "faqs": [
            ("Do I have to be a weekly customer to get a repair?", "No, but weekly customers get priority scheduling. Most pump and filter problems we see on routes get caught before they turn into emergencies."),
        ],
    },
    {
        "slug": "pool-equipment-upgrades",
        "name": "Equipment Upgrades",
        "short": "Variable-speed pumps, saltwater conversions and energy-saving upgrades.",
        "icon": "bolt",
        "title": "Variable-Speed Pumps & Salt Conversions, Lexington SC",
        "meta": "Lower your pool's power bill with a variable-speed pump, or convert to saltwater. Pool equipment upgrades in Lexington & Richland County, SC.",
        "h1": "Pool Equipment Upgrades: Variable-Speed Pumps & Salt Conversions",
        "lead": "An old single-speed pump can be one of the biggest power draws at your house. A variable-speed pump can save roughly $300–$800 or more a year. A saltwater conversion means far fewer chlorine runs.",
        "included_title": "Upgrades we install",
        "included": [
            ("Variable-speed pumps", "Run slower and longer for the same filtration at a fraction of the power."),
            ("Saltwater conversions", "Your pool makes its own chlorine; softer-feeling water and fewer jugs to haul."),
            ("Energy-efficient equipment", "Right-sized filters and automation that match how you actually use the pool."),
            ("Straight-talk recommendations", "If an upgrade won't pay off for your pool, we'll say so."),
        ],
        "signs_title": "Worth considering if…",
        "signs": [
            "Your pump is single-speed and more than a few years old",
            "Your summer power bill jumps when the pool opens",
            "You're tired of buying and storing chlorine",
            "Your equipment is failing anyway and needs replacement",
        ],
        "faqs": [
            ("How much can a variable-speed pump save?", "It depends on your current pump, run time and power rates. Many pool owners save roughly $300–$800 or more a year. We'll estimate it for your setup during the evaluation."),
        ],
    },
    {
        "slug": "pool-liner-repair",
        "name": "Liner Repair & Replacement",
        "short": "Honest assessment, then the right specialist for the job.",
        "icon": "search",
        "title": "Pool Liner Repair & Replacement in Lexington, SC",
        "meta": "Torn, faded or leaking vinyl pool liner? We assess it honestly and connect you with trusted liner specialists in the Midlands.",
        "h1": "Pool Liner Repair & Replacement",
        "lead": "Liners are specialty work, so we don't pretend otherwise. We assess the damage, tell you whether it's a patch or a replacement, and connect you with a liner specialist we trust.",
        "included_title": "How it works",
        "included": [
            ("Assessment", "We check for tears, wrinkles, fading and leaks during a visit."),
            ("Patch when possible", "Small tears and punctures can often be patched, even underwater."),
            ("Specialist referral", "For replacements, we refer you to a specialist we'd use on our own pool."),
            ("Water care after", "New liners need careful chemistry early on. We handle that part."),
        ],
        "signs_title": "Signs of a liner problem",
        "signs": [
            "Water level dropping faster than evaporation",
            "Wrinkles, bulges or liner pulling from the track",
            "Faded, brittle or stained vinyl",
            "Visible tears or punctures",
        ],
        "faqs": [],
    },
    {
        "slug": "pool-surface-gunite-repair",
        "name": "Surface & Gunite Repair",
        "short": "Plaster and gunite assessment with trusted resurfacing referrals.",
        "icon": "layers",
        "title": "Pool Surface & Gunite Repair in Lexington, SC",
        "meta": "Rough, stained or cracking pool plaster? We assess pool surfaces and connect you with trusted resurfacing specialists in Lexington & Columbia, SC.",
        "h1": "Pool Surface & Gunite Repair",
        "lead": "Rough plaster, stains and cracks often start with water chemistry. We figure out the cause, protect the surface you have, and bring in a resurfacing specialist when it's time.",
        "included_title": "How we help",
        "included": [
            ("Surface assessment", "Stains, etching, roughness and cracks identified and explained."),
            ("Chemistry that protects", "Balanced water slows etching and scaling on plaster and gunite."),
            ("Resurfacing referral", "When it's time, we connect you with specialists we trust."),
            ("Start-up care", "Fresh plaster needs careful start-up chemistry. We can handle it."),
        ],
        "signs_title": "Signs your surface needs attention",
        "signs": [
            "Rough spots that snag swimsuits or scrape feet",
            "Brown, green or chalky stains that won't brush off",
            "Visible cracks or hollow-sounding areas",
            "Plaster that's more than 10–15 years old",
        ],
        "faqs": [],
    },
]

# ---------------------------------------------------------------- AREAS
# Existing slugs kept: lexington, columbia, irmo, chapin, west-columbia.
# New pages added: cayce, forest-acres, blythewood.
AREAS = [
    {
        "slug": "pool-service-lexington-sc", "city": "Lexington", "county": "Lexington County",
        "zips": "29072, 29073", "existing": True,
        "intro": "Lexington is home. We grew up here, our routes start here, and most of our customers are a short drive from the Town Center. If you're anywhere from Red Bank to Lake Murray's south shore, we're probably already in your neighborhood each week.",
        "local": [
            ("Spring pollen is relentless", "Pine and oak pollen coat Lexington pools every March and April. It feeds algae and clogs filters, so we brush and clean filters more often during pollen season."),
            ("Summer storms dilute your water", "Afternoon thunderstorms can drop inches of rain in an hour. We rebalance after heavy rain so a storm doesn't turn into a green pool."),
            ("Long swim season", "Lexington pools are often swimmable from May into October, so consistent weekly care matters more than in places with short summers."),
        ],
        "faqs": [
            ("Do you offer weekly pool service in Lexington, SC?", "Yes. Lexington is our home base, with weekly routes throughout 29072 and 29073. Call or text (803) 394-0765 for a free evaluation."),
        ],
    },
    {
        "slug": "pool-service-gilbert-sc", "city": "Gilbert", "county": "Lexington County",
        "zips": "29054", "existing": False,
        "intro": "Gilbert is peach country, home of the Lexington County Peach Festival every Fourth of July, and a short drive west of Lexington. Plenty of Gilbert pools sit on bigger, wooded or rural lots, and they're on our weekly Lexington County routes just like pools in town.",
        "local": [
            ("Bigger lots, more debris", "Wooded and rural lots mean pine straw, leaves and heavy spring pollen. Weekly skimming, basket cleaning and brushing keep it from feeding algae."),
            ("Topping off from a well?", "Well water can carry iron and other metals that stain plaster and tint the water. Tell us at your evaluation and we'll test for it before it becomes a stain."),
            ("Same service as in town", "Gilbert customers get the same route day, flat monthly rate and door hanger after every visit as our Lexington customers."),
        ],
        "faqs": [
            ("Do you offer pool service in Gilbert, SC?", "Yes. Gilbert (29054) is part of our Lexington County service area, with weekly routes, green-to-clean recovery and pump and filter repair."),
        ],
    },
    {
        "slug": "pool-service-batesburg-leesville-sc", "city": "Batesburg-Leesville", "county": "Lexington County",
        "zips": "29006, 29070", "existing": False,
        "intro": "Batesburg-Leesville sits at the western edge of Lexington County, a long way from most pool companies' routes. It isn't too far for us: we're a Lexington County family business, and the whole county is our service area.",
        "local": [
            ("Weekly service out west", "The same weekly checklist, flat monthly rate and door hanger our customers in Lexington get, without having to beg someone to drive out."),
            ("Well water and older equipment", "Many homes here fill from a well, and many pools have seen a lot of seasons. We test for metals and keep an eye on aging pumps and filters on every visit."),
            ("Green pool? No draining", "Pools that sat unused come back with our Green to Clean recovery, usually without draining a drop."),
        ],
        "faqs": [
            ("Do you service pools in Batesburg-Leesville?", "Yes. Batesburg-Leesville (29006 and 29070) is part of our Lexington County service area. Call or text (803) 394-0765 to get on a route."),
        ],
    },
    {
        "slug": "pool-service-columbia-sc", "city": "Columbia", "county": "Richland County",
        "zips": "29201–29229", "existing": True,
        "intro": "Columbia didn't get the nickname \"Famously Hot\" by accident. Long, steamy summers burn through chlorine fast, and many pools in established neighborhoods like Shandon, Rosewood and Northeast Columbia run on equipment that's seen a lot of seasons.",
        "local": [
            ("Heat burns off chlorine", "When water temperatures climb into the upper 80s, chlorine demand jumps. Weekly testing keeps you ahead of the algae that loves warm water."),
            ("Older equipment, older pools", "Many in-town pools have aging pumps and filters. Our weekly equipment check catches leaks and failing motors before they strand you mid-July."),
            ("Mature trees", "Leafy neighborhoods mean full skimmer baskets and more brushing, which our weekly visit covers."),
        ],
        "faqs": [
            ("Do you service pools inside Columbia city limits?", "Yes. We service Columbia and the surrounding Richland County communities, including Forest Acres and Northeast Columbia."),
        ],
    },
    {
        "slug": "pool-service-irmo-sc", "city": "Irmo", "county": "Lexington & Richland Counties",
        "zips": "29063", "existing": True,
        "intro": "Irmo sits right where Lexington and Richland counties meet, between Lake Murray and the Harbison area. We run routes through Irmo every week and serve pools on both sides of the county line.",
        "local": [
            ("Two counties, one route", "Whether your address says Lexington or Richland County, we come out on the same weekly schedule."),
            ("Lake-area debris", "Homes near the lake and wooded lots see heavy leaf and pollen loads. We plan our brushing and filter cleaning around them."),
            ("Busy family pools", "Lots of Irmo pools see heavy summer use, which means higher chlorine demand. Weekly balancing keeps the water comfortable and safe."),
        ],
        "faqs": [
            ("Is Irmo in your service area?", "Yes. Irmo (29063) is on our weekly routes, including neighborhoods toward Lake Murray and Harbison."),
        ],
    },
    {
        "slug": "pool-service-chapin-sc", "city": "Chapin", "county": "Lexington County",
        "zips": "29036", "existing": True,
        "intro": "They call Chapin the Capital of Lake Murray, and plenty of Chapin pools belong to lake homes and weekend places. These pools need care whether or not anyone's there to see them.",
        "local": [
            ("Second homes and lake houses", "If you're only at the lake some weekends, weekly service means the pool is clean when you arrive, not green."),
            ("Openings & closings", "Seasonal opening and closing service, discounted for weekly customers."),
            ("Wooded lots", "Pines and hardwoods around Chapin homes mean pollen in spring and leaves in fall. We plan for both."),
        ],
        "faqs": [
            ("Can you service my Chapin lake house pool while I'm away?", "Yes. Many of our Chapin customers aren't home on service day. Your door hanger and our follow-up let you know everything's handled."),
        ],
    },
    {
        "slug": "pool-service-west-columbia-sc", "city": "West Columbia", "county": "Lexington County",
        "zips": "29169, 29170, 29172", "existing": True,
        "intro": "From neighborhoods near the Congaree River to newer subdivisions out toward Lexington, West Columbia has every kind of pool: older plaster, vinyl, above-ground and brand-new salt systems. We service them all.",
        "local": [
            ("Every pool type", "In-ground, above-ground, plaster, vinyl, salt or chlorine. Our technicians are CPO certified and work on all of them."),
            ("Older pools that need a reset", "Neglected or long-unused pools are common here. Our Green to Clean recovery brings them back without draining."),
            ("Quick to reach", "West Columbia is minutes from our Lexington base, which makes repair calls fast."),
        ],
        "faqs": [
            ("Do you serve all of West Columbia?", "Yes. We cover 29169, 29170 and 29172, including Springdale and the areas along the river."),
        ],
    },
    {
        "slug": "pool-service-cayce-sc", "city": "Cayce", "county": "Lexington County",
        "zips": "29033", "existing": False,
        "intro": "Cayce homeowners get the same weekly routes, flat monthly pricing and door-hanger visit reports as our Lexington customers. We're just across the river from Columbia and a few minutes from home base.",
        "local": [
            ("Established neighborhoods", "Many Cayce pools have been around for decades. Our equipment checks help squeeze more life out of older pumps and filters."),
            ("River-valley humidity", "Hot, humid summers near the Congaree push chlorine demand up. Weekly balancing keeps up with it."),
            ("Straight answers on repairs", "If something's failing, we'll tell you plainly whether to repair or replace."),
        ],
        "faqs": [
            ("Do you offer pool service in Cayce, SC?", "Yes. Cayce (29033) is part of our Lexington County service area with weekly routes."),
        ],
    },
    {
        "slug": "pool-service-forest-acres-sc", "city": "Forest Acres", "county": "Richland County",
        "zips": "29206", "existing": False,
        "intro": "Forest Acres lives up to its name: big, mature trees over nearly every backyard. That shade is beautiful, but it fills pools with leaves, pollen and organic debris that pool owners fight all year.",
        "local": [
            ("Heavy leaf load", "Thorough skimming, basket cleaning and brushing every week are built into Full Service."),
            ("Phosphates from debris", "Decaying leaves feed algae. We watch for it and treat it before the pool turns."),
            ("Filters work harder", "Shaded, leafy pools clog filters faster. Full Service Plus includes cartridge cleaning every 90 days."),
        ],
        "faqs": [
            ("Do you service pools in Forest Acres?", "Yes. Forest Acres (29206) is part of our Richland County service area."),
        ],
    },
    {
        "slug": "pool-service-blythewood-sc", "city": "Blythewood", "county": "Richland County",
        "zips": "29016", "existing": False,
        "intro": "Blythewood keeps growing, and so does the number of new pools in its subdivisions. Many are saltwater systems that need the right care from day one to protect the equipment you just paid for.",
        "local": [
            ("New pool start-ups", "Fresh plaster and new equipment need careful chemistry in the first weeks. We handle start-up balancing."),
            ("Salt systems", "We clean salt cells twice a year and swap in a dummy cell for winter, so your cell lasts."),
            ("Set it and forget it", "Busy families get a flat monthly rate and a visit report every week, with nothing to manage."),
        ],
        "faqs": [
            ("Is Blythewood in your service area?", "Yes. We serve Blythewood (29016) and northeast Richland County. Call or text to confirm your route day."),
        ],
    },
]

# Real reviews from the current site (palmettopoolsolutions.com home and /about), full text.
# All three are Lexington customers. Add Columbia / Irmo / Chapin reviews as Mike collects them (never invent).
REVIEWS = [
    ("Jenn S.", "Lexington, SC", "This has to be the friendliest and best pool service out there. I called several places that wouldn't even service my above ground pool. When I called Mike, he said no problem. My pool has been crystal clear and clean all summer long. In this day and age you can't be too careful who you trust to do service at your house. Mike and his crew have gone above and beyond as far as kind, impeccable quality service. As long as I own my pool, Palmetto Pool Solutions are the only people I will use for my pool!"),
    ("Sherri O.", "Lexington, SC", "Great service and transparency! Mike gave me a quote, showed up on time and communicated with me through the process of replacing our pool pump! Great experience and great guy. Folks that serve with integrity are hard to find sometimes. I will use Mike and Palmetto Pool Solutions again!"),
    ("Traci W.", "Lexington, SC", "OMG Mike is wonderful!! I called him about our pool and even though he was swamped he found a way to fit us in. His communication was amazing and he made sure to follow up to make sure all was good. I strongly recommend him for any pool concerns you might have!!"),
]

GENERAL_FAQS = [
    ("How much does pool service cost?", "Every pool is different: size, type, tree cover and equipment all matter. After a free evaluation we give you one flat monthly rate. No teaser pricing, no surprise fees."),
    ("What's the difference between the plans?", "Balance covers water chemistry only, for people who like to clean their own pool. Full Service adds skimming, brushing, vacuuming and equipment checks. Full Service Plus adds scheduled salt cell and cartridge filter cleaning plus discounted openings and closings."),
    ("Do I need to be home on service day?", "No. We just need gate access and pets secured. You'll find a door hanger checking off everything we did, with any comments and your next service date."),
    ("Are you certified and insured?", "Yes. We're CPO certified (Certified Pool Operator), licensed and fully insured."),
    ("What if I call and you don't answer?", "We answer our phone. If you do hit voicemail, expect a callback within the hour during business hours."),
    ("Do you service above-ground and saltwater pools?", "Yes. In-ground, above-ground, saltwater and chlorine pools are all on our routes."),
]

CALENDAR = [
    ("January–February", "Winter watch", ["Keep the pump running on freezing nights to protect plumbing", "Swap in a dummy salt cell; real cells can't produce in cold water", "Check water level and chemistry every couple of weeks", "Good time to schedule equipment upgrades before the spring rush"]),
    ("March–April", "Pollen season", ["Yellow pine pollen coats everything, so brush and skim often", "Clean filters more frequently; pollen clogs them fast", "Watch phosphates; pollen feeds early-season algae", "Open covered pools before water warms and algae starts"]),
    ("May", "Ramp-up", ["Water temperatures climb, and so does chlorine demand", "Check stabilizer (CYA) levels before peak sun", "Clean the salt cell before summer", "Confirm the pump run time for longer days"]),
    ("June–August", "Peak heat & storms", ["Test and balance weekly at minimum; heat burns off chlorine", "Rebalance after heavy thunderstorms dilute the water", "Run the pump longer; circulation fights algae", "Watch for pump strain on the hottest days"]),
    ("September–October", "Still swimming", ["Midlands pools often stay swimmable into October", "Leaf drop begins, so skimmer baskets fill faster", "Clean the cartridge filter after summer", "Decide on winter care vs. closing"]),
    ("November–December", "Wind-down", ["Close the pool or switch to winter maintenance", "Keep leaves off covers and out of the water", "Protect equipment from the first freezes", "Schedule repairs during the slow season"]),
]


# Logo: the real logo (assets/logo.png is a white knockout cut from Mike's JPG, so it sits on any navy).


PLANS_FAQS = GENERAL_FAQS[:3] + [
    ("Are chemicals included in the monthly rate?", "Your evaluation quote spells out exactly what's included, so there are no surprise chemical charges on your bill."),
    ("Can I switch plans later?", "Yes. If your needs change, like adding a salt system or wanting us to take over the cleaning, just call or text and we'll move you to the plan that fits."),
    ("Do you offer service year-round?", "Yes. Midlands pools are often swimmable from May into October, and we offer winter care as well as seasonal openings and closings."),
]

CONFIG = {
  "business": {
    "name": "Palmetto Pool Solutions", "legal_name": "Palmetto Pool Solutions, LLC",
    "domain": "https://palmettopoolsolutions.com",
    "phone": "(803) 394-0765", "tel": "+18033940765", "email": "palmettopoolsolutions@gmail.com",
    "schema_type": ["LocalBusiness", "HomeAndConstructionBusiness"],
    "description": "Family-owned in Lexington County, SC. CPO-certified weekly pool service, green pool recovery, pump and filter repair and equipment upgrades for homeowners in Lexington and Richland counties.",
    "address": {"locality": "Lexington", "region": "SC"},   # service-area business: no street (the street is only in the Terms contact block)
    "geo": (33.9815, -81.2362),
    "hours": [(["Monday","Tuesday","Wednesday","Thursday","Friday"], "08:00", "17:00")],
    "hours_text": "Mon–Fri 8:00 AM – 5:00 PM",
    "counties": ["Lexington County, SC", "Richland County, SC"],
    "founder": "Mike Brazell",
    "knows_about": ["Pool maintenance", "Pool water chemistry", "Salt chlorine generators", "Green pool recovery", "Variable-speed pool pumps"],
    "social": {"facebook": "https://www.facebook.com/palmettopoolsolutionsllc", "instagram": "https://www.instagram.com/palmettopoolsolutions/"},
  },
  "theme": {
    # primary = the navy sampled from Mike's own logo (#1b227d), so the header and logo read as one piece.
    "colors": {"primary": "#1b227d", "primary_deep": "#11165a", "secondary": "#27b3c2", "secondary_deep": "#0f7f8c",
               "secondary_wash": "#e3f6f8", "accent": "#f3b53f", "accent_text": "#11165a", "surface": "#f7f2e9"},
    "fonts": {"display": "oswald", "body": "inter"},   # Oswald echoes the condensed capitals of his logo
    "radius": "soft", "heading_case": "none", "divider": "wave", "texture": "ripples", "hero_layout": "card",
  },
  "logo": {"type": "image", "file": "logo.png", "width": 114, "height": 60, "schema_file": "logo-schema.jpg"},
  "favicon_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#1b227d"/><path d="M16 29c.5-6 .5-11-.3-16" stroke="#fff" stroke-width="2.4" fill="none"/><path d="M15.7 13c-3-3-7-3-10-1M15.7 13c-1-4-4-6-7-6M15.7 13c2-4 5-6 9-6M15.7 13c3-2 7-2 10 1" stroke="#fff" stroke-width="1.6" fill="none" stroke-linecap="round"/><path d="M24 3a4.5 4.5 0 1 0 3 8 3.6 3.6 0 1 1-3-8z" fill="#fff"/></svg>',
  "og_image": "og-image.jpg",        # real photo of Mike with the company banner, 1200x630
  "integrations": {
    "form_mode": "web3forms",
    "web3forms_access_key": "e088f1a2-f364-4726-a392-3e348ce9e112",   # created with palmettopoolsolutions@gmail.com (public by design)
    "web3forms_subject": "New pool evaluation request from palmettopoolsolutions.com",
    "web3forms_from_name": "Palmetto Pool Solutions website",
    "thank_you_slug": "thank-you",
    "gtm_id": "GTM-K3752MP5",          # Mike's OWN Tag Manager account; GA4 + generate_lead tags live inside it
    "google_review_write_url": "https://g.page/r/CSSJuhDXidrPEBM/review",   # Mike's GBP review link: "★★★★★ Leave us a Google review" button + footer link
  },
  "launched": False,                 # set True only after Mike approves and --check is clean; launch blockers then STOP the build
  "labels": {
    "cta": "Free Pool Evaluation", "cta_short": "Free Evaluation", "cta_long": "Get a Free Pool Evaluation",
    "phone_prefix": "Call or text", "topbar_promise": "Family-owned in Lexington County. We answer our phone, and missed calls get a callback within the hour.",
    "footer_blurb": "Family-owned in Lexington County, SC. CPO-certified pool care for homeowners across Lexington & Richland counties. Licensed and fully insured.",
    "footer_services_title": "Plans & Services",
    "reviews_title": "What our Lexington County neighbors are saying",
    "cta_band_title": "Ready to stop thinking about your pool?",
    "cta_band_text": "Call or text Mike's team, and we'll set up a free pool evaluation. You'll get an honest look at your pool and one flat monthly number.",
    "aside_title": "Get a free pool evaluation", "aside_text": "We answer our phone. If we miss you, we call back within the hour.",
    "aside_badges": "✓ Family-owned in Lexington County · ✓ CPO certified · ✓ Licensed & insured",
  },
  "home": {
    "title": "Weekly Pool Service & Maintenance Plans in Lexington, SC",
    "meta": "Family-owned weekly pool service in Lexington & Richland counties, SC. CPO certified, flat monthly rate, visit report every week. (803) 394-0765",
    "eyebrow": "Family-owned in Lexington County, SC",
    "h1": "Weekly pool service for Lexington homeowners who are <em>done</em> chasing their pool company",
    "lead": "Lifelong Lexington County locals caring for pools across Lexington and Richland counties. One flat monthly rate, the same route day every week, and a visit report on your door after every service.",
    "secondary_cta": ("Compare Plans", "pool-maintenance-plans"),
    "proof": ["Serving Lexington & Richland counties", "Above-ground & in-ground", "Salt & chlorine pools"],
    "hero_owner": {"photo": "photos/mike-brazell-avatar.jpg", "alt": "Mike Brazell, owner of Palmetto Pool Solutions",
                   "name": "Mike Brazell, owner", "text": "CPO certified · Lifelong Lexington County resident"},
    # Mirrors Mike's real door hanger (assets/photos/palmetto-pool-door-hanger.jpg): checklist front, comments + next service on the back.
    "hero_card": {"label": "Door hanger", "title": "We performed the following services on your pool", "sub": "Left on your door after every visit", "badge": "Example", "hanger": True,
                  "checks": ["Water tested", "Water level", "Baskets cleaned", "Deck blown off", "Equipment checked", "Filter cleaned", "Brushed & vacuumed", "Water balanced"],
                  "note": "Service comments: \"Pine pollen heavy this week, cleaned the filter.\" Date of next service: next Tuesday.",
                  "link": ("See our actual door hanger", "services/weekly-pool-maintenance", "#photos")},   # hero_card.link: (label, slug, optional #anchor)
    "trust": [("home", "Family-Owned", "Lexington County, SC"), ("badge", "CPO Certified", "Certified Pool Operator"),
              ("shield", "Licensed & Insured", "Fully covered, every visit"), ("phone", "We Answer", "Callback within the hour")],
    # Mike's own words, from the current /about page.
    "owner": {"eyebrow": "Meet the owner", "title": "Hi, I'm Mike Brazell.",
              "photo": {"file": "photos/mike-brazell-owner-lexington-parade.jpg", "alt": "Mike Brazell, owner of Palmetto Pool Solutions, standing beside the company's parade float and banner",
                        "w": 600, "h": 760, "caption": "Mike with the Palmetto Pool Solutions float"},
              "story_html": "<p>I'm the owner of Palmetto Pool Solutions and a lifelong Lexington County resident.</p><p>I started this company because I kept hearing the same story from homeowners across Lexington and Richland counties: they'd hire a pool company, pay on time, and then wonder if anyone was actually coming. No callbacks. No documentation. No accountability.</p><p>So I made one simple commitment: every pool we service gets treated like it's our own. Like our kids are swimming in it. That means showing up on the same day every week, leaving a door hanger after every visit, and answering the phone. If we miss your call, we call you right back.</p>",
              "signature": "Mike Brazell", "signature_role": "Owner · Certified Pool Operator (CPO)",
              "links": [("Get a free pool evaluation", "contact"), ("Read our story", "about")]},
    "why": {"eyebrow": "Why we exist",
            "quote_html": "No-shows. Vague pricing. Wondering if anyone actually came by. <em>That's not how pool service should work.</em>",
            "body": "You're not asking for much. You want a pool that's clean, safe and ready whenever you are. So we built our whole service around the things other pool companies skip.",
            "items": [("phone", "We answer our phone.", "Call or text and we pick up. Hit voicemail? Expect a callback within the hour."),
                      ("doc", "We document every visit.", "A door hanger checking off every service we performed, with comments and your next service date. Every single time."),
                      ("calendar", "We show up on schedule.", "Same route day each week, with standardized checklists and random quality checks."),
                      ("home", "We're your neighbor, not a franchise.", "No 1-800 number and no call center. You talk to people who live here and know Midlands pools season by season.")]},
    "cards": {"eyebrow": "Built for Midlands pools", "title": "What your pool is up against in Lexington & Columbia",
              "lead": "Pools here fight the same four things every year. Our weekly routes are planned around them.",
              "items": [("leaf", "Spring pine pollen", "Yellow pollen coats pools every March and April, clogs filters and feeds early algae. We brush and clean filters more often in pollen season.", ("Midlands pool care calendar", "pool-care-calendar")),
                        ("drop", "Summer thunderstorms", "An afternoon storm can drop inches of rain in an hour and dilute your chlorine. We rebalance after heavy rain so a storm doesn't turn into a green pool.", ("Why storms cloud your pool", "post/why-is-my-pool-water-cloudy-lexington-sc")),
                        ("thermo", "\"Famously Hot\" August", "Water in the upper 80s burns through chlorine. Weekly testing keeps you ahead of the algae that loves warm water.", ("August pool care", "post/august-pool-care-lexington-sc")),
                        ("calendar", "A long swim season", "Midlands pools often stay swimmable into October, so closing too early is a common mistake. We'll help you pick the right week.", ("When to close your pool", "post/when-to-close-pool-lexington-sc"))]},
    "steps": {"eyebrow": "Getting started", "title": "From first call to swimming in about 10 minutes of your time",
              "items": [("Call or text", "(803) 394-0765. We answer, or call back within the hour."),
                        ("Free pool evaluation", "We inspect your pool and equipment and tell you exactly what we see. No pressure, no jargon."),
                        ("Pick your plan", "One flat monthly number based on your actual pool. No surprise fees."),
                        ("Enjoy your pool", "We handle the rest. You'll find the visit report on your door.")]},
    "order": ["trust", "owner", "tiers", "why", "reviews", "cards", "steps", "services", "areas", "quiz", "blog", "faq", "cta"],
  },
  "tiers": {
    "enabled": True, "slug": "pool-maintenance-plans", "nav_label": "Maintenance Plans",
    "title": "Pool Maintenance Plans in Lexington & Columbia, SC",
    "meta": "Compare weekly pool maintenance plans in Lexington & Richland County, SC: Balance, Full Service and Full Service Plus. Flat monthly rate, free evaluation.",
    "h1": "Pool Maintenance Plans in Lexington &amp; Columbia, SC",
    "lead": "Three clear plans, one flat monthly rate, and a visit report every week. Pick how much you want us to handle and we'll take care of the rest.",
    "home_title": "Pick the level of care that fits how you use your pool",
    "home_lead": "Every plan includes weekly visits, CPO-certified water chemistry and a visit report. You choose how much else we handle.",
    "price_label": "One flat monthly rate", "price_note": "Quoted after your free pool evaluation. No teaser pricing.",
    "card_cta": "Get my {name} quote",
    "items": PLANS,
    "compare_lead": "Every plan comes with a CPO-certified technician, the same route day each week and a door-hanger visit report.",
    "compare": [
        ("Weekly water test & chemical balancing", 1, 1, 1), ("Skimmer & pump baskets emptied", 1, 1, 1), ("Door-hanger visit report", 1, 1, 1),
        ("Surface skimming", 0, 1, 1), ("Brush walls, steps & tile line", 0, 1, 1), ("Vacuum pool floor", 0, 1, 1),
        ("Equipment check & small adjustments", "Quick look", 1, 1), ("Priority repair scheduling", 0, 1, 1),
        ("Salt cell cleaning (2× per year)", 0, 0, 1), ("Winter dummy-cell swap", 0, 0, 1),
        ("Cartridge filter cleaning (every 90 days)", 0, 0, 1), ("Discounted opening & closing", 0, 0, 1)],
    "quiz": {"eyebrow": "Plan finder", "title": "Not sure which plan? Answer two questions.",
             "questions": [{"q": "How hands-on do you want to be?", "options": [("Handle everything for me", "full-service"), ("I'll clean, you do the chemistry", "balance")]},
                           {"q": "What kind of system does your pool have?", "options": [("Saltwater", "full-service-plus"), ("Chlorine + cartridge filter", "full-service-plus"), ("Chlorine + sand/DE filter", "full-service"), ("Not sure", "full-service")]}]},
    "pricing_explainer": {"title": "How our pricing works",
        "body_html": "<p>Pool service pricing varies with pool size, type (in-ground or above-ground, salt or chlorine), tree cover and the age of your equipment. A pool under three pines needs more work than one in an open yard.</p><p>So we start with a <strong>free pool evaluation</strong>. We look at your pool and equipment, then give you <strong>one flat monthly number</strong>. That's what you pay, every month. No teaser rates that spike after month one, and no surprise fees.</p>",
        "factors_title": "What affects your monthly rate",
        "factors": ["Pool size and gallons", "In-ground or above-ground", "Saltwater or traditional chlorine", "Filter type (cartridge, sand or DE)", "Trees and debris load", "Equipment age and condition"]},
    "faqs": PLANS_FAQS,
  },
  "services_hub": {"slug": "services", "nav_label": "Services", "title": "Pool Services in Lexington & Columbia, SC",
    "meta": "Pool cleaning, weekly maintenance, green pool recovery, pump & filter repair and equipment upgrades in Lexington & Richland County, SC.",
    "h1": "Pool Services in Lexington &amp; Richland County",
    "lead": "Weekly maintenance, green pool recovery, pump and filter repair, salt cell care and equipment upgrades, all from one CPO-certified local team.",
    "home_count": 6, "home_title": "Full-service residential pool care", "home_lead": "From routine weekly maintenance to emergency green pool recovery, we've got your pool covered all year."},
  "services": SERVICES,
  "areas": {
    "enabled": True, "hub_slug": "service-areas", "nav_label": "Service Areas", "link_prefix": "Pool Service",
    "hub_title": "Pool Service Areas: Lexington & Richland County", "hub_meta": "Weekly pool service across Lexington County (Lexington, Chapin, Irmo, Gilbert, Batesburg-Leesville and more) plus Columbia, Forest Acres and Blythewood.",
    "hub_h1": "Pool Service Areas in Lexington &amp; Richland County", "hub_lead": "Family-owned in Lexington County, with weekly routes across both counties: from Batesburg-Leesville, Gilbert and Chapin to Columbia, Forest Acres and Blythewood.",
    "home_title": "Proudly serving Lexington & Richland counties",
    "groups": [{"name": "Lexington County", "note": "Home base", "slugs": ["pool-service-lexington-sc", "pool-service-chapin-sc", "pool-service-west-columbia-sc", "pool-service-cayce-sc", "pool-service-irmo-sc", "pool-service-gilbert-sc", "pool-service-batesburg-leesville-sc"],
                "also": ["Swansea", "Pelion", "Gaston", "Pine Ridge", "South Congaree", "Springdale", "Summit", "Red Bank", "Oak Grove", "Seven Oaks"], "also_tail": " and every other community in Lexington County."},
               {"name": "Richland County", "note": "Weekly routes", "slugs": ["pool-service-columbia-sc", "pool-service-forest-acres-sc", "pool-service-blythewood-sc", "pool-service-irmo-sc"]}],
    "footer_slugs": ["pool-service-lexington-sc", "pool-service-columbia-sc", "pool-service-irmo-sc", "pool-service-chapin-sc", "pool-service-west-columbia-sc"],   # compact footer: no keyword-stuffed city list
    "footer_note": "All of Lexington County, plus Columbia and nearby Richland County.",
    "outside_note": "Anywhere in Lexington County is in our service area. In Richland County or near a county line? Call or text; our routes may run right past you.",
    "service_where_text": "We serve homeowners throughout Lexington and Richland counties, including",
    "page_title": "Pool Service & Maintenance Plans in {city}, {region}",
    "page_meta": "Weekly pool cleaning & maintenance plans in {city}, {region}. CPO-certified, family-owned, flat monthly rate. Call or text (803) 394-0765.",
    "page_h1": "Pool Service &amp; Maintenance Plans in {city}, {region}",
    "local_title": "Pool care in {city}: what's different here", "aside_title": "Pool service in {city}",
    "tiers_blurb_html": "Choose <strong>Balance</strong> if you like cleaning your own pool and want the chemistry handled, <strong>Full Service</strong> if you want us to do it all, or <strong>Full Service Plus</strong> for saltwater and cartridge-filter pools that need scheduled preventive care.",
    "shared_faqs": [("How much is pool service in {city}?", "Every pool is different, so we start with a free evaluation and quote one flat monthly rate. No teaser pricing, no surprise fees.")],
    "pages": AREAS,
  },
  "resource": {
    "enabled": True, "slug": "pool-care-calendar", "nav_label": "Pool Care Calendar",
    "title": "Midlands Pool Care Calendar: Lexington & Columbia, SC",
    "meta": "When to open, how to handle pollen season, storms and summer heat, and how to winterize a pool in Lexington, Columbia and the South Carolina Midlands.",
    "h1": "The Midlands Pool Care Calendar", "lead": "A month-by-month guide to pool care in Lexington, Columbia and the rest of the Midlands, from pollen season to peak heat to winter.",
    "cards": CALENDAR, "faq_title": "Seasonal pool care questions",
    "faqs": [("When should I open my pool in the Midlands?", "Most Lexington and Columbia pool owners open in March or April, before water warms and algae starts, and ideally before peak pollen season."),
             ("Should I close my pool for winter in South Carolina?", "Many Midlands owners run a winter maintenance routine instead of a full closing, since winters are mild. Either way, protect equipment on freezing nights and swap in a dummy salt cell."),
             ("Why does my pool turn green after a storm?", "Heavy summer rain dilutes chlorine and washes in debris and phosphates. Test and rebalance after big storms.")],
    "cta_title": "Rather not keep track of all this?", "cta_text": "Every item on this calendar is built into our maintenance plans. We'll handle the season, and you just swim.",
  },
  "blog": {
    "enabled": True, "index_slug": "blog", "post_prefix": "post",   # keeps the old site's URLs: /blog and /post/<slug>
    "category_prefix": "posts/category",                           # keeps /posts/category/<slug> archive URLs as real pages
    "categories": {
        "Pool Maintenance Tips": {"slug": "pool-maintenance-tips", "h1": "Pool Maintenance Tips for Lexington, SC", "lead": "Weekly, monthly and seasonal pool care advice from a CPO-certified, family-owned Lexington County team."},
        "Lexington, SC Pool Care": {"slug": "lexington-sc-pool-care", "h1": "Lexington, SC Pool Care", "lead": "Pool care written for Lexington and the Midlands: our pollen, our storms, our long swim season."},
        "Pool Problems & Fixes": {"slug": "pool-problems-fixes", "h1": "Pool Problems & Fixes", "lead": "Cloudy water, green water and other common pool problems, and how to fix them."},
        "Seasonal Pool Care": {"slug": "seasonal-pool-care", "h1": "Seasonal Pool Care in the Midlands", "lead": "Opening, closing and everything in between, timed for South Carolina seasons."},
        "Pool Equipment": {"slug": "pool-equipment", "h1": "Pool Equipment Advice", "lead": "Pumps, filters and salt systems: warning signs, repair-or-replace and how to make equipment last."},
    },
    "nav_label": "Blog", "title": "Pool Care Tips for Lexington, SC Homeowners",
    "meta": "Pool care tips for Lexington & Richland County, SC homeowners from Mike Brazell and the family-owned, CPO-certified Palmetto Pool Solutions team.",
    "h1": "Pool care tips &amp; advice for Lexington, SC homeowners",
    "lead": "Practical advice for Midlands pools, from pollen season to closing time, written by a family-owned Lexington County pool team.",
    "default_author": "Palmetto Pool Solutions", "home_title": "Pool care tips from our team",
    "area_related_title": "Pool care tips for {city} homeowners",
  },
  "about": {"title": "About Mike Brazell & Palmetto Pool Solutions, Lexington SC",
    "meta": "Meet Mike Brazell, lifelong Lexington County resident and owner of family-owned, CPO-certified Palmetto Pool Solutions. We answer our phone.",
    "h1": "Family-Owned Pool Service in Lexington County, SC", "lead": "Palmetto Pool Solutions is owned by Mike Brazell, a lifelong Lexington County resident. It's built on a simple idea: answer the phone, show up, and do what we said we'd do. Every time.",
    "story_title": "Hi, I'm Mike Brazell",
    # Mike's own words from the current /about page.
    "story_html": "<p>I'm the owner of Palmetto Pool Solutions and a lifelong Lexington County resident.</p><p>I started this company because I kept hearing the same story from homeowners across Lexington and Richland counties: they'd hire a pool company, pay on time, and then wonder if anyone was actually coming. No callbacks. No documentation. No accountability. Just a pool that may or may not be safe.</p><p>I knew there was a better way, and that's exactly what Palmetto Pool Solutions was built to be.</p><h3>The Palmetto Pool difference</h3><p>I've lived in Lexington County my whole life. I know the neighborhoods, the summers, and the kind of Southern hospitality that means you actually do what you say you're going to do.</p><p>When I started Palmetto Pool Solutions, I made one simple commitment: every pool we service gets treated like it's our own. Like our kids are swimming in it. Like we're hosting the cookout.</p><p>That means showing up consistently. Documenting every visit. Answering the phone, and if we happen to miss your call, calling you right back before you've even had time to wonder.</p><p><strong>Our goal is simple:</strong> the only question you should ever have about your pool is \"Am I swimming today?\" Not \"Did they come?\" or \"Is the water safe?\"</p><p>We're your neighbors. There's no 1-800 number or corporate script here. When something comes up, you talk to someone who actually cares about your pool, because it reflects directly on our family name.</p>",
    "photo": {"file": "photos/mike-brazell-owner-lexington-parade.jpg", "alt": "Mike Brazell, owner of Palmetto Pool Solutions, beside the company's parade float and banner", "w": 600, "h": 760, "caption": "Mike Brazell, owner and Certified Pool Operator"},
    # "team": [{"name": ..., "role": ..., "bio": ..., "photo": "photos/..."}],   # add Mike's family/crew once names + photos are confirmed
    "list_title": "Our quality assurance system",
    "list": ["Door-hanger visit report after every service", "Standardized technician checklists on every pool", "Random weekly quality checks on our routes", "Callback within the hour if we miss your call", "Mike is a Certified Pool Operator (CPO)", "Licensed and fully insured"]},
  "contact": {"title": "Free Pool Evaluation in Lexington, SC",
    "meta": "Schedule a free pool evaluation with family-owned Palmetto Pool Solutions in Lexington or Richland County, SC. Call or text (803) 394-0765.",
    "h1": "Schedule Your Free Pool Evaluation", "lead": "Tell us a little about your pool and we'll reach out to set up a time. Prefer to talk? Call or text, because we answer our phone.",
    "selects": [("Pool type", ["In-ground, chlorine", "In-ground, saltwater", "Above-ground", "Not sure"])],
    "select_names": {"Pool type": "pool_type"},
    "message_label": "Anything we should know? (green water, equipment issues, gate code notes)",
    "consent_text": "Yes, Palmetto Pool Solutions may text me about this request and my service. Message & data rates may apply. Reply STOP to opt out. Consent is not a condition of service.",
    "submit": "Request my free evaluation", "note": "We'll call or text to schedule. No pressure, no obligation.",
    "success": "Thanks! We got your request and will call or text you shortly.",
    "next_steps": ["We call or text to pick a time", "We inspect your pool & equipment", "You get one flat monthly number"]},
  "thank_you": {"title": "Thank you", "h1": "Thanks, we got your request.",
    "lead": "Mike's team will call or text you shortly to set up your free pool evaluation.",
    "text": "Need us sooner? We answer our phone."},
  "reviews": REVIEWS,
  "faqs": GENERAL_FAQS,
  "legal_pages": [("privacypolicy", "Privacy Policy"), ("termsandconditions", "Terms of Service"), ("accessibility", "Accessibility Statement")],
  "redirects": [("/contact-page", "/contact/"), ("/pool-service-columbia-sc2", "/pool-service-columbia-sc/"), ("/home", "/"),
                ("/posts", "/blog/"), ("/terms", "/termsandconditions/"), ("/sitemap", "/sitemap.xml"),
                ("/posts/author/*", "/about/"), ("/posts/tag/*", "/blog/"),
                # links inside the old blog posts pointed at these (they 404 on the old site too)
                ("/weekly-pool-maintenance", "/services/weekly-pool-maintenance/"), ("/pump-filter-services", "/services/pool-pump-filter-repair/"),
                ("/green-to-clean", "/services/green-to-clean-pool-recovery/")],
}
