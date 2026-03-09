import re

with open(r'c:\Users\mateo\Desktop\antigravy\website\quotes\Quotes Landing Page.html', 'r', encoding='utf-8') as f:
    html = f.read()

colors = ['orange', 'blue', 'emerald', 'purple', 'rose', 'grey']
idx = [0]

def inject_classes(match):
    color = colors[idx[0] % len(colors)]
    idx[0] += 1
    
    article_tag = match.group(0)
    if 'card-glow' not in article_tag:
        article_tag = article_tag.replace('masonry-card', f'masonry-card card-glow card-accent-{color}')
    return article_tag

html = re.sub(r'<article class="masonry-card([^"]*)"', inject_classes, html)

with open(r'c:\Users\mateo\Desktop\antigravy\website\quotes\Quotes Landing Page.html', 'w', encoding='utf-8') as f:
    f.write(html)
