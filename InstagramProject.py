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
loginElements = browser.find_elements(By.CLASS_NAME, "_aa48")
username = "lpdfqbogndjrmztokl"
password = "passwordy"

if len(loginElements) >= 2:
    username_input = loginElements[0]
    password_input = loginElements[1]
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

# Wait, visit profile page, wait, visit following list
sleep(random.random()+5)
browser.get("https://www.instagram.com/lpdfqbogndjrmztokl/")
sleep(random.random()+3)
browser.get("https://www.instagram.com/lpdfqbogndjrmztokl/following/")

# Find followers and take names
sleep(5)
followers = set()
followerElementSet = set()
print("Set created")

# followerElements = browser.find_elements(By.CLASS_NAME, "x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3")
# followerElements = browser.find_element(By.XPATH, "//div[contains(@class, 'x1dm5mii') and contains(@class, 'x16mil14') and contains(@class, 'xiojian') and contains(@class, 'x1yutycm') and contains(@class, 'x1lliihq') and contains(@class, 'x193iq5w') and contains(@class, 'xh8yej3')]")
followerElements = browser.find_element(By.XPATH, "//a[contains(@class, 'x1i10hfl') and contains(@class, 'xjbqb8w') and contains(@class, 'x1ejq31n') and contains(@class, 'xd10rxx') and contains(@class, 'x1sy0etr') and contains(@class, 'x17r0tee') and contains(@class, 'x972fbf') and contains(@class, 'xcfux6l') and contains(@class, 'x1qhh985') and contains(@class, 'xm0m39n') and contains(@class, 'x9f619') and contains(@class, 'x1ypdohk') and contains(@class, 'xt0psk2') and contains(@class, 'xe8uvvx') and contains(@class, 'xdj266r') and contains(@class, 'x11i5rnm') and contains(@class, 'xat24cr') and contains(@class, 'x1mh8g0r') and contains(@class, 'xexx8yu') and contains(@class, 'x4uap5') and contains(@class, 'x18d9i69') and contains(@class, 'xkhd6sd') and contains(@class, 'x16tdsg8') and contains(@class, 'x1hl2dhg') and contains(@class, 'xggy1nq') and contains(@class, 'x1a2a7pz') and contains(@class, 'notranslate') and contains(@class, '_a6hd')]")
# /html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[1]/div/div/div/div[2]/div/div/div/div/div/a
# followerElements = browser.find_elements(By.XPATH, "/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[1]/div/div/div/div[2]/div/div/div/div")

print("Follower Element raw", followerElements)
followerElementSet.add(followerElements)

print("Follower element set", followerElementSet)
print("Found")
# print(len(followerElements))

for element in followerElementSet:
    print(element)
    href = element.get_attribute('href')
    if href:
        name = href.split("/")[3]
        followers.add(name)
        print(name)
    else:
        print("Not found")


# Take follower set and write in a txt file
with open('FollowerList.txt', "w") as file:
    for follower in followers:
       file.write(follower + "\n")

sleep(15)

browser.close()