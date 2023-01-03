import requests
from bs4 import BeautifulSoup as bp

res = requests.get('https://scraping-training.vercel.app/site?postCount=20&title=%E3%81%93%E3%82%8C%E3%81%AF{no}%E3%81%AE%E8%A8%98%E4%BA%8B%E3%81%A7%E3%81%99&dateFormat=YYYY-MM-DD&isTime=true&timeFormat=&isImage=true&interval=360&isAgo=true&countPerPage=10&page=1&robots=true&')
soup = bp(res.content,'html.parser')

#クラスを指定して取得
div_tags = soup.find_all('div', class_='post-title font-bold')

#文字列のみに成型
div_str = [x.string for x in div_tags]

for word in div_str:
  print(word)