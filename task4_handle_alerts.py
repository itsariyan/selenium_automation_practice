from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
btn=driver.find_element(By.CSS_SELECTOR,"button[onclick='jsAlert()']")
btn.click()
time.sleep(3)
alert=driver.switch_to.alert
alert.accept()
result=driver.find_element(By.ID,"result")
print(result.text)
time.sleep(4)
