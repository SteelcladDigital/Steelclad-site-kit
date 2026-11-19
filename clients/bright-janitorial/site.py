"""Bright Janitorial Services: client config for Steelclad Site Kit.
Commercial cleaning, Columbia, SC (office at 1931 Assembly St.), serving the Midlands and South Carolina.
Build: python3 build.py bright-janitorial
Forms: Web3Forms (vasylb@brightjs.net). Tracking: the client's OWN GTM container. No GoHighLevel.
Every URL on the old GHL site is kept: /, /about, /services, /services/<8 services>, /facilities-we-serve, /privacy-policy."""
import importlib.util, os
_DIR = os.path.dirname(os.path.abspath(__file__))
def _load(name):
    spec = importlib.util.spec_from_file_location(f"bright_{name}", os.path.join(_DIR, name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
_svc = _load("services"); _areas = _load("areas")
SERVICES, PH = _svc.SERVICES, _svc.PH
AREAS, GROUPS = _areas.AREAS, _areas.GROUPS
FAVICON_SVG = open(os.path.join(_DIR, "source", "favicon.svg")).read()
PHONE, TEL = "(803) 553-8693", "+18035538693"

# Real testimonials from the current brightjs.net home page (names and titles as published there).
REVIEWS = [
    ("Mark Colby", "Facilities Manager, Mungo Homes (Irmo complex)", "Excellent job! Thank you for your hard work and we appreciate all you do!"),
    ("Susan Motz", "Executive Assistant, Presbyterian Communities of South Carolina", "Wow, what a difference! The fresh scent when you walk in is amazing. It looked fantastic! Thank you so much for all you do!"),
    ("Kandi Mills", "General Manager, Classic Ford Lincoln Columbia", "We were all saying how great it looks this morning when we walked in!!"),
]

CITY_LIST = "Columbia, Lexington, Irmo, Chapin, Blythewood, Newberry, Sumter, Orangeburg, Aiken, Greenville, Spartanburg, Greer, Anderson, Rock Hill, Fort Mill, Florence, Charleston, North Charleston, Summerville, Mount Pleasant and Ridgeville"

GENERAL_FAQS = [
    ("What areas do you serve?", f"We're based in Columbia, SC and serve the Midlands and communities across South Carolina, including {CITY_LIST}. Not sure if we cover your location? Call or text {PHONE} and we'll confirm."),
    ("What types of facilities do you clean?", "Offices, medical and dental facilities, retail spaces and showrooms, warehouses and industrial facilities, construction projects, multi-tenant properties, schools and daycares, auto dealerships and property management portfolios. No job is too small or too large."),
    ("Do you offer one-time cleaning or only recurring contracts?", "Both. We offer one-time cleanings for move-ins, move-outs, post-construction and annual deep cleans, plus recurring contracts for facilities that need consistent coverage."),
    ("Can you clean outside our business hours?", "Yes. We build the schedule around your hours: before you open, after you close, overnight or on weekends. We operate seven days a week, 9 AM to 9 PM, with 24/7 emergency response."),
    ("What products and equipment do you use?", "Diversey professional-grade cleaning and infection-prevention chemistry, Kärcher commercial floor equipment and Pro-Team vacuums with HEPA filters."),
    ("Are you bonded and insured?", "Yes. Bright Janitorial Services is fully bonded and insured, and we provide documentation on request."),
    ("How fast will I hear back about a quote?", "We respond within one business day. For anything urgent, call or text " + PHONE + "."),
]

# ---------------------------------------------------------------- FACILITIES WE SERVE (Steelclad copy, /facilities-we-serve)
SL = lambda s: "services/" + s
FACILITIES = {
    "slug": "facilities-we-serve", "nav_label": "Facilities We Serve",
    "title": "Facilities We Serve | Commercial Cleaning Columbia, SC",
    "meta": "Commercial cleaning for offices, medical facilities, retail, warehouses, construction projects and multi-tenant properties in Columbia, SC.",
    "h1": "Commercial Cleaning for Every Type of Facility in Columbia, SC",
    "lead": "Office. Medical. Retail. Warehouse. Post-construction. And more. If it's a commercial space in Columbia, the Midlands or across South Carolina, we clean it.",
    "sections": [
        {"eyebrow": "Every facility is different", "title": "A cleaning program built around how your space actually operates",
         "html": "<p>An office building has different needs than a medical clinic. A retail storefront needs a different approach than a warehouse. A property management company overseeing a portfolio has different requirements than an office manager who just needs one space handled reliably every week.</p><p>Bright Janitorial Services works across a wide range of commercial facilities throughout Columbia and the Midlands. With 18 years in commercial environments, we understand what your facility type actually requires, not just what cleaning looks like in general. One building or many, 1,000 square feet or 100,000: we build the program around your facility, your schedule and your standards.</p>"},
        {"eyebrow": "Facility types", "title": "Facilities we clean in Columbia & across South Carolina", "bg": "sand",
         "cards": [
            ("doc", "Office Buildings & Workspaces", "Single-tenant suites to multi-floor buildings, cleaned around your team's hours: desks, restrooms, conference rooms, break rooms and lobbies.", [("Office cleaning", SL("office-cleaning"))]),
            ("heart", "Medical & Healthcare Facilities", "Medical offices, dental practices and outpatient clinics need a higher standard. We use Diversey infection-prevention chemistry and protocol-driven processes.", [("Medical & healthcare cleaning", SL("medical-healthcare"))]),
            ("star", "Retail & Commercial Spaces", "Storefronts, sales floors, dressing rooms, stockrooms and restrooms kept to the standard your customers expect from the moment they walk in.", [("Commercial & retail cleaning", SL("commercial-retail-cleaning"))]),
            ("truck", "Industrial Facilities & Warehouses", "Warehouses, distribution centers and manufacturing facilities cleaned around your shifts, with Kärcher equipment built for large-format floors.", [("Industrial & warehouse cleaning", SL("industrial-warehouse-cleaning"))]),
            ("tool", "Construction Projects & New Builds", "Rough cleanup through final detail for contractors, developers and owners: drywall dust, overspray, debris and adhesive, handled.", [("Post-construction cleanup", SL("post-construction-cleanup"))]),
            ("layers", "Multi-Tenant & Mixed-Use Properties", "Shared lobbies, restrooms and common areas held to one standard across the building, with one vendor for the whole property.", [("Office cleaning", SL("office-cleaning")), ("Day porters", SL("day-porter-services"))]),
            ("home", "Property Management Portfolios", "One trusted vendor across your buildings: consistent standards, responsive communication, move-out cleaning between tenants and no babysitting required.", [("All services", "services")]),
            ("users", "Daycare & Education", "High-touch learning areas, toys, restrooms and rest areas cleaned with products chosen for spaces where children learn and play.", [("Office cleaning", SL("office-cleaning"))]),
            ("badge", "Auto Dealerships", "High-gloss showroom floors, service-area cleaning, customer lounges and sales offices kept customer-ready.", [("Floor care", SL("floor-care"))]),
            ("sparkle", "Any Facility Needing Floor Care", "Offices, retail, clinics, warehouses and schools: hard floors stripped, waxed, buffed and maintained on a schedule.", [("Floor care", SL("floor-care"))]),
         ]},
        {"eyebrow": "Who we work with", "title": "The people responsible for how a facility looks and runs",
         "cards": [
            ("doc", "Office Managers", "One less thing on your list. Cleaning on a schedule you can count on, with no vendor-chasing and no inspecting the work yourself.", []),
            ("home", "Property Managers & Building Owners", "Consistent, professional cleaning across your properties. Responsive communication. One point of contact. No surprises.", []),
            ("heart", "Medical Practice Managers", "Infection-prevention cleaning that meets the standard your patients and staff expect, from a team that understands clinical spaces.", []),
            ("truck", "Facility Directors", "Structured programs for large or multi-use facilities, built around your operations, your compliance requirements and your standards.", []),
            ("tool", "General Contractors", "Post-construction cleanup that closes out your project correctly: on time, thorough and without you managing the details.", []),
         ]},
        {"eyebrow": "Service area", "title": "Serving Columbia, the Midlands and South Carolina", "bg": "sand",
         "html": f'<p>Bright Janitorial Services is based in Columbia and provides commercial cleaning throughout the Midlands and across South Carolina, including {CITY_LIST}. <a href="/service-area/">See every area we serve</a>, or call {PHONE} to confirm coverage for your location.</p>'},
    ],
    "faqs": [
        ("Do you work with small facilities or only large commercial buildings?", "Both. No job is too small or too large. Whether it's a small professional office or a large multi-building property, we'll put together a plan that fits."),
        ("Can you handle facilities with both office and warehouse space?", "Yes. Mixed-use facilities with office, warehouse, production or any combination are well within our scope. We clean the full building under one service program."),
        ("Do you offer one-time cleaning or only recurring contracts?", "Both. One-time cleanings for move-ins, move-outs, post-construction, annual deep cleans and projects, plus recurring contracts for facilities that need consistent coverage."),
        ("Can you work around our facility's operating hours?", "Yes. We build our schedule around your hours: before you open, after you close, overnight or on weekends. Your operations come first."),
        ("Do you serve facilities outside of Columbia?", "Yes. We serve the Midlands and communities across South Carolina. Contact us with your location and we'll confirm coverage."),
        ("Are you bonded and insured?", "Yes. Fully bonded and insured, with documentation available on request."),
    ],
    "schema_service": "Commercial Cleaning by Facility Type",
    "cta_title": "Tell us about your facility. We'll put together a plan.",
    "cta_text": "Call or text for a free quote. We respond within one business day.",
}

# ---------------------------------------------------------------- RESOURCE: cleaning frequency checklist (link-worthy guide)
CHECKLIST = [
    ("Every visit · daily", "Daily janitorial", ["Empty and reline trash and recycling", "Clean, disinfect and restock restrooms", "Wipe and sanitize high-touch points: handles, switches, rails, counters", "Clean break room counters, sinks and appliance exteriors", "Vacuum traffic lanes and entry mats; sweep and mop hard floors", "Spot-clean entrance glass and lobby surfaces"]),
    ("Weekly", "Weekly detail", ["Dust ledges, sills, partitions and furniture", "Vacuum the full carpeted area, including edges", "Clean interior glass, partitions and elevator panels", "Wipe chairs, phones and shared equipment", "Clean microwave and refrigerator exteriors; check fridge for clean-out"]),
    ("Monthly", "Monthly attention", ["Dust vents, returns and high surfaces", "Clean baseboards and door frames", "Spray-buff or burnish high-traffic hard floors", "Deep-clean restroom grout and partitions", "Check mats, dispensers and supplies for replacement"]),
    ("Quarterly", "Quarterly projects", ["Hot-water extraction for high-traffic carpet", "Detail-clean light fixtures and diffusers", "Wash walls and doors in high-touch areas", "Pressure wash entrances, sidewalks and dumpster pads"]),
    ("Once or twice a year", "Floor restoration", ["Strip and refinish VCT and other waxed floors", "Full-area carpet extraction", "Deep-clean upholstery in lobbies and conference rooms", "Exterior window cleaning"]),
    ("During business hours", "Day porter coverage", ["Restroom checks and restocking through the day", "Lobby, entrance glass and mat upkeep", "Trash runs before bins overflow", "Immediate spill response and hazard cleanup"]),
]
CHECKLIST_BODY = """
<h2>How to use this checklist</h2>
<p>Every facility is different, so treat this as a starting point. Frequency depends on four things: how many people use the space, what kind of space it is (a medical office needs more disinfection than a warehouse office), your floor types, and the standard your tenants, patients or customers expect. A busy lobby may need daily burnishing; a quiet private office may only need weekly vacuuming.</p>
<h2>Put the scope in writing</h2>
<p>The most common reason commercial cleaning goes wrong isn't effort. It's that nobody wrote down what \"clean\" means. Before you sign with any cleaning company, ask for a written scope that lists each task, how often it's done and which areas it covers. Then you, your cleaning team and your building all hold the same standard.</p>
<h2>Questions to ask any cleaning company</h2>
<ul class="checklist">
<li><strong>Are you bonded and insured?</strong> Ask for documentation before the first visit.</li>
<li><strong>Will the same team clean my facility every time?</strong> Turnover is the biggest cause of missed tasks.</li>
<li><strong>What products and equipment do you use?</strong> Professional-grade disinfectants and HEPA vacuums make a measurable difference.</li>
<li><strong>How do I reach you when something comes up?</strong> You want a direct line and a fast response, not a call center.</li>
<li><strong>Do you handle floor care, day porters and light maintenance too?</strong> Fewer vendors means fewer gaps.</li>
</ul>
<p>Bright Janitorial Services builds every program from a walk-through and puts the scope in writing. See our <a href="/services/office-cleaning/">office cleaning</a>, <a href="/services/floor-care/">floor care</a> and <a href="/services/day-porter-services/">day porter services</a>, or <a href="/contact/">request a free quote</a>.</p>
<p style="font-size:.9rem;color:var(--c-muted)">This checklist is general guidance for commercial facilities. Healthcare and other regulated facilities should also follow their own infection-control policies and any requirements that apply to them.</p>
"""

CONTACT_FORM = {
    "extra_inputs": [("company", "Company / facility name", "organization", False, True),
                     ("location", "Service location(s)", "street-address", False, True)],
    "selects": [("Facility type", ["", "Office", "Medical or dental", "Retail or showroom", "Warehouse or industrial", "Construction project", "Multi-tenant or property management", "School or daycare", "Auto dealership", "Other"]),
                ("Service needed", ["", "Commercial / office cleaning", "Commercial & retail cleaning", "Medical & healthcare cleaning", "Industrial & warehouse cleaning", "Post-construction cleanup", "Floor care", "Day porter services", "Light building maintenance", "Not sure / several"]),
                ("How often?", ["", "Daily / nightly", "Several times a week", "Weekly", "Every other week or monthly", "One-time cleaning", "Not sure yet"])],
    "select_names": {"Facility type": "facility_type", "Service needed": "service", "How often?": "frequency"},
    "select_placeholder": "Choose one", "city_select": False,
    "message_label": "Facility details / service scope (square footage, frequency, specific requirements)",
    "consent_text": "I agree to receive calls, texts and emails from Bright Janitorial Services about my request. Consent is not a condition of purchase. Msg/data rates may apply. Reply STOP to opt out.",
    "submit": "Request my free quote", "note": "No obligation. We respond within one business day.",
    "success": "Thanks! We got your request and will respond within one business day.",
}

CONFIG = {
  "business": {
    "name": "Bright Janitorial Services", "legal_name": "Bright Janitorial Services LLC",
    "domain": "https://brightjs.net",
    "phone": PHONE, "tel": TEL, "email": "vasylb@brightjs.net",
    "schema_type": ["LocalBusiness", "ProfessionalService"],
    "description": "Columbia, SC commercial cleaning company with 18 years of experience: office, medical, retail, industrial and warehouse, post-construction, floor care, day porter and light building maintenance services across the Midlands and South Carolina.",
    "address": {"street": "1931 Assembly St., 2nd Floor", "locality": "Columbia", "region": "SC", "zip": "29201"},
    "geo": (34.0007, -81.0348),
    "hours": [(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "09:00", "21:00")],
    "hours_text": "Mon–Sun 9 AM–9 PM · 24/7 emergency response",
    "counties": ["Richland County, SC", "Lexington County, SC", "South Carolina"],
    "knows_about": ["Commercial cleaning", "Janitorial services", "Office cleaning", "Medical facility cleaning", "Industrial and warehouse cleaning", "Post-construction cleaning", "Commercial floor care", "Day porter services", "Light building maintenance"],
    "slogan": "Quality. Communication. Reliability.",
    "social": {},
  },
  "theme": {
    # Logo colors: royal blue #0A0AAA and sun yellow #FFD420. Header: the client's teal #4d9db5 (kept from the current site).
    # The logo is a transparent cutout sitting straight on the teal header; in the dark footer it sits on a teal plate so it
    # looks the same. Teal + white text fails contrast, so header nav text is deep navy. Hero/dark sections use the logo blue;
    # buttons use the logo yellow with navy text.
    "colors": {"primary": "#0a0aaa", "primary_deep": "#06065e", "secondary": "#8fd3e6", "secondary_deep": "#1f6f88",
               "secondary_wash": "#eaf5f9", "accent": "#ffd420", "accent_text": "#06065e", "surface": "#f3f8fa",
               "ink": "#151b45", "muted": "#4a5270", "texture": "#4d9db5", "highlight": "#ffd420"},
    "fonts": {"display": "outfit", "body": "inter"},
    "radius": "soft", "heading_case": "none", "divider": "angle", "texture": "none", "hero_layout": "centered",
    "header_bg": "#4d9db5", "header_ink": "#06065e", "logo_plate": "footer", "logo_plate_bg": "#4d9db5",
  },
  "logo": {"type": "image", "file": "logo.webp", "schema_file": "logo-light-bg.png", "width": 221, "height": 160, "display_height": 76},
  "favicon_svg": FAVICON_SVG,
  "integrations": {
    "form_mode": "web3forms",
    "web3forms_access_key": "dab4b782-5770-417d-b091-63dfc91b431b",   # created with vasylb@brightjs.net (public by design)
    "web3forms_subject": "New quote request from brightjs.net",
    "web3forms_from_name": "Bright Janitorial website",
    "thank_you_slug": "thank-you",
    "gtm_id": "GTM-TP8G6H5L",          # client's OWN Tag Manager account (GA4 G-JQ13XPG8GG lives inside GTM, not here)
    "google_reviews_url": "https://g.page/r/CWpeyki_epxREBM/review",   # from Vasyl's GBP dashboard (opens the write-a-review box)
    "google_reviews_label": "★★★★★ Leave us a 5-star Google review",
  },
  # "launched": leave off until Vasyl approves the preview and --check is clean.
  "labels": {
    "cta": "Get a Free Quote", "cta_short": "Free Quote", "cta_long": "Get Your Free Quote",
    "phone_prefix": "Call or text", "topbar_promise": "Bonded & insured · 18 years of commercial cleaning",
    "footer_blurb": "Commercial cleaning from Columbia, SC for the Midlands and South Carolina. Quality. Communication. Reliability.",
    "footer_services_title": "Services",
    "reviews_title": "Trusted by businesses across the Midlands",
    "cta_band_title": "Ready for a facility you're proud of?",
    "cta_band_text": "No job is too big or too small. Call or text for a free quote. We respond within one business day.",
    "aside_title": "Get a free quote", "aside_text": "Tell us about your facility. We respond within one business day.",
    "aside_badges": "✓ Bonded & insured · ✓ 18 years · ✓ Diversey, Kärcher & Pro-Team HEPA",
  },
  "home": {
    "title": "Commercial Cleaning Services in Columbia, SC",
    "meta": "Commercial cleaning and janitorial services in Columbia, SC and across South Carolina: offices, medical, retail, warehouses, floors. Bonded & insured.",
    "eyebrow": "Bonded · Insured · Commercial facility care",
    "h1": "Commercial Cleaning in Columbia, SC: <em>Quality Is Our Top Priority, Every Time.</em>",
    "lead": "Bright Janitorial Services brings 18 years of professional-grade janitorial experience to offices, medical facilities, warehouses and commercial properties across Columbia, the Midlands and South Carolina.",
    "secondary_cta": ("See Our Services", "services"),
    "proof": ["Bonded & insured", "18 years in commercial cleaning", "90% of new clients come from referrals"],
    "trust": [("shield", "Bonded & insured", "Documentation on request"), ("badge", "18 years", "Commercial cleaning experience"),
              ("users", "90% referrals", "Of new clients come from referrals"), ("clock", "7 days a week", "9 AM–9 PM · 24/7 emergency response")],
    "why": {"eyebrow": "What sets us apart",
            "quote_html": "Quality. Communication. <em>Reliability.</em>",
            "body": "You shouldn't have to worry about your building's cleanliness. When you hire Bright Janitorial, you hand off the whole problem: no micromanaging crews, no inspecting restrooms, no chasing callbacks. Just dependable routines that run in the background.",
            "items": [("sparkle", "Quality", "Diversey professional-grade chemistry with Kärcher and Pro-Team HEPA equipment. A level of clean your team notices from day one."),
                      ("phone", "Communication", "Responsive and easy to reach. When something comes up, we handle it, and we tell you."),
                      ("check", "Reliability", "We show up on schedule, every time. You won't need to manage us or follow up."),
                      ("users", "The same team", "The same trained people on every visit, so nothing gets lost in a hand-off.")]},
    "steps": {"eyebrow": "How we work", "title": "From first call to a facility that handles itself",
              "items": [("We listen first", "Tell us about your facility, your traffic and what hasn't worked before. Call or text " + PHONE + "."),
                        ("We build a custom plan", "After a walk-through, you get a documented scope: tasks, frequency and schedule, in writing."),
                        ("We show up and deliver", "The same trained team, the same process, every visit."),
                        ("We stay accountable", "Proactive communication, and fast fixes if anything is ever missed.")]},
    "form": {"eyebrow": "Free quote", "title": "Request a free commercial cleaning proposal",
             "lead": "Tell us about your facility and we'll respond within one business day. Prefer to talk? Call or text " + PHONE + ".",
             "points": ["Walk-through and written scope", "One-time or recurring service", "Bonded & insured, documentation on request"],
             "form": CONTACT_FORM},
    "gallery": {"eyebrow": "Our work", "title": "Real before & after results",
                "lead": "Photos from Bright Janitorial jobs, not stock images.",
                "photos": [PH["tile_before"], PH["tile_after"], PH["carpet_before"], PH["carpet_after"], PH["pc_before"], PH["pc_after"]], "pairs": True},
    "order": ["trust", "services", "why", "gallery", "steps", "reviews", "form", "areas", "faq", "cta"],
  },
  "services_hub": {"slug": "services", "nav_label": "Services", "home_count": 8,
    "title": "Commercial Cleaning Services Columbia, SC",
    "meta": "Commercial cleaning services in Columbia, SC: office, retail, medical, industrial, post-construction, floor care, day porter and light maintenance.",
    "h1": "Commercial Cleaning Services in Columbia, SC",
    "lead": "Facility-grade cleaning and routine maintenance for single buildings and multi-site portfolios, tailored to your industry, your schedule and your standards.",
    "home_title": "A complete range of commercial cleaning services",
    "home_lead": "Reliable cleaning and routine maintenance across single and multi-facility portfolios, from nightly office cleaning to floor restoration and day porters.",
    "body_html": f"""<h2>One commercial cleaning partner for the whole building</h2>
<p>Bright Janitorial Services is a Columbia, SC commercial cleaning company with 18 years of experience. We clean offices, medical facilities, retail spaces, warehouses and new construction, and we also handle the work most janitorial companies hand off: floor stripping and waxing, carpet extraction, day porters and light building maintenance. That means fewer vendors, fewer gaps and one point of contact.</p>
<p>Every program starts with a walk-through and a written scope. We use Diversey professional-grade chemistry, Kärcher commercial floor equipment and Pro-Team HEPA vacuums, and the same trained team cleans your facility every visit. We're fully bonded and insured, and nearly 90% of our new clients come from referrals.</p>
<p>We serve Columbia and the Midlands and facilities across South Carolina, including {CITY_LIST}. See <a href="/facilities-we-serve/">the facilities we serve</a>, <a href="/service-area/">our service area</a>, or <a href="/commercial-cleaning-checklist/">our commercial cleaning checklist</a>.</p>""",
    "faqs": GENERAL_FAQS[:4] + GENERAL_FAQS[5:6], "faq_title": "Commercial cleaning questions",
    "schema_service": "Commercial Cleaning Services"},
  "services": SERVICES,
  "custom_pages": [FACILITIES],
  "areas": {
    "enabled": True, "hub_slug": "service-area", "nav_label": "Service Area", "link_prefix": "Commercial Cleaning", "services_listed": 8,
    "footer": "short", "footer_limit": 8, "footer_title": "Midlands Service Areas",   # plain city names, Midlands first; the rest via the hub
    "hub_title": "Service Area: Commercial Cleaning Across South Carolina",
    "hub_meta": "Bright Janitorial Services provides commercial cleaning from Columbia across the Midlands, Upstate, York County, the Pee Dee and the Lowcountry.",
    "hub_h1": "Commercial Cleaning Across Columbia, the Midlands &amp; South Carolina",
    "hub_lead": "Based in downtown Columbia, we serve the Midlands every day and take on facilities and projects across South Carolina.",
    "home_title": "Serving Columbia, the Midlands & South Carolina",
    "groups": GROUPS,
    "outside_note": "Don't see your city? Call or text. We take on facilities across South Carolina.",
    "service_where_text": "Based in Columbia, we serve facilities across the Midlands and South Carolina, including",
    "page_title": "Commercial Cleaning in {city}, {region}",
    "page_meta": "Commercial cleaning in {city}, SC: offices, medical, retail, warehouses, floor care & day porters. Bonded & insured. Free quote: (803) 553-8693.",
    "page_h1": "Commercial Cleaning &amp; Janitorial Services in {city}, {region}",
    "local_title": "Commercial cleaning in {city}", "aside_title": "Service in {city}",
    "shared_faqs": [("How much does commercial cleaning cost in {city}?", "It depends on your square footage, how often you need service and the scope. We walk the facility, then give you a written proposal with the tasks, frequency and price. Quotes are free.")],
    "pages": AREAS,
  },
  "resource": {
    "enabled": True, "slug": "commercial-cleaning-checklist", "nav_label": "Cleaning Checklist",
    "title": "Commercial Cleaning Checklist: Daily to Yearly Tasks",
    "meta": "A free commercial cleaning checklist for facility managers: what to clean daily, weekly, monthly, quarterly and yearly, plus questions to ask a cleaner.",
    "h1": "The Commercial Cleaning Checklist for Facility Managers",
    "lead": "What should be cleaned every day, every week and once a year? A plain-English frequency checklist for offices, medical suites, retail spaces and multi-tenant buildings, from a Columbia, SC commercial cleaning company.",
    "cards": CHECKLIST, "body_html": CHECKLIST_BODY, "faq_title": "Cleaning frequency questions",
    "faqs": [("How often should an office be professionally cleaned?", "Most busy offices need restrooms, trash and high-touch surfaces handled daily or nightly, with dusting and full vacuuming weekly. Smaller or low-traffic offices often do well with service two or three times a week."),
             ("How often should commercial floors be stripped and waxed?", "Most commercial floors benefit from a full strip and wax once or twice a year, with scheduled buffing or burnishing in between. High-traffic spaces may need it more often."),
             ("What is a day porter, and do I need one?", "A day porter is an on-site cleaner during business hours who handles restrooms, trash, lobbies and spills as they happen. High-traffic buildings, medical complexes and multi-tenant properties benefit most."),
             ("What should be in a commercial cleaning scope of work?", "Each task, how often it's done and which areas it covers, plus who to contact when something comes up. A written scope keeps everyone holding the same standard.")],
    "cta_title": "Want this checklist handled for you?", "cta_text": "We'll walk your facility and turn it into a written scope with a schedule and a price.",
  },
  "about": {"title": "About Bright Janitorial Services | Columbia, SC",
    "meta": "Bright Janitorial Services is a Columbia, SC commercial cleaning company with 18 years of experience, built on quality, communication and reliability.",
    "h1": "18 Years of Commercial Cleaning Experience, Built Into Every Job We Do",
    "lead": "Bright Janitorial Services is a Columbia, SC commercial cleaning company built on three things we treat as a daily operating standard, not a slogan: quality, communication and reliability.",
    "story_title": "Why we built Bright Janitorial",
    "story_html": "<p>Anyone who has managed a commercial building has seen it: a cleaning company bids low, starts strong, then cuts corners. Crews turn over. Calls go unanswered. And the facility manager ends up inspecting restrooms and chasing a vendor instead of running the building.</p><p>Bright Janitorial Services was built to be the opposite. We select our team carefully, train them well and send the same professionals to your facility every visit. We use Diversey professional-grade chemistry, Kärcher commercial floor equipment and Pro-Team HEPA vacuums, because the right products and tools are part of doing the job right.</p><p><strong>It works:</strong> nearly 90% of our new clients come from referrals by existing clients. When property managers and facility directors recommend us to their colleagues, we know we're doing something right.</p>",
    "list_title": "How we work",
    "list": ["We listen first, then build a custom, documented plan", "The same trained team on every visit", "Diversey chemistry, Kärcher equipment and Pro-Team HEPA vacuums", "Proactive communication, and fast fixes if anything is missed", "One-time cleanings and recurring contracts", "Fully bonded and insured, with documentation on request", "Office at 1931 Assembly St., 2nd Floor, Columbia, SC 29201"],
    "photos_title": "Our work", "photos": [PH["tile_before"], PH["tile_after"], PH["carpet_before"], PH["carpet_after"]], "photos_pairs": True},
  "contact": {"title": "Get a Free Quote | Bright Janitorial Services, Columbia SC",
    "meta": "Request a free commercial cleaning proposal from Bright Janitorial Services in Columbia, SC. We respond within one business day. (803) 553-8693.",
    "h1": "Request a Free Commercial Cleaning Proposal",
    "lead": "Tell us about your facility and we'll respond within one business day. Prefer to talk? Call or text (803) 553-8693.",
    **CONTACT_FORM,
    "next_steps": ["We respond within one business day", "We walk your facility and listen", "You get a written scope, schedule and price"],
    "faqs": [GENERAL_FAQS[0], GENERAL_FAQS[2], GENERAL_FAQS[5], GENERAL_FAQS[6]], "page_type": "ContactPage"},
  "thank_you": {"title": "Thank you", "h1": "Thanks, we got your request.", "lead": "We'll respond within one business day.", "text": "Need us sooner?"},
  "reviews": REVIEWS,
  "faqs": GENERAL_FAQS,
  "legal_pages": [("privacy-policy", "Privacy Policy")],
  "redirects": [("/home", "/"), ("/index", "/"),
                ("/services/commecial-retail-spaces", "/services/commercial-retail-cleaning/"),   # misspelled "Learn more" link on the old /services page
                ("/services/commercial-retail-spaces", "/services/commercial-retail-cleaning/"),
                ("/contact-us", "/contact/"), ("/quote", "/contact/")],
}
