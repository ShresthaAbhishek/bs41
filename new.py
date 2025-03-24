from bs4 import BeautifulSoup
import requests

url = 'https://www.newegg.com/p/0GA-00CM-00513?Item=9SIA4REJ9J2529&cm_sp=PremiumSellerStore_MKPL-_-P0_9SIA4REJ9J2529-_-03202025'

results = requests.get(url)
soup = BeautifulSoup(results.text, "html.parser")


prices = soup.find_all(string="$")
parent = prices[0].parent #finding the parent tag that contains $
print(parent)# printing parent


strong = parent.find("strong")#finds parent tag containing <strong>
print(strong.string)#printing strong 

