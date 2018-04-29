# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# ブラウザを開きます
driver = webdriver.Chrome()

# ブラウザを開く。
driver = webdriver.Chrome()
# Googleの検索TOP画面を開く。
driver.get("https://www.google.co.jp/")
# 検索語として「selenium」と入力し、Enterキーを押す。
driver.find_element_by_id("lst-ib").send_keys("ポケモン")
driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
# タイトルに「Selenium - Web Browser Automation」と一致するリンクをクリックする。
driver.find_element_by_link_text("ポケモンセンターオンライン").click()
driver.find_element_by_link_text("ログイン/会員登録").click()
id = driver.find_element_by_id("login_mail")
id.send_keys("ID")
password = driver.find_element_by_id("login_pass")
password.send_keys("password")
login_button = driver.find_element_by_id("login_submit")
login_button.click()

# 5秒間待機してみる。
sleep(5)
# ブラウザを終了する。
driver.close()