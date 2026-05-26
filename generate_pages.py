import os
import re

# Read template file
source_path = '/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/decora-website.html'
with open(source_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Helper to extract blocks from decora-website.html
def extract_head_template(html):
    # Extract up to </head>
    head_part = html.split('</head>')[0]
    # Remove existing title, description, keywords, canonical
    head_part = re.sub(r'<title>.*?</title>', '', head_part)
    head_part = re.sub(r'<meta name="description" [^>]+>', '', head_part)
    head_part = re.sub(r'<meta name="keywords" [^>]+>', '', head_part)
    head_part = re.sub(r'<link rel="canonical" [^>]+>', '', head_part)
    head_part = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head_part, flags=re.DOTALL)
    return head_part.strip()

def extract_nav(html):
    start_tag = '<!-- ========== NAV ========== -->'
    end_tag = '<!-- ========== HERO ========== -->'
    if start_tag in html and end_tag in html:
        return start_tag + html.split(start_tag)[1].split(end_tag)[0]
    return ""

def extract_contact_form(html):
    start_tag = '<!-- ========== CONTACT & QUOTE FORM ========== -->'
    end_tag = '<!-- ========== AREAS SERVED ========== -->'
    if start_tag in html and end_tag in html:
        return start_tag + html.split(start_tag)[1].split(end_tag)[0]
    return ""

def extract_footer(html):
    start_tag = '<!-- ========== FOOTER ========== -->'
    end_tag = '<script>'
    if start_tag in html and end_tag in html:
        return start_tag + html.split(start_tag)[1].split(end_tag)[0]
    return ""

def extract_scripts(html):
    start_tag = '<script>'
    if start_tag in html:
        return start_tag + html.split(start_tag)[-1]
    return ""

# Common elements
head_base = extract_head_template(template_content)
nav_block = extract_nav(template_content)
contact_block = extract_contact_form(template_content)
footer_block = extract_footer(template_content)
scripts_block = extract_scripts(template_content)

# Define sub-page list
services = {
    'building-envelope': {
        'title': 'Building Envelope Restoration Toronto | Decora Building Restoration',
        'description': 'Expert building envelope restoration in Toronto and the GTA. Façade repair, waterproofing, cladding & sealant systems. Free site assessment. Call 416-285-7788.',
        'keywords': 'building envelope restoration Toronto, facade repair Toronto, waterproofing contractor Toronto, cladding repair Toronto, sealant systems Toronto',
        'h1': 'Building Envelope Restoration in Toronto & the GTA',
        'subtitle': 'Comprehensive engineering-grade repair, waterproofing, and rehabilitation of your building\'s exterior envelope system.',
        'breadcrumbs': '→ <a href="/services/building-envelope/" style="color: var(--white); text-decoration: none;">Building Envelope Restoration</a>',
        'schema': '''{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Building Envelope Restoration",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Decora Building Restoration Ltd",
    "telephone": "+1-416-285-7788"
  },
  "areaServed": {
    "@type": "City",
    "name": "Toronto"
  },
  "description": "Comprehensive repair and rehabilitation of your building's exterior systems — walls, cladding, sealants, flashing, and waterproofing. We stop water before it becomes a structural crisis."
}''',
        'faq_schema': '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is building envelope restoration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Building envelope restoration is the repair and reinforcement of all components that separate a building's interior from the outside environment. This includes exterior walls, cladding, sealants, waterproofing membranes, insulation, and flashing systems to prevent water leaks and drafts."
      }
    },
    {
      "@type": "Question",
      "name": "How often should window sealants and caulking be replaced?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Window sealants and expansion joints typically last between 10 to 15 years depending on environmental exposure. We recommend annual inspections to catch cracking, shrinking, or adhesion loss before water penetrates the interior."
      }
    },
    {
      "@type": "Question",
      "name": "Do you work directly with building engineers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, Decora regularly collaborates with third-party engineering consultants, property managers, and condo boards. We provide fully compliant documentation, transparent change-order workflows, and adhere strictly to project specifications."
      }
    }
  ]
}''',
        'content': '''
        <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; align-items: start;">
          <div>
            <h2 class="display display-sm" style="margin-bottom: 1.5rem;">Protecting Your Asset From Water & Structural Degradation</h2>
            <p style="font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
              The building envelope is your property\'s primary line of defense against the harsh Canadian climate. When sealants fail, brick spalls, or cladding pulls away, moisture finds a path inside. Over time, water infiltration compromises structural concrete, rusts steel reinforcing bars, and leads to expensive emergency repairs. At Decora Building Restoration, we specialize in sealing, repairing, and insulating commercial and multi-residential envelopes.
            </p>
            <p style="font-size: 1rem; line-height: 1.8; margin-bottom: 2rem; color: var(--text-secondary);">
              Our building envelope services are engineered to address the root causes of failure rather than just masking the symptoms. By utilizing state-of-the-art membranes, industrial-grade sealants, and premium masonry matching, we restore thermal performance and prevent structural decay.
            </p>

            <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">Our Comprehensive Envelope Scope</h3>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 3rem;">
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Façade Repair & Restoration</strong>
                <span style="color: var(--text-secondary);">Structural repairs to concrete panels, EIFS, cladding, and exterior wood or composite finishes. We fix cracking, displacement, and degradation.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Window Sealants & Expansion Joints</strong>
                <span style="color: var(--text-secondary);">Removal and replacement of failed caulking, polyurethane sealants, and structural expansion joints. We ensure continuous thermal and moisture barriers.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Exterior Cladding Repair & Replacement</strong>
                <span style="color: var(--text-secondary);">Securing, repairing, or completely replacing failing metal panels, stucco, siding, and curtain wall flashing systems.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Waterproofing Membranes</strong>
                <span style="color: var(--text-secondary);">Installation of liquid-applied and sheet-applied air/vapour barriers behind cladding systems to ensure long-term dryness.</span>
              </li>
            </ul>

            <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">Why Address Envelope Failure Early?</h3>
            <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
              Delaying envelope maintenance is one of the costliest decisions a condo board or property owner can make. What starts as a small window leak can expand into structural concrete spalling, rusted steel lintels, mold growth inside drywall cavities, and skyrocketing energy bills due to heat loss. Decora provides detailed inspections and staging plans so repairs can be executed in phases, optimizing reserve fund allocation and minimizing tenant disruption.
            </p>
          </div>

          <div style="background: var(--dark-surface); padding: 2.5rem; border-radius: 12px; border: 1px solid var(--border);">
            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Key Indicators of Failure</h4>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1rem; font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 2rem;">
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Damp drywall or water stains near windows</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Cracked, peeling, or missing window caulking</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Mortar crumbling or white salt stains on brickwork</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Bulging bricks or misaligned exterior cladding</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Sudden draftiness or rising heating costs</li>
            </ul>

            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Our Process</h4>
            <ol style="padding-left: 1.2rem; color: var(--text-secondary); font-size: 0.9rem; line-height: 1.8;">
              <li style="margin-bottom: 0.5rem;">Visual & thermal drone inspections.</li>
              <li style="margin-bottom: 0.5rem;">Engineering report coordination and cost planning.</li>
              <li style="margin-bottom: 0.5rem;">High-durability sealant injection and membrane lay.</li>
              <li style="margin-bottom: 0.5rem;">Rigorous water testing to guarantee zero leaks.</li>
            </ol>
          </div>
        </div>

        <!-- Custom FAQ for this Service -->
        <div style="margin-top: 5rem; border-top: 1px solid var(--border); padding-top: 4rem;">
          <h3 class="display display-sm" style="text-align: center; margin-bottom: 3rem;">Frequently Asked Questions</h3>
          <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.5rem;">
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;" open>
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">What is building envelope restoration?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                Building envelope restoration is the repair and reinforcement of all components that separate a building's interior from the outside environment. This includes exterior walls, cladding, sealants, waterproofing membranes, insulation, and flashing systems to prevent water leaks and drafts.
              </p>
            </details>
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;">
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">How often should window sealants and caulking be replaced?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                Window sealants and expansion joints typically last between 10 to 15 years depending on environmental exposure. We recommend annual inspections to catch cracking, shrinking, or adhesion loss before water penetrates the interior.
              </p>
            </details>
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;">
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">Do you work directly with building engineers?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                Yes, Decora regularly collaborates with third-party engineering consultants, property managers, and condo boards. We provide fully compliant documentation, transparent change-order workflows, and adhere strictly to project specifications.
              </p>
            </details>
          </div>
        </div>
        '''
    },
    'balcony-restoration': {
        'title': 'Balcony Restoration & Repair Toronto | Decora Building Restoration',
        'description': 'Balcony slab restoration, waterproofing membranes & structural repair for condos and multi-residential buildings in Toronto and the GTA. Call 416-285-7788.',
        'keywords': 'balcony restoration Toronto, balcony repair Toronto, balcony slab restoration, condo balcony waterproofing, concrete balcony repair GTA',
        'h1': 'Balcony Restoration & Repair for Toronto Condos',
        'subtitle': 'Professional concrete slab restoration, waterproofing membranes, railing upgrades, and structural rehabilitation for condo balconies.',
        'breadcrumbs': '→ <a href="/services/balcony-restoration/" style="color: var(--white); text-decoration: none;">Balcony Restoration</a>',
        'schema': '''{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Balcony Restoration & Repair",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Decora Building Restoration Ltd",
    "telephone": "+1-416-285-7788"
  },
  "areaServed": {
    "@type": "City",
    "name": "Toronto"
  },
  "description": "Concrete slab restoration, membrane waterproofing, railing upgrades, and structural rehabilitation for condo balconies and terraces — compliant with RCA and condo regulations."
}''',
        'faq_schema': '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does a typical balcony restoration project take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a mid-rise condominium, a comprehensive balcony restoration project typically takes between 8 to 14 weeks depending on the number of balconies, the extent of concrete decay, and weather conditions."
      }
    },
    {
      "@type": "Question",
      "name": "Can we use balconies during the restoration process?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For safety reasons, balconies are strictly off-limits to residents during concrete chipping, membrane application, and railing installation. We coordinate closely with property managers to minimize noise and access disruption."
      }
    },
    {
      "@type": "Question",
      "name": "Why is concrete balcony spalling dangerous?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Concrete spalling (chipping and cracking) exposes internal steel rebar to moisture and salt, causing it to rust and expand. This expansion breaks the surrounding concrete further, posing structural safety risks and overhead falling hazards."
      }
    }
  ]
}''',
        'content': '''
        <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; align-items: start;">
          <div>
            <h2 class="display display-sm" style="margin-bottom: 1.5rem;">Slab Delamination, Railing Integrity, and Waterproofing Membranes</h2>
            <p style="font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
              Balconies are highly vulnerable to the freeze-thaw cycles of Toronto winters. When road salts (chlorides) are carried by wind or tracked onto balconies, they dissolve in moisture and seep into the concrete. This triggers corrosion of the internal structural steel reinforcement. As steel rusts, it expands up to ten times its original volume, cracking and fracturing the concrete slab. This structural decay, known as spalling, poses extreme safety hazards.
            </p>
            <p style="font-size: 1rem; line-height: 1.8; margin-bottom: 2rem; color: var(--text-secondary);">
              Decora Building Restoration provides comprehensive balcony rehabilitation services for high-rise and mid-rise residential condominiums. We replace delaminated concrete, apply industrial-grade waterproofing traffic coatings, and upgrade structural railing assemblies to bring buildings up to current Ontario Building Code standards.
            </p>

            <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">Our Balcony Restoration Capabilities</h3>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 3rem;">
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Concrete Slab Edge & Underside Repair</strong>
                <span style="color: var(--text-secondary);">Chipping out deteriorated concrete, cleaning and coating exposed rebar, and executing structural concrete patches to restore the original profile.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Waterproofing Membrane Systems</strong>
                <span style="color: var(--text-secondary);">Application of high-performance elastomeric polyurethane membranes that seal concrete against water and salt intrusion, featuring anti-slip texture.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Railing Upgrade & Post Pocket Repairs</strong>
                <span style="color: var(--text-secondary);">Replacing outdated railings with modern aluminum and glass systems, ensuring secure post anchorage and repairing corrosion around structural pocket embeds.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Condo Board & Resident Coordination</strong>
                <span style="color: var(--text-secondary);">Providing comprehensive scheduling, dust mitigation, balcony access management, and regular progress reports for property managers and residents.</span>
              </li>
            </ul>

            <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">A Typical Balcony Restoration Project</h3>
            <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
              Balcony restoration is an intrusive process. Chipping concrete generates loud noise and dust. That\'s why we develop detailed tenant-communication guides. We phase our work (e.g., doing one stack or vertical elevation at a time) so that residents know exactly when their balcony will be worked on. Typically, a project on a 20-storey tower takes 10 to 14 weeks to complete, resulting in balconies that are structurally sound, look brand new, and are protected for another 20+ years.
            </p>
          </div>

          <div style="background: var(--dark-surface); padding: 2.5rem; border-radius: 12px; border: 1px solid var(--border);">
            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Warning Signs of Balcony Failure</h4>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1rem; font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 2rem;">
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Rust stains bleeding through concrete undersides</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Cracking or peeling paint/coatings on the floor</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Loose, wobbly, or rusting railing posts</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Small pieces of concrete falling from slab edges</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Water pooling against the building wall due to poor slope</li>
            </ul>

            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Our Guarantee</h4>
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.7;">
              Every balcony membrane installation is backed by our comprehensive warranty. We use materials from market leaders (Sika, BASF) and ensure absolute code compliance.
            </p>
          </div>
        </div>

        <!-- Custom FAQ for this Service -->
        <div style="margin-top: 5rem; border-top: 1px solid var(--border); padding-top: 4rem;">
          <h3 class="display display-sm" style="text-align: center; margin-bottom: 3rem;">Frequently Asked Questions</h3>
          <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.5rem;">
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;" open>
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">How long does a typical balcony restoration project take?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                For a mid-rise condominium, a comprehensive balcony restoration project typically takes between 8 to 14 weeks depending on the number of balconies, the extent of concrete decay, and weather conditions.
              </p>
            </details>
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;">
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">Can we use balconies during the restoration process?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                For safety reasons, balconies are strictly off-limits to residents during concrete chipping, membrane application, and railing installation. We coordinate closely with property managers to minimize noise and access disruption.
              </p>
            </details>
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;">
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">Why is concrete balcony spalling dangerous?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                Concrete spalling (chipping and cracking) exposes internal steel rebar to moisture and salt, causing it to rust and expand. This expansion breaks the surrounding concrete further, posing structural safety risks and overhead falling hazards.
              </p>
            </details>
          </div>
        </div>
        '''
    },
    'masonry-repair': {
        'title': 'Masonry Repair & Tuck Pointing Toronto | Decora Building Restoration',
        'description': 'Brick repair, mortar repointing, tuck pointing & lintel restoration for commercial and multi-residential buildings across Toronto and the GTA. Call 416-285-7788.',
        'keywords': 'masonry repair Toronto, tuck pointing Toronto, brick repair Toronto, brick repointing GTA, lintel repair Toronto, mortar repointing Toronto',
        'h1': 'Masonry Repair & Tuck Pointing in Toronto & the GTA',
        'subtitle': 'Expert brick repair, mortar tuck pointing, lintel restoration, and heritage masonry preservation for commercial properties.',
        'breadcrumbs': '→ <a href="/services/masonry-repair/" style="color: var(--white); text-decoration: none;">Masonry Repair & Tuck Pointing</a>',
        'schema': '''{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Masonry Repair & Tuck Pointing",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Decora Building Restoration Ltd",
    "telephone": "+1-416-285-7788"
  },
  "areaServed": {
    "@type": "City",
    "name": "Toronto"
  },
  "description": "Brick replacement, mortar repointing, spandrel repair, lintel restoration, and concrete block work. We match existing materials so repairs are invisible to the eye and durable for decades."
}''',
        'faq_schema': '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the difference between tuck pointing and repointing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Repointing is the process of removing deteriorated mortar joints between bricks and replacing them with fresh mortar. Tuck pointing is a decorative technique that adds a contrasting, thin line of mortar (often white) over the repointed joint to give the illusion of perfectly straight, narrow joints."
      }
    },
    {
      "@type": "Question",
      "name": "Can mortar repointing be done in winter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, but special precautions must be taken. Mortar cannot freeze while curing, so we use temporary heating enclosures and specialized low-temperature mortar formulations when working in freezing temperatures."
      }
    },
    {
      "@type": "Question",
      "name": "Why are my building's bricks cracking and breaking?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bricks usually crack (spall) due to trapped moisture freezing and expanding inside the brick. This can be caused by failed mortar joints, leaking flashing, or improper coatings that seal moisture inside the brick instead of letting it breathe."
      }
    }
  ]
}''',
        'content': '''
        <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; align-items: start;">
          <div>
            <h2 class="display display-sm" style="margin-bottom: 1.5rem;">Preserving Structural Stability and Aesthetic Value</h2>
            <p style="font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
              Brick and mortar have been the foundation of Toronto\'s architecture for over a century. However, mortar joints are designed to be softer and more porous than the bricks themselves, serving as an escape route for moisture. Over time, wind, rain, and freezing winters wear away this mortar, leaving joints hollow. Without the support of solid mortar, bricks absorb excessive water, crack, bulge, and eventually fall out of the wall, leading to major structural collapse.
            </p>
            <p style="font-size: 1rem; line-height: 1.8; margin-bottom: 2rem; color: var(--text-secondary);">
              Decora Building Restoration provides professional masonry repair and tuck pointing services. We match the chemical composition, density, and color of your building\'s historical or modern mortar, ensuring that our structural repairs blend in invisibly and stand up to decades of weathering.
            </p>

            <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">Our Masonry Solutions Include</h3>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 3rem;">
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Mortar Repointing & Tuck Pointing</strong>
                <span style="color: var(--text-secondary);">Removing decayed mortar to a depth of 1 inch using dust-controlled grinders and replacing it with high-strength, breathable mortar.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Structural Lintel & Shelf Angle Replacement</strong>
                <span style="color: var(--text-secondary);">Restoring rusted steel lintels over windows and masonry shelf angles, which expand and cause horizontal masonry cracking (often called "jacking").</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Spalled & Damaged Brick Replacement</strong>
                <span style="color: var(--text-secondary);">Carefully removing damaged brick units and replacing them with color-matched salvage or new heritage bricks.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Water Repellents & Breathable Coatings</strong>
                <span style="color: var(--text-secondary);">Application of silane/siloxane sealers that prevent water absorption while letting vapor escape from the masonry.</span>
              </li>
            </ul>

            <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">The Importance of Material Matching</h3>
            <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
              Using modern Portland cement on historical lime-based masonry is one of the most common mistakes in restoration. Portland cement is too hard and dense for old brick, trapping water and causing the brick face to shatter. Our specialists perform laboratory mortar analysis to determine the exact blend of sand, lime, and cement required for your building.
            </p>
          </div>

          <div style="background: var(--dark-surface); padding: 2.5rem; border-radius: 12px; border: 1px solid var(--border);">
            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">When to Call Decora</h4>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1rem; font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 2rem;">
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Mortar crumbling, falling out, or easily scraped away</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Bricks with cracked faces or missing chunks</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Horizontal cracks following mortar lines near windows</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Bricks pushing outward from the flat plane of the wall</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> White, powdery salt deposits (efflorescence) on exterior brick</li>
            </ul>

            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Our Heritage Standards</h4>
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.7;">
              We adhere strictly to the Standards and Guidelines for the Conservation of Historic Places in Canada for all heritage projects.
            </p>
          </div>
        </div>

        <!-- Custom FAQ for this Service -->
        <div style="margin-top: 5rem; border-top: 1px solid var(--border); padding-top: 4rem;">
          <h3 class="display display-sm" style="text-align: center; margin-bottom: 3rem;">Frequently Asked Questions</h3>
          <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.5rem;">
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;" open>
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">What is the difference between tuck pointing and repointing?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                Repointing is the process of removing deteriorated mortar joints between bricks and replacing them with fresh mortar. Tuck pointing is a decorative technique that adds a contrasting, thin line of mortar (often white) over the repointed joint to give the illusion of perfectly straight, narrow joints.
              </p>
            </details>
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;">
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">Can mortar repointing be done in winter?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                Yes, but special precautions must be taken. Mortar cannot freeze while curing, so we use temporary heating enclosures and specialized low-temperature mortar formulations when working in freezing temperatures.
              </p>
            </details>
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;">
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">Why are my building's bricks cracking and breaking?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                Bricks usually crack (spall) due to trapped moisture freezing and expanding inside the brick. This can be caused by failed mortar joints, leaking flashing, or improper coatings that seal moisture inside the brick instead of letting it breathe.
              </p>
            </details>
          </div>
        </div>
        '''
    },
    'parking-garage-restoration': {
        'title': 'Parking Garage Restoration Toronto | Decora Building Restoration',
        'description': 'Underground parking garage rehabilitation in Toronto and the GTA. Slab repair, traffic decks, waterproofing & structural repair. Call 416-285-7788.',
        'keywords': 'parking garage restoration Toronto, underground parking garage repair Toronto, parking garage slab repair, traffic deck restoration GTA, concrete slab repair parking garage Toronto',
        'h1': 'Parking Garage Rehabilitation & Restoration in Toronto',
        'subtitle': 'Heavy commercial slab repair, columns, traffic deck membranes, expansion joints, drainage, and cathodic protection.',
        'breadcrumbs': '→ <a href="/services/parking-garage-restoration/" style="color: var(--white); text-decoration: none;">Parking Garage Restoration</a>',
        'schema': '''{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Parking Garage Rehabilitation",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Decora Building Restoration Ltd",
    "telephone": "+1-416-285-7788"
  },
  "areaServed": {
    "@type": "City",
    "name": "Toronto"
  },
  "description": "Underground and above-grade garage restoration including slab repairs, column repairs, traffic decks, drainage systems, and cathodic protection. We keep your garage functional and structurally sound."
}''',
        'faq_schema': '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why is water dripping from my parking garage ceiling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Water dripping from the ceiling is usually a sign of a failed expansion joint, cracked slab, or broken waterproofing membrane on the level above. This water contains dissolved road salts, which accelerate structural concrete corrosion."
      }
    },
    {
      "@type": "Question",
      "name": "What is a traffic deck coating?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A traffic deck coating is an elastomeric, multi-layered polyurethane membrane applied to concrete floors in garages. It prevents water, vehicle oil, and road salts from soaking into the concrete and corroding the steel rebar."
      }
    },
    {
      "@type": "Question",
      "name": "How does cathodic protection work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cathodic protection is an electrochemical system that prevents concrete corrosion. By applying a very low electrical current to the internal steel rebar, we neutralize the chemical process that causes steel to rust."
      }
    }
  ]
}''',
        'content': '''
        <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; align-items: start;">
          <div>
            <h2 class="display display-sm" style="margin-bottom: 1.5rem;">Slab Delamination, Traffic Deck Coatings, and Cathodic Protection</h2>
            <p style="font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
              Underground parking garages represent one of the largest structural maintenance items for multi-residential and commercial properties. Because vehicles bring in water, salt, and snow during Toronto\'s winters, the concrete slab is constantly exposed to chlorides. When these chemicals soak into the slab, they corrode the steel reinforcing structure. The concrete then delaminates, columns crack, and expansion joints fail, letting water leak into lower levels.
            </p>
            <p style="font-size: 1rem; line-height: 1.8; margin-bottom: 2rem; color: var(--text-secondary);">
              Decora Building Restoration provides comprehensive parking garage rehabilitation. Our team has the specialized engineering capabilities required to repair post-tensioned slabs, apply high-durability traffic deck systems, install cathodic protection, and rebuild drainage systems.
            </p>

            <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">Our Garage Restoration Capabilities</h3>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 3rem;">
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Full & Partial Depth Slab Repair</strong>
                <span style="color: var(--text-secondary);">Chipping out delaminated concrete, reinforcing or replacing rusted structural rebar, and casting new high-strength concrete patches.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Traffic Deck Membranes</strong>
                <span style="color: var(--text-secondary);">Application of heavy-duty, slip-resistant polyurethane deck coatings (e.g., Sika or MasterBuilders) that seal the slab against water and chloride penetration.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Structural Column & Wall Repair</strong>
                <span style="color: var(--text-secondary);">Repairing load-bearing columns, shear walls, and foundation cracks via epoxy injection or concrete form-and-pour techniques.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Expansion Joints & Drainage Upgrades</strong>
                <span style="color: var(--text-secondary);">Installing heavy-duty elastomeric gland expansion joints and cleaning or replacing drain lines to prevent water accumulation.</span>
              </li>
            </ul>

            <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">Institutional and Public Infrastructure Experience</h3>
            <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
              Our portfolio includes major parking garage rehabilitation projects for municipal and institutional clients. Notable projects include the heavy structural slab repairs at the **Region of Peel (Sheridan Villa)** and the full multi-level waterproofing and traffic deck installation at the **City of Kitchener (City Hall Garage)**. We operate under rigorous health, safety, and air-filtration guidelines to allow garages to remain partially occupied during construction.
            </p>
          </div>

          <div style="background: var(--dark-surface); padding: 2.5rem; border-radius: 12px; border: 1px solid var(--border);">
            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Garage Risk Indicators</h4>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1rem; font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 2rem;">
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Water dripping through ceiling expansion joints</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Powdery white stains (leaching) on concrete ceilings</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Rust stains on concrete floors or columns</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Hollow sounding spots on floors when driven over</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Concrete chunks breaking away from columns or beams</li>
            </ul>

            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Our Qualifications</h4>
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.7;">
              Decora is WSIB compliant, fully bonded, and carries comprehensive commercial liability insurance. We work with all leading structural engineering firms in Ontario.
            </p>
          </div>
        </div>

        <!-- Custom FAQ for this Service -->
        <div style="margin-top: 5rem; border-top: 1px solid var(--border); padding-top: 4rem;">
          <h3 class="display display-sm" style="text-align: center; margin-bottom: 3rem;">Frequently Asked Questions</h3>
          <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.5rem;">
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;" open>
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">Why is water dripping from my parking garage ceiling?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                Water dripping from the ceiling is usually a sign of a failed expansion joint, cracked slab, or broken waterproofing membrane on the level above. This water contains dissolved road salts, which accelerate structural concrete corrosion.
              </p>
            </details>
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;">
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">What is a traffic deck coating?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                A traffic deck coating is an elastomeric, multi-layered polyurethane membrane applied to concrete floors in garages. It prevents water, vehicle oil, and road salts from soaking into the concrete and corroding the steel rebar.
              </p>
            </details>
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;">
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">How does cathodic protection work?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                Cathodic protection is an electrochemical system that prevents concrete corrosion. By applying a very low electrical current to the internal steel rebar, we neutralize the chemical process that causes steel to rust.
              </p>
            </details>
          </div>
        </div>
        '''
    },
    'maintenance-programs': {
        'title': 'Building Maintenance Programs Toronto | Decora Building Restoration',
        'description': 'Preventative building maintenance and inspections for condominium corporations and commercial properties in Toronto & the GTA. Call 416-285-7788.',
        'keywords': 'building maintenance program Toronto, preventative building maintenance GTA, commercial building inspection Toronto, condo building maintenance GTA',
        'h1': 'Preventative Building Maintenance Programs in Toronto',
        'subtitle': 'Proactive inspections, seasonal waterproofing touch-ups, and minor concrete repairs to extend the lifespan of your structural assets.',
        'breadcrumbs': '→ <a href="/services/maintenance-programs/" style="color: var(--white); text-decoration: none;">Maintenance Programs</a>',
        'schema': '''{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Building Maintenance Programs",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Decora Building Restoration Ltd",
    "telephone": "+1-416-285-7788"
  },
  "areaServed": {
    "@type": "City",
    "name": "Toronto"
  },
  "description": "Proactive building maintenance, annual inspections, and minor concrete or sealant repairs for condo corporations, commercial property owners, and managers."
}''',
        'faq_schema': '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is included in a building maintenance program?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our programs include annual visual inspections of the building envelope, balcony slabs, and parking garage. They also cover minor repairs like window caulking touch-ups, localized concrete patch repairs, drain cleaning, and sealant membrane inspections."
      }
    },
    {
      "@type": "Question",
      "name": "How does preventative maintenance save money?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "By catching small hairline cracks, failing caulking joints, or minor membrane tears early, we prevent water from reaching internal reinforcing steel. Restoring a small area costs a fraction of a full-scale structural overhaul."
      }
    }
  ]
}''',
        'content': '''
        <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; align-items: start;">
          <div>
            <h2 class="display display-sm" style="margin-bottom: 1.5rem;">Annual Inspections, Sealant Maintenance, and Minor Repairs</h2>
            <p style="font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
              Many property managers only call a restoration contractor when there is a major leak, concrete chunk falls off, or an engineering firm fails their structural assessment. At this point, the repairs are already extremely costly, loud, and disruptive. A proactive, scheduled maintenance program is the single most effective tool to extend the life of your building\'s concrete and masonry systems while protecting your reserve fund.
            </p>
            <p style="font-size: 1rem; line-height: 1.8; margin-bottom: 2rem; color: var(--text-secondary);">
              Decora Building Restoration designs custom, multi-year maintenance and inspection packages. We check your building envelope, balconies, and parking garages on a regular schedule, executing minor repairs before they turn into major structural emergencies.
            </p>

            <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">Our Maintenance Offerings Include</h3>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 3rem;">
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Annual Exterior visual Inspections</strong>
                <span style="color: var(--text-secondary);">A comprehensive visual walk-through and report by our restoration specialists to check the integrity of your masonry, concrete, and coatings.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Local Caulking & Sealant Maintenance</strong>
                <span style="color: var(--text-secondary);">Inspecting window frames, roof flashing, and structural expansion joints, replacing localized failed sections to keep the envelope watertight.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Drainage & Expansion Joint Flush</strong>
                <span style="color: var(--text-secondary);">Clearing dirt, debris, and winter road salts from parking garage drainage systems and expansion joint glands to prevent standing water and concrete corrosion.</span>
              </li>
              <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Localized Slab Patching</strong>
                <span style="color: var(--text-secondary);">Chipping out and patching small areas of concrete spalling on balconies or in parking garages before reinforcement decay spreads.</span>
              </li>
            </ul>

            <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">Reserve Fund Planning Support</h3>
            <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
              Condominium corporations in Ontario are required to perform Reserve Fund Studies every three years. Decora works alongside engineering firms and condo boards to help forecast structural maintenance costs. By integrating preventative maintenance into your long-term plan, we help smooth out expenditures, preventing sudden, massive special assessments and keeping condo fees stable.
            </p>
          </div>

          <div style="background: var(--dark-surface); padding: 2.5rem; border-radius: 12px; border: 1px solid var(--border);">
            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Benefits of Proactive Care</h4>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1rem; font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 2rem;">
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Extends structural concrete lifespan by up to 15 years</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Saves up to 70% compared to emergency concrete repairs</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Prevents sudden, costly special assessments for condo owners</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Clear compliance documentation for insurers and engineers</li>
              <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Enhanced safety for residents and pedestrians</li>
            </ul>
          </div>
        </div>

        <!-- Custom FAQ for this Service -->
        <div style="margin-top: 5rem; border-top: 1px solid var(--border); padding-top: 4rem;">
          <h3 class="display display-sm" style="text-align: center; margin-bottom: 3rem;">Frequently Asked Questions</h3>
          <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.5rem;">
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;" open>
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">What is included in a building maintenance program?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                Our programs include annual visual inspections of the building envelope, balcony slabs, and parking garage. They also cover minor repairs like window caulking touch-ups, localized concrete patch repairs, drain cleaning, and sealant membrane inspections.
              </p>
            </details>
            <details style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem;">
              <summary style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 500; cursor: pointer; color: var(--white); margin-bottom: 0.75rem;">How does preventative maintenance save money?</summary>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; padding-left: 1rem;">
                By catching small hairline cracks, failing caulking joints, or minor membrane tears early, we prevent water from reaching internal reinforcing steel. Restoring a small area costs a fraction of a full-scale structural overhaul.
              </p>
            </details>
          </div>
        </div>
        '''
    }
}

about_page = {
    'title': 'About Decora Building Restoration | 35 Years Serving Toronto & the GTA',
    'description': 'Family-owned commercial restoration contractor serving Toronto and the GTA since 1990. Specialists in concrete, envelope, balcony & masonry. Call 416-285-7788.',
    'keywords': 'building restoration company Toronto, best building restoration contractor GTA, licensed restoration contractor Toronto, insured building contractor Toronto',
    'h1': 'About Decora Building Restoration Ltd.',
    'subtitle': 'A family-owned commercial restoration contractor delivering engineering-grade craftsmanship in Toronto since 1990.',
    'breadcrumbs': '→ <span style="color: var(--white);">About Us</span>',
    'schema': '''{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "mainEntity": {
    "@type": "LocalBusiness",
    "name": "Decora Building Restoration Ltd",
    "telephone": "+1-416-285-7788",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "319 Comstock Rd",
      "addressLocality": "Scarborough",
      "addressRegion": "ON",
      "postalCode": "M1L 2H3",
      "addressCountry": "CA"
    }
  }
}''',
    'content': '''
    <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; align-items: start;">
      <div>
        <h2 class="display display-sm" style="margin-bottom: 1.5rem;">Quality, Accountability, and Structural Longevity</h2>
        <p style="font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
          Founded in 1990, Decora Building Restoration Ltd. has spent over three decades building a reputation as one of the GTA\'s most trusted structural restoration contractors. What began as a family-owned masonry business has grown into a full-service commercial, multi-residential, and institutional contractor. Our core focus remains unchanged: protecting and restoring the physical envelope and concrete structures of the buildings where Ontarians live and work.
        </p>
        <p style="font-size: 1rem; line-height: 1.8; margin-bottom: 2rem; color: var(--text-secondary);">
          Unlike large corporate conglomerates, Decora is built on personal accountability. Our leadership team remains directly involved in every project, working closely with property managers, condominium boards, and structural engineering firms to deliver on-time, compliant, and transparent results.
        </p>

        <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">Our Core Principles</h3>
        <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 3rem;">
          <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
            <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Engineering-First Mindset</strong>
            <span style="color: var(--text-secondary);">We do not cover up structural issues. We work with engineering consultants to address the source of concrete degradation, moisture leaks, and masonry failure.</span>
          </li>
          <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
            <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Family-Owned Accountability</strong>
            <span style="color: var(--text-secondary);">Every project is backed by our family name. If a challenge arises, our leadership is on-site within hours to resolve it.</span>
          </li>
          <li style="border-left: 3px solid var(--gold); padding-left: 1.5rem;">
            <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.25rem; color: var(--white);">Decades of GTA Experience</strong>
            <span style="color: var(--text-secondary);">We know how local buildings age under Southern Ontario\'s extreme climate. We understand the specific rules, guidelines, and bylaws of Toronto-area municipalities.</span>
          </li>
        </ul>

        <h3 class="display display-sm" style="margin-bottom: 1.25rem; font-size: 1.8rem;">A Track Record You Can Trust</h3>
        <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
          From high-rise condominium complexes in Scarborough and North York to commercial parking garages in Mississauga, our work stands the test of time. We have successfully delivered infrastructure projects for public sector entities like the **Region of Peel (Sheridan Villa)** and the **City of Kitchener (City Hall Garage)**. We carry comprehensive bonding, full WSIB compliance, and $10 million in commercial liability insurance.
        </p>
      </div>

      <div style="background: var(--dark-surface); padding: 2.5rem; border-radius: 12px; border: 1px solid var(--border);">
        <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1.25rem; color: var(--white);">Our Credentials</h4>
        <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1rem; font-size: 0.9rem; color: var(--text-secondary);">
          <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Fully Licensed & Registered in Ontario</li>
          <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> WSIB Compliant & Good Standing</li>
          <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> $10M Commercial Liability Insurance</li>
          <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> Bonded for Large-Scale Municipal Works</li>
          <li style="display: flex; gap: 0.5rem; align-items: start;"><span style="color: var(--gold);">✓</span> 35+ Years Active Construction Experience</li>
        </ul>
      </div>
    </div>
    '''
}

contact_page = {
    'title': 'Contact Decora Building Restoration | Free GTA Site Assessment',
    'description': 'Contact Decora Building Restoration for building envelope, balcony, masonry, and garage restoration in Toronto & the GTA. Call 416-285-7788.',
    'keywords': 'licensed restoration contractor Toronto, building restoration reviews Toronto, contact building restoration Toronto',
    'h1': 'Get In Touch',
    'subtitle': 'Request your free, no-obligation site assessment. Fill out the form or call us directly. We respond to all inquiries within one business day.',
    'breadcrumbs': '→ <span style="color: var(--white);">Contact</span>',
    'schema': '''{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "mainEntity": {
    "@type": "LocalBusiness",
    "name": "Decora Building Restoration Ltd",
    "telephone": "+1-416-285-7788",
    "email": "info@decorarestoration.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "319 Comstock Rd",
      "addressLocality": "Scarborough",
      "addressRegion": "ON",
      "postalCode": "M1L 2H3",
      "addressCountry": "CA"
    }
  }
}''',
    'content': '''
    <div style="margin-bottom: 4rem;">
      <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary); max-width: 800px; margin: 0 auto; text-align: center;">
        Need an expert to review a structural concern, assess water damage, or review engineering bid packages? Our engineering-backed team is available to visit your property across Toronto and the Greater Toronto Area.
      </p>
    </div>
    '''
}

cities = {
    'scarborough': 'Scarborough',
    'toronto': 'Toronto',
    'mississauga': 'Mississauga',
    'north-york': 'North York',
    'etobicoke': 'Etobicoke',
    'markham': 'Markham',
    'vaughan': 'Vaughan',
    'richmond-hill': 'Richmond Hill',
    'oakville': 'Oakville',
    'brampton': 'Brampton'
}

# Template for generating static sub-pages
def make_page(title, description, keywords, canonical, schema, breadcrumbs, h1, subtitle, content, is_contact_page=False):
    # Determine what contact form markup to use (clean GHL form)
    form_html = contact_block if not is_contact_page else ""
    
    # We will build the page HTML
    page_html = f'''{head_base}
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{canonical}" />
<script type="application/ld+json">
{schema}
</script>
</head>
<body>
{nav_block}

<!-- ========== PAGE HERO ========== -->
<section id="page-hero" style="padding-top: 10rem; padding-bottom: 5rem; background: var(--near-black); border-bottom: 1px solid var(--border); position: relative; overflow: hidden; color: #ffffff !important;">
  <div class="hero-bg" aria-hidden="true" style="background: linear-gradient(rgba(15, 23, 42, 0.95), rgba(15, 23, 42, 0.95)), url(\'/RESTORTATION/images/hero.png\') center/cover; opacity: 0.1; position: absolute; inset: 0;"></div>
  <div class="container" style="position: relative; z-index: 2;">
    <div style="margin-bottom: 1.5rem;">
      <span class="overline"><a href="/" style="color: var(--gold); text-decoration: none;">Home</a> {breadcrumbs}</span>
    </div>
    <h1 class="display display-md" style="margin-bottom: 1.5rem; color: #ffffff !important;">{h1}</h1>
    <p style="color: rgba(255, 255, 255, 0.85); max-width: 600px; font-size: 1.1rem; line-height: 1.7;">{subtitle}</p>
  </div>
</section>

<!-- ========== PAGE CONTENT ========== -->
<section id="page-content" style="background: #ffffff; padding: 6rem 0; color: #0f172a;">
  <div class="container">
    {content}
  </div>
</section>

{form_html}

{footer_block}
{scripts_block}
</body>
</html>
'''
    # Relative path normalization (e.g. so images in subdirectories load correctly)
    # Since our page is in a directory like /services/building-envelope/index.html,
    # any asset references like "RESTORTATION/" need to point to "/RESTORTATION/"
    page_html = page_html.replace('src="RESTORTATION/', 'src="/RESTORTATION/')
    page_html = page_html.replace('url(\'RESTORTATION/', 'url(\'/RESTORTATION/')
    page_html = page_html.replace('url(\\\"RESTORTATION/', 'url(\\\"/RESTORTATION/')
    page_html = page_html.replace('url(\\\'/RESTORTATION/', 'url(\\\'/RESTORTATION/')
    return page_html

# Write the homepage (root index.html)
homepage_seo_content = template_content
# Add canonical to root decora-website.html (which is index.html)
with open('/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/index.html', 'w', encoding='utf-8') as f:
    f.write(homepage_seo_content)

# Process Services pages
os.makedirs('/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/services', exist_ok=True)
for slug, info in services.items():
    page_dir = f'/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/services/{slug}'
    os.makedirs(page_dir, exist_ok=True)
    canonical = f'https://decorarestoration.com/services/{slug}/'
    
    # Merge service and FAQ schema
    merged_schema = f'''[
  {info['schema']},
  {info['faq_schema']}
]'''
    
    html = make_page(
        title=info['title'],
        description=info['description'],
        keywords=info['keywords'],
        canonical=canonical,
        schema=merged_schema,
        breadcrumbs=info['breadcrumbs'],
        h1=info['h1'],
        subtitle=info['subtitle'],
        content=info['content']
    )
    with open(f'{page_dir}/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# Process About page
about_dir = '/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/about'
os.makedirs(about_dir, exist_ok=True)
about_html = make_page(
    title=about_page['title'],
    description=about_page['description'],
    keywords=about_page['keywords'],
    canonical='https://decorarestoration.com/about/',
    schema=about_page['schema'],
    breadcrumbs=about_page['breadcrumbs'],
    h1=about_page['h1'],
    subtitle=about_page['subtitle'],
    content=about_page['content']
)
with open(f'{about_dir}/index.html', 'w', encoding='utf-8') as f:
    f.write(about_html)

# Process Contact page
contact_dir = '/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/contact'
os.makedirs(contact_dir, exist_ok=True)
contact_html = make_page(
    title=contact_page['title'],
    description=contact_page['description'],
    keywords=contact_page['keywords'],
    canonical='https://decorarestoration.com/contact/',
    schema=contact_page['schema'],
    breadcrumbs=contact_page['breadcrumbs'],
    h1=contact_page['h1'],
    subtitle=contact_page['subtitle'],
    content=contact_page['content'],
    is_contact_page=True
)
# Re-append GHL contact form to contact page since it's the core contact page!
contact_html = contact_html.replace('<!-- ========== PAGE CONTENT ========== -->\n<section id="page-content" style="background: #ffffff; padding: 6rem 0; color: #0f172a;">\n  <div class="container">\n    \n    <div style="margin-bottom: 4rem;">\n      <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary); max-width: 800px; margin: 0 auto; text-align: center;">\n        Need an expert to review a structural concern, assess water damage, or review engineering bid packages? Our engineering-backed team is available to visit your property across Toronto and the Greater Toronto Area.\n      </p>\n    </div>\n    \n  </div>\n</section>', f'<!-- ========== PAGE CONTENT ========== -->\n<section id="page-content" style="background: #ffffff; padding: 4rem 0; color: #0f172a;">\n  <div class="container">\n    <div style="margin-bottom: 4rem;">\n      <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary); max-width: 800px; margin: 0 auto; text-align: center;">\n        Need an expert to review a structural concern, assess water damage, or review engineering bid packages? Our engineering-backed team is available to visit your property across Toronto and the Greater Toronto Area.\n      </p>\n    </div>\n  </div>\n</section>\n{contact_block}')

with open(f'{contact_dir}/index.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

# Process Local Area pages
os.makedirs('/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/areas', exist_ok=True)
for city_slug, city_name in cities.items():
    page_dir = f'/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/areas/{city_slug}'
    os.makedirs(page_dir, exist_ok=True)
    canonical = f'https://decorarestoration.com/areas/{city_slug}/'
    
    title = f'Building Restoration {city_name} | Decora Building Restoration'
    description = f'Building envelope, balcony, masonry & parking garage restoration in {city_name}. Serving {city_name} since 1990. Call 416-285-7788.'
    keywords = f'building restoration {city_name.lower()}, balcony repair {city_name.lower()}, masonry repair {city_name.lower()}'
    h1 = f'Building Restoration Services in {city_name}'
    subtitle = f'Trusted commercial restoration contractor serving condominium corporations, property managers, and building owners in {city_name}.'
    
    schema = f'''{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Decora Building Restoration Ltd",
  "telephone": "+1-416-285-7788",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "319 Comstock Rd",
    "addressLocality": "Scarborough",
    "addressRegion": "ON",
    "postalCode": "M1L 2H3",
    "addressCountry": "CA"
  }},
  "areaServed": {{
    "@type": "City",
    "name": "{city_name}"
  }}
}}'''

    content = f'''
    <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; align-items: start;">
      <div>
        <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
          Decora Building Restoration has been serving {city_name} property managers and condo corporations since 1990. Our team handles building envelope repair, balcony restoration, masonry tuck pointing, and parking garage rehabilitation across {city_name} and the surrounding area.
        </p>
        <p style="font-size: 1rem; line-height: 1.8; margin-bottom: 2rem; color: var(--text-secondary);">
          We understand the specific environmental and structural challenges facing properties in {city_name}. Southern Ontario\'s extreme temperature shifts subject building facades and parking decks to severe stress. Our localized engineering solutions ensure your property remains compliant, secure, and moisture-free.
        </p>
        
        <h3 class="display display-sm" style="font-size: 1.8rem; margin-bottom: 1rem;">Services We Offer in {city_name}</h3>
        <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 3rem;">
          <li style="border: 1px solid var(--border); padding: 1.5rem; border-radius: 8px;">
            <strong style="display: block; margin-bottom: 0.5rem; color: var(--white);"><a href="/services/building-envelope/" style="color: var(--white); text-decoration: none; border-bottom: 1px solid var(--gold);">Building Envelope</a></strong>
            <span style="font-size: 0.85rem; color: var(--text-secondary);">Comprehensive exterior walls, cladding, caulking and window sealants.</span>
          </li>
          <li style="border: 1px solid var(--border); padding: 1.5rem; border-radius: 8px;">
            <strong style="display: block; margin-bottom: 0.5rem; color: var(--white);"><a href="/services/balcony-restoration/" style="color: var(--white); text-decoration: none; border-bottom: 1px solid var(--gold);">Balcony Restoration</a></strong>
            <span style="font-size: 0.85rem; color: var(--text-secondary);">Concrete slab repairs, waterproofing membranes, and railing upgrades.</span>
          </li>
          <li style="border: 1px solid var(--border); padding: 1.5rem; border-radius: 8px;">
            <strong style="display: block; margin-bottom: 0.5rem; color: var(--white);"><a href="/services/masonry-repair/" style="color: var(--white); text-decoration: none; border-bottom: 1px solid var(--gold);">Masonry & Tuck Pointing</a></strong>
            <span style="font-size: 0.85rem; color: var(--text-secondary);">Brick replacement, mortar repointing, and steel lintel restoration.</span>
          </li>
          <li style="border: 1px solid var(--border); padding: 1.5rem; border-radius: 8px;">
            <strong style="display: block; margin-bottom: 0.5rem; color: var(--white);"><a href="/services/parking-garage-restoration/" style="color: var(--white); text-decoration: none; border-bottom: 1px solid var(--gold);">Parking Garage Rehab</a></strong>
            <span style="font-size: 0.85rem; color: var(--text-secondary);">Underground slab repairs, traffic coatings, and drainage upgrades.</span>
          </li>
        </ul>
      </div>

      <div style="background: var(--dark-surface); padding: 2.5rem; border-radius: 12px; border: 1px solid var(--border);">
        <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Service Guarantee</h4>
        <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
          We coordinate directly with your building's engineering firm and provide transparent schedules to minimize tenant disruption.
        </p>
        <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.7;">
          To book a free, no-obligation site assessment at your property in {city_name}, fill out the contact form or call 416-285-7788.
        </p>
      </div>
    </div>
    '''
    
    html = make_page(
        title=title,
        description=description,
        keywords=keywords,
        canonical=canonical,
        schema=schema,
        breadcrumbs=f'→ <a href="/areas/{city_slug}/" style="color: var(--white); text-decoration: none;">{city_name}</a>',
        h1=h1,
        subtitle=subtitle,
        content=content
    )
    with open(f'{page_dir}/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# Process Blog pages
blog_dir = '/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/blog'
os.makedirs(blog_dir, exist_ok=True)

# 1. Blog posts data
blog_posts = {
    '5-signs-condo-balcony-needs-attention': {
        'title': '5 Signs Your Condo\'s Balcony Needs Immediate Attention | Decora',
        'description': 'Is your building\'s concrete safe? Learn the 5 warning signs of concrete balcony deterioration, rust staining, and rebar corrosion. Call 416-285-7788.',
        'keywords': 'balcony cracking condo, balcony repair signs, concrete spalling balcony, condo balcony repair Toronto',
        'h1': '5 Signs Your Condo\'s Balcony Needs Immediate Attention',
        'subtitle': 'A guide for property managers and condominium boards on spotting structural concrete spalling and railing issues early.',
        'breadcrumbs': '→ <a href="/blog/" style="color: var(--white); text-decoration: none;">Blog</a> → <span style="color: var(--white);">5 Signs Your Balcony Needs Attention</span>',
        'schema': '''{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "5 Signs Your Condo's Balcony Needs Immediate Attention",
  "description": "Learn the 5 critical warning signs of condo balcony concrete degradation, rust spalling, and railing failure.",
  "author": {
    "@type": "Organization",
    "name": "Decora Building Restoration Ltd"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Decora Building Restoration Ltd",
    "logo": {
      "@type": "ImageObject",
      "url": "https://decorarestoration.com/RESTORTATION/images/logo.png"
    }
  },
  "datePublished": "2025-06-01"
}''',
        'content': '''
        <article style="max-width: 800px; margin: 0 auto;">
          <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 2rem; color: var(--text-secondary);">
            Balconies are suspended concrete slabs exposed to Southern Ontario's extreme weather, road salts, and moisture. Over time, concrete deteriorates, compromising safety. For condo boards and property managers, catching these issues early prevents high repair costs and safety hazards. Here are the 5 critical signs your balconies need professional assessment:
          </p>

          <h3 class="display display-sm" style="font-size: 1.8rem; margin-top: 2rem; margin-bottom: 1rem; color: var(--white);">1. Rust Stains Bleeding Through the Concrete</h3>
          <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
            If you notice reddish-brown streaks on the underside or edges of concrete balconies, it is a direct indicator of internal steel corrosion. Water containing dissolved salt has penetrated the concrete and reached the reinforcing steel rebar. As the steel rusts, it bleeds oxide through the porous concrete.
          </p>

          <h3 class="display display-sm" style="font-size: 1.8rem; margin-top: 2rem; margin-bottom: 1rem; color: var(--white);">2. Concrete Cracking and Spalling (Flaking)</h3>
          <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
            Rusting steel rebar expands up to ten times its original size. This massive internal expansion forces the surrounding concrete to crack and flake away, a process known as spalling. Spalled concrete poses immediate safety risks: chunks can fall onto common areas below, and the structural integrity of the balcony is actively degrading.
          </p>

          <h3 class="display display-sm" style="font-size: 1.8rem; margin-top: 2rem; margin-bottom: 1rem; color: var(--white);">3. Loose or Deteriorating Railing Posts</h3>
          <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
            Inspect the connections where railing posts enter the concrete slab. These "post pockets" are common entry points for moisture. If the steel posts rust or the surrounding concrete grout cracks, the railing becomes loose. A wobbly railing represents a severe liability and safety violation.
          </p>

          <h3 class="display display-sm" style="font-size: 1.8rem; margin-top: 2rem; margin-bottom: 1rem; color: var(--white);">4. Peeling or Bubbling Waterproofing Membranes</h3>
          <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
            Condo balconies require a high-performance elastomeric membrane coating to keep water from soaking into the concrete. If this coating is worn away, peeling, or forming bubbles, water is getting trapped underneath. This hastens concrete degradation and leads to rapid slab delamination.
          </p>

          <h3 class="display display-sm" style="font-size: 1.8rem; margin-top: 2rem; margin-bottom: 1rem; color: var(--white);">5. Water Pooling or Infiltration Into Units</h3>
          <p style="line-height: 1.8; margin-bottom: 2rem; color: var(--text-secondary);">
            Balconies must be sloped away from the building to allow rain to drain off. If water pools against the exterior wall or door threshold, it will eventually seep into the building envelope, causing interior water damage, drywall mold, and flooring damage inside the condo units.
          </p>

          <div style="background: var(--dark-surface); padding: 2rem; border-radius: 8px; border: 1px solid var(--border); margin-top: 3rem;">
            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Request a Free Site Assessment</h4>
            <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
              Decora Building Restoration has restored condo balconies across the GTA since 1990. We coordinate with your engineering firm to deliver code-compliant concrete repairs and modern railing systems.
            </p>
            <p style="font-weight: 500;"><a href="/contact/" style="color: var(--gold); text-decoration: none; border-bottom: 1px solid var(--gold);">Book Your Visual Site Visit Today →</a></p>
          </div>
        </article>
        '''
    },
    'what-is-building-envelope-restoration': {
        'title': 'What Is Building Envelope Restoration? Explainer | Decora',
        'description': 'What is building envelope restoration? Learn how envelope repair, window caulking & cladding rehabilitation stops leaks and cuts energy costs in Toronto. Call 416-285-7788.',
        'keywords': 'what is building envelope restoration, building envelope repair Toronto, facade repair GTA, condo waterproofing envelope',
        'h1': 'What Is Building Envelope Restoration?',
        'subtitle': 'A plain-language guide for Toronto property managers and condo boards on exterior wall, cladding, and sealant systems.',
        'breadcrumbs': '→ <a href="/blog/" style="color: var(--white); text-decoration: none;">Blog</a> → <span style="color: var(--white);">What is Building Envelope Restoration</span>',
        'schema': '''{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "What Is Building Envelope Restoration? A Plain-Language Guide",
  "description": "Learn what building envelope restoration is, what components are repaired, and why it is critical for commercial buildings.",
  "author": {
    "@type": "Organization",
    "name": "Decora Building Restoration Ltd"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Decora Building Restoration Ltd",
    "logo": {
      "@type": "ImageObject",
      "url": "https://decorarestoration.com/RESTORTATION/images/logo.png"
    }
  },
  "datePublished": "2025-06-15"
}''',
        'content': '''
        <article style="max-width: 800px; margin: 0 auto;">
          <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 2rem; color: var(--text-secondary);">
            While the term "building envelope" sounds technical, it simply refers to the physical barrier that separates a building's conditioned interior from the outdoor elements. This barrier includes walls, windows, sealants, cladding, roof flashing, and foundation waterproofing. When these components fail, moisture leaks in, leading to structural damage and energy loss.
          </p>

          <h3 class="display display-sm" style="font-size: 1.8rem; margin-top: 2rem; margin-bottom: 1rem; color: var(--white);">The Components of the Envelope</h3>
          <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
            The envelope is a complex system designed to regulate moisture, air pressure, and temperature. Its core components include:
          </p>
          <ul style="color: var(--text-secondary); line-height: 1.8; padding-left: 1.5rem; margin-bottom: 1.5rem;">
            <li><strong>Air/Vapour Barrier:</strong> Prevents air drafts and controls moisture migration through walls.</li>
            <li><strong>Cladding & Cladding Support:</strong> The visible exterior (e.g. brick, stucco, metal panels, or EIFS).</li>
            <li><strong>Window Sealants & Glazing:</strong> The caulking and structural sealants that close the gaps around windows and joints.</li>
            <li><strong>Flashing & Weep Holes:</strong> Systems that collect water that penetrates the cladding and direct it back outside safely.</li>
          </ul>

          <h3 class="display display-sm" style="font-size: 1.8rem; margin-top: 2rem; margin-bottom: 1rem; color: var(--white);">Why Does Envelope Failure Happen?</h3>
          <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
            Envelopes fail due to thermal movement (expansion and contraction under heat and cold), UV exposure from the sun, and aging materials. In Toronto, caulking and sealants typically last 10 to 15 years. If not replaced, they crack and shrink, allowing rain and snow to seep into the wall cavity.
          </p>

          <h3 class="display display-sm" style="font-size: 1.8rem; margin-top: 2rem; margin-bottom: 1rem; color: var(--white);">What Does a Restoration Involve?</h3>
          <p style="line-height: 1.8; margin-bottom: 1.5rem; color: var(--text-secondary);">
            An envelope restoration is not a cosmetic coat of paint. It is a structural repair process. Depending on the building, it involves:
          </p>
          <ul style="color: var(--text-secondary); line-height: 1.8; padding-left: 1.5rem; margin-bottom: 2rem;">
            <li>Stripping and replacing failed caulking and polyurethane window sealants.</li>
            <li>Repairing structural cracks in the exterior concrete panels or masonry.</li>
            <li>Replacing damaged EIFS (stucco) panels or reinforcing metal panel anchors.</li>
            <li>Re-routing flashing and clear weep paths so water does not get trapped.</li>
          </ul>

          <div style="background: var(--dark-surface); padding: 2rem; border-radius: 8px; border: 1px solid var(--border); margin-top: 3rem;">
            <h4 class="display display-sm" style="font-size: 1.4rem; margin-bottom: 1rem; color: var(--white);">Need an Envelope Inspection?</h4>
            <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
              Proactive envelope maintenance stops drafts, resolves interior leaks, and drastically lowers building utility bills.
            </p>
            <p style="font-weight: 500;"><a href="/contact/" style="color: var(--gold); text-decoration: none; border-bottom: 1px solid var(--gold);">Book a Free Building envelope Assessment →</a></p>
          </div>
        </article>
        '''
    }
}

# 2. Write individual blog posts
for slug, info in blog_posts.items():
    post_dir = f'/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/blog/{slug}'
    os.makedirs(post_dir, exist_ok=True)
    canonical = f'https://decorarestoration.com/blog/{slug}/'
    
    html = make_page(
        title=info['title'],
        description=info['description'],
        keywords=info['keywords'],
        canonical=canonical,
        schema=info['schema'],
        breadcrumbs=info['breadcrumbs'],
        h1=info['h1'],
        subtitle=info['subtitle'],
        content=info['content']
    )
    with open(f'{post_dir}/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# 3. Write Blog Home Page (/blog/index.html)
blog_home_content = '''
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 3rem; margin-top: 2rem;">
  <!-- Post 1 -->
  <div style="border: 1px solid var(--border); border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 10px 25px rgba(0,0,0,0.04); display: flex; flex-direction: column;">
    <div style="padding: 2.5rem; display: flex; flex-direction: column; flex-grow: 1;">
      <span class="overline" style="margin-bottom: 1rem; display: block;">Condo Balconies</span>
      <h3 class="display display-sm" style="font-size: 1.5rem; margin-bottom: 1rem; line-height: 1.3;"><a href="/blog/5-signs-condo-balcony-needs-attention/" style="color: var(--white); text-decoration: none; hover:color: var(--gold);">5 Signs Your Condo's Balcony Needs Immediate Attention</a></h3>
      <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin-bottom: 2rem; flex-grow: 1;">
        A guide for property managers and condominium boards on spotting concrete cracking, rust stains, wobbly railing posts, and membrane failures early.
      </p>
      <a href="/blog/5-signs-condo-balcony-needs-attention/" style="color: var(--gold); text-decoration: none; font-weight: 500; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.05em; display: inline-flex; align-items: center; gap: 0.5rem;">Read Article →</a>
    </div>
  </div>

  <!-- Post 2 -->
  <div style="border: 1px solid var(--border); border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 10px 25px rgba(0,0,0,0.04); display: flex; flex-direction: column;">
    <div style="padding: 2.5rem; display: flex; flex-direction: column; flex-grow: 1;">
      <span class="overline" style="margin-bottom: 1rem; display: block;">Building Envelope</span>
      <h3 class="display display-sm" style="font-size: 1.5rem; margin-bottom: 1rem; line-height: 1.3;"><a href="/blog/what-is-building-envelope-restoration/" style="color: var(--white); text-decoration: none;">What Is Building Envelope Restoration?</a></h3>
      <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin-bottom: 2rem; flex-grow: 1;">
        A plain-language guide for property managers explaining the role of window sealants, cladding support, and flashing systems in stopping leaks.
      </p>
      <a href="/blog/what-is-building-envelope-restoration/" style="color: var(--gold); text-decoration: none; font-weight: 500; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.05em; display: inline-flex; align-items: center; gap: 0.5rem;">Read Article →</a>
    </div>
  </div>
</div>
'''
blog_home_html = make_page(
    title='Building Restoration Blog | Educational Restoration Guides | Decora',
    description='Educational building envelope, balcony, masonry, and parking garage restoration guides from Toronto\'s expert restoration contractor. Call 416-285-7788.',
    keywords='building restoration blog Toronto, balcony repair guides, masonry restoration tips',
    canonical='https://decorarestoration.com/blog/',
    schema='''{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "Decora Building Restoration Blog",
  "url": "https://decorarestoration.com/blog/",
  "publisher": {
    "@type": "Organization",
    "name": "Decora Building Restoration Ltd"
  }
}''',
    breadcrumbs='→ <span style="color: var(--white);">Blog</span>',
    h1='Decora Restoration Blog',
    subtitle='Expert insights, technical guides, and preventative maintenance strategies for multi-residential and commercial properties.',
    content=blog_home_content
)
with open(f'{blog_dir}/index.html', 'w', encoding='utf-8') as f:
    f.write(blog_home_html)


# Generate Sitemap.xml
urls = [
    'https://decorarestoration.com/',
    'https://decorarestoration.com/about/',
    'https://decorarestoration.com/contact/',
    'https://decorarestoration.com/blog/',
    'https://decorarestoration.com/blog/5-signs-condo-balcony-needs-attention/',
    'https://decorarestoration.com/blog/what-is-building-envelope-restoration/'
]
for slug in services.keys():
    urls.append(f'https://decorarestoration.com/services/{slug}/')
for city_slug in cities.keys():
    urls.append(f'https://decorarestoration.com/areas/{city_slug}/')

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    sitemap_xml += f'  <url>\n    <loc>{url}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
# Set priority for home
sitemap_xml = sitemap_xml.replace('<loc>https://decorarestoration.com/</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>', '<loc>https://decorarestoration.com/</loc>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>')
sitemap_xml += '</urlset>'

with open('/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)


# Generate Robots.txt
robots_txt = '''User-agent: *
Allow: /

Sitemap: https://decorarestoration.com/sitemap.xml
'''
with open('/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_txt)

print("Page generation successfully completed!")
