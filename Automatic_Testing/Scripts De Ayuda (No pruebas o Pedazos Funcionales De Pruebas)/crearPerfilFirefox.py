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

class misMetodosPago(unittest.TestCase):
    def setUp(self):
        global driver
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_profile.set_preference("privacy.socialtracking.block_cookies", False)
        firefox_profile.set_preference("privacy.trackingprotection.socialtracking", False)
        firefox_profile.set_preference("security.fileuri.strict_origin_policy", False)
        privacy.trackingprotection.socialtracking.enabled
        privacy.socialtracking.block_cookies.enabled
        driver = webdriver.Firefox(firefox_profile=firefox_profile,executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")

     #Esta configuración es la que se creo para  cargar el perfil sin reglas de seguridad 
        #fp = webdriver.FirefoxProfile('/Users/DELL/Documents/Scripts de python/selenium_python/Automatic_Testing/PerfilFirefox')
        #driver = webdriver.Firefox(firefox_profile=fp,executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")
        #driver.get("https://gobstore-qa.firebaseapp.com/")
            
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
