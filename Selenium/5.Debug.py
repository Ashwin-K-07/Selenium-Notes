## DEBUG
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Browser launch
driver = webdriver.Chrome()

# Get
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5) #Dynamic Wait

crtbtn = driver.find_element(By.XPATH, "(// a[@role = 'button'])[2]")
crtbtn.click()

# Static Wait
time.sleep(5) # To avoid errors

firstname = driver.find_element(By.NAME, "firstname")
firstname.send_keys("Ashwin")

lastname = driver.find_element(By.NAME, "lastname")
lastname.send_keys("K")

phone = driver.find_element(By.NAME, "reg_email__")
phone.send_keys("976543210")


def add():
    a=10
    b=20
    c=a+b
    print(c)

def sub():
    a=10
    b=20
    c=a-b
    print(c)

add()
sub()
