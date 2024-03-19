## ACTIONS
# Mouse over action
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Browser launch
driver = webdriver.Chrome()

driver.get("https://www.greenstechnologys.com/python-training.html")
driver.implicitly_wait(10)
driver.maximize_window()

a = ActionChains(driver)
move1 = driver.find_element(By.XPATH, "//div[text() = 'Courses ']")
a.move_to_element(move1).perform()

move2 = driver.find_element(By.XPATH, "//span[text() = 'Software Testing (12)']")
a.move_to_element(move2).perform()

move3 = driver.find_element(By.XPATH, "//span[text()='Selenium Certification Training']")
a.click(move3).perform()

# Another Method
a.move_to_element(move1).move_to_element(move2).click(move3).perform()

time.sleep(6)


import time

# Drag and Drop
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Browser Launch
driver = webdriver.Chrome()

# Get
driver.get("http://demo.guru99.com/test/drag_drop.html")
driver.implicitly_wait(10)
driver.maximize_window()

a = ActionChains(driver)
# Drag and Drop
from1 = driver.find_element(By.XPATH, "(//a[@class='button button-orange'])[5]")
to1 = driver.find_element(By.ID, "bank")

a.drag_and_drop(from1,to1).perform()

# Click and Hold---> Move To---> Release
a.click_and_hold(from1).move_to_element(to1).release().perform()
time.sleep(4)

# Click and Hold ----> Release
a.click_and_hold(from1).release(to1).perform()


















