import collections
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


#URLを設定
URL = 'http://enworddojo.holy.jp/index.php'

#オプション
options = Options()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
# options.add_argument('--headless')

#Chromeを起動
driver = webdriver.Chrome(options=options)

#登録したURLにアクセスする
driver.get(URL)

#カレントページのURLを取得
cur_url = driver.current_url
#カレントページのURLを表示
# print(cur_url)

words = []
answer = []

for i in range(50):
  try:
    elem = driver.find_element(By.CSS_SELECTOR,
  ("button[id='nextbutton2']"))
  except:
    print('Error')
    time.sleep(10000)
  driver.execute_script('arguments[0].click();',elem)
  if i % 2 == 0:
    elem = driver.find_element(By.CSS_SELECTOR,'h3')
    words.append(elem.text)
    elem = driver.find_element(By.CSS_SELECTOR,("span[id='mean']"))
    answer.append(elem.text)
  
output = collections.Counter(words)
output2 = collections.Counter(answer)
print('出題された英単語で一番多かったもの',max(output),output[max(output)],end='')
print('回')
print('出題された解答で一番多かったもの',max(output2),output2[max(output2)],end='')
print('回')

#Chromeを終了
driver.quit()