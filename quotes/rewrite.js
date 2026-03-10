const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'Quotes - Dive.html');
let html = fs.readFileSync(filePath, 'utf8');

const colors = ['orange', 'blue', 'emerald', 'purple', 'rose', 'grey'];
let colorIdx = 0;

const regex = /<button class="list-item([^"]*)" onclick="([^"]*)"\s*data-theme="([^"]*)"\s*data-author="([^"]*)".*?<\/button>/gs;

const newHtml = html.replace(regex, (match, classes, onclick, theme, author) => {
    const color = colors[colorIdx % colors.length];
    colorIdx++;

    // Check if it's active
    const isActive = classes.includes('active') ? ' active' : '';

    // Extract numeral, quote, author_text
    const numeralMatch = /<span[^>]*>(.*?)<\/span>/.exec(match);
    const numeral = numeralMatch ? numeralMatch[1].trim() : '';

    const quoteMatch = /<p[^>]*line-clamp[^>]*>([\s\S]*?)<\/p>/.exec(match);
    const quote = quoteMatch ? quoteMatch[1].trim() : '';

    const authorMatch = /<p[^>]*uppercase[^>]*>([\s\S]*?)<\/p>/.exec(match);
    const authorText = authorMatch ? authorMatch[1].trim() : '';

    return `<button class="list-item${isActive} text-left w-full group relative outline-none mb-6 rounded-xl" onclick="${onclick}" data-theme="${theme}" data-author="${author}">
                    <article class="masonry-card card-glow card-accent-${color} p-8 block w-full transition-transform hover:-translate-y-1">
                        <span class="roman-numeral-center" style="font-size: 6rem; bottom: -1rem; right: 1rem; opacity: 0.04;">${numeral}</span>
                        <div class="relative z-10 flex flex-col justify-center mb-6">
                            <p class="text-xl leading-snug text-[#1A1A18] line-clamp-3 italic text-left">
                                ${quote}
                            </p>
                        </div>
                        <div class="relative z-10 flex flex-col gap-3 pt-4 border-t border-[#1A1A18]/5">
                            <div class="text-[9px] self-start tracking-widest uppercase text-[#263524] bg-[#263524]/5 px-2 py-1">
                                ${theme}
                            </div>
                            <p class="text-[9px] tracking-widest uppercase font-sans font-bold text-[#A5A59D]">
                                ${authorText}
                            </p>
                        </div>
                    </article>
                </button>`;
});

fs.writeFileSync(filePath, newHtml, 'utf8');
console.log(`Replaced ${colorIdx} items.`);
