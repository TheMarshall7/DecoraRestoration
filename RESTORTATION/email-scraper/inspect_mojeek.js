const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const query = 'Preferred 1 Restoration North Bay Ontario';
    const url = `https://www.mojeek.com/search?q=${encodeURIComponent(query)}`;
    
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 5000
        });
        
        const $ = cheerio.load(response.data);
        console.log('Results container class/id:');
        
        $('ul.results, ol.results, div.results').each((i, el) => {
            console.log('Container tag:', el.name, 'class:', $(el).attr('class'), 'id:', $(el).attr('id'));
        });
        
        const links = [];
        $('.results li a').each((i, el) => {
            const href = $(el).attr('href');
            const text = $(el).text().trim();
            links.push({ text: text, href: href });
        });
        
        console.log('All links inside results list:', links);
    } catch(err) {
        console.error(err.message);
    }
}

test();
