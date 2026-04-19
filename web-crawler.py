import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
from bs4 import BeautifulSoup

# Sensitive endpoints to flag
sensitive = [
    '/admin', '/login', '/config', '/backup',
    '/dashboard', '/api', '/secret', '/test',
    '/dev', '/staging', '/upload', '/passwd'
]

def crawl(url):
    print(f"\n Crawling: {url}")
    print("-" * 50)
    
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Page title
        title = soup.find('title')
        print(f" Title: {title.text if title else 'No title found'}")
        print(f" Status Code: {response.status_code}")
        
        # Extract all links
        links = soup.find_all('a')
        print(f" Total Links Found: {len(links)}\n")
        
        flagged = []
        normal = []
        
        for link in links:
            href = link.get('href')
            if href:
                # Check if link contains sensitive endpoint
                is_sensitive = any(s in href.lower() for s in sensitive)
                if is_sensitive:
                    flagged.append(href)
                else:
                    normal.append(href)
        
        # Print flagged links
        if flagged:
            print(" SENSITIVE ENDPOINTS FOUND:")
            for f in flagged:
                print(f"    {f}")
        else:
            print(" No sensitive endpoints detected")
            
        # Print normal links summary
        print(f"\n Normal links: {len(normal)}")
        for link in normal[:5]:  # Show first 5 only
            print(f"  → {link}")
        if len(normal) > 5:
            print(f"  ... and {len(normal)-5} more")
            
    except Exception as e:
        print(f" Error crawling {url}: {e}")

# Target URLs
urls = [
    "https://example.com",
    "https://python.org",
]

for url in urls:
    crawl(url)
