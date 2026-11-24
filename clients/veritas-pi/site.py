# Veritas Investigative Group: Lexington, SC private investigator (SLED License No. 4362)
# Rebuilt from the client-approved GHL site (never live). ALL BODY COPY IS VERBATIM FROM GHL: do not edit wording here
# without client approval. Kit additions are limited to titles, meta descriptions, alt text, schema and links.
# Text markup: *gold italic*, **bold**, [label](/slug/). Layout: "sections" (see build.py sx_page).
import os
_here = os.path.dirname(os.path.abspath(__file__))
FAVICON = open(os.path.join(_here, "source", "favicon.svg"), encoding="utf-8").read()

PHONE = "(803) 904-1755"
CTA = ("Contact Veritas", "contact")
NOT_SURE = {"type": "cta", "h2": "Not Sure Where to *Start?*", "lead": "Tell us about your situation. We'll help you understand your options."}

SVC = {   # slug: (name, nav label)
    "pi":   ("services/private-investigations-surveillance", "Private Investigations & Surveillance", "Private Investigations"),
    "atty": ("services/attorney-litigation-support", "Attorney & Litigation Support", "Attorney & Litigation Support"),
    "ins":  ("services/insurance-investigations", "Insurance Investigations", "Insurance Investigations"),
    "corp": ("services/corporate-business-investigations", "Corporate & Business Investigations", "Corporate & Business"),
    "poly": ("services/polygraph-services", "Polygraph Services", "Polygraph Services"),
    "cir":  ("services/critical-investigative-response", "Critical Investigative Response", "Critical Invest Response"),
    "intl": ("services/international-investigative-services", "International Investigative Services", "International Investigative"),
    "bg":   ("services/background-due-diligence", "Background & Due Diligence", "Background & Due Diligence"),
    "sec":  ("services/security-consulting-risk-management", "Security Consulting & Risk Management", "Security Consulting"),
}
ORDER = ["pi", "atty", "ins", "corp", "poly", "cir", "intl", "bg", "sec"]
def S(k): return SVC[k][0]
def L(k): return "/" + SVC[k][0] + "/"
SERVICES_TRAIL = ("Services", "services")
def svc_trail(k): return [SERVICES_TRAIL, (SVC[k][1], S(k))]

CREDS = [
    ("shield", "South Carolina Licensed Private Investigator", "SLED LICENSE NO. 4362"),
    ("briefcase", "South Carolina Licensed, Bonded & Insured", ""),
    ("star", "Career Federal Law Enforcement Criminal Investigator", ""),
    ("world", "Domestic & International Investigative Experience", ""),
]

MEMBER_OF = ["South Carolina Association of Legal Investigators (SCALI)", "National Association of Legal Investigators (NALI)",
             "Association of Certified Fraud Examiners (ACFE)", "National Council of Investigation & Security Services (NCISS)",
             "World Association of Professional Investigators (WAPI)"]

CONFIG = {
    "layout": "sections",
    "business": {
        "name": "Veritas Investigative Group",
        "legal_name": "Veritas Investigative Group",
        "domain": "https://veritaspigroup.com",
        "phone": PHONE, "tel": "+18039041755",
        "email": "mark@veritaspigroup.com",
        "hours_text": "",
        "schema_type": "ProfessionalService",
        "description": "Licensed South Carolina private investigator based in Lexington, SC (SLED License No. 4362), providing investigations, surveillance, attorney and insurance support, polygraph, background and due diligence, and security consulting.",
        "address": {"locality": "Lexington", "region": "SC"},   # service-area business: no street address shown or marked up
        "area_served": [{"@type": "City", "name": "Lexington, SC"}, {"@type": "City", "name": "Columbia, SC"}, {"@type": "State", "name": "South Carolina"}],
        "founder": "Mark Henson",
        "slogan": "Uncover What Matters",
        "knows_about": [SVC[k][1] for k in ORDER],
        "schema_extra": {
            "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license", "name": "South Carolina private investigation license, SLED License No. 4362",
                              "recognizedBy": {"@type": "GovernmentOrganization", "name": "South Carolina Law Enforcement Division (SLED)", "url": "https://www.sled.sc.gov/"}},
            "identifier": {"@type": "PropertyValue", "propertyID": "SLED License No.", "value": "4362"},
        },
        "social": {},
    },
    "theme": {
        "colors": {"primary": "#0a0f1c", "primary_deep": "#05080f", "secondary": "#161d2f", "secondary_deep": "#0f1525", "secondary_wash": "#e9dcc0",
                   "accent": "#c5a059", "highlight": "#d9b877", "accent_text": "#0a0f1c", "surface": "#161d2f", "ink": "#ffffff", "muted": "#a3abbd"},
        "fonts": {"display": "instrument-serif", "body": "work-sans"},
        "radius": "sharp", "heading_case": "none", "divider": "none", "texture": "none",
        "hero_image": "hero.jpg",   # drop the GHL hero photo in assets/hero.jpg to use it; until then a CSS navy/gold background is used
    },
    "logo": {"type": "image", "file": "logo-dark.png", "footer_file": "logo-dark.png", "width": 190, "height": 56},   # cut from the client's 02_horizontal_logo (source/logo-pack)
    "favicon_svg": FAVICON,
    "og_image": "og-image.jpg",
    "labels": {"cta": "Contact", "reach_verb": "Call", "header_call": f"Call {PHONE}"},
    "nav": [
        {"label": "Home", "slug": ""},
        {"label": "Services", "slug": "services", "children": [(SVC[k][2], S(k)) for k in ORDER]},
        {"label": "About", "slug": "about", "children": [("Founder", "about/founder")]},
        {"label": "Contact", "slug": "contact"},
    ],
    "footer": {
        "name": "Veritas Investigative Group",
        "kicker": "SLED LICENSE NO. 4362",
        "text": "Licensed, Bonded & Insured. Operating under strict regulatory oversight of the South Carolina Law Enforcement Division (SLED) pursuant to S.C. Code Ann. § 40-18.",
        "contact_label": "Institutional inquiries, legal counsel retaining, and formal casework:",
        "disclaimer": "Veritas Investigative Group is licensed by the South Carolina Law Enforcement Division (SLED), License No. 4362. Services are provided in accordance with applicable law and the facts of each matter, and Veritas does not guarantee any particular result. Client information is held in confidence, subject to legal process. Whether reports or evidence are admissible in any proceeding is determined by the court. Veritas is not a law firm and does not provide legal advice.",
        "copyright": "© 2026 Veritas Investigative Group. All rights reserved. SLED License #4362. Licensed, Bonded & Insured.",
    },
    "contact": {
        "slug": "contact", "form_name": "contact",
        "name_split": True, "name_required": False, "first_label": "First Name", "last_label": "Last Name",
        "phone_label": "Phone *", "email_label": "Email *", "email_required": True,
        "message_label": "Nature of Request *", "message_required": True,
        "placeholders": {"first_name": "Enter your first name", "last_name": "Enter your last name", "phone": "+1 (555) 000-0000",
                         "email": "your@email.com", "message": "Type your message here"},
        "submit": "Submit", "submit_class": "sx-btn",
    },
    "integrations": {
        "form_mode": "web3forms",
        "web3forms_access_key": "e088f1a2-f364-4726-a392-3e348ce9e112",
        "web3forms_subject": "New website inquiry: Veritas Investigative Group",
        "gtm_id": "GTM-KF4BGX7C",
    },
    "reviews": [], "faqs": [],

    # ------------------------------------------------------------------ pages (same pages and order as GHL)
    "pages": [
        # 1. Home
        {"slug": "", "exact_title": True,
         "title": "Private Investigator in Lexington & Columbia, SC | Veritas",
         "meta": "SLED-licensed private investigator in Lexington, SC, serving Columbia and all of South Carolina, with federal investigative experience. Call (803) 904-1755",
         "sections": [
            {"type": "hero", "tall": True, "h1": ["Investigative Experience.", "Specialized *Expertise.*", "Proven Capability."],
             "lead": "Veritas Investigative Group provides specialized investigative services to individuals, attorneys, businesses, insurers, and government clients - based in South Carolina, with investigative experience that extends into international matters.",
             "buttons": [CTA, ("Explore Services", "services")]},
            {"type": "text", "h2": "Experience & *Credibility*",
             "paras": ["Veritas was founded on over two decades of investigative experience. That experience began as uniformed patrol service and progressed into a career as a Special Agent and Supervisory Special Agent in federal law enforcement, conducting and supervising complex criminal investigations throughout the United States and around the world."],
             "creds": CREDS},
            {"type": "text", "h2": "Methodology Built on Federal *Experience*",
             "paras": ["Every investigation begins with understanding your situation and clearly defining your objectives. From there, Veritas applies the same discipline and methodology built with our extensive investigative experience — see [Our Philosophy](/about/#our-philosophy) on the About page."]},
            {"type": "audience", "h2": "Specialized Investigative *Services*", "lead": "Veritas works directly with the people and organizations who need answers.",
             "cards": [
                {"icon": "fingerprint", "h3": "Individuals & Families", "p": "Personal matters call for discretion and a clear plan. Whether it's a relationship concern, a missing family member, or a background question, Veritas walks you through your options starting with the first conversation.", "link": ("Private Investigations & Surveillance", S("pi"))},
                {"icon": "scale", "h3": "Attorneys & Law Firms", "p": "Veritas supports litigation with thorough investigative research, witness and subject location, and evidence development - delivered with the discretion and documentation your case requires.", "link": ("Attorney & Litigation Support", S("atty"))},
                {"icon": "shield-check", "h3": "Insurance Companies", "p": "From claims verification to fraud investigations, Veritas provides the surveillance and reporting insurers rely on to make informed decisions.", "link": ("Insurance Investigations", S("ins"))},
                {"icon": "briefcase", "h3": "Businesses & Corporations", "p": "Protect your organization with workplace investigations, corporate due diligence, and risk assessments grounded in real investigative experience.", "link": ("Corporate & Business Investigations", S("corp"))},
             ],
             "disciplines": {"lead": "Veritas Investigative Group provides investigative services across the following disciplines",
                             "items": [(SVC[k][1], S(k)) for k in ORDER], "button": ("View All Services", "services")}},
            {"type": "split_cta", "h2": "Do You Need a Private *Investigator?*",
             "lead": "Tell us about your situation. We'll help you understand your options and determine how Veritas can best assist.",
             "card": {"icon": "lock", "title": "Confidential Consultation",
                      "p": "Do You Need a Private Investigator? Tell us about your situation. We'll help you understand your options and determine how Veritas can best assist.",
                      "button": CTA}},
         ]},

        # 2. Services
        {"slug": "services", "trail": [SERVICES_TRAIL], "page_type": "CollectionPage",
         "title": "Private Investigative Services in South Carolina",
         "meta": "Nine investigative services from Lexington, SC: surveillance, litigation support, insurance, corporate, polygraph, background checks and more.",
         "schema": [{"@type": "ItemList", "name": "Investigative services", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "name": SVC[k][1], "url": "https://veritaspigroup.com" + L(k)} for i, k in enumerate(ORDER)]}],
         "sections": [
            {"type": "hero", "h1": "Private Investigative *Services* in South Carolina",
             "lead": "Veritas offers nine investigative services for individuals, attorneys, insurers, businesses and government clients. Each is delivered with the methodology of federal criminal casework and documented as if it may one day be tested in court. Use the short summaries below to find the right starting point, or contact Veritas and we'll help you sort it out.",
             "buttons": [CTA]},
            {"type": "svc_grid", "h2": "Specialized Investigative *Services*", "lead": "Veritas Group provides investigative services across the following disciplines.",
             "items": [
                {"h3": "Private Investigations & Surveillance", "link": ("Learn More", S("pi")),
                 "p": "When you need clear, reliable information about a personal or family matter, Veritas provides thorough investigation and surveillance handled with discretion. Every case begins with a clear understanding of your goals and a plan built around them.",
                 "bullets": ["Domestic & Family Investigations", "Child Custody Investigations", "Missing Persons & Locate Services"]},
                {"h3": "Attorney & Litigation Support", "link": ("Learn More", S("atty")),
                 "p": "Veritas supports attorneys and legal teams with investigative research that holds up under scrutiny. From locating witnesses to developing evidence, the work is built on the same standards used in federal criminal investigations — backed by direct experience testifying in both state and federal court.",
                 "bullets": ["Civil & Criminal Litigation Support", "Witness & Subject Location", "Investigative Research & Evidence Development"]},
                {"h3": "Insurance Investigations", "link": ("Learn More", S("ins")),
                 "p": "Veritas helps insurance carriers and adjusters verify claims and identify fraud through surveillance, activity verification, and clearly documented investigative reporting.",
                 "bullets": ["Claims Investigations", "Fraud Investigations", "Surveillance & Activity Verification"]},
                {"h3": "Corporate & Business Investigations", "link": ("Learn More", S("corp")),
                 "p": "Businesses face risk from within the organization and outside it. Veritas conducts workplace investigations, misconduct inquiries, and due diligence to help business leaders make informed decisions and protect their organizations.",
                 "bullets": ["Internal & Workplace Investigations", "Employee Misconduct Investigations", "Corporate Due Diligence (see [Background & Due Diligence](" + L("bg") + ") below)"]},
                {"h3": "Polygraph Services", "link": ("Learn More", S("poly")),
                 "p": "Veritas provides single-issue and screening polygraph examinations for agencies, attorneys, insurers, and private clients, conducted by examiners with decades of federal-level experience."},
                {"h3": "Critical Investigative Response", "link": ("Learn More", S("cir")),
                 "p": "Some matters can't wait. Veritas provides time-sensitive investigative support for urgent domestic and international situations, mobilizing quickly when clients need immediate answers.",
                 "bullets": ["Domestic & International: Time-Sensitive Investigative Support"]},
                {"h3": "International Investigative Services", "link": ("Learn More", S("intl")),
                 "p": "Veritas provides investigative support for matters that cross borders, drawing on direct experience coordinating with international law enforcement and government partners.",
                 "bullets": ["International Investigations", "Cross-Border Investigative Support", "International Investigative Coordination"]},
                {"h3": "Background & Due Diligence", "link": ("Learn More", S("bg")),
                 "p": "From pre-employment screening to corporate due diligence, Veritas provides the background research individuals and organizations need to make informed decisions with confidence.",
                 "bullets": ["Pre-Employment Screening & Background Checks", "Personal & Professional Background Checks"]},
                {"h3": "Security Consulting & Risk Management", "link": ("Learn More", S("sec")),
                 "p": "Veritas provides practical, experience-based security consulting to help organizations identify vulnerabilities and prepare for critical incidents before they happen.",
                 "bullets": ["Security & Risk Assessments", "Workplace Violence Response Planning", "Security Policies & Procedures"]},
             ]},
            {**NOT_SURE, "button": CTA},
         ]},

        # 3. About
        {"slug": "about", "trail": [("About", "about")], "page_type": "AboutPage", "exact_title": True,
         "title": "About Veritas Investigative Group | Lexington, SC",
         "meta": "Veritas Investigative Group brings the discipline and standards of federal criminal investigations to private investigative work throughout South Carolina.",
         "sections": [
            {"type": "hero", "plain": True, "h1": "About *Veritas Investigative Group*",
             "paras": ["Veritas Investigative Group was founded to bring the same discipline, judgment, and standards used in federal criminal investigations to private investigative work throughout South Carolina — with the experience to support matters that reach beyond state and national borders.",
                       "That standard didn't come from a training manual — it came from over two decades of working real cases, from patrol work through complex federal investigations. Veritas exists because individuals, attorneys, and businesses deserve investigators held to that same bar."]},
            {"type": "text", "id": "our-philosophy", "h2": "Our *Philosophy*", "motto_index": 0,
             "paras": ["Listen. Understand. Plan. Investigate. Report.",
                       "Every investigation begins with understanding the situation, clearly defining the client's objectives, and determining how Veritas can best assist. Our approach is grounded in experience, discretion, and a commitment to clear and credible results."]},
            {"type": "text", "h2": "Experience & *Credibility*", "creds": CREDS},
            {"type": "cta", "h2": "Ready to discuss your situation? *Contact Veritas*", "lead": "Tell us about your situation. We'll help you understand your options.", "button": CTA},
         ]},

        # 4. Founder
        {"slug": "about/founder", "trail": [("About", "about"), ("Founder", "about/founder")], "page_type": "ProfilePage",
         "title": "Mark Henson, Founder",
         "meta": "Mark Henson founded Veritas Investigative Group after a career from patrol officer to federal Special Agent and Supervisory Special Agent.",
         "schema": [{"@type": "Person", "@id": "https://veritaspigroup.com/about/founder/#person", "name": "Mark Henson", "jobTitle": "Founder",
                     "worksFor": {"@id": "https://veritaspigroup.com/#business"}, "url": "https://veritaspigroup.com/about/founder/",
                     "memberOf": [{"@type": "Organization", "name": n} for n in MEMBER_OF]}],
         "sections": [
            {"type": "hero", "plain": True, "h1": "Founder of *Veritas Investigative Group*",
             "lead": "Veritas Investigative Group was founded by Mark Henson, who began his law enforcement career in 1998 as a uniformed patrol officer. His career progressed from local law enforcement to federal criminal investigations, including service as a Special Agent and Supervisory Special Agent, where he conducted and supervised complex criminal investigations throughout the United States and around the world."},
            {"type": "text", "h2": "Investigative *Experience*",
             "paras": ["Throughout his career, Mark Henson has conducted and supervised complex criminal investigations involving undercover operations, physical and electronic surveillance, confidential source management, high-risk operational planning, and intelligence development. His experience includes the use of specialized investigative techniques and technologies, including tracking systems and cellular data extraction and analysis, as well as the collection, evaluation, and preservation of evidence and coordination of investigations involving multiple agencies and jurisdictions throughout the United States and internationally. His work has included close, ongoing collaboration with prosecutors and defense attorneys, along with extensive experience providing testimony in both state and federal court."]},
            {"type": "text", "h2": "International *Experience*",
             "paras": ["Mark Henson's international investigative experience includes complex matters involving international Drug Trafficking Organizations (DTOs) and other Transnational Criminal Organizations (TCOs). His work included strategic coordination with foreign government officials and law enforcement leaders in advisory, assistance, and operational roles, coordination of intelligence sharing among multinational partners, and briefings for government officials, law enforcement leaders, and investigative personnel."]},
            {"type": "text", "h2": "Professional *Affiliations*",
             "paras": ["Mark Henson is a member of the following professional investigative associations:"], "list": MEMBER_OF},
            {"type": "text", "h2": "Leadership & *Philosophy*",
             "paras": ["Veritas was founded on the belief that effective investigations begin with listening and understanding - not assumptions. Every matter requires a thorough understanding of the circumstances, the client's objectives, and the questions that need to be answered. From there, experience, investigative judgment, and disciplined methodology guide the work toward clear and credible results."]},
            {**NOT_SURE, "button": CTA},
         ]},

        # 5. Contact
        {"slug": "contact", "trail": [("Contact", "contact")], "page_type": "ContactPage",
         "title": "Contact a Private Investigator",
         "meta": f"Contact Veritas Investigative Group in Lexington, SC. Call {PHONE} or send a confidential request and we'll help you understand your options.",
         "sections": [
            {"type": "contact", "h1": "Tell Us About Your *Situation*",
             "lead": "We'll help you understand your options and determine how Veritas can best assist.",
             "call_label": f"Call Veritas {PHONE}"},
            {"type": "numbered", "h2": "What Happens *Next?*", "items": [
                ("1. Initial Consultation", "Discuss the situation, answer questions, clarify objectives, and determine whether and how Veritas can assist."),
                ("2. Assessment & Engagement", "If appropriate, establish the scope and terms of the engagement."),
                ("3. Investigation & Reporting", "Conduct the agreed services and provide clear documentation of the work and findings."),
            ]},
         ]},

        # 6. Private Investigations & Surveillance
        {"slug": S("pi"), "trail": svc_trail("pi"), "service": "Private Investigations & Surveillance",
         "service_offers": ["Domestic & Family Investigations", "Child Custody Investigations", "Missing Persons & Locate Services"],
         "title": "Private Investigator & Surveillance in South Carolina",
         "meta": "Discreet surveillance, infidelity, child custody and missing persons investigations from a SLED-licensed private investigator in Lexington, SC.",
         "sections": [
            {"type": "hero", "h1": "Private Investigations & *Surveillance*",
             "lead": "When you need clear, reliable information about a personal or family matter, Veritas provides thorough investigation and surveillance handled with discretion. Every case begins with a clear understanding of your goals and a plan built around them.",
             "buttons": [CTA]},
            {"type": "items", "h2": "What This *Covers*", "items": [
                ("Domestic & Family Investigations", "Investigating suspected infidelity or verifying a partner's or family member's activities, conducted discreetly and documented in a way that gives you clear answers."),
                ("Child Custody Investigations", "Documentation of parenting time, home environment, and behavior relevant to a custody matter, gathered with an eye toward what is most likely to hold up in family court."),
                ("Missing Persons & Locate Services", "Locating a family member who has lost contact, using licensed investigative databases, field verification, and direct outreach where appropriate."),
            ]},
            {"type": "steps", "h2": "How Veritas *Works*", "items": [
                ("Step 1: Initial Consultation.", "Understand the situation, your concerns, and what outcome you're hoping to reach."),
                ("Step 2: Investigative Path.", "A clear plan and cost estimate before any work begins, so there are no surprises."),
                ("Step 3: Field Work & Surveillance.", "Discreet surveillance and investigation conducted with professionalism and respect for everyone involved."),
                ("Step 4: Reporting.", "A clear, documented report of findings, delivered directly and confidentially."),
            ]},
            {"type": "text", "h2": "Why Experience *Matters*",
             "paras": ["Personal investigations touch some of the most sensitive moments in a person's life. Over two decades of investigative experience — including complex, high-stakes federal casework — means every matter is handled with the discretion, judgment, and professionalism it deserves."]},
            {"type": "bullets", "h2": "Who This Is *For*", "items": [
                "Individuals who suspect infidelity or dishonesty in a relationship",
                "Parents navigating a custody matter who need documented, credible evidence",
                "Families searching for a missing relative",
                "Anyone who needs clear answers about a personal situation, handled discreetly"]},
            {"type": "faq", "h2": "Common *Questions*", "items": [
                ("Is my investigation confidential?", "Yes. All personal investigations are handled with strict confidentiality, and findings are shared only with you, except where disclosure is required by law."),
                ("Will I know what's happening throughout the investigation?", "You'll be kept informed at appropriate points in the process, and Veritas is available to answer questions about where things stand."),
                ("Can findings be used in a legal proceeding, like a custody case?", "Findings are documented with that possibility in mind from the start, although whether evidence is admitted is ultimately up to the court."),
            ]},
            {**NOT_SURE, "button": CTA},
         ]},

        # 7. Attorney & Litigation Support
        {"slug": S("atty"), "trail": svc_trail("atty"), "service": "Attorney & Litigation Support",
         "service_offers": ["Witness & Subject Location", "Investigative Research & Evidence Development", "Civil & Criminal Litigation Support"],
         "title": "Attorney & Litigation Support Investigator, SC",
         "meta": "Witness location, evidence development and civil and criminal defense investigation for SC attorneys, backed by state and federal court testimony.",
         "sections": [
            {"type": "hero", "h1": "Attorney & Litigation *Support*",
             "lead": "Veritas supports attorneys and legal teams with investigative research that holds up under scrutiny, backed by firsthand courtroom experience testifying in both state and federal court. From locating witnesses to developing evidence, the work is built on the same standards used in federal criminal investigations.",
             "buttons": [("Discuss a Case", "contact")]},
            {"type": "items", "h2": "What This *Covers*", "items": [
                ("Witness & Subject Location", "Finding a witness who's moved, changed jobs, or gone quiet using licensed investigative databases, field verification, and direct-contact skip tracing, documented so the process can be explained if the location itself is ever challenged."),
                ("Investigative Research & Evidence Development", "Background research on opposing parties, verification of claims made in depositions or filings, asset location, and surveillance that turns a suspicion into documented evidence — built with the expectation it may be cross-examined or entered into the record."),
                ("Civil & Criminal Litigation Support", "Veritas works both sides of the docket, supporting plaintiff and defense counsel in civil matters. In criminal cases, Veritas assists defense attorneys on a case-by-case basis with independent, fact-based investigation."),
            ]},
            {"type": "steps", "h2": "How Veritas *Works*", "items": [
                ("Step 1: Case Intake.", "Understanding the legal theory, the timeline, and what specific facts or individuals need to be developed or verified."),
                ("Step 2: Investigative Path.", "A scoped plan built around your objectives and budget, agreed to before work begins."),
                ("Step 3: Field Work & Documentation.", "Surveillance, interviews, records research, or location work conducted with an eye toward how the results will hold up if challenged."),
                ("Step 4: Reporting.", "Clear, organized reporting delivered on your timeline, written to be usable — not just informative."),
            ]},
            {"type": "text", "h2": "Why Courtroom Matters *Here*",
             "paras": ["A lot of investigative work never gets tested. This does. Two decades of federal investigative experience includes direct, ongoing work with prosecutors and defense attorneys, and firsthand experience testifying in both state and federal court — not just gathering information, but standing behind it under cross-examination. That's a different discipline than investigative work that's never had to survive a courtroom, and it shapes how every report is built from the first day of an engagement."]},
            {"type": "bullets", "h2": "Who This Is *For*", "items": [
                "Plaintiff and defense attorneys who need an independent investigator for civil litigation",
                "Criminal defense attorneys who need independent investigation and fact development",
                "Law firms that need a witness or subject located before a filing deadline",
                "Firms building a case where surveillance or field verification could materially change the outcome"]},
            {"type": "faq", "h2": "Common *Questions*", "items": [
                ("Can Veritas testify about its own findings if needed?", "Yes. Investigative work is conducted with documentation and process standards designed to hold up if testimony is required, and testimony experience in both state and federal court is part of the firm's background."),
                ("How fast can an investigation start?", "Many matters can begin within days of an initial consultation, depending on scope and availability. For time-sensitive situations, see [Critical Investigative Response](" + L("cir") + ")."),
                ("Does Veritas work with firms outside South Carolina?", "Veritas is licensed and based in South Carolina. Attorneys outside the state are welcome to reach out to discuss whether a matter falls within scope, or to be connected with a trusted investigator in the appropriate jurisdiction."),
            ]},
            {**NOT_SURE, "button": ("Discuss a Case", "contact")},
         ]},

        # 8. Insurance Investigations
        {"slug": S("ins"), "trail": svc_trail("ins"), "service": "Insurance Investigations",
         "service_offers": ["Claims Investigations", "Fraud Investigations", "Surveillance & Activity Verification"],
         "title": "Insurance Investigations in South Carolina",
         "meta": "Claims verification, insurance fraud investigations and activity-check surveillance for carriers, adjusters, SIU teams and MGAs across South Carolina.",
         "sections": [
            {"type": "hero", "h1": "Insurance *Investigations*",
             "lead": "Veritas helps insurance carriers and adjusters verify claims and identify fraud through surveillance, activity verification, and clearly documented investigative reporting.",
             "buttons": [("Discuss a Claim", "contact")]},
            {"type": "items", "h2": "What This *Covers*", "items": [
                ("Claims Investigations", "Independent verification of the facts behind a claim, providing carriers with objective, well-documented findings to support the claims decision process."),
                ("Fraud Investigations", "Investigation of claims where fraud is suspected, including surveillance, records research, and activity verification to establish a clear factual record."),
                ("Surveillance & Activity Verification", "Documented surveillance to verify a claimant's reported activity level or limitations, delivered with timestamped video and written reporting prepared for use in claims files or litigation."),
            ]},
            {"type": "steps", "h2": "How Veritas *Works*", "items": [
                ("Step 1: Referral & Case Review.", "Review the claim file and the specific questions the carrier or adjuster needs answered."),
                ("Step 2: Investigative Plan.", "A scoped plan matched to the claim's value and complexity, agreed to before work begins."),
                ("Step 3: Surveillance & Verification.", "Fieldwork conducted within legal and ethical bounds, with attention to admissibility."),
                ("Step 4: Reporting.", "Clear, thoroughly documented reporting prepared with litigation in mind, delivered on the carrier's timeline."),
            ]},
            {"type": "text", "h2": "Why This Experience *Matters*",
             "paras": ["Insurance investigations require the same rigor as a criminal case file — documentation that holds up to scrutiny, whether that's an internal claims review or a courtroom. Over two decades of investigative and courtroom experience shapes every report Veritas produces."]},
            {"type": "bullets", "h2": "Who This Is *For*", "items": [
                "Claims adjusters who need independent verification of a claim",
                "SIU (Special Investigations Unit) teams evaluating suspected fraud",
                "Insurance defense attorneys building a case around a disputed claim",
                "MGAs and carriers who need a reliable investigative vendor relationship, not a one-off contractor"]},
            {"type": "faq", "h2": "Common *Questions*", "items": [
                ("How quickly can surveillance begin on an active claim?", "Often within days of receiving the referral, depending on the facts and scheduling. Urgent claims may be able to move faster."),
                ("Is Veritas familiar with SIU documentation standards?", "Yes — reporting is built to the same evidentiary standard used in federal investigations, with claims and litigation use in mind."),
                ("Does Veritas work directly with carriers, or only through vendor panels?", "Veritas is available to work directly with carriers, adjusters, and MGAs, and is glad to discuss vendor panel relationships as well."),
            ]},
            {**NOT_SURE, "button": ("Discuss a Claim", "contact")},
         ]},

        # 9. Corporate & Business Investigations
        {"slug": S("corp"), "trail": svc_trail("corp"), "service": "Corporate & Business Investigations",
         "service_offers": ["Internal & Workplace Investigations", "Employee Misconduct Investigations", "Corporate Due Diligence"],
         "title": "Corporate & Workplace Investigations in South Carolina",
         "meta": "Independent workplace, employee misconduct and internal investigations for South Carolina businesses, coordinated with HR and legal counsel.",
         "sections": [
            {"type": "hero", "h1": "Corporate & Business *Investigations*",
             "lead": "Businesses face risk from within the organization and outside it. Veritas conducts workplace investigations, misconduct inquiries, and due diligence to help business leaders make informed decisions and protect their organizations.",
             "buttons": [CTA]},
            {"type": "items", "h2": "What This *Covers*", "items": [
                ("Internal & Workplace Investigations", "Independent, objective investigation of workplace complaints or incidents, conducted objectively and documented carefully in case the findings are later challenged."),
                ("Employee Misconduct Investigations", "Investigation of suspected theft, policy violations, or other misconduct, using the same investigative discipline applied to federal criminal cases."),
                ("Corporate Due Diligence", "See the [Background & Due Diligence](" + L("bg") + ") page for full detail on how Veritas evaluates companies, principals, and business relationships before a partnership, hire, or transaction."),
            ]},
            {"type": "steps", "h2": "How Veritas *Works*", "items": [
                ("Step 1: Initial Consultation.", "Understand the concern, the individuals involved, and any HR or legal considerations already in play."),
                ("Step 2: Investigative Plan.", "A scoped plan built in coordination with HR or legal counsel where appropriate."),
                ("Step 3: Investigation.", "Interviews, records review, and fieldwork conducted objectively and discreetly."),
                ("Step 4: Reporting.", "A clear, thoroughly documented report of findings, prepared for internal decision-making and, if needed, legal proceedings."),
            ]},
            {"type": "text", "h2": "Why Independence *Matters*",
             "paras": ["An internal investigation conducted by someone within the organization can raise questions about objectivity. Veritas provides an independent, outside perspective — backed by federal investigative experience — that protects both the integrity of the investigation and the organization's interests."]},
            {"type": "bullets", "h2": "Who This Is *For*", "items": [
                "HR leaders and business owners handling a workplace complaint",
                "Companies evaluating a partner, vendor, or acquisition target",
                "Organizations that need an independent investigator rather than an internal one",
                "Businesses building a relationship with an investigator before they need one urgently"]},
            {"type": "faq", "h2": "Common *Questions*", "items": [
                ("Will the investigation stay confidential?", "Yes — findings are shared only with the individuals you designate, typically ownership, HR leadership, or legal counsel, except where disclosure is required by law."),
                ("Can Veritas work alongside our employment attorney?", "Yes, and it's often the right approach. Veritas coordinates with legal counsel as the matter requires."),
                ("What's the difference between this and corporate due diligence?", "Workplace investigations look inward at conduct within the organization. Due diligence looks outward, at a company or individual you're considering doing business with. See [Background & Due Diligence](" + L("bg") + ") for more."),
            ]},
            {**NOT_SURE, "button": CTA},
         ]},

        # 10. Polygraph Services
        {"slug": S("poly"), "trail": svc_trail("poly"), "service": "Polygraph Services",
         "service_offers": ["Screening Examinations", "Single-Issue Examinations"],
         "title": "Polygraph Examinations in South Carolina",
         "meta": "Screening and single-issue polygraph examinations by examiners with 25+ years of federal-level experience, for agencies, attorneys and private clients.",
         "sections": [
            {"type": "hero", "h1": "Polygraph *Services*",
             "lead": "Veritas provides professional polygraph examinations for government agencies, international clients, attorneys, businesses, insurance carriers, and corporate and private clients. Veritas examiners have extensive experience conducting both standard and tailored screening examinations, as well as single-issue examinations, dependent on the facts, circumstances, and objectives of the matter.",
             "buttons": [CTA]},
            {"type": "text", "h2": "Our *Examiners*",
             "paras": ["Veritas examiners each bring 25+ years of federal-level experience across anti-terrorism, organized crime, narcotics, and Transnational Criminal Organization (TCO) investigations. Detailed examiner qualifications and CVs are available to prospective clients on request."]},
            {"type": "text", "h2": "Screening *Examinations*",
             "paras": ["Screening examinations address multiple areas of concern when no specific incident is under investigation. Veritas examiners have broad experience with national security, corporate security, and suitability testing formats. These examinations help agencies and eligible employers assess integrity and risk in pre-employment, periodic, and security settings, and are available to government agencies, international clients, and employers permitted to use them under federal law."]},
            {"type": "text", "h2": "Single-Issue *Examinations*",
             "paras": ["Single-issue examinations focus on a specific, known incident or allegation. Veritas examiners have conducted examinations in a wide range of matters, including:"],
             "list": ["Criminal investigations", "Violent crime", "Kidnapping", "Sexual assault", "Insurance fraud", "Inventory control and loss", "Product liability"]},
            {"type": "text", "h2": "Testing *Techniques*",
             "paras": ["Veritas examiners have experience and expertise in the federally approved testing formats, including the Law Enforcement Pre-Employment Test (LEPET), the Modified General Question Technique (MGQT), the Zone Comparison Technique (ZONE), and the Test for Espionage and Sabotage (TES). The technique for each examination is chosen to fit the issue being tested and the needs of the client."]},
            {"type": "text", "h2": "Our Professional *Approach*",
             "paras": ["Every examination follows established professional standards, including a thorough pretest interview, careful question formulation, standardized data collection, and objective analysis. Clients receive timely results in a written report, with a clear account of what the results establish. Drawing on extensive international experience, examinations can also be conducted in languages other than English, with interpreter support arranged as needed."]},
            {**NOT_SURE, "button": CTA},
         ]},

        # 11. Critical Investigative Response
        {"slug": S("cir"), "trail": svc_trail("cir"), "service": "Critical Investigative Response",
         "service_offers": ["Rapid Deployment", "Domestic & International Response"],
         "title": "Critical & Urgent Investigative Response, SC",
         "meta": "Time-sensitive investigative support for urgent domestic and international matters: missing family members, corporate incidents, legal deadlines.",
         "sections": [
            {"type": "hero", "h1": "Critical Investigative *Response*",
             "lead": "Some matters can't wait. Veritas provides time-sensitive investigative support for urgent domestic and international situations, mobilizing quickly when clients need immediate answers.",
             "buttons": [("Contact Veritas Immediately", "contact")]},
            {"type": "items", "h2": "What This *Covers*", "items": [
                ("Rapid Deployment", "When a situation is developing in real time — a missing family member, an active corporate incident, a time-critical legal deadline — Veritas prioritizes urgent matters and mobilizes quickly."),
                ("Domestic & International Response", "Experience coordinating urgent investigative response both within the United States and internationally, drawing on established relationships and investigative coordination experience."),
            ]},
            {"type": "steps", "h2": "How Veritas *Works*", "items": [
                ("Step 1: Immediate Contact", "Reach out directly; urgent matters are prioritized over standard intake."),
                ("Step 2: Rapid Assessment.", "A fast, focused assessment of what's known, what's needed, and what can be done immediately."),
                ("Step 3: Mobilization.", "Investigative resources deployed as quickly as the situation allows."),
                ("Step 4: Ongoing Communication.", "Regular updates as the situation develops, rather than waiting for a final report."),
            ]},
            {"type": "text", "h2": "Why Rapid Response Experience *Matters*",
             "paras": ["Time-sensitive investigations require the same judgment and composure required in federal crisis response work. Veritas brings that same discipline to urgent civilian matters, whether it's a family emergency or an active business risk."]},
            {"type": "bullets", "h2": "Who This Is *For*", "items": [
                "Families facing an urgent missing-persons situation",
                "Businesses responding to an active internal incident",
                "Attorneys facing a fast-approaching filing deadline that requires immediate investigative work",
                "Anyone facing a time-critical situation who needs an investigator to act quickly"]},
            {"type": "faq", "h2": "Common *Questions*", "items": [
                ("How fast can Veritas respond?", "Response times depend on the situation, but urgent matters are prioritized — contact Veritas directly to discuss timing for your specific circumstances."),
                ("Does this cost more than a standard investigation?", "Rapid-response engagements are scoped individually based on urgency and resource needs; this will be discussed clearly before work begins."),
                ("Is this only for domestic situations?", "No. Veritas has experience coordinating time-sensitive matters internationally as well as domestically, depending on the jurisdiction involved."),
            ]},
            {**NOT_SURE, "button": ("Contact Veritas Immediately", "contact")},
         ]},

        # 12. International Investigative Services
        {"slug": S("intl"), "trail": svc_trail("intl"), "service": "International Investigative Services",
         "service_offers": ["International Investigations", "Cross-Border Investigative Support", "International Investigative Coordination"],
         "title": "International Investigations from South Carolina",
         "meta": "Cross-border investigative support and international coordination, with particular depth in the Caribbean, Central America and South America.",
         "sections": [
            {"type": "hero", "h1": "International Investigative *Services*",
             "lead": "Veritas provides investigative support for matters that cross borders, drawing on direct experience coordinating with international law enforcement and government partners.",
             "buttons": [("Discuss an International Matter", "contact")]},
            {"type": "items", "h2": "What This *Covers*", "items": [
                ("International Investigations", "Support for matters involving individuals, assets, or activity outside the United States, coordinated through established international relationships and investigative experience, and subject to local laws in each jurisdiction."),
                ("Cross-Border Investigative Support", "Assistance connecting domestic matters to relevant facts, individuals, or records located internationally."),
                ("International Investigative Coordination", "Coordination with foreign law enforcement, government contacts, and vetted international partners, where appropriate and permitted, to support complex matters that cross jurisdictional lines."),
            ]},
            {"type": "steps", "h2": "How Veritas *Works*", "items": [
                ("Step 1: Initial Consultation.", "Understand the international dimension of the matter and what's realistically achievable."),
                ("Step 2: Coordination Plan.", "Identify the right partners, contacts, or resources needed in the relevant country or region."),
                ("Step 3: Investigation & Coordination.", "Work conducted directly or through vetted international partners, as the matter requires."),
                ("Step 4: Reporting.", "Clear reporting on findings and coordination outcomes."),
            ]},
            {"type": "text", "h2": "Why This Experience *Matters*",
             "paras": ["Few domestic PI firms have direct experience with international investigative work. Veritas's founder spent years coordinating with foreign government officials and law enforcement leaders on complex international matters — experience that informs private international investigative work."]},
            {"type": "bullets", "h2": "Who This Is *For*", "items": [
                "Attorneys and businesses with a matter involving individuals or assets abroad",
                "Individuals with a family or personal matter that crosses international borders",
                "Companies operating in or expanding into international markets, particularly the Caribbean, Central America, and South America"]},
            {"type": "faq", "h2": "Common *Questions*", "items": [
                ("Is Veritas licensed to conduct investigations outside the United States?", "Veritas is licensed as a private investigative firm in South Carolina. International work is conducted through direct experience, established relationships, and coordination with appropriately licensed or authorized partners in the relevant jurisdiction."),
                ("What regions does Veritas have the most experience in?", "Experience includes coordination across multiple regions, with particular depth in matters involving the Caribbean, Central America, and South America."),
                ("How does an international matter typically start?", "With a conversation about what's known, what's needed, and what's realistically achievable given the jurisdiction involved."),
            ]},
            {**NOT_SURE, "button": ("Discuss an International Matter", "contact")},
         ]},

        # 13. Background & Due Diligence
        {"slug": S("bg"), "trail": svc_trail("bg"), "service": "Background & Due Diligence",
         "service_offers": ["Pre-Employment Screening & Background Checks", "Personal & Professional Background Checks", "Individual & Executive Due Diligence", "Corporate Due Diligence"],
         "title": "Background Checks & Due Diligence in South Carolina",
         "meta": "Pre-employment screening, personal and executive background checks and corporate due diligence, verified by a licensed SC investigator.",
         "sections": [
            {"type": "hero", "h1": "Background & Due *Diligence*",
             "lead": "From pre-employment screening to corporate due diligence, Veritas provides the background research individuals and organizations need to make informed decisions with confidence.",
             "buttons": [("Request a Background Investigation", "contact")]},
            {"type": "items", "h2": "What This *Covers*", "items": [
                ("Pre-Employment Screening & Background Checks", "Verification of a candidate's background prior to hiring, conducted in compliance with applicable background screening laws."),
                ("Personal & Professional Background Checks", "Background research on an individual for personal or professional reasons — a new business partner, a caregiver, or someone entering your life in a significant way."),
                ("Individual & Executive Due Diligence", "Background investigation on a specific person — a prospective executive hire, business partner, or key individual — including criminal and litigation history, financial red flags, and credential verification."),
                ("Corporate Due Diligence", "Investigative due diligence on companies and business relationships — including ownership and litigation history, regulatory standing, and reputational risk review — to support partnerships, vendor relationships, and transactions."),
            ]},
            {"type": "steps", "h2": "How Veritas *Works*", "items": [
                ("Step 1: Scope the Request.", "Define exactly what needs to be verified and why."),
                ("Step 2: Research Plan.", "Identify which records, databases, and verification methods apply."),
                ("Step 3: Investigation.", "Conduct research using licensed investigative databases and, where needed, field verification."),
                ("Step 4: Reporting.", "Deliver a clear, organized report of findings."),
            ]},
            {"type": "text", "h2": "Why Thoroughness *Matters*",
             "paras": ["Background research is only as good as the diligence behind it. Veritas applies the same investigative standards used in federal casework to background and due diligence work — going beyond a database search to verify what matters most, where verification is possible."]},
            {"type": "bullets", "h2": "Who This Is *For*", "items": [
                "Employers hiring for sensitive or leadership positions",
                "Individuals entering a new personal or business relationship",
                "Companies evaluating a partner, vendor, or acquisition target",
                "Attorneys who need background verification to support a case"]},
            {"type": "faq", "h2": "Common *Questions*", "items": [
                ("How is this different from an online background check service?", "Many online services return database records automatically, with little or no verification. Veritas conducts investigative research, working to verify, contextualize, and follow up on what the records show. Records can be incomplete or out of date, so findings are reported with any limitations noted."),
                ("How long does a background investigation take?", "It depends on scope — a standard background check may take a few days, while corporate due diligence can take longer depending on complexity."),
                ("Is this compliant with background screening laws like the FCRA?", "Yes — background screening is conducted in compliance with applicable federal and state law."),
            ]},
            {**NOT_SURE, "button": ("Request a Background Investigation", "contact")},
         ]},

        # 14. Security Consulting & Risk Management
        {"slug": S("sec"), "trail": svc_trail("sec"), "service": "Security Consulting & Risk Management",
         "service_offers": ["Security & Risk Assessments", "Workplace Violence Response Planning", "Security Policies & Procedures"],
         "title": "Security Consulting & Risk Assessments, SC",
         "meta": "Security and risk assessments, workplace violence response planning and security policy reviews for hospitality and corporate clients in SC.",
         "sections": [
            {"type": "hero", "h1": "Security Consulting & Risk *Management*",
             "lead": "Veritas provides practical, experience-based security consulting to help organizations identify vulnerabilities and prepare for critical incidents before they happen.",
             "buttons": [("Request a Security Assessment", "contact")]},
            {"type": "items", "h2": "What This *Covers*", "items": [
                ("Security & Risk Assessments", "On-site or remote assessment of physical security, procedures, and vulnerabilities, with practical recommendations grounded in real investigative and law enforcement experience."),
                ("Workplace Violence Response Planning", "Development of response plans and training to prepare an organization for a critical workplace incident, built on experience with real-world crisis response."),
                ("Security Policies & Procedures", "Development or review of security policies and procedures to close gaps and align practices with actual risk."),
            ]},
            {"type": "steps", "h2": "How Veritas *Works*", "items": [
                ("Step 1: Initial Assessment.", "Understand the organization, its facilities, and its specific risk profile."),
                ("Step 2: Risk Review.", "A focused review of physical security, procedures, and any known vulnerabilities."),
                ("Step 3: Recommendations.", "Practical, prioritized recommendations, not a generic checklist."),
                ("Step 4: Implementation Support.", "Support developing or refining policies, procedures, or training as needed."),
            ]},
            {"type": "text", "h2": "Why Real-World Experience *Matters*",
             "paras": ["Security consulting is only as good as the experience behind it. Veritas draws on two decades of federal law enforcement and crisis response experience to provide security guidance that reflects how real incidents actually unfold — not just industry checklists."]},
            {"type": "bullets", "h2": "Who This Is *For*", "items": [
                "Hospitality and corporate operators wanting to assess physical security and vulnerabilities",
                "Organizations without an internal security function",
                "Businesses preparing workplace violence response plans for the first time",
                "Companies that experienced a security incident and want an outside review"]},
            {"type": "faq", "h2": "Common *Questions*", "items": [
                ("Is this a one-time assessment or an ongoing relationship?", "Both are available — some clients want a single assessment, others prefer an ongoing advisory relationship."),
                ("Do you provide training, not just consulting?", "Yes — training on topics like workplace violence response can be included as part of an engagement."),
                ("What industries does Veritas typically work with?", "Experience spans multiple sectors, with particular interest in hospitality and corporate clients seeking practical, real-world security guidance."),
            ]},
            {**NOT_SURE, "button": ("Request a Security Assessment", "contact")},
         ]},
    ],
}
