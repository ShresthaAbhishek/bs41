from bs4 import BeautifulSoup
import requests

url_template = 'https://catalog.dallascollege.edu/content.php?catoid=4&navoid=939&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D={page}'
total_pages = 27

# Set to store already seen course headers (to avoid duplicates)
seen_headers = set()

for page_num in range(1, total_pages + 1):
    url = url_template.format(page=page_num)
    print(f"Scraping page {page_num}...")
    results = requests.get(url)
    soup = BeautifulSoup(results.text, 'html.parser')
    
    block_content = soup.find('td', class_='block_content_outer')
    if block_content:
        page_tables = block_content.find_all('table', class_='table_default')
        if len(page_tables) > 1:
            course_table = page_tables[3]
            course_types = course_table.find_all('p')
            for header in course_types:
                strong_text = header.text.strip()
                
                # Check if the header has already been printed
                if strong_text not in seen_headers:
                    print(strong_text)
                    seen_headers.add(strong_text)  # Add to set to avoid future duplicates
                
        else:
            print(f"Less than two tables found on page {page_num}")
    else:
        print(f"No div with class 'block_content_outer' found on page {page_num}")

print("Scraping completed.")
