import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
from bs4 import BeautifulSoup

def crawl(url):
    print(f"\n Crawling: {url}")
    
    # Get the webpage
    response = requests.get(url)
    
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract page title
    title = soup.find('title')
    print(f" Title: {title.text if title else 'No title found'}")
    
    # Extract all links
    links = soup.find_all('a')
    print(f"\n Links found: {len(links)}")
    
    for link in links:
        href = link.get('href')
        text = link.text.strip()
        if href:
            print(f"   {text[:30]} | {href}")

# Crawl multiple URLs
urls = [
    "https://example.com",
    "https://wikipedia.org",
    "https://python.org"
]

for url in urls:
    crawl(url)
