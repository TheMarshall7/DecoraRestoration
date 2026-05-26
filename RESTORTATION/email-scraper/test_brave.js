const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://search.brave.com/search?q=${encodeURIComponent(query)}`;
    
    try {
        console.log("Fetching Brave Search...");
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5'
            },
            timeout: 5000
        });
        
        console.log('Status:', response.status);
        console.log('HTML length:', response.data.length);
        
        const $ = cheerio.load(response.data);
        console.log('Page Title:', $('title').text());
        
        const links = [];
        // Brave results are in class "svelte-..." or standard class selectors.
        // Let's print out all href values that look like external websites.
        $('a').each((i, el) => {
            const href = $(el).attr('href');
            const text = $(el).text().trim();
            if (href && href.startsWith('http') && !href.includes('brave.com') && !href.includes('google.com')) {
                links.push({ text: text.substring(0, 45), href: href });
            }
        });
        
        console.log('Brave Links found:', links.slice(0, 10));
    } catch(err) {
        console.error('Brave error:', err.message);
    }
}

test();
