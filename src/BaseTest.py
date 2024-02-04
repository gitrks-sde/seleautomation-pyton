from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
time.sleep(5)