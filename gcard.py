from bs4 import BeautifulSoup
import requests
import re

search_term = input('What product do you want to search for? ')
url = f"https://www.newegg.com/p/pl?d={search_term}"

# Add headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
doc = BeautifulSoup(response.text, "html.parser")

# Find the pagination text safely
page_text = doc.find(class_="list-tool-pagination-text")

if page_text and page_text.strong:
    pages = int(page_text.strong.text.split('/')[-1])  # Extract total pages safely
else:
    print("Pagination element not found! Defaulting to 1 page.")
    pages = 1  # Default to 1 if pagination info is missing

print(f'Total pages found: {pages}')

# Loop through all pages
for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={search_term}&page={page}"
    response = requests.get(url, headers=headers)
    doc = BeautifulSoup(response.text, "html.parser")

    # Find product listings
    div = doc.find(class_='item-cells-wrap border-cells short-video-box items-list-view is-list')
    
    if div:
        items = div.find_all(text=re.compile(search_term, re.IGNORECASE))
        for item in items:
            print(f'Item found: {item}')
    else:
        print(f"No items found on page {page}. Check HTML structure.")
        
print(f"Total of {len(items)*6} found")
        
    