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
        const links = [];
        
        $('a').each((i, el) => {
            const href = $(el).attr('href') || '';
            const text = $(el).text().trim();
            const classNames = $(el).attr('class') || '';
            const dataAttributes = JSON.stringify($(el).data()) || '';
            
            if (href.includes('website') || href.includes('/bus/') || classNames.includes('website') || dataAttributes.includes('website')) {
                links.push({ text: text, href: href, class: classNames, data: dataAttributes });
            }
        });
        
        console.log('Matches:', links);
    } catch(err) {
        console.error(err.message);
    }
}

test();
