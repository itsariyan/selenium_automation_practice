from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/login")
username=driver.find_element(By.ID,"username")
password=driver.find_element(By.ID,"password")
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
btn=driver.find_element(By.CSS_SELECTOR,"i[class='fa fa-2x fa-sign-in']")
btn.click()
text=driver.find_element(By.ID,"flash")
print(text.text)
