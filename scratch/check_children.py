with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m = re.search(r'<div class="row g-4" data-stagger>(.*?)</div>\s*<nav', html, re.DOTALL)
if m:
    content = m.group(1)
    div_depth = 0
    direct_children = 0
    for tag in re.findall(r'</?div\b[^>]*>', content):
        if tag.startswith('</'):
            div_depth -= 1
        else:
            if div_depth == 0:
                direct_children += 1
            div_depth += 1
    print('Direct children count:', direct_children)
    print('Final div depth:', div_depth)
else:
    print('Pattern not found')
