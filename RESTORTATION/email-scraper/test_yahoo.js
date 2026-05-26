const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
    
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 5000
        });
        
        const $ = cheerio.load(response.data);
        const hrefs = [];
        $('a').each((i, el) => {
            const href = $(el).attr('href');
            if (href) hrefs.push(href);
        });
        console.log('All hrefs found (first 30):', hrefs.slice(0, 30));
    } catch(err) {
        console.error(err.message);
    }
}

test();
