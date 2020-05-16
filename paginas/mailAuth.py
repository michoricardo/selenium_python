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
import msvcrt

class correoauth:
    def __init__(self,driver):
        
        self.driver=driver
    def inicioConCorreo(self):
        while True:
            try:
                print("Holaaaaaaaaaaaaaaaa")
                tiempoinicial = time.time()
                print("La prueba inicia en: ", time.asctime())
                esperaBoton = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html/body/header/div/div/section/button[2]")))
                print("Haciendo click en iniciar sesión GOBSTORE")
                esperaBoton.click()
                self.driver.implicitly_wait(3)
                #Mail AUTH
                mailAuth = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="emailLoginForm"]')))
                if mailAuth is not None:
                    print("Campo para autenticación por mail encontrado,escribiendo email")
                    mailAuth.send_keys("micho@gobstore.mx")
                    mailpwd = self.driver.find_element_by_xpath('//*[@id="pwdLoginForm"]')
                    if mailpwd is not None:
                        print("Se encontró el campo para password, enviando contraseña...")
                        mailpwd.send_keys("C0business.")
                    boton_ingresar = self.driver.find_element_by_xpath('//*[@id="btnLoginForm"]')
                    if boton_ingresar is not None:
                        print("Se encontró el botón ingresar, haciendo click")
                        boton_ingresar.click()
                        print("Inicio de sesión exitoso")
                        time.sleep(4)
            except KeyboardInterrupt:
                print("Salemossss")
                break
            except (ElementClickInterceptedException) as e:
                raise ValueError("No se pudo hacer click en un elemento") from e
                #print("Ocurrio un errors", e)

            except:
                print("Ocurrió otro errorrrrr")
                #raise
            else:
                print (u"\u001b[48;5;"+ "Nada detuvo el script")
                final = time.time()
                print("La prueba tomó", final-tiempoinicial, "segundos")
    def tearDown(self):
        driver.quit()
  

if __name__ == "__main__":
   unittest.main()
