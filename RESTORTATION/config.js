const siteConfig = {
    // 1. GLOBAL IDENTITY (Default values, overridden if a lead is loaded)
    business_name: "Preferred 1 Restoration",
    city: "North Bay",
    state: "Ontario",
    service_area: "North Bay, Ontario",
    phone: "+1 249-358-7911",
    email: "emergency@preferred1restoration.ca",
    logo_text: "Preferred 1 Restoration", // Used if logo_url is empty
    logo_url: "", // e.g., "./images/logo.png"

    // 2. DESIGN SYSTEM & COLORS (Tailored for Water/Fire Restoration)
    primary_color: "#0f172a",   // Deep Slate Blue (Premium Dark Navy)
    secondary_color: "#ff6b35", // Glowing Safety Orange (Emergency / Heat / Fire)
    accent_color: "#0ea5e9",    // Electric Cyan (Clean Water / Dry Air)
    bg_color: "#f8fafc",        // Light Slate BG
    text_color: "#1e293b",      // Dark Slate Text

    // 3. SEO & TRUST DATA
    google_maps_description: "Preferred 1 Restoration is your trusted 24/7 disaster recovery partner in North Bay and surrounding areas. We provide rapid-response water damage restoration, structural drying, fire and smoke damage cleanup, mold remediation, and sewage extraction to protect your property and health.",
    trust_badges: [
        "★ 5.0 Google Rated Specialists",
        "Direct Insurance Billing",
        "45-Min Response Time",
        "Licensed, Bonded & Insured"
    ],

    // 4. SERVICES (2x2 Grid)
    services_list: [
        {
            title: "Water Damage Restoration",
            description: "Immediate water extraction, industrial dehumidification, and advanced thermal mapping to rescue flooded basements and burst pipes.",
            icon: "💧"
        },
        {
            title: "Fire & Smoke Cleanup",
            description: "Deep soot removal, smoke odor neutralizers, structural sanitizing, and full reconstruction to return your home to pre-loss condition.",
            icon: "🔥"
        },
        {
            title: "Mold Remediation",
            description: "Safe mold containment, HEPA air filtration, source removal, and moisture control to ensure healthy indoor air quality.",
            icon: "🦠"
        },
        {
            title: "Sewage & Emergency Services",
            description: "Biohazard sewage cleanup, emergency tarping, window board-ups, and storm damage response available 24/7.",
            icon: "🚨"
        }
    ],

    // 5. WHY CHOOSE US
    why_us: [
        "24/7 Emergency Dispatch - We Arrive in 45 Mins",
        "Direct Insurance Billing - We Handle All the Paperwork",
        "IICRC Certified Technicians Using State-Of-The-Art Gear",
        "Complete Restoration From Extraction to Full Rebuild"
    ],

    // 6. TESTIMONIALS
    reviews: [
        {
            name: "Sarah Jenkins",
            text: "A water pipe burst in our basement at 2 AM. Preferred 1 Restoration arrived in 35 minutes, extracted the water, and dried out the drywall. They handled the entire claim with our insurance. Unbelievable service!",
            rating: 5
        },
        {
            name: "Mark T.",
            text: "After a severe kitchen fire, the smoke damage was terrible. The crew was extremely thorough, eliminated all odor, and rebuilt our cabinets beautifully.",
            rating: 5
        },
        {
            name: "Emily R.",
            text: "Found black mold in our laundry room. They isolated the area immediately, removed the mold safely, and solved the leak. Professional and clean!",
            rating: 5
        }
    ]
};
