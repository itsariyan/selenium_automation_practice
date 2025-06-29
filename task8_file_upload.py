from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
upload=driver.find_element(By.ID,"file-upload")
upload.send_keys("C:\Users\Personal\Pictures\download.jpeg")
uploadkey=driver.find_element(By.ID,"file-submit")
uploadkey.click()

driver.quit()
