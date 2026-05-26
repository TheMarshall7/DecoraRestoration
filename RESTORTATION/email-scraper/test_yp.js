const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const name = 'Preferred 1 Restoration';
    const city = 'North Bay';
    const url = `https://www.yellowpages.ca/search/si/1/${encodeURIComponent(name)}/${encodeURIComponent(city)}+ON`;
    
    try {
        console.log("Fetching YellowPages.ca...");
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
        
        const websites = [];
        // Yellowpages.ca has website links in a tag with attribute data-mp="true" or inside a class="mlr-link mlr-link-website" or similar.
        // Let's print out all hrefs containing '.ca' or '.com' that are not yellowpages
        $('a').each((i, el) => {
            const href = $(el).attr('href') || '';
            const text = $(el).text().trim();
            if (href.startsWith('http') && !href.includes('yellowpages.ca') && !href.includes('google.com') && !href.includes('facebook.com')) {
                websites.push({ text: text, href: href });
            }
        });
        
        console.log('Found Links:', websites.slice(0, 10));
    } catch(err) {
        console.error('YP error:', err.message);
    }
}

test();
