import requests
from bs4 import BeautifulSoup
import json
import argparse
import time
import sys

def scrape_google_scholar(query, max_pages=5):
    base_url = "https://scholar.google.com/scholar"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    all_papers = []

    for page in range(0, max_pages):
        print("Fetching page", page+1, "...")
        params = {'q': query, 'start': page * 10}
        if page == 0:
            # directly using start=0 will get a request denial
            response = requests.get(f"https://scholar.google.com/scholar?q={query}", headers=headers)
        else:
            response = requests.get(base_url, headers=headers, params=params)
        # BeautifulSoup to parse html information
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.select('.gs_ri'):
            try:
                title = item.select_one('.gs_rt').text
                preview = item.select_one('.gs_rs').text
                author_info = item.select_one('.gs_a').text
                all_papers.append({'title': title, 'preview': preview, 'author_info': author_info})
            except AttributeError:
                # Skipping item if it doesn't have title or preview
                continue
        
        time.sleep(5)  # Sleep to prevent being blocked by Google Scholar

    return all_papers

def main():
    #arg parsing
    print("Usage: python getGoogleScholar.py <search_query> --pages <number_of pages>")
    parser = argparse.ArgumentParser(description='Google Scholar Scraper')
    parser.add_argument('query', type=str, help='Search query for Google Scholar')
    parser.add_argument('--pages', type=int, default=5, help='Number of pages to scrape')
    args = parser.parse_args()
    query = args.query
    max_pages = args.pages

    results = scrape_google_scholar(query, max_pages)
    with open('results.json', 'w') as f:
        print("Dumping results to results.json...")
        json.dump(results, f, indent=4)
        print("Execution completed.")

if __name__ == "__main__":
    main()