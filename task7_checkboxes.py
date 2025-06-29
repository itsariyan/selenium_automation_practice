from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkboxes=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
if not checkboxes[0].is_selected():
    checkboxes[0].click()
    print("first checkbox was not selected.Now it is selected")
else:
    print("First checkbox was already selected")
    
if not checkboxes[1].is_selected():
    checkboxes[1].click()
    print("Second checkbox was not selected.Now it is selected")
else:
    print("Second checkbox was already selected")
time.sleep(3)
driver.quit()
