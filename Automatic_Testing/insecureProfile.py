import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from datetime import date
import os

class insecureClass(unittest.TestCase):
    def  test_insecureFirefox(self):
        #Perfil de micho testing
        #global driver
        fp = webdriver.FirefoxProfile('/Users/DELL/Documents/Scripts de python/selenium_python/Automatic_Testing/PerfilFirefox')
        driver = webdriver.Firefox(firefox_profile=fp,executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")
        driver.get("https://gobstore-qa.firebaseapp.com/")
        return driver
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
