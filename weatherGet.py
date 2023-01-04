import requests
from bs4 import BeautifulSoup

url = 'https://tenki.jp/forecast/6/30/6200/27213/'
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

dates = soup.find_all('h3', class_='left-style')
date = [x.text for x in dates]

samp = soup.find_all('span', 'value')
temp = [x.text for x in samp] 


print('大阪府泉佐野市')
print(date[0],'の気温')
print('最高',temp[0],'℃\t','最低',temp[1],'℃')