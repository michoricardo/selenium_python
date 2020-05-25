import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class domicilioMTY:
    def __init__(self,driver):
        
        self.driver=driver

    def altamty(self,nombreYapellido,celMTY,CPMTY,calleMTY,NumExtMTY,NumIntMTY,inBetweenMTY,indicacionesMTY):
        
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
        blank_celularMTY = self.driver.find_element_by_xpath("//*[@id='inputReceiverPhone']")
        print("Campo para celular encontrado")
        blank_celularMTY.send_keys(celMTY)
        print("Llenando campos de celular")
        blank_cpMTY = self.driver.find_element_by_xpath("//*[@id='inputPostalCode']")
        print("Campo para codigo postal encontrado")
        blank_cpMTY.send_keys(CPMTY)
        print("Llenando campos de codigo postal")
        self.driver.implicitly_wait(10)
        select = self.driver.find_element_by_id('inputSuburb')
        if select is not None:
            option = select.find_element_by_xpath("//*[@id='inputSuburb']/option[3]")
            option.click()
            print("Se encontró el selector")
            print("Seleccionando valor")
        blank_calleMTY = self.driver.find_element_by_id("inputStreet1")
        print("Campo para calle 1 encontrado")
        blank_calleMTY.send_keys(calleMTY)
        blank_NumExtMTY= self.driver.find_element_by_id("inputExtNumber")
        print("Campo para numero exterior encontrado")
        blank_NumExtMTY.send_keys(NumExtMTY)
        blank_NumIntMTY = self.driver.find_element_by_id("inputIntNumber")
        print("Campo para numero interior")
        blank_NumIntMTY.send_keys(NumIntMTY)
        blank_InBetweenMTY = self.driver.find_element_by_id("inputBetweenStreets")
        print("Campo para entre calles encontrado")
        blank_InBetweenMTY.send_keys(inBetweenMTY)
        blank_indicaciones = self.driver.find_element_by_id("inputAditionalInfo")
        print("Campo para indicaciones encontrado")
        blank_indicaciones.send_keys(indicacionesMTY)
        botonGuardarMTY = self.driver.find_element_by_id("saveAddressBtn")
        print("Boton guardar encontrado")
        botonGuardarMTY.click()
        #Dirección por default
        #time.sleep(4)
        #defaultShipTo=self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/button[2]').click()

        print("Setteando como default")
            

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
