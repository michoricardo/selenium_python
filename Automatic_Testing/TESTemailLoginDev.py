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

class loginFromEmailClassDev(unittest.TestCase):
    def  test_emailLog(self,driver):
        driver.get("https://gobstoredev.firebaseapp.com/")
        #Cerrar modal
        try:
            esperaModalMolesto = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PopupSignupForm_0"]/div[2]/div[1]'))).click()
            print("Se hizo click en el modal molesto del newsletter")
            print("<br>")
        except TimeoutException as exception:
            print("No se encontraron modales molestos de newsletter")
            print("<br>")
        except ElementNotInteractableException as exception:
            print("No se encontraron modales molestos de newsletter")
            print("<br>")
        #Termina manejo de modal
        esperaBoton = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html/body/header/div/div/section/button[2]")))
        print("Haciendo click en iniciar sesion GOBSTORE")
        print("<br>")
        esperaBoton.click()
        driver.implicitly_wait(3)
        #Mail AUTH
        mailAuth = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="emailLoginForm"]')))
        if mailAuth is not None:
            print("Campo para autenticacion por mail encontrado,escribiendo email")
            print("<br>")
            mailAuth.send_keys("micho@gobstore.mx")
            mailpwd = driver.find_element_by_xpath('//*[@id="pwdLoginForm"]')
        if mailpwd is not None:
            print("Se encontro el campo para password, enviando password...")
            print("<br>")
            mailpwd.send_keys("C0business.")
        boton_ingresar = driver.find_element_by_xpath('//*[@id="btnLoginForm"]')
        if boton_ingresar is not None:
            print("Se encontro el boton ingresar, haciendo click")
            print("<br>")
            boton_ingresar.click()
            print("Inicio de sesion exitoso")
            print("<br>")
            time.sleep(4)            
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
