"""Replace static announcement bars with marquee version across all pages."""
import os, re

# The new marquee HTML
MARQUEE_HTML = '''<!-- Announcement Bar -->
<div class="marquee-bar">
  <div class="marquee-track">
    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>
    <span>FREE ONGKIR MIN. ORDER 2 SET &nbsp;|&nbsp; CUSTOM DESIGN AVAILABLE</span>
    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>
    <span>FREE ONGKIR MIN. ORDER 2 SET &nbsp;|&nbsp; CUSTOM DESIGN AVAILABLE</span>
    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>
    <span>FREE ONGKIR MIN. ORDER 2 SET &nbsp;|&nbsp; CUSTOM DESIGN AVAILABLE</span>
  </div>
</div>'''

# Patterns to find and replace
OLD_PATTERNS = [
    # Pattern 1: with font-inter class (our-service)
    r'<!-- Top Announcement Bar -->\s*<div class="w-full bg-gradient-to-r from-\[#CE8A97\] to-\[#D89C9B\]">\s*<div class="max-w-\[1440px\] h-\[53px\] mx-auto flex items-center justify-center">\s*<p class="text-white text-xs tracking-widest font-inter">\s*SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW\s*</p>\s*</div>\s*</div>',
    # Pattern 2: without font-inter (press-on etc)
    r'<!-- Top Announcement Bar -->\s*<div class="w-full bg-gradient-to-r from-\[#CE8A97\] to-\[#D89C9B\]">\s*<div class="max-w-\[1440px\] h-\[53px\] mx-auto flex items-center justify-center">\s*<p class="text-white text-xs tracking-widest">\s*SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW\s*</p>\s*</div>\s*</div>',
    # Pattern 3: index.html announcement-bar class version
    r'<!-- Top Announcement Bar -->\s*<div class="w-full bg-gradient-to-r from-\[#CE8A97\] to-\[#D89C9B\] announcement-bar">\s*<div class="max-w-\[1440px\] h-\[40px\] mx-auto flex items-center justify-center">\s*<p class="[^"]*">\s*SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW\s*</p>\s*</div>\s*</div>',
    # Pattern 4: no comment, just the div (collaboration etc)
    r'<div class="w-full bg-gradient-to-r from-\[#CE8A97\] to-\[#D89C9B\]">\s*<div class="max-w-\[1440px\] h-\[53px\] mx-auto flex items-center justify-center">\s*<p class="text-white text-xs tracking-widest">\s*SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW\s*</p>\s*</div>\s*</div>',
]

files = [
    'index.html', 'our-service.html', 'press-on.html', 'tutorial.html',
    'tutorial-apply.html', 'tutorial-care.html', 'tutorial-measure.html',
    'booking.html', 'collaboration.html', 'wishlist.html',
    'product/almond.html', 'product/coffin.html',
    'product/square.html', 'product/stilettos.html'
]

for fname in files:
    if not os.path.exists(fname):
        continue
    try:
        with open(fname, encoding='utf-8') as f:
            content = f.read()
    except:
        with open(fname, encoding='latin-1') as f:
            content = f.read()

    replaced = False
    for pattern in OLD_PATTERNS:
        new_content, count = re.subn(pattern, MARQUEE_HTML, content, flags=re.DOTALL)
        if count > 0:
            content = new_content
            replaced = True

    if replaced:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Updated: {fname}')
    else:
        print(f'  Skip (no match): {fname}')

print('Done.')
