const axios = require('axios');
const cheerio = require('cheerio');

const leads = [
    { name: 'Preferred 1 Restoration', city: 'North Bay' },
    { name: 'Restoration Service', city: 'Concord' },
    { name: 'Raj Restoration Inc.', city: 'Scarborough' },
    { name: 'Promus Simcoe', city: 'Simcoe' },
    { name: 'Decora Building Restoration', city: 'Scarborough' }
];

async function findWebsite(name, city) {
    const query = `${name} ${city} Ontario`;
    const url = `https://www.mojeek.com/search?q=${encodeURIComponent(query)}`;
    
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 5000
        });
        
        const $ = cheerio.load(response.data);
        const links = [];
        
        $('a.ob, li a').each((i, el) => {
            const href = $(el).attr('href');
            if (href && href.startsWith('http') && !href.includes('mojeek.') && !href.includes('facebook.com') && !href.includes('yelp.com') && !href.includes('yellowpages.ca')) {
                links.push(href);
            }
        });
        
        return links.length > 0 ? links[0] : null;
    } catch(err) {
        return null;
    }
}

async function run() {
    for (const lead of leads) {
        const site = await findWebsite(lead.name, lead.city);
        console.log(`Lead: ${lead.name} (${lead.city}) -> Website: ${site}`);
        await new Promise(r => setTimeout(r, 1000));
    }
}

run();
