import requests
from bs4 import BeautifulSoup as bp

res = requests.get()
soup = bp(res.text,'html.parser')
h2_tags = soup.find_all('h2')
