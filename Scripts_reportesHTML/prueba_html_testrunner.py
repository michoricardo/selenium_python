import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
#from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 



class Espera(unittest.TestCase):



    def setUp(self):
        global driver
        driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
        
        #driver.implicitly_wait(15)
    
        driver.get("http://goodstartbook.com/pruebas/")

    def test1(self):
        espera = WebDriverWait(driver, 10)
        boton = espera.until(EC.element_to_be_clickable((By.ID,"proceed")))
        if boton is not None:
            boton.click()
            print("Ecsitosa")
           
        time.sleep(3)
        
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/ricar/Documents/GrillOnBox/PythonScripts'))
