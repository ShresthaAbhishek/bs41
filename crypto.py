from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

tbody = doc.tbody #getting tablebody(tbody)
trs = tbody.contents#  gives contents of the tbody tag

# print(trs) #trs[0].next_sibling gives next element 
           #trs[0].parent gives the tag before it
           #trs[0].decendants gives all the table decendentants /content
           
prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    
    fixed_name = name.p.string
    fixed_price = price.span.string
    
    prices[fixed_name] = fixed_price
# print(prices)
    print(f'Name: {fixed_name}')
    print(f'Price: {fixed_price}')
    print()
    
    

