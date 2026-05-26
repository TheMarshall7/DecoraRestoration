const axios = require('axios');
const cheerio = require('cheerio');

async function test(userAgent) {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
    
    try {
        console.log(`\nTesting User-Agent: ${userAgent.substring(0, 30)}...`);
        const response = await axios.get(url, {
            headers: {
                'User-Agent': userAgent
            },
            timeout: 5000
        });
        
        const $ = cheerio.load(response.data);
        console.log('HTML Length:', response.data.length);
        console.log('Title:', $('title').text());
        
        const links = [];
        $('a').each((i, el) => {
            const href = $(el).attr('href') || '';
            const text = $(el).text().trim();
            // Google's search result links on simple mobile/fallback browsers look like: /url?q=https://example.com/
            if (href.startsWith('/url?q=')) {
                const cleanUrl = decodeURIComponent(href.split('/url?q=')[1].split('&')[0]);
                if (!cleanUrl.includes('google.com')) {
                    links.push({ text: text.substring(0, 40), url: cleanUrl });
                }
            } else if (href.startsWith('http') && !href.includes('google.com')) {
                links.push({ text: text.substring(0, 40), url: href });
            }
        });
        
        console.log('Found Links:', links.slice(0, 8));
    } catch(err) {
        console.error('Error:', err.message);
    }
}

async function run() {
    const uas = [
        // 1. Mobile Safari
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        // 2. Old Opera/Mini
        'Opera/9.80 (Android; Opera Mini/36.1.2254/119.132; U; en) Presto/2.12.423 Version/12.16',
        // 3. Simple text browser (Lynx)
        'Lynx/2.8.9rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/1.1.1d',
        // 4. Default Axios (no UA)
        undefined
    ];
    
    for (const ua of uas) {
        await test(ua || 'Axios-Default');
    }
}

run();
