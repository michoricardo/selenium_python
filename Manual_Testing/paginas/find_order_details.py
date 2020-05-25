import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class findOrder:
    def __init__(self,driver):
        
        self.driver=driver
        #ordenTecleado = ""
    def encontrarOrden(self):
        self.driver.get("https://gobstore-qa.firebaseapp.com/admin/orders/all")
        time.sleep(2)
        selectorOperativos = self.driver.find_element_by_id("inputGroupOpSelectorQuery")
        if selectorOperativos is not None:
            print("Se encontró el selector de operativos")
            selectorOpcion = self.driver.find_element_by_xpath('//*[@id="inputGroupOpSelectorQuery"]/option[1]')
            print("Se encontró la opción 'Todos'")
            selectorOpcion.click()
            print("Seleccionando Todos")
        print("Las fechas de la búsqueda son por default")
        time.sleep(2)
        selectorFechaQuery = self.driver.find_element_by_id("typeOfSearchSelect")
        if selectorFechaQuery is not None:
            print("Se encontró el selector de búsqueda de fecha")
            selectorOpcionCreacion = self.driver.find_element_by_xpath('//*[@id="typeOfSearchSelect"]/option[2]')
            print("Seleccionando buscar por fecha de creación")
            selectorOpcionCreacion.click()
            time.sleep(2)
        btn_query_search = self.driver.find_element_by_id("searchOrdersBtn")
        if btn_query_search is not None:
            print("Botón buscar encontrado")
            btn_query_search.click()
            print("Pulsando...")
            time.sleep(6)
        folioOrden=input("Favor de indicar el folio de la orden")
        print("El folio de la orden que buscas es" ,folioOrden)
        searcher = self.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div[1]/div[1]/div[3]/div/input')
        searcher.send_keys(folioOrden)
        time.sleep(1)
        print("Haciendo click en enter...")
        searcher.send_keys(Keys.ENTER)
        time.sleep(6)
        detailsOrderBtn = self.driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[28]/button')
        if detailsOrderBtn is not None:
            print("Botón para ver detalles encontrado")
            detailsOrderBtn.click()
    def tearDown(self):
        driver.quit()
  

if __name__ == "__main__":
   unittest.main()
