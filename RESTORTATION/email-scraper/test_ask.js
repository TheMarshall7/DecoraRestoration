const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://www.ask.com/web?q=${encodeURIComponent(query)}`;
    
    try {
        console.log("Fetching Ask.com...");
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 5000
        });
        
        console.log('Status:', response.status);
        console.log('HTML length:', response.data.length);
        
        const $ = cheerio.load(response.data);
        console.log('Page Title:', $('title').text());
        
        const links = [];
        // Ask.com search results are in a.class="web-result-title-link" or inside div.PartialSearchResults-item
        $('a').each((i, el) => {
            const href = $(el).attr('href');
            const text = $(el).text();
            if (href && href.startsWith('http') && !href.includes('ask.com')) {
                links.push({ text: text.trim(), href: href });
            }
        });
        
        console.log('Ask.com Links found:', links.slice(0, 10));
    } catch(err) {
        console.error('Ask.com error:', err.message);
    }
}

test();
