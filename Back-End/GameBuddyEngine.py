from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

PATH = ".../chromedriver" # Path to chrome driver
DOWNLOADS = ".../Equinox" # Path to downloads folder
hyperlink = "https://steamdb.info/app/1067770/"

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled") # Enable Javascript
prefs = {"download.default_directory" : DOWNLOADS}
options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(options = options, executable_path = PATH)
driver.get(hyperlink)
driver.execute_script("window.scrollTo(100,document.body.scrollHeight/2)")
time.sleep(8)

try:
    download_button = driver.find_element_by_class_name("highcharts-exporting-group")
    download_button.click()
    #print(download_button)
    time.sleep(2)

    csv_button = driver.find_element_by_class_name("highcharts-menu-item")
    csv_button.click()
    #print(csv_button)
    time.sleep(2)
except:
    driver.close()

driver.close() # close the webpage

#download_list = os.listdir("/Users/joseph-vaiz-gomez/Documents/Equinox")
#csv_filename = [k for k in download_list if '.csv' in k]
