"""Fix marquee text — hapus FREE ONGKIR, hanya pakai teks asli."""
import os, re

MARQUEE_FIX = '''<!-- Announcement Bar -->
<div class="marquee-bar">
  <div class="marquee-track">
    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>
    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>
    <span>SCHEDULE YOUR CUSTOM NAIL DESIGN SESSION NOW</span>
  </div>
</div>'''

OLD = r'<!-- Announcement Bar -->\s*<div class="marquee-bar">.*?</div>\s*</div>'

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
    new_content, count = re.subn(OLD, MARQUEE_FIX, content, flags=re.DOTALL)
    if count > 0:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Fixed: ' + fname)
    else:
        print('Skip: ' + fname)
print('Done.')
