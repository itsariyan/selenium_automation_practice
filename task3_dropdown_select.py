from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
element=driver.find_element(By.ID,"dropdown")
options=Select(element)

options.select_by_value("1")
print("Option 1 has been selected")

driver.quit()
