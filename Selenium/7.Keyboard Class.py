# Keyboard Class(Robot Class)
# Both Mouse and keyboard to perform actions
import time
import keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Browser Launch
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Get
driver.get("https://www.facebook.com/")

txtuser = driver.find_element(By.ID, "email")
txtuser.send_keys("Ashwin")

a = ActionChains(driver)
a.double_click(txtuser).perform() # Double click
a.context_click(txtuser).perform() # Right click

# 3 Times Down (For selecting copy option)
keyboard.press("Down")
keyboard.release("Down")

keyboard.press("down")
keyboard.release("down")

keyboard.press("down")
keyboard.release("down")

# 1 Time Enter (For clicking coping option)
keyboard.press("Enter")
keyboard.release("Enter")

txtpass = driver.find_element(By.ID, "pass")
a.context_click(txtpass).perform()

# 4 Times Down(For selecting paste option)
for i in range(0,4,1):
    keyboard.press("down")
    keyboard.release("down")

# 1 Time Enter (For clicking paste option)
keyboard.press("enter")
keyboard.release("enter")
# to get the value and to print it
x=txtpass.get_attribute("value")
print(x)
time.sleep(10)

# Using Keyboard to perform actions
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

# Browser Launch
driver = webdriver.Chrome()

# Get
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
driver.maximize_window()

txtuser = driver.find_element(By.ID, "email")
txtuser.send_keys("Greens")

# Select All
keyboard.press("Control")
keyboard.press("A")
keyboard.release("Control")
keyboard.release("A")

# Copy
keyboard.press("Control")
keyboard.press("c")
keyboard.release("Control")
keyboard.release("c")

# Tab
keyboard.press("Tab")
keyboard.release("tab")

# Paste
keyboard.press("Control")
keyboard.press("V")
keyboard.release("Control")
keyboard.release("V")

# to get the value and to print it
txtpass = driver.find_element(By.ID, "pass")
y = txtpass.get_attribute("value")
print(y)


# Task
import time
import keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Browser Launch
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Get
driver.get("https://www.facebook.com/")

txtuser = driver.find_element(By.ID, "email")
txtuser.send_keys("Greens2024@gmail.com")

a = ActionChains(driver)
a.double_click(txtuser).double_click().perform() # Two Double clicks to select all text because of mailId(.com)
a.double_click(txtuser).click().perform() # Two Double clicks to select all text because of mailId(.com)

# (It selects only .com)
a.double_click(txtuser).double_click(txtuser).perform() # Two Double clicks Method 2
a.context_click(txtuser).perform() # Right click

# 3 Times Down (For selecting copy option)
keyboard.press("Down")
keyboard.release("Down")

keyboard.press("down")
keyboard.release("down")

keyboard.press("down")
keyboard.release("down")

# 1 Time Enter (For clicking coping option)
keyboard.press("Enter")
keyboard.release("Enter")

txtpass = driver.find_element(By.ID, "pass")
a.context_click(txtpass).perform()

# 4 Times Down(For selecting paste option)
for i in range(0,4,1):
    keyboard.press("down")
    keyboard.release("down")

# 1 Time Enter (For clicking paste option)
keyboard.press("enter")
keyboard.release("enter")
# to get the value and to print it
x=txtpass.get_attribute("value")
print(x)
time.sleep(10)






























