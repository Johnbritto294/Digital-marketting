import glob, re

for fname in ['about.html', 'features.html', 'index.html', 'blog.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    idx = text.find('cta')
    while idx != -1:
        snippet = text[max(0, idx-80):min(len(text), idx+100)]
        print(f"=== {fname} at {idx} ===")
        print(snippet.replace('\n', ' '))
        idx = text.find('cta', idx + 10)
