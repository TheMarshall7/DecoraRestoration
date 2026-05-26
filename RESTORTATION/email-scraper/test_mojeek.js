const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://www.mojeek.com/search?q=${encodeURIComponent(query)}`;
    
    try {
        console.log("Fetching Mojeek...");
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
        // Mojeek search results are inside a.ob or in h2 a
        $('a.ob, li a').each((i, el) => {
            const href = $(el).attr('href');
            const text = $(el).text().trim();
            if (href && href.startsWith('http') && !href.includes('mojeek.')) {
                links.push({ text: text.substring(0, 45), href: href });
            }
        });
        
        console.log('Mojeek Links found:', links.slice(0, 15));
    } catch(err) {
        console.error('Mojeek error:', err.message);
    }
}

test();
