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
from selenium.webdriver.common.keys import Keys

class googleOauth:
    def __init__(self,driver):
        
        self.driver=driver
    def inicioConGoogle(self):
        print("Iniciar sesion con Google")
        print("Para iniciar sesión con Google, debes permitir aplicaciones de terceros y  que tu navegador permita automatizacion")
        input("Presiona ENTER si ya estás desloggeado de email")
        self.driver.get("https://gobstore-qa.firebaseapp.com/")
        time.sleep(3)
        gobstoreGoogleAuth=self.driver.find_element_by_xpath("//*[@id='loginModalContent']/div/div[1]/a/i")
        print("abriendo la página principal")
        esperaBoton = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable((By.XPATH,"/html/body/header/div/div/section/button[2]")))
        print("Haciendo click en iniciar sesión GOBSTORE")
        esperaBoton.click()
        self.driver.implicitly_wait(3)
        self.driver.implicitly_wait(50)
        if gobstoreGoogleAuth is not None:
            print("Haciendo click en iniciar sesión con Google")
            gobstoreGoogleAuth.click()
            self.driver.implicitly_wait(10)
            handles=self.driver.window_handles
            for handle in handles:
                self.driver.switch_to.window(handle)
                print("Cambio de ventana hacia Google auth")
                print(self.driver.title)
        campoDeEmail=self.driver.find_element_by_name("identifier").send_keys("axolotlcode@gmail.com")
        print("Campo de email encontrado, escribiendo datos")
        botonsiguiente=self.driver.find_element_by_id("identifierNext").click()
        if botonsiguiente is not None:
            print("Haciendo click en botón para continuar")
            botonsiguiente.click()
            time.sleep(5)
        try:
            campoDePassword=self.driver.find_element_by_name("password")
            if campoDePassword is not None:
                print("Campo para password encontrado, escribiendo password")
                campoDePassword.send_keys("examplepassword")
            time.sleep(3)
            botonsiguientepwd=self.driver.find_element_by_id("passwordNext")
            if botonsiguientepwd is not None:
                print("Haciendo click en siguiente")
                botonsiguientepwd.click()
                new_window = self.driver.window_handles[0]
                self.driver.switch_to.window(new_window)
                print("Inicio de sesión exitoso")
        except NoSuchElementException as exception:
                print("El navegador o la cuenta no permiten automatizaciones")
                print("Inicio de sesión con Google no exitoso")
    def tearDown(self):
        driver.quit()
  

if __name__ == "__main__":
   unittest.main()
