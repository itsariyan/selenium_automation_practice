from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
print("Page title:", driver.title) 
driver.quit()
