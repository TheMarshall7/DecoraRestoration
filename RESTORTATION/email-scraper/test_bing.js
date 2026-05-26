const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://www.bing.com/search?q=${encodeURIComponent(query)}`;
    
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5'
            },
            timeout: 5000
        });
        
        const $ = cheerio.load(response.data);
        const hrefs = [];
        $('a').each((i, el) => {
            const href = $(el).attr('href');
            if (href) hrefs.push(href);
        });
        console.log('All Bing hrefs (first 30):', hrefs.slice(0, 30));
    } catch(err) {
        console.error('Bing error:', err.message);
    }
}

test();
