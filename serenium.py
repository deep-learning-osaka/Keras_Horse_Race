

# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# ブラウザを開きます
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
# Googleの検索TOP画面を開く。
driver.get("https://grp02.id.rakutßen.co.jp/rms/nid/loginfwd?__event=LOGIN&service_id=n58&return_url=%2Fbet%2F")

#パスワードとユーザーIDを入力します
id = driver.find_element_by_name("u")
id.send_keys("ID")
password = driver.find_element_by_name("p")
password.send_keys("password")

#ログインボタンを押下します
login_button = driver.find_element_by_class_name("loginbutton")
login_button.click()

sleep(5)
# ブラウザを終了します
driver.close()

