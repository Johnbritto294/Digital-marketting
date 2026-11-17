with open('blog.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Searching for custom styles or inline style:')
import re
for m in re.finditer(r'style="([^"]*)"', text):
    print(m.group(0))
