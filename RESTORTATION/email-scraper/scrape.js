const fs = require('fs');
const path = require('path');
const axios = require('axios');
const cheerio = require('cheerio');

const csvPath = '/home/isiata/Documents/Brian Marshall/HVAC/RESTORTATION/sunday_open_leads.csv';
const outputPath = '/home/isiata/Documents/Brian Marshall/HVAC/RESTORTATION/sunday_open_leads_enriched.csv';

const sleep = ms => new Promise(r => setTimeout(r, ms));

function parseCSV(csvContent) {
    const lines = csvContent.split(/\r?\n/);
    const result = [];
    const headers = lines[0].split(',');
    
    for (let i = 1; i < lines.length; i++) {
        if (!lines[i].trim()) continue;
        
        const row = [];
        let inQuotes = false;
        let currentCell = '';
        
        for (let j = 0; j < lines[i].length; j++) {
            const char = lines[i][j];
            if (char === '"') {
                inQuotes = !inQuotes;
            } else if (char === ',' && !inQuotes) {
                row.push(currentCell.trim());
                currentCell = '';
            } else {
                currentCell += char;
            }
        }
        row.push(currentCell.trim());
        
        const obj = {};
        headers.forEach((header, idx) => {
            obj[header] = row[idx] ? row[idx].replace(/^"|"$/g, '') : '';
        });
        result.push(obj);
    }
    return result;
}

function escapeCSVCell(value) {
    if (value === null || value === undefined) return '';
    let valStr = String(value);
    if (valStr.includes(',') || valStr.includes('"') || valStr.includes('\n') || valStr.includes('\r')) {
        return '"' + valStr.replace(/"/g, '""') + '"';
    }
    return valStr;
}

async function findWebsite(name, city) {
    const query = `${name} ${city} Ontario website`;
    // Using duckduckgo.com/html/ which is much less likely to block automated requests
    const searchUrl = `https://duckduckgo.com/html/?q=${encodeURIComponent(query)}`;
    
    try {
        const response = await axios.get(searchUrl, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 8000
        });
        const $ = cheerio.load(response.data);
        const links = [];
        
        $('.result__url').each((i, el) => {
            const rawUrl = $(el).attr('href') || $(el).text();
            if (rawUrl) links.push(rawUrl.trim());
        });
        
        const directories = [
            'facebook.com', 'yelp.com', 'yellowpages.ca', 'threebestrated.ca', 
            'mapquest.com', 'instagram.com', 'linkedin.com', 'houzz.com', 
            'zoominfo.com', 'homestars.com', 'bark.com', 'kijiji.ca', 'outscraper.com',
            'duckduckgo.com'
        ];
        
        for (let rawUrl of links) {
            let cleanUrl = rawUrl;
            if (rawUrl.includes('uddg=')) {
                const parts = rawUrl.split('uddg=');
                if (parts.length > 1) {
                    cleanUrl = decodeURIComponent(parts[1].split('&')[0]);
                }
            }
            if (!cleanUrl.startsWith('http')) {
                cleanUrl = 'https://' + cleanUrl;
            }
            
            try {
                const parsedUrl = new URL(cleanUrl);
                const host = parsedUrl.hostname.toLowerCase();
                const isDirectory = directories.some(dir => host.includes(dir));
                if (!isDirectory) {
                    return cleanUrl;
                }
            } catch(e) {
                // ignore invalid
            }
        }
    } catch(err) {
        // ignore
    }
    return null;
}

function extractEmailsFromString(str, emailSet) {
    const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}/g;
    const matches = str.match(emailRegex);
    if (matches) {
        matches.forEach(email => {
            const cleanEmail = email.toLowerCase().trim();
            if (!cleanEmail.endsWith('.png') && 
                !cleanEmail.endsWith('.jpg') && 
                !cleanEmail.endsWith('.jpeg') && 
                !cleanEmail.endsWith('.gif') &&
                !cleanEmail.endsWith('.webp') &&
                !cleanEmail.startsWith('example@') &&
                !cleanEmail.startsWith('yourname@') &&
                !cleanEmail.startsWith('email@') &&
                !cleanEmail.includes('duckduckgo') &&
                !cleanEmail.includes('github') &&
                !cleanEmail.includes('google')) {
                emailSet.add(cleanEmail);
            }
        });
    }
}

async function findEmailsFromWebsite(url) {
    if (!url) return null;
    const emails = new Set();
    
    try {
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 8000
        });
        const html = response.data;
        extractEmailsFromString(html, emails);
        
        if (emails.size > 0) {
            return Array.from(emails);
        }
        
        const $ = cheerio.load(html);
        const contactLinks = [];
        
        $('a').each((i, el) => {
            const href = $(el).attr('href');
            const text = $(el).text().toLowerCase();
            if (href) {
                const cleanHref = href.toLowerCase();
                if (cleanHref.includes('contact') || cleanHref.includes('about') || text.includes('contact') || text.includes('about')) {
                    let absoluteUrl = href;
                    if (!href.startsWith('http')) {
                        const base = new URL(url);
                        absoluteUrl = new URL(href, base.origin).toString();
                    }
                    contactLinks.push(absoluteUrl);
                }
            }
        });
        
        const uniqueLinks = Array.from(new Set(contactLinks)).slice(0, 2);
        for (const link of uniqueLinks) {
            try {
                const pageRes = await axios.get(link, {
                    headers: {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                    },
                    timeout: 5000
                });
                extractEmailsFromString(pageRes.data, emails);
                if (emails.size > 0) break;
            } catch(e) {
                // ignore
            }
        }
    } catch (err) {
        // ignore
    }
    
    return emails.size > 0 ? Array.from(emails) : null;
}

async function searchSnippetEmail(name, city) {
    const query = `"${name}" "${city}" email contact`;
    const searchUrl = `https://duckduckgo.com/html/?q=${encodeURIComponent(query)}`;
    
    try {
        const response = await axios.get(searchUrl, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            },
            timeout: 6000
        });
        const emails = new Set();
        extractEmailsFromString(response.data, emails);
        return emails.size > 0 ? Array.from(emails) : null;
    } catch(err) {
        return null;
    }
}

async function start() {
    const csvContent = fs.readFileSync(csvPath, 'utf8');
    const leads = parseCSV(csvContent);
    
    console.log(`Starting email lookup for ${leads.length} leads...`);
    
    const enrichedLeads = [];
    
    for (let i = 0; i < leads.length; i++) {
        const lead = leads[i];
        console.log(`\n[${i+1}/${leads.length}] Processing: ${lead.Name} (${lead.City})`);
        
        let website = null;
        let emails = null;
        
        // Step 1: Find Website
        website = await findWebsite(lead.Name, lead.City);
        if (website) {
            console.log(`   Website found: ${website}`);
            await sleep(1000);
            
            // Step 2: Extract email from website
            emails = await findEmailsFromWebsite(website);
        } else {
            console.log(`   No website found.`);
        }
        
        // Step 3: Fallback search snippet email lookup
        if (!emails || emails.length === 0) {
            console.log(`   No email on site. Trying search snippet fallback...`);
            await sleep(1000);
            emails = await searchSnippetEmail(lead.Name, lead.City);
        }
        
        if (emails && emails.length > 0) {
            lead.Email = emails.join('; ');
            console.log(`   👉 Email(s) found: ${lead.Email}`);
        } else {
            lead.Email = 'Not Found';
            console.log(`   ❌ No email found.`);
        }
        
        lead.Website = website || 'Not Found';
        
        enrichedLeads.push(lead);
        
        // Periodic saving so we don't lose progress if it stops
        saveProgress(enrichedLeads);
        
        // Wait between leads to be polite
        await sleep(1500);
    }
    
    console.log(`\nFinished! Enriched file saved at ${outputPath}`);
}

function saveProgress(enrichedLeads) {
    const headers = [
        'Name', 'Phone', 'City', 'State', 'Postal Code', 
        'Address', 'Rating', 'Google Maps Link', 'Sunday Hours', 
        'Business Type', 'Website', 'Email'
    ];
    
    let csvContent = headers.join(',') + '\n';
    
    enrichedLeads.forEach(lead => {
        const row = [
            escapeCSVCell(lead['Name']),
            escapeCSVCell(lead['Phone']),
            escapeCSVCell(lead['City']),
            escapeCSVCell(lead['State']),
            escapeCSVCell(lead['Postal Code']),
            escapeCSVCell(lead['Address']),
            escapeCSVCell(lead['Rating']),
            escapeCSVCell(lead['Google Maps Link']),
            escapeCSVCell(lead['Sunday Hours']),
            escapeCSVCell(lead['Business Type']),
            escapeCSVCell(lead['Website']),
            escapeCSVCell(lead['Email'])
        ];
        csvContent += row.join(',') + '\n';
    });
    
    fs.writeFileSync(outputPath, csvContent, 'utf-8');
}

start().catch(console.error);
