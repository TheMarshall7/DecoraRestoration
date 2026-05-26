const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const url = 'https://www.yellowpages.ca/search/si/1/Preferred+1+Restoration/North+Bay+ON';
    
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        });
        
        const $ = cheerio.load(response.data);
        const results = [];
        
        // Let's find all merchant cards. They usually have class "listing" or "merchant-card" or similar
        $('.listing').each((i, el) => {
            const name = $(el).find('.jsListingName').text().trim();
            const websiteBtn = $(el).find('a.mlr__item__cta[href*="redirect="], a[href*="/gourl/"]');
            let website = 'None';
            
            if (websiteBtn.length > 0) {
                const href = websiteBtn.attr('href') || '';
                const parts = href.split('redirect=');
                if (parts.length > 1) {
                    website = decodeURIComponent(parts[1].split('&')[0]);
                }
            }
            
            results.push({ name: name, website: website });
        });
        
        console.log('YP Merchant Listings found:', results);
    } catch(err) {
        console.error(err.message);
    }
}

test();
