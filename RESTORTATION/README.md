# 💧 High-Converting Water Damage & Restoration Website Template Engine

This is a premium, high-converting, local SEO-optimized website template designed specifically for **Water Damage & Disaster Restoration Services**. It features a centralized configuration and a **Dynamic Lead Personalization Engine** that lets you instantly generate personalized site pitches for your leads.

---

## 📁 File Structure
- `index.html`: The core landing page layout engineered for high conversion rates.
- `seo-landing-page.html`: The landing page optimized for service-specific SEO routing.
- `style.css`: The premium design system (Bento Grids, Glassmorphism, polished animations).
- `template-engine.js`: The Javascript engine that handles DOM injection, automated SEO tagging, image loading, and the dynamic lead selector widget.
- `config.js`: Centralized file containing the default branding and text configurations.
- `leads-data.js`: A compiled JSON-style database of your 155 scraped leads.
- `Outscraper-20260512105555s92_water_damage_restoration_service_+2.xlsx`: The raw Excel lead file.

---

## 🎯 How to Pitch Leads Using This Template

This website template has been upgraded with a **Dynamic Lead Customizer** designed specifically for sales outreach. Instead of duplicating folders and manually editing files for every client, the template reads lead information directly from `leads-data.js` based on the URL.

### Method 1: The Floating Lead Customizer Panel (Self-Service Selector)
1. Open `index.html` in your browser (using any local server or simply double-clicking).
2. Look at the bottom-right corner. You will see a gear icon (`⚙️`).
3. Click it to open the **🎯 Lead Customizer** panel.
4. Select any of the **155 leads** from the dropdown menu.
5. The landing page will immediately reload and change to fit that business! The following elements are updated instantly:
   - **Business Name** (replaces all logo, heading, and footer mentions)
   - **Phone Number** (replaces header, CTA buttons, and links with their actual clickable `tel:` link)
   - **City & State** (localizes the hero section, subtitles, headings, and SEO meta tags)
   - **Google Review Rating** (updates the trust badge to display their actual star rating)
   - **Google Maps Listing Image** (automatically pulls the lead's Google Maps image/street view as the hero section background and the "About" section image)
   - **Address** (adds their official Google Maps address to the footer, linking directly to their directions)

### Method 2: Personalized URL Parameters
When sending pitches to prospective clients, you can send them a direct link with their lead ID.
- **Example Link:** `http://localhost:3000/index.html?lead=1` (Loads SRS Restoration)
- **Example Link:** `http://localhost:3000/index.html?lead=2` (Loads Preferred 1 Restoration)

To share this:
1. Open the Lead Customizer panel on the page.
2. Select the client in the dropdown.
3. Click the **"Copy Pitch Link"** button. This will copy the exact personalized URL to your clipboard.
4. Paste it into your email/SMS/outreach message!

---

## 🛠️ Modifying Defaults
If you want to change the default website colors or the fallback business details, open `config.js`:
- `primary_color`: Controls buttons, dark gradient overlays, and main text highlights (default is deep restoration blue `#0284c7`).
- `secondary_color`: Controls emergency buttons, alert badges, and attention grabbers (default is emergency orange `#f97316`).
- `services_list`: Modify the services, description, and emojis in the Bento Grid.

---

## 🤖 The Automated Restoration SEO Engine
When a lead is loaded via URL, the site automatically executes:
1. **Dynamic Titles:** Rewrites `<title>` to target the local city and state (e.g. `Preferred 1 Restoration | Top-Rated Damage Restoration in North Bay, Ontario`).
2. **Metadata Optimization:** Injects custom `<meta name="description">` using the local city and service type.
3. **Structured Schema:** Automatically generates a `WaterDamageRestorationService` JSON-LD schema payload in the head for Google rich snippet search visibility.
4. **Accessible Alt Tags:** Updates all images to have localized alt descriptions containing the client's business name and city.
