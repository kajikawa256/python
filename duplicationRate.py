import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('–headless')
options.add_argument('–no-sandbox')
options.add_argument('–disable-dev-shm-usage')

URL = 'http://enworddojo.holy.jp/index.php'

#Chromeを起動
driver = webdriver.Chrome()

#登録したURLにアクセスする
driver.get(URL)

#カレントページのURLを取得
cur_url = driver.current_url
#カレントページのURLを表示
# print(cur_url)

button = driver.find_element(By.CSS_SELECTOR,
("button[id='nextbutton2']"))
driver.execute_script('arguments[0].click();',button)
time.sleep(3)

#Chromeを終了
driver.quit()