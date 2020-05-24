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
   test_classes_to_run = []
   veces=input("Cuantas : ? ")
   vecesnum= int(veces)
   for i in range(0,vecesnum):
      test_classes_to_run.append(Espera)
   print(test_classes_to_run)
   print("debería de verse : ", vecesnum, "veces")
   
#Segunda parte del tutorial en stackoverflow
   loader = TestLoader()
   #global suites_list
   suites_list = []
   for test_class in test_classes_to_run:
      suite = loader.loadTestsFromTestCase(Espera)
      suites_list.append(suite)
   big_suite = unittest.TestSuite(suites_list)
   runner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/ricar/Documents/GrillOnBox/PythonScripts')
   runner.run(big_suite)
