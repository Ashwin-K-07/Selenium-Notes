import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.facebook.com/")
# driver.implicitly_wait(10)
# driver.maximize_window()
#
# crtbtn = driver.find_element(By.XPATH, "(//a[@role='button'])[2]")
# crtbtn.click()
#
# drp = driver.find_element(By.ID,"month")
# S = Select(drp)
#
# # Select By Index
# S.select_by_index(2)
#
# # Select By Value
# S.select_by_value("4")
#
# # Select By Visible Text
# S.select_by_visible_text("Nov")
#
# # Is Multiple
# # print(S.is_multiple)
#
# #-- Get Options(It is used to get all the elements from the web element)
# # Ex for getting one value using slice operator
# options = S.options # List <Web Element>
# we = options[0] # Web Element
# print(we.text)
#
# # Ex for getting all values using for loop
# for i in range(0,12,1):
#     options = S.options  # List <Web Element>
#     we = options[i]
#     print(we.text)
#
# time.sleep(4)



# # Browser Launch
driver = webdriver.Chrome()

# Get
driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
driver.implicitly_wait(10)
driver.maximize_window()

drp = driver.find_element(By.NAME, "multipleselect[]")
s=Select(drp)

# # Select By Index
# s.select_by_index(0)
#
# # Select By Value
# s.select_by_value("msmanual")
#
# # Select By Visible Text
# s.select_by_visible_text("Agile Methodology")
# time.sleep(4)

# Get All Options
# print("---ALL OPTIONS---")
# ## Method 1
# options = s.options
# for i in range(0,4,1):
#     we = options[i]
#     print(we.text)

## Method 2
# for i in range(0,4,1):
#     options = s.options
#     we = options[i]
#     print(we.text)
#
#
# Get All Selected Options
# print("---ALL SELECTED OPTIONS---")               ## There is no method 2 because we have to declare the variable 1st and
# seloptions = s.all_selected_options         ##---then to give the len(var).
# for i in range(0,len(seloptions),1):
#     l = seloptions[i]
#     print(l.text)

# for i in range(0,3,1):
#     options = s.all_selected_options
#     l = options[i]
#     print(l.text)


# # Get First Selected Option
# print("---FIRST SELECTED OPTION---")
# wee = s.first_selected_option # We can select the options by any order and this code takes the first option in the
# print(wee.text)  #---dropdown box on the browser. It doesn't take the first option according to the order we selected
# time.sleep(2)

# Deselect ( Deselects only if options are selected)
# s.deselect_by_index(0) # By index
# s.deselect_by_value("msmanual") # By Value
# s.deselect_by_visible_text("Agile Methodology") # By Visible Text
# s.deselect_all() # Deselects all option
# time.sleep(5)

# # Select All Methods
# # Select All by Index
# for i in range(0,4,1):
#     s.select_by_index(i)

# Select All by Value
# options = s.options
# for i in range(0,4,1):
#     we = options[i]
#     x=we.get_attribute("value")
#     s.select_by_value(x)
#
# # Select All by Text
# options = s.options
# for i in range(0,4,1):
#     we = options[i]
#     x=we.get_attribute("innerText")
#     s.select_by_visible_text(x)






























