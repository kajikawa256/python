import collections
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


#URLを設定
URL = 'http://enworddojo.holy.jp/index.php'

#オプション
options = Options()
options.add_argument('--headless')

#Chromeを起動
driver = webdriver.Chrome(options=options)

#登録したURLにアクセスする
driver.get(URL)

#カレントページのURLを取得
cur_url = driver.current_url
#カレントページのURLを表示
# print(cur_url)

words = []

for i in range(50):
  elem = driver.find_element(By.CSS_SELECTOR,
("button[id='nextbutton2']"))
  driver.execute_script('arguments[0].click();',elem)
  if i % 2 == 0:
    elem = driver.find_element(By.CSS_SELECTOR,'h3')
    words.append(elem.text)
  
output = collections.Counter(words)
print(output)

#Chromeを終了
driver.quit()