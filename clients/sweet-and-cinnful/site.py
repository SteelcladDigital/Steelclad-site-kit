"""Sweet & Cinnful — client config for Steelclad Site Kit.
Home bakery (no storefront, pickup + local delivery), Lexington SC. Email + order form only (no phone).
Build: python3 build.py sweet-and-cinnful [--preview]
Prices come from the client's published menu image (Nov 2026). Anything unconfirmed is listed in NOTES.md."""

EMAIL = "cinnamonrlarkin@gmail.com"

# ---------------------------------------------------------------- PHOTOS (client's own, cropped to remove people)
P = {
    "three": {"file": "gallery/number-3-garbage-truck-cake.jpg", "w": 744, "h": 830,
              "alt": "Number 3 birthday cake shaped like a road with green buttercream trim and a toy garbage truck",
              "caption": "Garbage-truck “3” cake for a third birthday"},
    "mermaid": {"file": "gallery/mermaid-birthday-cake.jpg", "w": 744, "h": 992,
                "alt": "Tall mermaid birthday cake in pink, lavender and teal buttercream with chocolate mermaid tails and piped flowers",
                "caption": "Mermaid ombré birthday cake"},
    "rodeo": {"file": "gallery/chocolate-birthday-cake.jpg", "w": 580, "h": 740,
              "alt": "Chocolate-glazed birthday cake with whipped cream rosettes, cookie crumbles and a rodeo cake topper",
              "caption": "Chocolate birthday cake for a rodeo party"},
    "holiday": {"file": "gallery/holiday-cookies-church-event.jpg", "w": 744, "h": 802,
                "alt": "Rows of white-chocolate-dipped holiday cookies with holly decorations on a long table",
                "caption": "Holiday cookies for a church event"},
    "xmas": {"file": "gallery/christmas-tree-cupcakes.jpg", "w": 744, "h": 992,
             "alt": "Christmas cupcakes topped with snack-cake tree pieces and red and green icing drizzle",
             "caption": "Christmas tree snack-cake cupcakes"},
    "bundt": {"file": "gallery/cookie-butter-bundt-cake.jpg", "w": 744, "h": 992,
              "alt": "Bundt cake topped with cookie butter drizzle, piped frosting and crushed spiced cookies",
              "caption": "Cookie butter bundt cake"},
    "cookie": {"file": "gallery/chocolate-butterscotch-cookie.jpg", "w": 744, "h": 992,
               "alt": "Thick cookie loaded with chocolate chips and butterscotch chips",
               "caption": "Chocolate chip & butterscotch cookies"},
    "cow": {"file": "gallery/cow-cupcakes.jpg", "w": 744, "h": 992,
            "alt": "A dozen cow-face cupcakes with white buttercream, black spots and pink noses",
            "caption": "Cow birthday cupcakes"},
}
ALL_PHOTOS = [P[k] for k in ("mermaid", "three", "cow", "holiday", "bundt", "xmas", "cookie", "rodeo")]

# ---------------------------------------------------------------- MENU (from the client's published menu)
MENU = [
    {"slug": "custom-cakes", "name": "Custom Cakes", "tag": "Most requested", "featured": True,
     "price": "$55 & up", "price_note": "Final price depends on size and design",
     "for": "Birthday, shower and celebration cakes in buttercream, designed around your theme.",
     "why": "You have a date, a theme and a crowd to feed.",
     "items": ["Your theme, colors and inspiration photos", "Your choice of flavor", "Number and shaped cakes",
               "Gluten-free and dietary requests reviewed with you"]},
    {"slug": "cupcakes", "name": "Cupcakes", "tag": "Party favorite",
     "price": "$30 / dozen", "price_note": "Two dozen for $50",
     "for": "Classic and seasonal flavors, decorated to match the party.",
     "why": "You want something easy to hand out.",
     "items": ["Classic and seasonal flavors", "Themed decorating", "Gluten-free requests welcome", "Order by the dozen"]},
    {"slug": "cookies", "name": "Cookies", "tag": "By the dozen",
     "price": "$30 / dozen", "price_note": "Big batches for events",
     "for": "Signature cookies and holiday trays, from one dozen to a whole event.",
     "why": "You're feeding a church, school or office crowd.",
     "items": ["Signature chocolate chip & butterscotch", "Holiday and seasonal cookies", "Event and party batches",
               "Cookie cakes from $45"]},
]

# ---------------------------------------------------------------- SERVICES (money pages, flat keyword URLs)
SERVICES = [
    {
        "slug": "custom-cakes-lexington-sc", "name": "Custom Cakes", "icon": "cake",
        "short": "Birthday, shower and celebration cakes in buttercream, built around your theme. From $55.",
        "title": "Custom Birthday Cakes in Lexington, SC",
        "meta": "Custom birthday and celebration cakes from a Lexington, SC home bakery. Buttercream, your theme and colors, from $55. Pickup or local delivery.",
        "h1": "Custom Cakes in Lexington, SC",
        "lead": "Birthday, shower and celebration cakes, designed around your theme and baked to order by Cinnamon Larkin in her Lexington home bakery. Custom cakes start at $55.",
        "included_title": "What goes into your custom cake",
        "included": [
            ("Your theme and colors", "Send your theme, color palette and inspiration photos with your order. Cinnamon designs the cake around them."),
            ("Your choice of flavor", "Pick a flavor preference on the order form, and Cinnamon will confirm it when she replies."),
            ("Number and shaped cakes", "From a road-shaped number 3 with a toy garbage truck to a tall mermaid cake in ombré buttercream."),
            ("Dietary notes up front", "Gluten-free requests and allergy notes go right on the order form, so they're part of the plan from the start."),
        ],
        "photos_title": "Recent custom cakes",
        "photos": [P["three"], P["mermaid"], P["rodeo"]],
        "signs_title": "Cake pricing at a glance",
        "signs": [
            "Custom cakes start at $55; size and design set the final price",
            "Cookie cakes start at $45",
            "Bundt cakes are $45",
            "Your price and details are confirmed before anything is baked",
        ],
        "faqs": [
            ("How much does a custom cake cost in Lexington, SC?", "Custom cakes from Sweet & Cinnful start at $55. The size, number of servings and decoration set the final price, which Cinnamon confirms after she reviews your request."),
            ("How far ahead should I order a birthday cake?", "As early as you can. Every cake is made by one baker, so popular dates fill up. Send your request with the date and Cinnamon will confirm whether it's available."),
            ("Can you make a gluten-free cake?", "Gluten-free requests are welcome. Choose your dietary needs on the order form and add any allergy notes, and Cinnamon will tell you what she can do for your order."),
            ("Can I send a picture of the cake I want?", "Yes. The order form has an upload for inspiration photos. Send as many as you like, along with your theme and colors."),
        ],
    },
    {
        "slug": "custom-cookies-lexington-sc", "name": "Cookies", "icon": "cookie",
        "short": "Signature cookies and holiday trays by the dozen, including big batches for events. $30 a dozen.",
        "title": "Cookies by the Dozen in Lexington, SC",
        "meta": "Signature chocolate chip, holiday and event cookies from a Lexington, SC home bakery. $30 a dozen, cookie cakes from $45. Order online.",
        "h1": "Cookies by the Dozen in Lexington, SC",
        "lead": "Thick signature cookies, dipped holiday cookies and big event batches, baked to order in Lexington. Cookies are $30 a dozen, and cookie cakes start at $45.",
        "included_title": "Cookies Cinnamon bakes",
        "included": [
            ("Signature cookies", "Thick, chewy cookies loaded with chocolate and butterscotch chips."),
            ("Holiday cookies", "White-chocolate-dipped holiday cookies with piped holly, made by the tray."),
            ("Event batches", "Church events, school parties and office trays. Send your headcount and date with the order."),
            ("Cookie cakes", "One giant cookie decorated for the occasion, from $45."),
        ],
        "photos_title": "Recent cookie orders",
        "photos": [P["holiday"], P["cookie"]],
        "signs_title": "Popular for",
        "signs": [
            "Church and school events",
            "Holiday trays and gifting",
            "Office treats and thank-you gifts",
            "Birthday party favors",
        ],
        "faqs": [
            ("How much are cookies?", "Cookies are $30 a dozen. Cookie cakes start at $45, depending on size and decoration."),
            ("Can you bake cookies for a big event?", "Yes. Large holiday and event batches, like the church-event cookies on this page, are part of what Cinnamon bakes. Send your count and date early so she can fit it in."),
        ],
    },
    {
        "slug": "cupcakes-lexington-sc", "name": "Cupcakes", "icon": "cupcake",
        "short": "Classic and seasonal flavors, decorated to your theme. $30 a dozen, $50 for two dozen.",
        "title": "Custom Cupcakes in Lexington, SC",
        "meta": "Themed and gluten-free-friendly cupcakes from a Lexington, SC home bakery. $30 a dozen or $50 for two dozen. Pickup or local delivery.",
        "h1": "Custom Cupcakes in Lexington, SC",
        "lead": "Classic and seasonal cupcakes, decorated to match your party, from a Lexington home bakery. Cupcakes are $30 a dozen or $50 for two dozen.",
        "included_title": "What makes these cupcakes yours",
        "included": [
            ("Themed decorating", "Cow faces for a farm birthday, snack-cake trees at Christmas. Tell Cinnamon the theme and she'll design the tops."),
            ("Classic and seasonal flavors", "Choose your flavor preference on the order form."),
            ("Gluten-free requests", "Choose gluten-free under dietary needs, add any allergy notes, and Cinnamon will confirm what she can make."),
            ("Party-ready counts", "Order by the dozen: $30 for 12 or $50 for 24."),
        ],
        "photos_title": "Recent cupcake orders",
        "photos": [P["cow"], P["xmas"]],
        "signs_title": "Great for",
        "signs": ["Kids' birthday parties", "Classroom celebrations", "Showers and holiday parties", "Anywhere slicing a cake is a hassle"],
        "faqs": [
            ("How much are cupcakes?", "Cupcakes are $30 for a dozen or $50 for two dozen."),
            ("Do you make gluten-free cupcakes?", "Gluten-free requests are welcome. Note it under dietary needs on the order form and Cinnamon will confirm what she can do."),
        ],
    },
]

# ---------------------------------------------------------------- AREAS (pickup in Lexington; delivery to confirm)
# NOTE: delivery radius not yet confirmed by the client; copy says "ask on your order". See NOTES.md.
AREAS = [
    {
        "slug": "custom-cakes-irmo-sc", "city": "Irmo", "county": "Lexington & Richland Counties", "zips": "29063",
        "intro": "Irmo families order birthday cakes, cupcakes and cookie trays from Sweet & Cinnful, a home bakery just down the road in Lexington. Pick up in Lexington, or ask about delivery to Irmo when you order.",
        "local": [
            ("Fall party season", "Irmo's fall calendar fills up fast, from the Okra Strut weekend to back-to-school birthdays. Send your date early so it's on Cinnamon's calendar."),
            ("Lake Murray get-togethers", "Lake and dock parties call for treats that travel. Cookies and cupcakes hold up better than a tall buttercream cake on a hot afternoon."),
            ("Easy hand-offs", "Pickup is in Lexington by arrangement. If you'd rather have it brought to you, choose delivery on the order form."),
        ],
        "faqs": [("Do you deliver custom cakes to Irmo?", "Delivery is available in some areas around Lexington. Choose delivery on the order form with your Irmo address and Cinnamon will confirm whether your date and location work.")],
    },
    {
        "slug": "custom-cakes-chapin-sc", "city": "Chapin", "county": "Lexington County", "zips": "29036",
        "intro": "From lake-house birthdays to church gatherings, Chapin orders custom cakes, cupcakes and cookies from Sweet & Cinnful in neighboring Lexington.",
        "local": [
            ("Lake weekends", "Chapin sits on the shores of Lake Murray. For boat days and dock parties, cookies and cupcakes are the easiest treats to pack and share."),
            ("Church and community events", "Cookies by the dozen make big gatherings simple. Send your headcount and Cinnamon will help size the order."),
            ("Plan around the heat", "Buttercream softens in the sun. Keep cakes in air conditioning until serving time. The party dessert guide has more tips."),
        ],
        "faqs": [("Can I get a custom cake for a Chapin event?", "Yes. Order online with your date and theme. Pickup is in Lexington, and you can ask about delivery to Chapin on the order form.")],
    },
    {
        "slug": "custom-cakes-west-columbia-sc", "city": "West Columbia", "county": "Lexington County", "zips": "29169, 29170, 29172",
        "intro": "West Columbia birthdays, showers and office parties get the same made-to-order cakes, cupcakes and cookies as Sweet & Cinnful's Lexington customers, a short drive up the road.",
        "local": [
            ("Office treats", "Cookies and cupcakes by the dozen are an easy thank-you for coworkers and clients."),
            ("Riverwalk picnics", "Heading to the riverfront? Cookies and cupcakes travel better than a tall layer cake on a warm day."),
            ("Quick pickup", "Pickup is in Lexington by arrangement, or ask about delivery when you order."),
        ],
        "faqs": [("Do you serve West Columbia?", "Yes. Many orders are picked up in Lexington, and you can request delivery to West Columbia on the order form. Cinnamon will confirm availability for your date.")],
    },
    {
        "slug": "custom-cakes-cayce-sc", "city": "Cayce", "county": "Lexington County", "zips": "29033",
        "intro": "Cayce customers order custom cakes, cupcakes and cookie trays from Sweet & Cinnful for birthdays, game days and holidays. Every order is baked by hand in Lexington.",
        "local": [
            ("Game-day and tailgate treats", "Cupcakes and cookies decorated in your team's colors are easy to share at a tailgate or watch party."),
            ("Holiday trays", "Dipped holiday cookies and seasonal cupcakes for family get-togethers and office parties."),
            ("Pickup or delivery", "Pick up in Lexington, or choose delivery on the order form and Cinnamon will confirm."),
        ],
        "faqs": [("Can you decorate cupcakes in team colors?", "Yes. Add your colors and any inspiration photos to the order form, and Cinnamon will design around them.")],
    },
    {
        "slug": "custom-cakes-gilbert-sc", "city": "Gilbert", "county": "Lexington County", "zips": "29054",
        "intro": "Gilbert's backyard birthdays and summer get-togethers deserve a cake made for the occasion. Sweet & Cinnful bakes custom cakes, cupcakes and cookies to order in nearby Lexington.",
        "local": [
            ("Summer celebrations", "Gilbert's summer runs from the Peach Festival on the Fourth of July to backyard birthdays. Keep buttercream cakes cool and out of direct sun until serving."),
            ("Farm-themed parties", "Cow-face cupcakes and other farm themes are a Sweet & Cinnful favorite. Send your idea with your order."),
            ("Rural delivery", "Pickup is in Lexington. If you're farther out, ask about delivery on the order form and Cinnamon will let you know."),
        ],
        "faqs": [("Do you deliver to Gilbert?", "Ask on the order form. Delivery is available in some areas around Lexington, and Cinnamon will confirm whether your address and date work.")],
    },
]

REVIEWS = [
    ("The Burns Family", "Lexington, SC", "Huge shoutout to Cinnamon. Not only are her sweets divine, but her warm personality made the whole process a joy. You can really taste the care she puts into every bite. Highly recommended!"),
    ("Kris L.", "Lexington, SC", "I cannot recommend Sweet & Cinnful enough! As someone who is gluten-free, Cinnamon was so accommodating! She made me the most amazing cupcakes, the texture and taste were incredible, and they looked stunning! Definitely order from her!"),
    ("Sam B.", "Lexington, SC", "Cinnamon truly makes some of the best desserts! Everything we've ordered has been top quality, both in taste and presentation. You can tell she puts so much care and heart into every order. Whether you need cookies, a cake, or cake pops, you really can't go wrong with anything on her menu! And her brownies? Easily one of my favorites - highly recommend giving her a try!"),
    ("Nichole C.", "Sweet & Cinnful customer", "Cinnamon is the absolute BEST! Not only are her treats delicious, she is one of the sweetest and caring people I know. From her cheesecakes to her cupcakes and everything in between, she should be everyone's go to for desserts!"),
]

GENERAL_FAQS = [
    ("How do I place an order?", "Fill out the custom order form with your date, what you'd like, your theme and any inspiration photos. Cinnamon reviews every request and gets back to you to confirm availability, price and next steps."),
    ("How much do custom cakes, cupcakes and cookies cost?", "Custom cakes start at $55, cupcakes are $30 a dozen ($50 for two dozen) and cookies are $30 a dozen. The full menu with every price is on the Menu & Prices page."),
    ("Do you deliver, or is it pickup only?", "Both. Orders can be picked up in Lexington by arrangement, and delivery is available in some nearby areas. Choose pickup or delivery on the order form and Cinnamon will confirm."),
    ("Can you accommodate gluten-free or allergy needs?", "Gluten-free and dietary requests are welcome. Choose your dietary needs on the order form and list every allergy, and Cinnamon will tell you what she can do. Everything is made in a home kitchen, so share all allergies up front."),
    ("How far in advance should I order?", "As early as you can. Sweet & Cinnful is a one-baker home bakery, so dates fill up, especially around holidays and graduation season."),
    ("Is Sweet & Cinnful a storefront bakery?", "No. It's a home bakery in Lexington, SC. Every order is made to order, so there's no walk-in counter. Pickup details come with your order confirmation."),
]

GUIDE_CARDS = [
    ("Up to 12 guests", "Family dinner or small birthday", ["A small round cake (6-inch is about 12 party slices)", "Or a dozen cupcakes", "Add a dozen cookies as take-home treats"]),
    ("15–25 guests", "Classroom or backyard party", ["An 8-inch round is about 24 party slices", "Or two dozen cupcakes ($50)", "A dozen cake pops for the kids' table ($24)"]),
    ("30–40 guests", "Showers and milestone birthdays", ["A 10-inch round is about 38 party slices", "Or a smaller cake plus two dozen cupcakes", "Brownies or cookies stretch the dessert table"]),
    ("50+ guests", "Church, school and office events", ["Cookies and cupcakes are the easiest to serve", "Plan on 1–2 cookies per guest", "Send your headcount and Cinnamon will help size it"]),
]

GUIDE_BODY = """<h2>Keeping buttercream happy in South Carolina heat</h2>
<p>Buttercream softens quickly in a Midlands summer. A few habits keep your cake looking the way it did at pickup:</p>
<ul>
<li><strong>Ride flat and cool.</strong> Set the box on a flat floorboard or trunk floor, not a slanted seat, and run the air conditioning before you load it.</li>
<li><strong>Go straight home.</strong> A parked car heats up fast. Make the bakery your last stop.</li>
<li><strong>Keep it inside until serving time.</strong> Outdoor parties are hard on buttercream. Keep the cake in air conditioning and bring it out when it's time to sing.</li>
<li><strong>Choose travel-friendly treats for the lake or a tailgate.</strong> Cookies and cupcakes hold up far better than a tall layer cake on a hot dock.</li>
</ul>
<h2>What to send with your order</h2>
<p>The <a href="/place-custom-order/">custom order form</a> asks for everything Cinnamon needs to plan your treats. Having these ready makes it quick:</p>
<ul>
<li>Your pickup or event date, and whether you need pickup or delivery</li>
<li>What you'd like (cake, cupcakes, cookies or a mix) and roughly how many guests</li>
<li>Your occasion, theme and color palette</li>
<li>Inspiration photos (the form takes uploads)</li>
<li>Flavor preference, dietary needs and every allergy</li>
<li>A budget, if you have one in mind</li>
</ul>
<p>Not sure how much to order? Put your headcount in the order and Cinnamon will recommend a size. You can see every starting price on the <a href="/menu-pricing-page/">menu &amp; prices</a> page.</p>"""


CONFIG = {
  "business": {
    "name": "Sweet & Cinnful", "legal_name": "Sweet & Cinnful",
    "domain": "https://sweetandcinnful.com",
    "phone": "", "tel": "",                      # no published phone: the kit shows email links instead
    "email": EMAIL,
    "schema_type": "Bakery", "price_range": "$$",
    "description": "Home bakery in Lexington, SC making custom cakes, cupcakes, cookies, cake pops and more to order, with pickup in Lexington and local delivery.",
    "address": {"locality": "Lexington", "region": "SC"},   # home bakery: no public street address
    "geo": (33.9815, -81.2362),
    "hours": [],
    "hours_text": "Pickup by arrangement",
    "counties": ["Lexington County, SC"],
    "founder": "Cinnamon Larkin",
    "slogan": "Baking smiles from my home to yours.",
    "knows_about": ["Custom cakes", "Birthday cakes", "Cupcakes", "Cookies", "Cake pops", "Gluten-free cupcakes"],
    "social": {"facebook": "https://facebook.com/cinnamon.larkin", "instagram": "https://instagram.com/__just_cinnamon"},
  },
  "theme": {
    "colors": {"primary": "#0e5966", "primary_deep": "#0a3f49", "secondary": "#5fbcd3", "secondary_deep": "#23798d",
               "secondary_wash": "#e8f6fa", "accent": "#f7b8d2", "accent_text": "#0a3f49", "surface": "#fff6f1",
               "ink": "#1f2a33", "muted": "#53606b"},
    "fonts": {"display": "fraunces", "body": "nunito-sans"},
    "radius": "round", "heading_case": "none", "divider": "wave", "texture": "none", "hero_layout": "image",
  },
  "logo": {"type": "image", "file": "logo.svg", "schema_file": "logo.png", "width": 152, "height": 72},   # client's Canva logo: vector lettering from her business card SVG (photo + decorations removed)
  "favicon_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#0e5966"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="17" fill="#ffc9de">S&amp;</text></svg>',
  "integrations": {
    "form_mode": "ghl_embed",
    "ghl_form_id": "iOW0QPcEwExTKLMCqQi5",   # existing "Custom Bakery Order Form" in the client's GHL sub-account
    "ghl_tracking_snippet": "",              # GHL > Settings > External Tracking > Copy Script (launch blocker)
    "ghl_chat_widget_id": "", "gtm_id": "", "google_reviews_url": ""},
  "launched": False,
  "labels": {
    "cta": "Place an Order", "cta_short": "Order", "cta_long": "Start Your Custom Order",
    "phone_prefix": "Email", "reach_verb": "Email",
    "alt_cta": ("See Menu & Prices", "menu-pricing-page"),
    "mbar_second_label": "Menu", "mbar_second_icon": "doc", "mbar_second_slug": "menu-pricing-page",
    "topbar_promise": "Custom cakes, cookies & cupcakes, baked to order in Lexington, SC",
    "footer_blurb": "A home bakery in Lexington, SC. Custom cakes, cupcakes and cookies, baked to order by Cinnamon Larkin.",
    "footer_services_title": "Menu",
    "reviews_title": "Raves & Craves",
    "cta_band_title": "Have a date coming up?",
    "cta_band_text": "Send your date, theme and inspiration photos. Cinnamon will confirm availability and price.",
    "aside_title": "Order from Cinnamon", "aside_text": "Questions before you order? Email her directly.",
    "aside_badges": "Home bakery · Lexington, SC · 5-star reviews",
  },
  "home": {
    "title": "Lexington SC Home Bakery: Custom Cakes & Cupcakes",
    "meta": "Custom cakes from $55, cupcakes and cookies $30 a dozen, baked to order by a Lexington, SC home bakery. Pickup or local delivery. Order online.",
    "eyebrow": "Home bakery · Lexington, SC",
    "h1": "Custom cakes, cookies &amp; cupcakes, <em>baked to order</em> in Lexington, SC",
    "lead": "Cinnamon Larkin bakes and decorates every order herself, from themed birthday cakes to trays of holiday cookies. Send your idea, and she'll confirm the details and price.",
    "secondary_cta": ("See Menu & Prices", "menu-pricing-page"),
    "proof": ["Prices posted up front", "Gluten-free requests welcome", "Pickup or local delivery"],
    "hero_image": P["mermaid"]["file"], "hero_image_alt": P["mermaid"]["alt"],
    "trust": [("cake", "Cakes from $55", "Buttercream, made to order"), ("star", "5-star reviews", "From Lexington families"),
              ("home", "One home baker", "Every order made by Cinnamon"), ("truck", "Pickup or delivery", "Choose on your order")],
    "gallery": {"eyebrow": "Favorite projects", "title": "Recent cakes, cupcakes and cookies",
                "lead": "Every order is designed around a theme, a date and a crowd. Here are a few favorites.",
                "photos": [P["three"], P["cow"], P["holiday"], P["bundt"], P["xmas"], P["cookie"]]},
    "why": {"eyebrow": "Meet the baker",
            "quote_html": "Baking smiles from <em>my home to yours.</em>",
            "body": "Sweet & Cinnful is Cinnamon Larkin's home bakery in Lexington. There's no factory and no counter staff, just one baker who plans, bakes and decorates every order for the people eating it.",
            "items": [("heart", "One baker, start to finish.", "Cinnamon designs, bakes and decorates every order herself."),
                      ("doc", "Prices posted up front.", "Starting prices for every cake, cupcake and cookie are on the menu, so you can plan before you ask."),
                      ("check", "Dietary needs taken seriously.", "Gluten-free requests and allergy notes are part of every order form."),
                      ("gift", "Made for your theme.", "Send your colors, theme and inspiration photos, and she'll design around them.")]},
    "steps": {"eyebrow": "How ordering works", "title": "From idea to pickup in four steps",
              "items": [("Send your request", "Use the order form to share your date, treats, theme, colors and inspiration photos."),
                        ("Cinnamon confirms", "She reviews every request and replies to confirm availability, price and details."),
                        ("Baked to order", "Your treats are baked and decorated for your date, never pulled from a case."),
                        ("Pickup or delivery", "Pick up in Lexington at an arranged time, or have it delivered where available.")]},
    "order": ["trust", "services", "gallery", "steps", "why", "reviews", "areas", "faq", "cta"],
  },
  "tiers": {
    "enabled": True, "slug": "menu-pricing-page", "nav_label": "Menu & Prices",
    "title": "Bakery Menu & Prices: Lexington, SC Home Bakery",
    "meta": "Sweet & Cinnful menu: custom cakes from $55, cupcakes $30/dozen, cookies $30/dozen, cake pops, brownies, bundt and cookie cakes. Lexington, SC.",
    "h1": "Menu &amp; Prices",
    "lead": "Every starting price, posted up front. Custom designs are confirmed after Cinnamon reviews your request, so you'll know the final price before anything is baked.",
    "home_title": "The favorites", "home_lead": "Cakes, cupcakes and cookies, baked to order in Lexington.",
    "price_label": "", "price_note": "",
    "card_cta": "Order {name}",
    "items": MENU,
    "addons": {"eyebrow": "Also on the menu", "title": "More treats",
               "lead": "Add these to a cake order or order them on their own.",
               "items": [("Cake Pops", "$24", "12 count"), ("Brownies", "$30", "12 count"),
                         ("Cookie Cakes", "$45 & up", "One giant cookie, decorated for the occasion"),
                         ("Bundt Cake", "$45", "Like the cookie butter bundt in the gallery"),
                         ("Cheesecake", "$45", "Whole cheesecake"), ("Mini Cheesecakes", "$30", "6 count")],
               "note": "Prices from Sweet & Cinnful's current menu. Larger or highly detailed designs are quoted individually."},
    "pricing_explainer": {"title": "How custom pricing works",
        "body_html": "<p>Menu prices are where each item starts. For custom cakes, the final price depends on how many people you're serving and how detailed the design is.</p><p>Send your request with your date, theme and inspiration photos. Cinnamon reviews it and replies with availability and your <strong>confirmed price before anything is baked</strong>.</p>",
        "factors_title": "What affects a custom price",
        "factors": ["Number of servings", "Cake size, shape and tiers", "Decorating detail and toppers", "Flavor and filling choices", "Dietary requests", "Delivery"]},
    "faqs": [GENERAL_FAQS[1], GENERAL_FAQS[3], GENERAL_FAQS[4],
             ("Can I order just a dozen of something?", "Yes. Cupcakes, cookies, brownies and cake pops are all sold by the dozen, so a small order is easy.")],
  },
  "services_hub": {"slug": "treats", "flat_urls": True, "nav_label": "Cakes & Treats",
    "title": "Custom Cakes, Cookies & Cupcakes in Lexington, SC",
    "meta": "Custom cakes from $55, cupcakes and cookies by the dozen, baked to order by Sweet & Cinnful, a home bakery in Lexington, SC.",
    "h1": "Custom Cakes, Cookies &amp; Cupcakes in Lexington, SC",
    "lead": "Everything is baked to order by one home baker in Lexington. Pick your treat, then send your date and theme.",
    "home_title": "What Cinnamon bakes", "home_lead": "Starting prices are right on the cards. Tap one to see recent orders and details."},
  "services": SERVICES,
  "areas": {
    "enabled": True, "hub_slug": "delivery-areas", "nav_label": "Areas", "link_prefix": "Custom Cakes",
    "hub_title": "Custom Cakes Near Lexington, SC: Areas Served",
    "hub_meta": "Custom cakes, cupcakes and cookies for Lexington, Irmo, Chapin, West Columbia, Cayce and Gilbert, SC. Pickup in Lexington or ask about delivery.",
    "hub_h1": "Custom Cakes for Lexington &amp; Nearby Towns",
    "hub_lead": "Every order is baked in Lexington. Pick up by arrangement, or ask about delivery to your town when you order.",
    "home_title": "Serving Lexington and nearby towns",
    "groups": [{"name": "Lake Murray area", "note": "Pickup in Lexington", "slugs": ["custom-cakes-irmo-sc", "custom-cakes-chapin-sc"]},
               {"name": "Around Lexington", "note": "Pickup in Lexington", "slugs": ["custom-cakes-west-columbia-sc", "custom-cakes-cayce-sc", "custom-cakes-gilbert-sc"]}],
    "outside_note": "Not listed? Ask about delivery on your order, or email",
    "service_where_text": "Orders are baked in Lexington and picked up there by arrangement. Customers also order from",
    "page_title": "Custom Cakes & Cupcakes in {city}, {region}",
    "page_meta": "Custom cakes, cupcakes and cookies for {city}, {region} from a Lexington home bakery. Cakes from $55. Pickup or ask about delivery.",
    "page_h1": "Custom Cakes, Cookies &amp; Cupcakes in {city}, {region}",
    "local_title": "Planning a party in {city}", "aside_title": "Order for {city}",
    "tiers_blurb_html": "Custom cakes start at <strong>$55</strong>, cupcakes and cookies are <strong>$30 a dozen</strong>, and cake pops are $24 for 12.",
    "services_listed": 3,
    "shared_faqs": [("How much is a custom cake in {city}?", "Custom cakes from Sweet & Cinnful start at $55. Cinnamon confirms your final price after reviewing your request, before anything is baked.")],
    "pages": AREAS,
  },
  "resource": {
    "enabled": True, "slug": "party-dessert-guide", "nav_label": "Party Guide",
    "title": "How Much Cake Do I Need? Party Dessert Guide",
    "meta": "How much cake, how many cupcakes and cookies per guest, and how to keep buttercream cool in South Carolina heat. A Lexington, SC baker's guide.",
    "h1": "How Much Cake Do I Need? A Party Dessert Guide",
    "lead": "A quick guide to sizing desserts by headcount, plus tips for getting buttercream through a South Carolina summer. Slice counts are typical party-size servings; Cinnamon will recommend a size for your order.",
    "cards": GUIDE_CARDS, "body_html": GUIDE_BODY, "faq_title": "Party dessert questions",
    "faqs": [("How many cupcakes should I order per guest?", "Plan on about one cupcake per guest, and a few extra for big eaters or second rounds. Two dozen covers most classroom and backyard parties."),
             ("How many cookies per person for an event?", "One to two cookies per guest works for most events. For a dessert table with other sweets, one each is usually plenty."),
             ("How do I keep a buttercream cake from melting outside?", "Keep it in air conditioning until serving time, out of direct sun, and transport it flat and cool. For outdoor events, cookies and cupcakes hold up better.")],
    "cta_title": "Tell Cinnamon your headcount", "cta_text": "Send your date and guest count with your order and she'll recommend the right size.",
  },
  "gallery_page": {"slug": "favorites", "nav_label": "Gallery",
    "title": "Custom Cake & Cupcake Gallery | Lexington, SC",
    "meta": "Photos of recent custom birthday cakes, cupcakes and cookies from Sweet & Cinnful, a home bakery in Lexington, SC.",
    "h1": "Favorite Projects", "lead": "A few favorite cakes, cupcakes and cookies from recent orders. See something you love? Send it as inspiration with your order.",
    "photos": ALL_PHOTOS,
    "cta_title": "Want something like this?", "cta_text": "Upload your inspiration photos on the order form and Cinnamon will design around them."},
  "blog": {"enabled": False},
  "about": {"title": "Meet Cinnamon Larkin | Sweet & Cinnful Bakery",
    "meta": "Meet Cinnamon Larkin, the founder and Chief Baking Officer of Sweet & Cinnful, a one-baker home bakery in Lexington, SC.",
    "h1": "Meet Cinnamon, the baker behind Sweet &amp; Cinnful",
    "lead": "Founder and Chief Baking Officer of a one-baker home bakery in Lexington, South Carolina.",
    "story_title": "Baking smiles from my home to yours",
    "story_html": "<p>Sweet &amp; Cinnful is Cinnamon Larkin's home bakery in Lexington, SC. She's the whole team: the person who reads your order, plans the design, bakes it and decorates it.</p><p>That's why her customers talk about the care as much as the cake. One gluten-free customer wrote that Cinnamon was <em>“so accommodating”</em>; another said you can taste the care she puts into every bite.</p><p>Her menu covers the celebrations Lexington families actually have: themed birthday cakes, cupcakes by the dozen, holiday cookies for church and school events, cake pops, brownies, bundt cakes and more.</p>",
    "list_title": "How Cinnamon works",
    "list": ["Every order baked and decorated by Cinnamon herself", "Designs built around your theme and photos",
             "Gluten-free and dietary requests reviewed with you", "Price and details confirmed before baking",
             "Pickup in Lexington or local delivery"]},
  "contact": {"slug": "place-custom-order", "title": "Place a Custom Order | Lexington, SC Bakery",
    "meta": "Order a custom cake, cupcakes or cookies from Sweet & Cinnful in Lexington, SC. Share your date, theme and inspiration photos online.",
    "h1": "Place a Custom Order",
    "lead": "Tell Cinnamon about your date, your treats and your theme. Upload inspiration photos if you have them. She'll review your request and reply to confirm availability, pricing and next steps.",
    "ghl_height": 1950, "page_type": "ContactPage",
    "next_steps": ["Cinnamon reviews your request", "She confirms availability, price and details", "Pickup in Lexington or delivery where available"],
    "faqs": [GENERAL_FAQS[2], GENERAL_FAQS[3], GENERAL_FAQS[4]]},
  "reviews": REVIEWS,
  "faqs": GENERAL_FAQS,
  "legal_pages": [("privacy-page", "Privacy Policy"), ("termsofservice", "Terms of Service"), ("accessibility", "Accessibility Statement")],
  "redirects": [("/privacy-policy", "/privacy-page/"), ("/order-now", "/place-custom-order/"), ("/menu", "/menu-pricing-page/"), ("/home", "/")],
}
