const axios = require('axios');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    // We can try a few public Searx instances
    const instances = [
        'https://searx.be',
        'https://searx.me',
        'https://search.ononoki.org',
        'https://searx.work',
        'https://baresearch.org'
    ];
    
    for (const instance of instances) {
        const url = `${instance}/search?q=${encodeURIComponent(query)}&format=json`;
        try {
            console.log(`Fetching from Searx instance: ${instance}...`);
            const response = await axios.get(url, {
                headers: {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                },
                timeout: 6000
            });
            
            console.log(`Success from ${instance}!`);
            const results = response.data.results || [];
            console.log(`Found ${results.length} results.`);
            
            const links = results.map(r => ({ title: r.title, url: r.url }));
            console.log('Results (first 5):', links.slice(0, 5));
            return; // Exit on first success
        } catch(err) {
            console.error(`Error from ${instance}:`, err.message);
        }
    }
}

test();
