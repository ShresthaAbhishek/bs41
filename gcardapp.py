from bs4 import BeautifulSoup
import requests
import re

gpu = input("What product do u want to search for? ")
url = f"https://www.newegg.ca/p/pl?d={gpu}"


#get the page and store it in page
response = requests.get(url).text 
#create a new soup/doc using html parser for page
doc = BeautifulSoup(response, "html.parser")    

page_text = doc.find('span' , class_ = "list-tool-pagination-text")

print(page_text)