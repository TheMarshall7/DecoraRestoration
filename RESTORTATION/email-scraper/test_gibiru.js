const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://gibiru.com/results.html?q=${encodeURIComponent(query)}`;
    
    try {
        console.log("Fetching Gibiru...");
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
        // Gibiru results are usually in a tags containing the link
        $('a').each((i, el) => {
            const href = $(el).attr('href');
            if (href && href.startsWith('http') && !href.includes('gibiru.com') && !href.includes('google.com')) {
                links.push(href);
            }
        });
        
        console.log('Gibiru Links found:', links.slice(0, 10));
    } catch(err) {
        console.error('Gibiru error:', err.message);
    }
}

test();
