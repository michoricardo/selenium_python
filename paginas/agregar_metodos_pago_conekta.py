import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class metodosDePagoConekta:
    def __init__(self,driver):
        
        self.driver=driver

    def altaTarjeta(self,nombre_tarjeta,numero_tarjeta,CVC_tarjeta,expiryMonth,expiryYear):
        
        self.driver.get("https://gobstore-qa.firebaseapp.com/micuenta/opcionesdepago")
        btn_agregar = self.driver.find_element_by_id('addPaymentSourceBtn')
        if btn_agregar is not None:
            print("Clickeando botón para agregar tarjeta")
            btn_agregar.click()
            self.driver.implicitly_wait(10)
            time.sleep(4)
        #blank_nombre_tarjeta = self.driver.find_element_by_xpath('//*[@id="newPaymentForm"]/div[2]/div/div/input')
        blank_nombre_tarjeta = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="newPaymentForm"]/div[2]/div/div/input')))
        if blank_nombre_tarjeta is not None:
            print("Campo para nombre de tarjeta encontrado")
            time.sleep(2)
            blank_nombre_tarjeta.send_keys(nombre_tarjeta)
            print("Llenando campos de nombre de Tarjeta")   
        blank_numero_tarjeta = self.driver.find_element_by_xpath("//*[@id='newPaymentForm']/div[3]/div[1]/div/input")
        print("Campo para numero de tarjeta encontrado")
        blank_numero_tarjeta.send_keys(numero_tarjeta)
        print("Llenando campos de numero de tarjeta")
        blank_CVC_tarjeta = self.driver.find_element_by_xpath("//*[@id='newPaymentForm']/div[3]/div[2]/div/input")
        print("Campo para CVC encontrado")
        blank_CVC_tarjeta.send_keys(CVC_tarjeta)
        print("Llenando campos de tarjeta")
        #self.driver.implicitly_wait(10)
        blank_expiryMonth = self.driver.find_element_by_xpath('//*[@id="newPaymentForm"]/div[4]/div/div/div/div[1]/input')
        print("Campo para mes de expiracion encontrado")
        blank_expiryMonth.send_keys(expiryMonth)
        blank_expiryYear= self.driver.find_element_by_xpath('//*[@id="newPaymentForm"]/div[4]/div/div/div/div[2]/input')
        print("Campo para año de expiracion encontrado")
        blank_expiryYear.send_keys(expiryYear)
        botonAgregarTarjeta = self.driver.find_element_by_id("savePaymentSourceBtn")
        print("Boton Agrear Tarjeta encontrado")
        botonAgregarTarjeta.click()
        time.sleep(3)
            

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
