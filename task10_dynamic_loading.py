from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
start = driver.find_element(By.CSS_SELECTOR, "#start button")
start.click()
wait = WebDriverWait(driver, 15)
element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
print(element.text)
driver.quit()
