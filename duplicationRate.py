from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

#オプション
options = webdriver.ChromeOptions()
options.add_argument('d--disable-blink-features=AutomationControlled')
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('–headless')
options.add_argument('–no-sandbox')
options.add_argument('–disable-dev-shm-usage')

#URLを設定
URL = 'http://enworddojo.holy.jp/index.php'

#高速化
desired = DesiredCapabilities().CHROME
desired['pageLoadStrategy'] = 'none'

#Chromeを起動
driver = webdriver.Chrome()

#登録したURLにアクセスする
driver.get(URL)

#カレントページのURLを取得
cur_url = driver.current_url
#カレントページのURLを表示
# print(cur_url)


for _ in range(10):
  elem = driver.find_element(By.CSS_SELECTOR,
("button[id='nextbutton2']"))
  driver.execute_script('arguments[0].click();',elem)
  #1秒待機
  # time.sleep(1)

#Chromeを終了
driver.quit()