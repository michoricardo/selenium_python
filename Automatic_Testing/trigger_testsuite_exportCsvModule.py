#Imports de testing/selenium
import unittest
from unittest import TestLoader,TestSuite,TextTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import HtmlTestRunner
from exportCsvModule import csvModule
from selenium.webdriver.firefox.options import Options
#Imports comunes python
import sys
import time
#Para desidentar: CTRL + SHIFT + BRACKET IZQ

if __name__ == "__main__":

   test_classes_to_run = []
   veces=input("Cuantas : ? ")
   vecesnum= int(veces)
   for i in range(0,vecesnum):
      test_classes_to_run.append(csvModule)
   print(test_classes_to_run)
   print("debería de verse : ", vecesnum, "veces")
   
#Segunda parte del tutorial en stackoverflow
   loader = TestLoader()
   #global suites_list
   suites_list = []
   for test_class in test_classes_to_run:
      suite = loader.loadTestsFromTestCase(csvModule)
      suites_list.append(suite)
   big_suite = unittest.TestSuite(suites_list)
   runner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/DELL/Documents/Scripts de python/selenium_python\Automatic_Testing')
   #runner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/ricar/Documents/GrillOnBox/PythonScripts')
   runner.run(big_suite)

