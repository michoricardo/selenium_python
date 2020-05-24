import unittest
from unittest import TestLoader,TestSuite,TextTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import prueba_html_testrunner
from prueba_html_testrunner import Espera

if __name__ == "__main__":
   #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/ricar/Documents/GrillOnBox/PythonScripts'))
   loader = TestLoader()
   suite = TestSuite((
       loader.loadTestsFromTestCase(Espera),
       loader.loadTestsFromTestCase(Espera)))
       
   #runner = TextTestRunner(verbosity=2)
   runner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/ricar/Documents/GrillOnBox/PythonScripts')
   runner.run(suite)
