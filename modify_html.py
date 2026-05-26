import re

file_path = '/home/isiata/Documents/Brian Marshall/HVAC/Decora Rstoration/decora-website.html'
with open(file_path, 'r') as f:
    content = f.read()

# 1. Update CSS variables to light theme with RESTORTATION colors
new_root = """:root {
  --gold: #0ea5e9;
  --gold-light: #ff6b35;
  --gold-pale: #e0f2fe;
  --near-black: #f8fafc;
  --charcoal: #ffffff;
  --dark-surface: #f1f5f9;
  --mid: #e2e8f0;
  --text-muted: #64748b;
  --text-secondary: #475569;
  --white: #0f172a;
  --off-white: #1e293b;
  --border: rgba(15, 23, 42, 0.1);
  --transition: 0.4s cubic-bezier(0.25,0.46,0.45,0.94);
}"""

content = re.sub(r':root\s*\{[^}]+\}', new_root, content)

# 2. Hardcoded colors
content = content.replace('rgba(255,255,255', 'rgba(15,23,42')
content = content.replace('rgba(184,150,90', 'rgba(14,165,233')
content = content.replace('#1A1A1A', '#f1f5f9')
content = content.replace('#2A2A2A', '#e2e8f0')
content = content.replace('#1E1A10', '#e0f2fe')
content = content.replace('#2A2210', '#bae6fd')
content = content.replace('stroke="white"', 'stroke="#0f172a"')
content = content.replace('stroke="#B8965A"', 'stroke="#0ea5e9"')
content = content.replace('#1a1812', '#e0f2fe')
content = content.replace('#222016', '#bae6fd')
content = content.replace('mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 30%,transparent 100%)', 'mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,white 30%,transparent 100%)')
content = content.replace('linear-gradient(135deg,#1A0E00,#0A0A0A 50%,#1A0E00)', 'linear-gradient(135deg,#bae6fd,#f8fafc 50%,#bae6fd)')

# 3. Replace placeholders with images
# For before/after placeholders
# Because there are 3 pairs, the first 3 will be "before" and the next 3 will be "after"
content = re.sub(r'<div class="ba-placeholder">\s*<svg[^>]+>.*?</svg>\s*<span[^>]*>CLIENT PHOTO</span>\s*</div>', '<img src="RESTORTATION/images/water_damage_before.png" style="width:100%;height:100%;object-fit:cover;" alt="Before">', content, count=3)
content = re.sub(r'<div class="ba-placeholder">\s*<svg[^>]+>.*?</svg>\s*<span[^>]*>CLIENT PHOTO</span>\s*</div>', '<img src="RESTORTATION/images/water_damage_after.png" style="width:100%;height:100%;object-fit:cover;" alt="After">', content, count=3)

# For project images
content = re.sub(r'<div class="project-img"[^>]*>\s*<div class="project-img-pattern"[^>]*></div>\s*<div[^>]*>\s*<svg[^>]+>.*?</svg>\s*<p[^>]*>Add Hero Project Photo</p>\s*</div>\s*</div>', '<div class="project-img" style="background: url(\\\'RESTORTATION/images/water_restoration.png\\\') center/cover;"><div class="project-img-pattern" aria-hidden="true"></div></div>', content, flags=re.DOTALL, count=1)
content = re.sub(r'<div class="project-img"[^>]*>\s*<div class="project-img-pattern"[^>]*></div>\s*<div[^>]*>\s*<svg[^>]+>.*?</svg>\s*</div>\s*</div>', '<div class="project-img" style="background: url(\\\'RESTORTATION/images/fire_cleanup.png\\\') center/cover; height: 220px;"><div class="project-img-pattern" aria-hidden="true"></div></div>', content, flags=re.DOTALL, count=1)
content = re.sub(r'<div class="project-img"[^>]*>\s*<div class="project-img-pattern"[^>]*></div>\s*<div[^>]*>\s*<svg[^>]+>.*?</svg>\s*</div>\s*</div>', '<div class="project-img" style="background: url(\\\'RESTORTATION/images/mold_remediation.png\\\') center/cover; height: 220px;"><div class="project-img-pattern" aria-hidden="true"></div></div>', content, flags=re.DOTALL, count=1)

# Hero BG
content = content.replace('<div class="hero-bg" aria-hidden="true"></div>', '<div class="hero-bg" aria-hidden="true" style="background: url(\'RESTORTATION/images/hero.png\') center/cover; opacity: 0.1;"></div>')


# 4. Insert chat widget
chat_widget = '''    <!-- Chat Widget -->
    <script src="https://widgets.leadconnectorhq.com/loader.js" data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" data-widget-id="69f07d5f2a45a437f24db049"></script>
</body>'''

content = content.replace('</body>', chat_widget)

with open(file_path, 'w') as f:
    f.write(content)

print("Modification complete.")
