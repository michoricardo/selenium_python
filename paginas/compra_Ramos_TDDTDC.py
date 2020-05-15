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


class shoppingRamosTDDTDC:
    def __init__(self,driver):
        
        self.driver=driver

    def compraChicharron(self):
        
        self.driver.get("https://gobstore-qa.firebaseapp.com/carnesramos")
        codigoPostal=input("¿MTY O CDMX?:")
        if codigoPostal == "MTY" or "mty":
            codigoPostal = "64849"
            print("Tu cp es:", codigoPostal)
        elif codigoPostal == "CDMX" or "cdmx":
            codigoPostal = "04510"
            print("Tu cp es:", codigoPostal)
        try:
            modal = WebDriverWait(self.driver,40).until(EC.presence_of_element_located((By.XPATH,'//*[@id="postalCodeModal"]/div/div/div[2]')))
            if modal is not None:
                blank_cp = self.driver.find_element_by_id("inputPostalCode")
                if blank_cp is not None:
                    print("Agregando CP ")
                    blank_cp.send_keys(codigoPostal)
                    vertienda = self.driver.find_element_by_id("btnGetOpByPostalCode")
                    vertienda.click()
                    time.sleep(3)
        except ElementNotInteractableException as exception:
            print("No teías que poner CP porque ya habías comprado :)")
        time.sleep(3)
        btn_chicharron = self.driver.find_element_by_xpath('//*[@id="customSectionsWrapper"]/div/div[2]/div[2]/div[1]')
        if btn_chicharron is not None:
            print("Clickeando imagen de chicharron para agregar a cart")
            btn_chicharron.click()
            self.driver.implicitly_wait(10)
            time.sleep(2)    
        btn_addToCart = self.driver.find_element_by_id("btnAddItemToCard")
        if btn_addToCart is not None:
            print("Haciendo click en Agregar al carrito/ QTY default (1)")
            btn_addToCart.click()
            self.driver.implicitly_wait(10)
            time.sleep(2)
        btn_checkCart = self.driver.find_element_by_xpath('/html/body/header/div/div/section/button[3]/span')
        if btn_checkCart is not None:
            print("Haciendo click para consultar carrito")
            btn_checkCart.click()
            self.driver.implicitly_wait(10)
            time.sleep(8)
        btn_proceedCheckout = self.driver.find_element_by_id("proceedToCheckout")
        if btn_proceedCheckout is not None:
            print("Haciendo click para proceder a checkout")
            btn_proceedCheckout.click()
            self.driver.implicitly_wait(10)
            time.sleep(8) 
        btn_TDD_TDC = self.driver.find_element_by_xpath('//*[@id="paymentTypeSelector"]/li[1]/a')
        if btn_TDD_TDC is not None:
            print("Eligiendo metodo de pago")
            btn_TDD_TDC.click()
            self.driver.implicitly_wait(10)
            time.sleep(8)
        datepicker = self.driver.find_element_by_xpath('//*[@id="inputDate"]')
        if datepicker is not None:
            print("Date picker encontrado")
            time.sleep(2)
            actions= ActionChains(self.driver)
            actions.move_to_element(datepicker).click().perform()
            print("Eligiendo fecha default")
        falto_algo=self.driver.find_element_by_xpath('//*[@id="extraComments"]').send_keys("No faltó nada")
        time.sleep(1)
        ordenar_btn=self.driver.find_element_by_xpath('//*[@id="handlePlaceOrder"]')
        if ordenar_btn is not None:
            print("Ordenando ...")
            ordenar_btn.click()
            time.sleep(2)


    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
