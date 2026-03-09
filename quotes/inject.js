const fs = require('fs');

const file = 'c:/Users/mateo/Desktop/antigravy/website/quotes/Quotes Landing Page.html';
let html = fs.readFileSync(file, 'utf8');

const colors = ['orange', 'blue', 'emerald', 'purple', 'rose', 'grey'];
let i = 0;

html = html.replace(/<article class="masonry-card([^"]*)"/g, (match, classes) => {
    if (match.includes('card-glow')) return match; // Already processed
    const color = colors[i % colors.length];
    i++;
    return `<article class="masonry-card card-glow card-accent-${color}${classes}"`;
});

fs.writeFileSync(file, html, 'utf8');
console.log('Done injecting classes.');
