from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
for add in range(1,6):

    add=driver.find_element(By.CSS_SELECTOR,"button[onclick='addElement()']")
    add.click()
    time.sleep(1)
for dlt in range(1,3):
    dlt=driver.find_element(By.CSS_SELECTOR,"button[onclick='deleteElement()']")
    dlt.click()
    time.sleep(1)
rem=driver.find_elements(By.CSS_SELECTOR,"button[onclick='deleteElement()']")
print(len(rem))

driver.quit()
