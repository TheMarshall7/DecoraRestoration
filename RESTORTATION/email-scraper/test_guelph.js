const cheerio = require('cheerio');

async function run() {
    const query = 'First Response Restoration Guelph Ontario website';
    const url = 'https://duckduckgo.com/html/?q=' + encodeURIComponent(query);
    
    try {
        const res = await fetch(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        });
        console.log('Status:', res.status);
        const html = await res.text();
        console.log('HTML Length:', html.length);
        const $ = cheerio.load(html);
        console.log('Title:', $('title').text());
        console.log('Includes error-lite:', html.includes('error-lite'));
    } catch(e) {
        console.error(e);
    }
}

run();
