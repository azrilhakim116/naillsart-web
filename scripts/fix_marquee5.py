"""Fix product pages announcement bar."""
import os, re

MARQUEE_HTML = '<!-- Announcement Bar -->\n<div class="marquee-bar">\n  <div class="marquee-track">\n    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>\n    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>\n    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>\n  </div>\n</div>'

PATTERN = r'<div[^>]+bg-gradient-to-r from-\[#7A2E2E\][^>]*>\s*<div class="max-w-\[1440px\] h-\[52px\][^>]*>\s*<p[^>]*>\s*SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW\s*</p>\s*</div>\s*</div>'

files = ['product/almond.html','product/coffin.html','product/square.html','product/stilettos.html']

for fname in files:
    with open(fname, encoding='utf-8', errors='replace') as f:
        content = f.read()
    new_content, count = re.subn(PATTERN, MARQUEE_HTML, content, flags=re.DOTALL)
    if count > 0:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Fixed: ' + fname)
    else:
        print('FAILED: ' + fname)
print('Done.')
