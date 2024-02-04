from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
input=driver.find_element(By.ID,"my-text-id")
input.send_keys("Tutorial");
time.sleep(5)