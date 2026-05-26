/* 
   Damage Restoration Website Template Engine
   Dynamically processes config.js and matches URL lead parameters.
*/

document.addEventListener("DOMContentLoaded", () => {
    // ==========================================
    // 1. DYNAMIC LEAD OVERRIDE SYSTEM
    // ==========================================
    const urlParams = new URLSearchParams(window.location.search);
    const leadIdParam = urlParams.get('lead');
    const leadNameParam = urlParams.get('leadName');

    let activeLead = null;

    // Search and match lead from leads-data.js
    if (typeof leadsData !== 'undefined' && leadsData.length > 0) {
        if (leadIdParam !== null) {
            const id = parseInt(leadIdParam, 10);
            if (id >= 0 && id < leadsData.length) {
                activeLead = leadsData[id];
            }
        } else if (leadNameParam !== null) {
            const query = leadNameParam.toLowerCase();
            activeLead = leadsData.find(l => l.name.toLowerCase().includes(query));
        }
    }

    // Apply lead data overrides to siteConfig
    if (activeLead) {
        siteConfig.business_name = activeLead.name;
        siteConfig.phone = activeLead.phone;
        siteConfig.city = activeLead.city;
        siteConfig.state = activeLead.state;
        siteConfig.service_area = activeLead.city && activeLead.city !== 'CA' ? `${activeLead.city}, ${activeLead.state}` : activeLead.state;
        siteConfig.logo_text = activeLead.name.length > 25 ? activeLead.name.substring(0, 22) + "..." : activeLead.name;
        siteConfig.google_maps_description = `${activeLead.name} is a premier certified restoration specialist in ${activeLead.city}, ${activeLead.state}. We provide 24/7 rapid water extraction, structural drying, mold remediation, and fire damage cleanup.`;
        
        // Dynamic rating badge
        if (activeLead.rating && activeLead.rating > 0) {
            siteConfig.trust_badges = [
                `★ ${activeLead.rating} Google Rated`,
                "Direct Insurance Billing",
                "45-Min Response Time",
                "IICRC Certified"
            ];
            
            // Add a personalized review based on rating
            siteConfig.reviews = [
                {
                    name: "Local Customer",
                    text: `Excellent service by ${activeLead.name}! They handled our restoration project in ${activeLead.city} with professional care. Highly recommended for any emergency cleanup.`,
                    rating: Math.round(activeLead.rating)
                },
                ...siteConfig.reviews.slice(0, 2)
            ];
        }
    }

    // ==========================================
    // 2. CSS VARIABLE INJECTION
    // ==========================================
    const root = document.documentElement;
    root.style.setProperty('--primary', siteConfig.primary_color);
    root.style.setProperty('--secondary', siteConfig.secondary_color);
    root.style.setProperty('--accent', siteConfig.accent_color);
    root.style.setProperty('--bg', siteConfig.bg_color);
    root.style.setProperty('--text', siteConfig.text_color);

    // ==========================================
    // 3. TEXT & DOM REPLACEMENTS
    // ==========================================
    const replaceText = (selector, text) => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(el => {
            if(el.tagName === 'A' && selector.includes('phone')) {
                el.href = `tel:${text.replace(/[^0-9+]/g, '')}`;
            }
            if(el.tagName === 'A' && selector.includes('email')) {
                el.href = `mailto:${text}`;
            }
            el.textContent = text;
        });
    };

    replaceText('[data-config="business_name"]', siteConfig.business_name);
    replaceText('[data-config="city"]', siteConfig.city);
    replaceText('[data-config="state"]', siteConfig.state);
    replaceText('[data-config="service_area"]', siteConfig.service_area);
    replaceText('[data-config="phone"]', siteConfig.phone);
    replaceText('[data-config="email"]', siteConfig.email);
    replaceText('[data-config="about_text"]', siteConfig.google_maps_description);

    // Handle Logo text/img
    const logoEl = document.getElementById('brand-logo');
    if (logoEl) {
        if (siteConfig.logo_url) {
            logoEl.innerHTML = `<img src="${siteConfig.logo_url}" alt="${siteConfig.business_name} Logo" style="max-height: 50px;">`;
        } else {
            logoEl.textContent = siteConfig.logo_text || siteConfig.business_name;
        }
    }

    // Inject Lead's Google Maps photo in Hero section and About image
    if (activeLead && activeLead.photo) {
        const heroEl = document.querySelector('.hero');
        if (heroEl) {
            heroEl.style.backgroundImage = `linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.8)), url('${activeLead.photo}')`;
        }
        const aboutImg = document.getElementById('about-image');
        if (aboutImg) {
            aboutImg.src = activeLead.photo;
            aboutImg.alt = `${activeLead.name} Facility/Listing Photo`;
        }
    }

    // Add Lead address in Footer if present
    if (activeLead && activeLead.address) {
        const footerContactLists = document.querySelectorAll('footer .footer-col ul');
        if (footerContactLists.length > 0) {
            const contactList = footerContactLists[0]; // First contact list
            const addressLi = document.createElement('li');
            addressLi.innerHTML = `Address: <a href="${activeLead.location_link}" target="_blank" style="text-decoration: underline; color: #94a3b8;">${activeLead.address}</a>`;
            contactList.appendChild(addressLi);
        }
    }

    // ==========================================
    // 4. RENDER DYNAMIC CARD LISTS
    // ==========================================
    // Trust Badges
    const badgeContainer = document.getElementById('trust-badges');
    if (badgeContainer && siteConfig.trust_badges) {
        badgeContainer.innerHTML = siteConfig.trust_badges.map(badge => 
            `<div class="badge">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="var(--secondary)">
                    <path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5zm-2 14l-4-4 1.41-1.41L10 13.17l6.59-6.59L18 8l-8 8z"/>
                </svg>
                <span>${badge}</span>
            </div>`
        ).join('');
    }

    // Services (4 grid cards)
    const gridServices = document.getElementById('services-grid');
    if (gridServices && siteConfig.services_list) {
        const cardImages = [
            './images/water_restoration.png',
            './images/fire_cleanup.png',
            './images/mold_remediation.png',
            './images/emergency_services.png'
        ];

        gridServices.innerHTML = siteConfig.services_list.map((srv, index) => {
            const bgImage = cardImages[index % cardImages.length];
            const bgStyle = `style="background-image: url('${bgImage}'); color: white;"`;
            
            return `
            <div class="service-card reveal-up" ${bgStyle}>
                <div class="service-icon" style="color: var(--primary); background: white;">${srv.icon}</div>
                <h3 style="color: white; font-size: 1.8rem; margin-bottom: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">${srv.title}</h3>
                <p style="color: rgba(255,255,255,0.95); font-size: 1.05rem; text-shadow: 0 1px 3px rgba(0,0,0,0.7);">${srv.description}</p>
            </div>
            `;
        }).join('');
    }

    // Why Choose Us
    const whyUsList = document.getElementById('why-us-list');
    if (whyUsList && siteConfig.why_us) {
        whyUsList.innerHTML = siteConfig.why_us.map(item => `
            <li>
                <svg width="24" height="24" viewBox="0 0 24 24" fill="var(--primary)"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                <span>${item}</span>
            </li>
        `).join('');
    }

    // Testimonials
    const reviewGrid = document.getElementById('reviews-grid');
    if (reviewGrid && siteConfig.reviews) {
        const starSVG = `<svg width="20" height="20" viewBox="0 0 24 24" fill="var(--accent)"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>`;
        reviewGrid.innerHTML = siteConfig.reviews.map(rev => {
            const stars = starSVG.repeat(rev.rating);
            return `
            <div class="review-card reveal-up">
                <div class="stars">${stars}</div>
                <p class="review-text">"${rev.text}"</p>
                <div class="review-author">- ${rev.name}</div>
            </div>
            `;
        }).join('');
    }

    // ==========================================
    // 5. INTERACTIVE & SCROLL ANIMATIONS
    // ==========================================
    // Before/After Slider Interactivity
    const initBeforeAfterSliders = () => {
        const containers = document.querySelectorAll('.before-after-container');
        containers.forEach(container => {
            const slider = container.querySelector('.before-after-slider');
            if (!slider) return;
            
            let isDragging = false;
            
            const setPosition = (clientX) => {
                const rect = slider.getBoundingClientRect();
                let percentage = ((clientX - rect.left) / rect.width) * 100;
                if (percentage < 0) percentage = 0;
                if (percentage > 100) percentage = 100;
                
                container.style.setProperty('--clip-pos', `${percentage}%`);
            };
            
            const onStart = (e) => {
                isDragging = true;
                const clientX = e.touches ? e.touches[0].clientX : e.clientX;
                setPosition(clientX);
            };
            
            const onMove = (e) => {
                if (!isDragging) return;
                const clientX = e.touches ? e.touches[0].clientX : e.clientX;
                setPosition(clientX);
            };
            
            const onEnd = () => {
                isDragging = false;
            };
            
            // Mouse events
            slider.addEventListener('mousedown', onStart);
            window.addEventListener('mousemove', onMove);
            window.addEventListener('mouseup', onEnd);
            
            // Touch events
            slider.addEventListener('touchstart', onStart, { passive: true });
            window.addEventListener('touchmove', onMove, { passive: true });
            window.addEventListener('touchend', onEnd);
        });
    };
    initBeforeAfterSliders();
    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetEl = document.querySelector(targetId);
            
            if (targetEl) {
                if (targetId === '#booking') {
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                    targetEl.classList.remove('flash-attention');
                    void targetEl.offsetWidth; 
                    targetEl.classList.add('flash-attention');
                    setTimeout(() => {
                        if(targetEl) targetEl.classList.remove('flash-attention');
                    }, 30000);
                } else {
                    targetEl.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // Scroll reveal observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

    document.querySelectorAll('.reveal-up').forEach(el => observer.observe(el));

    // ==========================================
    // 6. AUTO LOCAL SEO & SCHEMA INJECTION
    // ==========================================
    const setupIndepthSEO = () => {
        document.title = `${siteConfig.business_name} | Top-Rated Damage Restoration in ${siteConfig.city}, ${siteConfig.state}`;

        let metaDesc = document.querySelector('meta[name="description"]');
        if (!metaDesc) {
            metaDesc = document.createElement('meta');
            metaDesc.name = "description";
            document.head.appendChild(metaDesc);
        }
        
        const primaryService = siteConfig.services_list[0]?.title || "Damage Restoration";
        const cleanDesc = `${siteConfig.business_name} provides professional ${primaryService} in ${siteConfig.city}, ${siteConfig.state}. ${siteConfig.google_maps_description}`.substring(0, 155);
        metaDesc.content = cleanDesc + "...";

        // Open Graph Tags
        const ogTags = [
            { property: 'og:title', content: document.title },
            { property: 'og:description', content: metaDesc.content },
            { property: 'og:type', content: 'website' },
            { property: 'og:locale', content: 'en_US' }
        ];

        ogTags.forEach(tagData => {
            let meta = document.createElement('meta');
            meta.setAttribute('property', tagData.property);
            meta.setAttribute('content', tagData.content);
            document.head.appendChild(meta);
        });

        // Schema.org WaterDamageRestorationService
        const schemaJSON = {
            "@context": "https://schema.org",
            "@type": "WaterDamageRestorationService",
            "name": siteConfig.business_name,
            "image": activeLead && activeLead.photo ? activeLead.photo : "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=800&q=80",
            "telephone": siteConfig.phone,
            "email": siteConfig.email,
            "address": {
                "@type": "PostalAddress",
                "addressLocality": siteConfig.city,
                "addressRegion": siteConfig.state,
                "addressCountry": "CA"
            },
            "url": window.location.href,
            "description": metaDesc.content,
            "priceRange": "$$$",
            "openingHoursSpecification": [
                {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ],
                    "opens": "00:00",
                    "closes": "23:59"
                }
            ]
        };

        if (activeLead && activeLead.address) {
            schemaJSON.address.streetAddress = activeLead.address;
        }

        const scriptEl = document.createElement('script');
        scriptEl.type = 'application/ld+json';
        scriptEl.text = JSON.stringify(schemaJSON, null, 2);
        document.head.appendChild(scriptEl);
        
        // Image Alt Attributes
        document.querySelectorAll('img').forEach((img, index) => {
            if (!img.alt || img.alt.trim() === '') {
                img.alt = `${siteConfig.business_name} in ${siteConfig.city} - Damage Restoration Specialists Image ${index+1}`;
            }
        });
    };

    setupIndepthSEO();

    // ==========================================
    // 7. FLOATING LEAD DEMO CONTROLLER
    // ==========================================
    const injectDemoPanel = () => {
        if (typeof leadsData === 'undefined' || leadsData.length === 0) return;

        // CSS Styles for panel
        const style = document.createElement('style');
        style.innerHTML = `
            .demo-panel {
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 320px;
                background: rgba(255, 255, 255, 0.85);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
                z-index: 99999;
                font-family: 'Plus Jakarta Sans', sans-serif;
                color: #1e293b;
                overflow: hidden;
                transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.3s ease;
                font-size: 14px;
            }
            .demo-panel.minimized {
                transform: translate(260px, 120px) scale(0.3);
                opacity: 0;
                pointer-events: none;
            }
            .demo-trigger {
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 54px;
                height: 54px;
                border-radius: 50%;
                background: linear-gradient(135deg, var(--primary), #0284c7);
                color: white;
                box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
                border: none;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 99998;
                font-size: 24px;
                transition: transform 0.2s ease;
            }
            .demo-trigger:hover {
                transform: scale(1.05);
            }
            .demo-panel-header {
                background: var(--primary);
                color: white;
                padding: 12px 16px;
                font-weight: 800;
                display: flex;
                justify-content: space-between;
                align-items: center;
                letter-spacing: 0.5px;
            }
            .demo-panel-body {
                padding: 16px;
            }
            .demo-panel-row {
                margin-bottom: 12px;
            }
            .demo-panel-label {
                font-weight: 700;
                font-size: 11px;
                text-transform: uppercase;
                color: #64748b;
                margin-bottom: 4px;
                display: block;
            }
            .demo-select {
                width: 100%;
                padding: 8px 12px;
                border-radius: 8px;
                border: 1px solid #cbd5e1;
                background: white;
                font-family: inherit;
                font-size: 13px;
                color: inherit;
                cursor: pointer;
                outline: none;
            }
            .demo-select:focus {
                border-color: var(--primary);
            }
            .demo-btn {
                width: 100%;
                padding: 8px 12px;
                border-radius: 8px;
                background: #f1f5f9;
                color: #1e293b;
                font-weight: 700;
                border: 1px solid #cbd5e1;
                cursor: pointer;
                text-align: center;
                font-size: 12px;
                display: inline-block;
                box-sizing: border-box;
                transition: background 0.2s ease;
            }
            .demo-btn:hover {
                background: #e2e8f0;
            }
            .demo-btn-primary {
                background: var(--secondary);
                color: white;
                border: none;
            }
            .demo-btn-primary:hover {
                background: #ea580c;
            }
            .demo-meta-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 8px;
                margin-bottom: 12px;
                background: #f8fafc;
                padding: 10px;
                border-radius: 8px;
                border: 1px dashed #cbd5e1;
            }
            .demo-meta-val {
                font-weight: 600;
                color: #0f172a;
            }
            .demo-close-btn {
                background: none;
                border: none;
                color: white;
                font-weight: bold;
                font-size: 16px;
                cursor: pointer;
                opacity: 0.8;
            }
            .demo-close-btn:hover {
                opacity: 1;
            }
            .demo-toast {
                position: fixed;
                bottom: 90px;
                right: 20px;
                background: #1e293b;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                z-index: 100000;
                font-weight: 600;
                transform: translateY(20px);
                opacity: 0;
                transition: all 0.3s ease;
                pointer-events: none;
            }
            .demo-toast.show {
                transform: translateY(0);
                opacity: 1;
            }
        `;
        document.head.appendChild(style);

        // Toast element
        const toast = document.createElement('div');
        toast.className = 'demo-toast';
        toast.textContent = 'Demo link copied!';
        document.body.appendChild(toast);

        // Floating trigger button
        const trigger = document.createElement('button');
        trigger.className = 'demo-trigger';
        trigger.innerHTML = '⚙️';
        trigger.title = 'Open Lead Demo Panel';
        document.body.appendChild(trigger);

        // Control Panel card
        const panel = document.createElement('div');
        panel.className = 'demo-panel minimized';
        
        // Populate options
        const leadOptions = leadsData.map((lead, idx) => {
            const isSelected = activeLead && activeLead.id === lead.id;
            return `<option value="${lead.id}" ${isSelected ? 'selected' : ''}>#${lead.id} - ${lead.name.substring(0, 30)} (${lead.city})</option>`;
        }).join('');

        const selectedIndex = activeLead ? activeLead.id : "";
        const ratingVal = activeLead ? `${activeLead.rating} ★` : "N/A";
        const cityVal = activeLead ? activeLead.city : "Default";
        const typeVal = activeLead ? activeLead.type.replace(" service", "") : "Default";

        panel.innerHTML = `
            <div class="demo-panel-header">
                <span>🎯 Lead Customizer</span>
                <button class="demo-close-btn" id="demo-close">×</button>
            </div>
            <div class="demo-panel-body">
                <div class="demo-panel-row">
                    <label class="demo-panel-label">Select Client Lead</label>
                    <select class="demo-select" id="demo-select-lead">
                        <option value="">-- Default Template --</option>
                        ${leadOptions}
                    </select>
                </div>
                
                <div class="demo-meta-grid">
                    <div>
                        <span class="demo-panel-label">Rating</span>
                        <span class="demo-meta-val" id="demo-meta-rating">${ratingVal}</span>
                    </div>
                    <div>
                        <span class="demo-panel-label">City</span>
                        <span class="demo-meta-val" id="demo-meta-city">${cityVal}</span>
                    </div>
                    <div style="grid-column: span 2; margin-top: 4px;">
                        <span class="demo-panel-label">Business Type</span>
                        <span class="demo-meta-val" id="demo-meta-type" style="font-size: 11px;">${typeVal}</span>
                    </div>
                </div>

                <div class="demo-panel-row" style="display: flex; gap: 8px;">
                    <button class="demo-btn demo-btn-primary" id="demo-copy" style="flex: 1;">Copy Pitch Link</button>
                    <button class="demo-btn" id="demo-reset" style="flex: 1;">Reset</button>
                </div>
                
                ${activeLead ? `
                <div class="demo-panel-row" style="margin-bottom: 0; text-align: center;">
                    <a href="${activeLead.location_link}" target="_blank" style="color: var(--primary); font-weight: 700; text-decoration: underline; font-size: 12px;">View Original Google Maps Listing ↗</a>
                </div>` : ''}
            </div>
        `;
        document.body.appendChild(panel);

        // Panel toggle events
        trigger.addEventListener('click', () => {
            panel.classList.remove('minimized');
            trigger.style.transform = 'scale(0)';
        });

        document.getElementById('demo-close').addEventListener('click', () => {
            panel.classList.add('minimized');
            setTimeout(() => {
                trigger.style.transform = 'scale(1)';
            }, 200);
        });

        // Dropdown selection change
        const select = document.getElementById('demo-select-lead');
        select.addEventListener('change', (e) => {
            const val = e.target.value;
            const url = new URL(window.location.href);
            if (val === "") {
                url.searchParams.delete('lead');
            } else {
                url.searchParams.set('lead', val);
            }
            window.location.href = url.toString();
        });

        // Copy button
        document.getElementById('demo-copy').addEventListener('click', () => {
            const url = new URL(window.location.href);
            if (select.value) {
                url.searchParams.set('lead', select.value);
            } else {
                url.searchParams.delete('lead');
            }
            
            navigator.clipboard.writeText(url.toString()).then(() => {
                toast.classList.add('show');
                setTimeout(() => {
                    toast.classList.remove('show');
                }, 2000);
            });
        });

        // Reset button
        document.getElementById('demo-reset').addEventListener('click', () => {
            const url = new URL(window.location.href);
            url.searchParams.delete('lead');
            window.location.href = url.toString();
        });

        // If a lead is active, automatically expand the panel on first load to show options, but allow closing it
        if (activeLead && !sessionStorage.getItem('demo_panel_closed')) {
            panel.classList.remove('minimized');
            trigger.style.transform = 'scale(0)';
        }
        
        document.getElementById('demo-close').addEventListener('click', () => {
            sessionStorage.setItem('demo_panel_closed', 'true');
        });
    };

    injectDemoPanel();
});
