async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://duckduckgo.com/html/?q=${encodeURIComponent(query)}`;
    
    try {
        console.log("Fetching DDG with native fetch...");
        const response = await fetch(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }
        });
        
        console.log('Status:', response.status);
        const html = await response.text();
        console.log('HTML length:', html.length);
        console.log('Includes error-lite:', html.includes('error-lite'));
    } catch(err) {
        console.error('Fetch error:', err.message);
    }
}

test();
