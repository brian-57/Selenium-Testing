from selenium import webdriver
from selenium.webdriver.common.by import ByType

browser = webdriver.Firefox()
browser.get("https://tezzasolutions.com/software-testing/")
browser.maximize_window()
title = browser.title
print(title)
assert "Software Testing | Tezza Solutions" in title