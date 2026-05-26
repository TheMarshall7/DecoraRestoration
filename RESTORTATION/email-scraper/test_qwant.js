const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://lite.qwant.com/?q=${encodeURIComponent(query)}&t=web`;
    
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 5000
        });
        
        const $ = cheerio.load(response.data);
        const links = [];
        
        $('a').each((i, el) => {
            const href = $(el).attr('href');
            const text = $(el).text().trim();
            if (href && (href.includes('.ca') || href.includes('.com') || href.includes('.org')) && !href.includes('qwant')) {
                links.push({ text: text.substring(0, 45), href: href });
            }
        });
        
        console.log('Qwant External Links:', links);
    } catch(err) {
        console.error('Qwant error:', err.message);
    }
}

test();
