#!/usr/bin/env python3

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a new Safari window, wait for it to load, then go to Instagram's website.
browser = webdriver.Safari()
browser.implicitly_wait(5)
browser.get("https://instagram.com/")

# Wait between 2-12 seconds on Instagram's landing page before continuing.
import random
randomTime = random.random()*10+2
print("Wait " + str(randomTime) + " seconds.")
sleep(randomTime)

# Input the username and password of the account to be accessed. Quick pause between key strokes to appear natural.
elements = browser.find_elements(By.CLASS_NAME, "_aa48")
username = "username"
password = "password"

if len(elements) >= 2:
    username_input = elements[0]
    password_input = elements[1]
for x in username:
    username_input.send_keys(x)
    sleep(random.random()/4)
for x in password:
    password_input.send_keys(x)
    sleep(random.random()/4)

# Wait, then click the log in button.
sleep(random.random()/2)
login_button = browser.find_element(By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30']")
login_button.click()

sleep(15)

browser.close()