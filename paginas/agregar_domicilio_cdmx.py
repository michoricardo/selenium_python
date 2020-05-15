import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class domicilioCDMX:
    def __init__(self,driver):
        
        self.driver=driver

    def altaCDMX(self,nombreYapellido,celCDMX,CPCDMX,calleCDMX,NumExtCDMX,NumIntCDMX,inBetweenCDMX,indicacionesCDMX):
        
        self.driver.get("https://gobstore-qa.firebaseapp.com/micuenta/direcciones")
        btn_agregar = self.driver.find_element_by_xpath('//*[@id="addNewAddressBtn"]/i')
        if btn_agregar is not None:
            print("Clickeando botón para agregar direccion")
            btn_agregar.click()
            time.sleep(2)
        blank_nombre_apellido = self.driver.find_element_by_xpath('//*[@id="inputReceiverName"]')
        if blank_nombre_apellido is not None:
            print("Campo para nombre y apellido encontrado")
            blank_nombre_apellido.send_keys(nombreYapellido)
            print("Llenando campos de nombre y apelido")
        blank_celularCDMX = self.driver.find_element_by_xpath("//*[@id='inputReceiverPhone']")
        print("Campo para celular encontrado")
        blank_celularCDMX.send_keys(celCDMX)
        print("Llenando campos de celular")
        blank_cpCDMX = self.driver.find_element_by_xpath("//*[@id='inputPostalCode']")
        print("Campo para codigo postal encontrado")
        blank_cpCDMX.send_keys(CPCDMX)
        print("Llenando campos de codigo postal")
        self.driver.implicitly_wait(10)
        select = self.driver.find_element_by_id('inputSuburb')
        if select is not None:
            option = select.find_element_by_xpath("//*[@id='inputSuburb']/option[3]")
            option.click()
            print("Se encontró el selector")
            print("Seleccionando valor")
        blank_calleCDMX = self.driver.find_element_by_id("inputStreet1")
        print("Campo para calle 1 encontrado")
        blank_calleCDMX.send_keys(calleCDMX)
        blank_NumExtCDMX= self.driver.find_element_by_id("inputExtNumber")
        print("Campo para numero exterior encontrado")
        blank_NumExtCDMX.send_keys(NumExtCDMX)
        blank_NumIntCDMX = self.driver.find_element_by_id("inputIntNumber")
        print("Campo para numero interior encontrado")
        blank_NumIntCDMX.send_keys(NumIntCDMX)
        blank_indicaciones = self.driver.find_element_by_id("inputAditionalInfo")
        blank_InBetweenCDMX = self.driver.find_element_by_id("inputBetweenStreets")
        print("Campo para entre calles encontrado")
        blank_InBetweenCDMX.send_keys(inBetweenCDMX)
        blank_indicaciones = self.driver.find_element_by_id("inputAditionalInfo")
        print("Campo para indicaciones encontrado")
        blank_indicaciones.send_keys(indicacionesCDMX)
        botonGuardarCDMX = self.driver.find_element_by_id("saveAddressBtn")
        print("Boton guardar encontrado")
        botonGuardarCDMX.click()      
        #Dirección por default
        #time.sleep(4)
        #defaultShipTo=self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/button[2]').click()

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
