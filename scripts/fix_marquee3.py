"""Replace remaining static announcement bars with clean marquee."""
import os, re

MARQUEE_HTML = '''<!-- Announcement Bar -->
<div class="marquee-bar">
  <div class="marquee-track">
    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>
    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>
    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>
  </div>
</div>'''

# Catch any remaining static bar variants
PATTERN = r'(?:<!-- [^>]*[Aa]nnouncement[^>]* -->[\s]*)?' \
          r'<div[^>]+bg-gradient-to-r from-\[#(?:CE8A97|670F0D)\][^>]*>\s*' \
          r'<div[^>]+>\s*<p[^>]*>\s*SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW\s*</p>\s*</div>\s*</div>'

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
    with open(fname, encoding='utf-8', errors='replace') as f:
        content = f.read()

    if 'marquee-bar' in content:
        print('Already marquee: ' + fname)
        continue

    new_content, count = re.subn(PATTERN, MARQUEE_HTML, content, flags=re.DOTALL)
    if count > 0:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Fixed: ' + fname)
    elif 'SCHEDULE' in content:
        # fallback: find exact block
        idx = content.find('SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW')
        print('MANUAL CHECK NEEDED: ' + fname + ' (pos ' + str(idx) + ')')
        print(repr(content[idx-150:idx+80]))
    else:
        print('No bar found: ' + fname)

print('Done.')
