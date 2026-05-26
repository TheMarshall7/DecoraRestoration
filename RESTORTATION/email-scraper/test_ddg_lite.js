const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario website';
    
    try {
        console.log("Fetching DDG Lite...");
        const response = await axios.post('https://lite.duckduckgo.com/lite/', `q=${encodeURIComponent(query)}`, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            timeout: 5000
        });
        
        console.log('Status:', response.status);
        console.log('HTML length:', response.data.length);
        
        const $ = cheerio.load(response.data);
        console.log('Page Title:', $('title').text());
        
        const links = [];
        // In DDG Lite, results are inside table.links elements
        $('a').each((i, el) => {
            const href = $(el).attr('href');
            const text = $(el).text();
            if (href && href.startsWith('http') && !href.includes('duckduckgo.com')) {
                links.push({ text: text.trim(), href: href });
            }
        });
        
        console.log('DDG Lite Links found:', links.slice(0, 5));
    } catch(err) {
        console.error('DDG Lite error:', err.message);
        if (err.response) {
            console.error('Response data:', err.response.data);
        }
    }
}

test();
