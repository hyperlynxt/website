import re

with open(r'c:\Users\mateo\Desktop\antigravy\website\quotes\Quotes - Dive.html', 'r', encoding='utf-8') as f:
    html = f.read()

colors = ['orange', 'blue', 'emerald', 'purple', 'rose', 'grey']
color_idx = 0

def replacement(match):
    global color_idx
    color = colors[color_idx % len(colors)]
    color_idx += 1
    
    # Extract inner components
    full_button = match.group(0)
    onclick = match.group(1)
    theme = match.group(2)
    author = match.group(3)
    
    is_active = "active" in match.group(0).split('onclick')[0]
    active_cls = " active" if is_active else ""
    
    numeral_match = re.search(r'<span[^>]*>([^<]+)</span>', full_button)
    numeral = numeral_match.group(1).strip() if numeral_match else ""
    
    quote_match = re.search(r'<p[^>]*line-clamp[^>]*>(.*?)</p>', full_button, flags=re.DOTALL)
    quote = quote_match.group(1).strip() if quote_match else ""
    
    author_text_match = re.search(r'<p[^>]*uppercase[^>]*>(.*?)</p>', full_button, flags=re.DOTALL)
    author_text = author_text_match.group(1).strip() if author_text_match else ""
    
    return f'''<button class="list-item{active_cls} text-left w-full group relative outline-none mb-6 rounded-xl" onclick="{onclick}" data-theme="{theme}" data-author="{author}">
                    <article class="masonry-card card-glow card-accent-{color} p-8 block w-full transition-transform hover:-translate-y-1">
                        <span class="roman-numeral-center" style="font-size: 6rem; bottom: -1rem; right: 1rem; opacity: 0.04;">{numeral}</span>
                        <div class="relative z-10 flex flex-col justify-center mb-6">
                            <p class="text-xl leading-snug text-[#1A1A18] line-clamp-3 italic text-left">
                                {quote}
                            </p>
                        </div>
                        <div class="relative z-10 flex flex-col gap-3 pt-4 border-t border-[#1A1A18]/5">
                            <div class="text-[9px] self-start tracking-widest uppercase text-[#263524] bg-[#263524]/5 px-2 py-1">
                                {theme}
                            </div>
                            <p class="text-[9px] tracking-widest uppercase font-sans font-bold text-[#A5A59D]">
                                {author_text}
                            </p>
                        </div>
                    </article>
                </button>'''

# Match button structure
pattern = re.compile(r'<button class="list-item[^"]*" onclick="(.*?)"\s*data-theme="(.*?)"\s*data-author="(.*?)".*?</button>', flags=re.DOTALL)

new_html = pattern.sub(replacement, html)

with open(r'c:\Users\mateo\Desktop\antigravy\website\quotes\Quotes - Dive.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Replaced {color_idx} items.")
