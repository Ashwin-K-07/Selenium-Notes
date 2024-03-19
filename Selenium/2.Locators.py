import time ## time delay with time.sleep(seconds)

from selenium import webdriver
from selenium.webdriver.common.by import By
1
driver = webdriver.Chrome()
# 2
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
# ID

# User Name
txtuser = driver.find_element(By.ID, "email")
txtuser.send_keys("ashwinkgk07@gmail.com")

# Password
txtpass = driver.find_element(By.ID, "pass")
txtpass.send_keys("98764321")
print("Locators")
# # login
# butnlogin= driver.find_element(By.ID, "u_0_5_nb")
# butnlogin.click()
# time.sleep(4) ## time delay with import time


# Edge
# driver = webdriver.Chrome()
#
# driver.get("https://www.facebook.com/")
## NAME

# User Name
# txtuser = driver.find_element(By.NAME, "email")
# txtuser.send_keys("ashwinkgk07@gmail.com")
#
# Password
# txtpass = driver.find_element(By.NAME, "pass")
# txtpass.send_keys("98764321")
#
# login
# butnlogin= driver.find_element(By.NAME, "login")
# butnlogin.click()

# time.sleep(6)


## Instagram login By NAME
# 1
# driver = webdriver.Chrome()
# 2
# driver.get("https://www.instagram.com/")
# driver.get("https://www.instagram.com/accounts/login/") ## Don't use this type of link

## ID

# time.sleep(3)

# User Name
# txtuser = driver.find_element(By.NAME, "username")
# txtuser.send_keys("ashwinkgk07@gmail.com")

# Password
# txtpass = driver.find_element(By.NAME, "password")
# txtpass.send_keys("98764320001")

# login
# butnlogin= driver.find_element(By.NAME, "---")
# butnlogin.click()

# time.sleep(8)


## Netflix By ID
# 1
# driver = webdriver.Chrome()
# 2
# driver.get("https://www.netflix.com/login") # This url is used to find and fill both emailId and password
# driver.get("https://www.netflix.com/in/") #This url is used only to find_element(find) and send_keys(fill) emailId

## ID

# User Name
# txtuser = driver.find_element(By.ID, ":r0:")
# txtuser.send_keys("ashwinkgk07@gmail.com")

# Password
# txtpass = driver.find_element(By.ID, ":r3:")
# txtpass.send_keys("98764321")

# time.sleep(4)

# login
# butnlogin= driver.find_element(By.ID, "u_0_5_nb")
# butnlogin.click()

## Myntra

# driver = webdriver.Chrome()

# driver.get("https://www.myntra.com/login")

# txtuser = driver.find_element(By.XPATH, "//input[@autocomplete = 'new-password']")
# txtuser.send_keys("6382964622")

# txtpass = driver.find_element(By.XPATH, "//div[@class = 'submitBottomOption']")
# txtpass.click()

# time.sleep(6)



















