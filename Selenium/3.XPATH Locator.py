# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.facebook.com/")

# By CLASS
# txtusr = driver.find_element(By.CLASS_NAME, "inputtext _55r1 _6luy")
# txtusr.send_keys("Ashwin")

# Absolute XPATH(/) eg: /html/head/title/input.....

# Relative XPATH
# txtuser = driver.find_element(By.XPATH, "//input[@id='email']")
# txtuser.send_keys("ashwin234@gmail.com") # invalid mailid or phnno. or name is given login action is not performed
#
# txtpass = driver.find_element(By.XPATH, "//input[@type='password']")
# txtpass.send_keys("87654321")
#
# btnlogin = driver.find_element(By.XPATH, "//button[@type='submit']")
# btnlogin.click()
#
# time.sleep(6)

# 1 Way[For Web element]
# crtbtn = driver.find_element(By.XPATH, "(//a[@role='button'])[2]")
# crtbtn.click()

# 2 Way[List(Web element)]
# crbts = driver.find_elements(By.XPATH, "//a[@role='button']") #---> value--(By.XPATH, "(//a[@role='button'])")
# wb= crbts[1] # Slice Operator (index)
# wb.click()
# time.sleep(6)
