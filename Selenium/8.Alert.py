# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Browser Launch
# driver = webdriver.Chrome()
#
# # Get
# driver.get("https://demo.automationtesting.in/Alerts.html")
# driver.implicitly_wait(6)
# driver.maximize_window()
#
# # Simple Alert
# alt = driver.find_element(By.XPATH, "//button[@class='btn btn-danger']")
# alt.click()
# time.sleep(4)
# a = driver.switch_to.alert
# print(a.text)
# a.accept()
# time.sleep(3)
#
#
# # Confirm Alert
# d = driver.find_element(By.XPATH, "//a[text()='Alert with OK & Cancel ']")
# d.click()
#
# dl = driver.find_element(By.XPATH, "//button[text()='click the button to display a confirm box ']")
# dl.click()
# time.sleep(4)
#
# x = driver.switch_to.alert
# print(x.text)
# x.dismiss()
# time.sleep(3)
#
#
# # Prompt Alert
# ld = driver.find_element(By.XPATH, "//a[text()='Alert with Textbox ']")
# ld.click()
#
# lds = driver.find_element(By.XPATH, "//button[text()='click the button to demonstrate the prompt box ']")
# lds.click()
#
# y = driver.switch_to.alert
# y.send_keys("Yes")
# time.sleep(6)
# print(y.text)
# y.accept()
# time.sleep(6)













































