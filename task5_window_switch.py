from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
main_window = driver.current_window_handle
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(1)  
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break
print("New window title:", driver.title)
driver.switch_to.window(main_window)
print("Back to main window title:", driver.title)

driver.quit()
