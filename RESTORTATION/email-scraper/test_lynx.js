const axios = require('axios');
const cheerio = require('cheerio');

async function test() {
    const url = 'https://www.google.com/search?q=Preferred+1+Restoration+North+Bay+Ontario&hl=en';
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Lynx/2.8.9rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/1.1.1d'
            }
        });
        const $ = cheerio.load(response.data);
        const links = [];
        $('a').each((i, el) => {
            const href = $(el).attr('href') || '';
            const text = $(el).text().trim();
            links.push({ text: text, href: href });
        });
        console.log('All links:', links);
    } catch(err) {
        console.error(err.message);
    }
}

test();
