const axios = require('axios');
const cheerio = require('cheerio');

async function testQuery(name, city) {
    const url = `https://www.yellowpages.ca/search/si/1/${encodeURIComponent(name)}/${encodeURIComponent(city)}+ON`;
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 8000
        });
        const $ = cheerio.load(response.data);
        const results = [];
        $('.listing').each((i, el) => {
            const mName = $(el).find('.jsListingName').text().trim();
            const websiteBtn = $(el).find('a.mlr__item__cta[href*="redirect="], a[href*="/gourl/"]');
            let website = 'None';
            if (websiteBtn.length > 0) {
                const href = websiteBtn.attr('href') || '';
                const parts = href.split('redirect=');
                if (parts.length > 1) {
                    website = decodeURIComponent(parts[1].split('&')[0]);
                }
            }
            results.push({ name: mName, website: website });
        });
        console.log(`\nSearch for: "${name}" in "${city}" -> Found ${results.length} results:`);
        results.slice(0, 5).forEach(r => console.log(` - ${r.name} (${r.website})`));
    } catch(err) {
        console.error(`YP Search error for ${name}:`, err.message);
    }
}

async function run() {
    await testQuery('PuroClean Restoration Kingston', 'Kingston');
    await testQuery('EcoEnergy Environmental Services', 'Ottawa');
    await testQuery('Water Damage Restoration Windsor', 'Windsor');
}

run();
