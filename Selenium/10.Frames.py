# # Frames
# # DOM Synthax
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# # Browser Launch
# driver = webdriver.Chrome()
# # Get
# driver.get("https://chercher.tech/practice/frames-example-selenium-webdriver")
# driver.implicitly_wait(10)
# driver.maximize_window()
#
# # 2 Ways to Confirm the option is present inside the frame
# # 1. Right click(Reload Frame or Frame Resources)
# # 2. In DOM (IFRAME OR FRAMESET TAG)
#
# # 4 Ways to switch into the frame
# # driver.switch_to.frame(0) # By using Index
# # driver.switch_to.frame("frame1") # By Using ID
# # driver.switch_to.frame("name")  # By Using Name
#
# # By Using Web Element
# # e = driver.find_element(By.ID, "frame1") # txtbox is inside the frame tag
# driver.switch_to.frame("frame1")
# txtbox = driver.find_element(By.XPATH, "//input[@type='text']")
# txtbox.send_keys("Green Tech1")
# driver.switch_to.default_content()
# # time.sleep(3)
#
# # Drop Down
# driver.switch_to.frame("frame2")
#
# drp = driver.find_element(By.ID, "animals")
# s=Select(drp)
# s.select_by_index(3)
# driver.switch_to.default_content()
# time.sleep(3)
#
# # Check Box
# driver.switch_to.frame("frame1")
# driver.switch_to.frame("frame3")
# chckbox = driver.find_element(By.ID, "a")
# chckbox.click()
# time.sleep(2)
# chckbox.click()
# time.sleep(2)
#
# driver.switch_to.parent_frame()
# txtbox.send_keys(" Chennai")
# time.sleep(3)
#
# 
# # Task(HDFC BANK)