const axios = require('axios');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://api.duckduckgo.com/?q=${encodeURIComponent(query)}&format=json&no_html=1`;
    
    try {
        console.log("Fetching DDG API...");
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 5000
        });
        
        console.log('Status:', response.status);
        console.log('Keys in response:', Object.keys(response.data));
        console.log('AbstractURL:', response.data.AbstractURL);
        console.log('Results:', response.data.Results);
        console.log('RelatedTopics:', response.data.RelatedTopics ? response.data.RelatedTopics.slice(0, 3) : []);
    } catch(err) {
        console.error('DDG API error:', err.message);
    }
}

test();
