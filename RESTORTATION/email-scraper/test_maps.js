const axios = require('axios');

async function test() {
    const url = 'https://www.google.com/maps/place/Preferred+1+Restoration/@46.295225599999995,-79.454698,14z/data=!4m8!1m2!2m1!1sPreferred+1+Restoration!3m4!1s0x4d29aa60da26f7e9:0xe242ad8bdfd7ec44!8m2!3d46.295225599999995!4d-79.454698';
    
    try {
        console.log("Fetching Google Maps listing...");
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9'
            },
            timeout: 8000
        });
        
        console.log('Status:', response.status);
        console.log('HTML length:', response.data.length);
        
        // Let's search for URLs starting with http:// or https:// that are not google.com
        const urlRegex = /https?:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}[^\s"\\]*/g;
        const matches = response.data.match(urlRegex) || [];
        const externalUrls = new Set();
        
        matches.forEach(m => {
            try {
                const clean = m.split('\\')[0].split('"')[0].split(']')[0].split('[')[0].split(')')[0];
                const parsed = new URL(clean);
                const host = parsed.hostname.toLowerCase();
                if (!host.includes('google.') && !host.includes('gstatic.') && !host.includes('ggpht.') && !host.includes('googleapis.')) {
                    externalUrls.add(parsed.origin);
                }
            } catch(e) {
                // ignore
            }
        });
        
        console.log('Found External URLs:', Array.from(externalUrls));
    } catch(err) {
        console.error('Google Maps error:', err.message);
    }
}

test();
