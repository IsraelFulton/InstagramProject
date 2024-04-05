#!/usr/bin/env python3

from time import sleep
from selenium import webdriver

browser = webdriver.Safari()
browser.get("https://instagram.com/")

sleep(5)

browser.close()