const cheerio = require('cheerio');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://duckduckgo.com/html/?q=${encodeURIComponent(query)}`;
    
    try {
        console.log("Fetching DDG...");
        const response = await fetch(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        });
        
        const html = await response.text();
        const $ = cheerio.load(html);
        
        console.log('Page Title:', $('title').text());
        
        const links = [];
        // DuckDuckGo HTML results are in a.result__url or inside class result__snippet / result__snippet a
        $('.result__url').each((i, el) => {
            const rawUrl = $(el).attr('href') || $(el).text();
            if (rawUrl) links.push(rawUrl.trim());
        });
        
        console.log('Raw links found:', links.slice(0, 10));
        
        // Let's decode DDG redirects (e.g. /l/?kh=-1&uddg=https%3A%2F%2Fwww.preferred1restoration.ca%2F)
        const cleanLinks = links.map(rawUrl => {
            let cleanUrl = rawUrl;
            if (rawUrl.includes('uddg=')) {
                const parts = rawUrl.split('uddg=');
                if (parts.length > 1) {
                    cleanUrl = decodeURIComponent(parts[1].split('&')[0]);
                }
            }
            if (!cleanUrl.startsWith('http') && !cleanUrl.startsWith('/')) {
                cleanUrl = 'https://' + cleanUrl;
            }
            return cleanUrl;
        });
        
        console.log('Clean links found:', cleanLinks.slice(0, 10));
    } catch(err) {
        console.error('Error:', err.message);
    }
}

test();
