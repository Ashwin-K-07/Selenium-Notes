import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
#
# driver.get("https://www.facebook.com/")
#
# # By using XPATH Text
# crtpage = driver.find_element(By.XPATH, "//a[text()='Create a Page']")
# t=crtpage.text
# print(t)
#
# # By using XPATH contains for text
# face = driver.find_element(By.XPATH, "//h2[contains(text(),'Facebook')]")
# print(face.text)
#
# # By using XPATH contains attribute(for user name)
# txtuser = driver.find_element(By.XPATH, "//input[contains(@id,'em')]")
# txtuser.send_keys("Ashwin")
#
# # By using get_attribute("value") [for user name]
# x = txtuser.get_attribute("value")
# print(x)
#
# # By using XPATH contains attribute(for Password)
# txtpass = driver.find_element(By.XPATH, "//input[contains(@id,'pa')]")
# txtpass.send_keys("1234567")
#
# # By using get_attribute("value") [for Password]
# y = txtpass.get_attribute("value")
# print(y)
#
# # By using GET ATTRIBUTE("INNER TEXT")
# g = face.get_attribute("innerText")
# print(g)
# time.sleep(20)


## Task(Greens Technlogies) Method 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.greenstechnologys.com/python-training.html")
#
# insttname = driver.find_element(By.XPATH, "(//h6[text() = 'Greens Technology '])[3]")
# a=insttname.text
# print(a)
#
# area = driver.find_element(By.XPATH, "//span[text() = 'No.1, Apparao Colony,']")
# print(area.text)
#
# town = driver.find_element(By.XPATH, "//span[text() = ' Tambaram,']")
# print(town.text)
#
# subtown = driver.find_element(By.XPATH, "//span[text() = ' Sanatorium, ']")
# print(subtown.text)
#
# lndmrk = driver.find_element(By.XPATH, "//span[text() = 'Near HP Petrol Bunk, ']")
# print(lndmrk.text)

# city = driver.find_element(By.XPATH, "//span[text() = 'Chennai - 600047']") ## shows error
# city = driver.find_element(By.XPATH, "(//span[contains(text(), 'Chennai - 60004')])[1]")
# print(city.text)
#
#
# phno = driver.find_element(By.XPATH, "(//a[text()='+91 8939975577'])[7]")
# print(phno.text)
#
# mail = driver.find_element(By.XPATH, "(//a[text()='contact@greenstechnologys.com'])[11]")
# print(mail.text)


# Task Method 2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.greenstechnologys.com/python-training.html")
#
# instituteinfo = driver.find_element(By.XPATH, "(//div[@class = 'col-md-3 short-desc-with-logo widget widget_text'])[3]")
# print(instituteinfo.text)

































