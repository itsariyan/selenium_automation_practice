from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/large")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.save_screenshot("scroll_test.png")
print("Screenshot saved as scroll_test.png")
time.sleep(1)
driver.quit()
