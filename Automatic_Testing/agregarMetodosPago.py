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
        driver = webdriver.Firefox(executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")
        #driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
        driver.get("https://gobstore-qa.firebaseapp.com/")
        #Cerrar modal
        try:
            esperaModalMolesto = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PopupSignupForm_0"]/div[2]/div[1]'))).click()
            print("Se hizo click en el modal molesto del newsletter")
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

    def test_altaTarjeta(self):
        nombre_tarjeta=["Visa Correcta","Mastercard Correcta","American Express Correcta","Tarjeta Declinada","Tarjeta Insuficientes","Tarjeta MSI Error"]
        numero_tarjeta=["4242424242424242","5555555555554444","378282246310005","4000000000000002","4000000000000127","4111111111111111"]
        CVC_tarjeta="200"
        expiryMonth="10"
        expiryYear="22"
        for i in range(0,5):
            driver.get("https://gobstore-qa.firebaseapp.com/micuenta/opcionesdepago")
        try:
            btn_agregar = driver.find_element_by_id('addPaymentSourceBtn')
            if btn_agregar is not None:
                print("Clickeando botón para agregar tarjeta")
                btn_agregar.click()
                time.sleep(2)
                driver.implicitly_wait(10)
                time.sleep(4)
            blank_nombre_tarjeta = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="newPaymentForm"]/div[2]/div/div/input')))
            if blank_nombre_tarjeta is not None:
                print("Campo para nombre de tarjeta encontrado")
                time.sleep(2)
                blank_nombre_tarjeta.send_keys(nombre_tarjeta[i])
                print("Llenando campos de nombre de Tarjeta")   
                blank_numero_tarjeta =driver.find_element_by_xpath("//*[@id='newPaymentForm']/div[3]/div[1]/div/input")
                print("Campo para numero de tarjeta encontrado")
                blank_numero_tarjeta.send_keys(numero_tarjeta[i])
                print("Llenando campos de numero de tarjeta")
                blank_CVC_tarjeta = driver.find_element_by_xpath("//*[@id='newPaymentForm']/div[3]/div[2]/div/input")
                print("Campo para CVC encontrado")
                blank_CVC_tarjeta.send_keys(CVC_tarjeta)
                print("Llenando campos de tarjeta")
                #self.driver.implicitly_wait(10)
                blank_expiryMonth = driver.find_element_by_xpath('//*[@id="newPaymentForm"]/div[4]/div/div/div/div[1]/input')
                print("Campo para mes de expiracion encontrado")
                blank_expiryMonth.send_keys(expiryMonth)
                blank_expiryYear= driver.find_element_by_xpath('//*[@id="newPaymentForm"]/div[4]/div/div/div/div[2]/input')
                print("Campo para año de expiracion encontrado")
                blank_expiryYear.send_keys(expiryYear)
                botonAgregarTarjeta = driver.find_element_by_id("savePaymentSourceBtn")
                print("Boton Agrear Tarjeta encontrado")
                botonAgregarTarjeta.click()
                time.sleep(3)
                time.sleep(4)
        except ElementNotInteractableException as exception:
            print("No se encontró el botón para agregar un método de pago nuevo")

            
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
