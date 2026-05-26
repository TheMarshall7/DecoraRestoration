const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const name = 'Preferred 1 Restoration';
    const city = 'North Bay';
    const url = `https://411.ca/search/?q=${encodeURIComponent(name)}&l=${encodeURIComponent(city)}+ON`;
    
    try {
        console.log("Fetching 411.ca...");
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 8000
        });
        
        console.log('Status:', response.status);
        console.log('HTML length:', response.data.length);
        
        const $ = cheerio.load(response.data);
        console.log('Page Title:', $('title').text().trim());
        
        const links = [];
        $('a').each((i, el) => {
            const href = $(el).attr('href');
            if (href && href.startsWith('http') && !href.includes('411.ca')) {
                links.push(href);
            }
        });
        console.log('External Links:', links);
    } catch(err) {
        console.error('411.ca error:', err.message);
    }
}

test();
