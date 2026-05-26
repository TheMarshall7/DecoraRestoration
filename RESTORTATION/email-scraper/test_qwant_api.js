const axios = require('axios');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://api.qwant.com/v3/search/web?q=${encodeURIComponent(query)}&count=10&locale=en_US`;
    
    try {
        console.log("Fetching Qwant API with referer...");
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'Accept': 'application/json',
                'Referer': 'https://www.qwant.com/',
                'Origin': 'https://www.qwant.com/'
            },
            timeout: 5000
        });
        
        console.log('Status:', response.status);
        console.log('Results:', response.data.data.result.items.slice(0, 3));
    } catch(err) {
        console.error('Qwant API error:', err.message);
        if (err.response) {
            console.error('Response status:', err.response.status);
        }
    }
}

test();
