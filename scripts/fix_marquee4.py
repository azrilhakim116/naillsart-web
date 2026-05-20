"""Replace all remaining static announcement bar variants."""
import os, re

MARQUEE_HTML = '<!-- Announcement Bar -->\n<div class="marquee-bar">\n  <div class="marquee-track">\n    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>\n    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>\n    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>\n  </div>\n</div>'

# All known patterns
PATTERNS = [
    # #670F0D multiline
    r'<!-- TOP BAR -->\s*<div class="w-full bg-\[#670F0D\]">\s*<div class="flex items-center justify-center h-\[53px\] px-6">\s*<p class="text-white text-xs tracking-widest">\s*SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW\s*</p>\s*</div>\s*</div>',
    # #670F0D no comment
    r'<div class="w-full bg-\[#670F0D\]">\s*<div class="flex items-center justify-center h-\[53px\] px-6">\s*<p class="text-white text-xs tracking-widest">\s*SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW\s*</p>\s*</div>\s*</div>',
    # h-[44px] version (tutorial-apply, tutorial-care, booking)
    r'<div[^>]+>\s*<div class="max-w-\[1440px\] h-\[44px\][^>]*">\s*<p class="text-white text-\[11px\] tracking-widest">SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</p>\s*</div>\s*</div>',
    # wishlist simple bar
    r'<!-- TOP BAR -->\s*<div class="bg-\[#d8a1a1\] text-white text-center text-xs tracking-\[0\.3em\] py-3">\s*SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW\s*</div>',
    # product pages h-[52px]
    r'<div[^>]+from-\[#CE8A97\][^>]*to-\[#D89C9B\][^>]*">\s*<div class="max-w-\[1440px\] h-\[52px\][^>]*">\s*<p class="text-white text-xs tracking-\[0\.35em\]">\s*SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW\s*</p>\s*</div>\s*</div>',
    # product pages h-[52px] one line
    r'<div[^>]+from-\[#CE8A97\][^>]*to-\[#D89C9B\][^>]*">\s*<div class="max-w-\[1440px\] h-\[52px\][^>]*">\s*<p class="text-white text-xs tracking-\[0\.35em\]">SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</p>\s*</div>\s*</div>',
    # tutorial-measure
    r'<div class="w-full bg-\[#670F0D\]">\s*<div class="flex items-center justify-center h-\[53px\] px-6">\s*<p class="text-white text-xs tracking-widest">SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</p>\s*</div>\s*</div>',
]

files = [
    'tutorial.html', 'tutorial-apply.html', 'tutorial-care.html',
    'tutorial-measure.html', 'booking.html', 'collaboration.html',
    'wishlist.html', 'product/almond.html', 'product/coffin.html',
    'product/square.html', 'product/stilettos.html'
]

for fname in files:
    if not os.path.exists(fname):
        continue
    with open(fname, encoding='utf-8', errors='replace') as f:
        content = f.read()

    if 'marquee-bar' in content:
        print('Already OK: ' + fname)
        continue

    replaced = False
    for pat in PATTERNS:
        new_content, count = re.subn(pat, MARQUEE_HTML, content, flags=re.DOTALL)
        if count > 0:
            content = new_content
            replaced = True

    if replaced:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed: ' + fname)
    else:
        print('STILL NOT FIXED: ' + fname)

print('Done.')
