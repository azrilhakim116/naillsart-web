import os

files = [
    'index.html','our-service.html','press-on.html','tutorial.html',
    'tutorial-apply.html','tutorial-care.html','tutorial-measure.html',
    'booking.html','collaboration.html','wishlist.html',
    'product/almond.html','product/coffin.html','product/square.html','product/stilettos.html'
]

for f in files:
    try:
        with open(f, encoding='utf-8') as fh: c = fh.read()
    except:
        with open(f, encoding='latin-1') as fh: c = fh.read()
    issues = []
    style_count = c.count('<style>')
    if style_count > 1:
        issues.append('duplikat style x' + str(style_count))
    if 'translate-y-[300px]' in c or '-mt-[280px]' in c:
        issues.append('negative margin hack')
    if c.count('const sections') > 1:
        issues.append('duplikat JS sections var')
    if 'meta name="viewport"' not in c:
        issues.append('MISSING viewport')
    if 'mobile-menu' not in c and 'onnails-navbar' in c:
        issues.append('no mobile menu')
    if 'left-40' in c and 'w-[280px]' in c:
        issues.append('SELECT overflow mobile')
    if issues:
        print(f + ': ' + ', '.join(issues))
    else:
        print(f + ': OK')
