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

class reportGenerator:
    def __init__(self,driver):
        self.driver=driver
    def generandoReporte(self):
        
        exitosas=0
        interrupcion = 0
        clickInterrumpido = 0
        timeout = 0
        noElemento = 0
        selenium_platform = 0
        with open('mailAuth.txt') as fobj:
            
            lectura = fobj.readlines()
            for line in lectura:
                if "exitosa!!" in line:
                    exitosas = exitosas+1
                elif 'teclado' in line:
                    interrupcion = interrupcion+1
                elif 'clickeable' in line:
                    clickInterrumpido = clickInterrumpido+1
                elif 'agotado' in line:
                    timeout = timeout+1
                elif 'encontró' in line:
                    noElemento = noElemento+1
                elif 'plataforma' in line:
                    selenium_platform =selenium_platform+1
            print("Las exitosas fueron: ", exitosas)
            print("Se interrumpieron :", interrupcion)
            print("No se pudo hacer click" ,clickInterrumpido)
            print("Se agotó el tiempo de espera: ",timeout)
            print("No se encontró al elemento: ",noElemento)
            print("Otros errores: ", selenium_platform)
    def tearDown(self):
        driver.quit()
  

if __name__ == "__main__":
   unittest.main()
