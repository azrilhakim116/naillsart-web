"""
Fix mobile navbar: replace the desktop-only nav with a hamburger menu version
for all HTML pages.
"""
import os, re

ROOT_FILES = [
    'index.html', 'our-service.html', 'press-on.html', 'tutorial.html',
    'tutorial-apply.html', 'tutorial-care.html', 'tutorial-measure.html',
    'booking.html', 'collaboration.html', 'wishlist.html', 'contact.html',
    'terms.html'
]

PRODUCT_FILES = [
    'product/almond.html', 'product/coffin.html',
    'product/square.html', 'product/stilettos.html'
]

# ── helpers ──────────────────────────────────────────────────────────────────

def make_nav(prefix=''):
    """Return the full navbar inner HTML. prefix='' for root, '../' for product."""
    p = prefix  # e.g. '../' for product pages
    return f'''<!-- ================= NAVBAR DESKTOP ================= -->
<div class="desktop-nav max-w-[1440px] h-[84px] mx-auto flex items-center px-6 relative">
  <!-- LEFT -->
  <nav class="flex gap-4 font-[Kalnia] text-[14px] text-gray-800">
    <a href="{p}index.html" class="hover:text-[#CE8A97]">HOME</a>
    <a href="{p}our-service.html" class="hover:text-[#CE8A97]">OUR SERVICE</a>
    <a href="{p}press-on.html" class="hover:text-[#CE8A97]">PRESS-ON</a>
    <div x-data="{{ open: false }}" @mouseenter="open = true" @mouseleave="open = false" class="relative">
      <button class="flex items-center gap-1 hover:text-[#CE8A97]">
        PRODUCT <i class="fa-solid fa-chevron-down text-[10px]"></i>
      </button>
      <div x-show="open" x-transition class="absolute top-full mt-3 w-44 bg-white border rounded-xl shadow-xl z-50">
        <a href="{p}product/almond.html" class="block px-5 py-2 hover:bg-[#CE8A97] hover:text-white">ALMOND</a>
        <a href="{p}product/square.html" class="block px-5 py-2 hover:bg-[#CE8A97] hover:text-white">SQUARE</a>
        <a href="{p}product/stilettos.html" class="block px-5 py-2 hover:bg-[#CE8A97] hover:text-white">STILETTOS</a>
        <a href="{p}product/coffin.html" class="block px-5 py-2 hover:bg-[#CE8A97] hover:text-white">COFFIN</a>
      </div>
    </div>
    <a href="{p}tutorial.html" class="hover:text-[#CE8A97]">TUTORIALS</a>
  </nav>
  <!-- LOGO -->
  <div class="absolute left-1/2 -translate-x-1/2">
    <img src="{p}public/images/onnails.png" class="h-16 md:h-20" />
  </div>
  <!-- RIGHT -->
  <div class="ml-auto flex items-center gap-10 text-gray-800 font-[Kalnia] text-[14px]">
    <a href="{p}collaboration.html" class="hover:text-[#CE8A97]">COLLABORATION</a>
    <button @click="searchOpen = true" class="text-xl hover:text-[#CE8A97]">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-6 h-6">
        <circle cx="11" cy="11" r="7"/><line x1="16.65" y1="16.65" x2="21" y2="21"/>
      </svg>
    </button>
    <button onclick="window.location.href='{p}wishlist.html'">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-6 h-6 hover:text-[#CE8A97] transition">
        <rect x="3" y="3" width="18" height="18" rx="3"/><path d="M12 17s-4-2.5-4-5a2.5 2.5 0 0 1 4-2 2.5 2.5 0 0 1 4 2c0 2.5-4 5-4 5z"/>
      </svg>
    </button>
  </div>
</div>

<!-- ================= NAVBAR MOBILE ================= -->
<div class="md:hidden flex items-center justify-between px-5 h-[64px] relative">
  <!-- LOGO -->
  <img src="{p}public/images/onnails.png" class="h-12" />
  <!-- RIGHT ICONS -->
  <div class="flex items-center gap-4">
    <button @click="searchOpen = true" class="hover:text-[#CE8A97]">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-5 h-5">
        <circle cx="11" cy="11" r="7"/><line x1="16.65" y1="16.65" x2="21" y2="21"/>
      </svg>
    </button>
    <button onclick="window.location.href='{p}wishlist.html'" class="hover:text-[#CE8A97]">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-5 h-5">
        <rect x="3" y="3" width="18" height="18" rx="3"/><path d="M12 17s-4-2.5-4-5a2.5 2.5 0 0 1 4-2 2.5 2.5 0 0 1 4 2c0 2.5-4 5-4 5z"/>
      </svg>
    </button>
    <!-- Hamburger -->
    <button onclick="document.getElementById('mobile-menu').classList.toggle('open')" class="hamburger-btn" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</div>

<!-- ================= MOBILE MENU DRAWER ================= -->
<div id="mobile-menu" class="mobile-menu md:hidden">
  <a href="{p}index.html">HOME</a>
  <a href="{p}our-service.html">OUR SERVICE</a>
  <a href="{p}press-on.html">PRESS-ON</a>
  <!-- Product submenu -->
  <button onclick="document.getElementById('mobile-product').classList.toggle('hidden')" class="flex items-center justify-between w-full">
    PRODUCT <i class="fa-solid fa-chevron-down text-[10px]"></i>
  </button>
  <div id="mobile-product" class="mobile-submenu hidden">
    <a href="{p}product/almond.html">ALMOND</a>
    <a href="{p}product/square.html">SQUARE</a>
    <a href="{p}product/stilettos.html">STILETTOS</a>
    <a href="{p}product/coffin.html">COFFIN</a>
  </div>
  <a href="{p}tutorial.html">TUTORIALS</a>
  <a href="{p}collaboration.html">COLLABORATION</a>
  <a href="{p}booking.html">BOOKING</a>
</div>'''


def fix_file(path, prefix=''):
    """Replace old navbar div block with responsive version."""
    try:
        with open(path, encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, encoding='latin-1') as f:
            content = f.read()

    # We anchor on the div containing h-[84px] — the desktop nav wrapper.
    # Find the last occurrence of the search script end tag before the div.
    div_marker = '<div class="max-w-[1440px] h-[84px] mx-auto flex items-center px-6 relative">'
    alt_div_marker = '    <div class="max-w-[1440px] h-[84px] mx-auto flex items-center px-6 relative">'

    if div_marker not in content and alt_div_marker not in content:
        print(f'  WARNING: navbar div not found in {path}')
        return

    # Find the comment before the div (or just the div itself)
    start_marker = '<!-- ================= NAVBAR ================= -->\n' + div_marker
    if start_marker not in content:
        start_marker = '<!-- ================= NAVBAR ================= -->\n' + alt_div_marker
    if start_marker not in content:
        # No comment, just the div
        start_marker = div_marker if div_marker in content else alt_div_marker

    if start_marker not in content:
        print(f'  WARNING: navbar marker not found in {path}')
        return

    start_idx = content.index(start_marker)

    # Find </header> after the navbar start
    end_marker = '</header>'
    end_idx = content.index(end_marker, start_idx) + len(end_marker)

    new_nav = make_nav(prefix) + '\n</header>'
    content = content[:start_idx] + new_nav + content[end_idx:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Fixed: {path}')


# ── main ──────────────────────────────────────────────────────────────────────

for fname in ROOT_FILES:
    if os.path.exists(fname):
        fix_file(fname, prefix='')
    else:
        print(f'  SKIP (not found): {fname}')

for fname in PRODUCT_FILES:
    if os.path.exists(fname):
        fix_file(fname, prefix='../')
    else:
        print(f'  SKIP (not found): {fname}')

print('Done.')
