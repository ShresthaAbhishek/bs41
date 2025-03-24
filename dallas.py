from bs4 import BeautifulSoup
import requests
import re

url = "https://catalog.dallascollege.edu/content.php?catoid=4&catoid=4&navoid=939&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=1#acalog_template_course_filter"

results = requests.get(url)
soup = BeautifulSoup(results.text, 'html.parser')

# Find the div containing the tables
block_content = soup.find('td', class_='block_content_outer')

if block_content:
    # Find all tables within this div
    page_tables = block_content.find_all('table', class_='table_default')

    print(f"Found {len(page_tables)} tables inside 'block_content_outer'")

    if len(page_tables) > 1:
        course_table = page_tables[3]  # Get the fourth table
        course_types = course_table.find_all('p')  # Find all <p> elements
    
    for header in course_types:
        strong_text = header.text.strip()  # Extract text from each <p> element
        print(f"{strong_text}")  # Print each paragraph's text
    
    print(course_types[0].string if course_types else "No paragraphs found.")  # Print first <p> text
else:
    print("Less than two tables found inside 'block_content_outer'")

