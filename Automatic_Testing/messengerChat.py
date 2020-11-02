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
import emailLogin as emailFile #archivo que contiene login
import os

class messengerChatting(unittest.TestCase):
    #Metodo de login
    def setUp(self):
        emailFile.loginFromEmailClass().test_emailLog() #del archivo, llamar clase, llamar metodo
        #global driver
    def test_messChat(self):
        print("HOLAAAA")
            
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
