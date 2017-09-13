#!/usr/bin/env python
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def take_screenshot(driver, name, save_location):
  # Make sure the path exists.
  path = os.path.abspath(save_location)
  if not os.path.exists(path):
    os.makedirs(path)
  full_path = '%s/%s' % (path, name)
  driver.get_screenshot_as_file(full_path)
  return full_path

chrome_options = Options()
chrome_options.add_argument("--headless --disable-gpu")
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),chrome_options=chrome_options)
driver.get("https://www.cristinaaielli.com/collections")
last_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(1224,last_height)
driver.save_screenshot('screen.png')
screenshot = take_screenshot(driver, driver.title+'.png', '/Users/zyang/Documents/ddweb')
print last_height
print screenshot