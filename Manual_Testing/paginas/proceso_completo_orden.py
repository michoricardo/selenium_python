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

class ProcessOrder:
    def __init__(self,driver):
        
        self.driver=driver
    def OrdenDeProceso(self):
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
        #Empieza proceso de cambios de estado
        boton_status = self.driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[7]/span/i')
        if boton_status is not None:
            print("Botón para cambiar de status encontrado")
            boton_status.click()
            time.sleep(3)
        try:
            boton_nueva = self.driver.find_element_by_xpath('//*[@id="placedOrderOptn"]')
            if boton_nueva is not None:
                print("Botón para confirmar (Campanita) orden encontrado")
                boton_nueva.click()
                time.sleep(3)
        except ElementClickInterceptedException as exception:
            print("La orden va un paso más adelante que ser nueva")
            time.sleep(2)
        #Cerrar modal con "CONFIRMAR"
        try:
            boton_confirma = self.driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
            if boton_confirma is not None:
                print("Botón confirmar (para cerrar) encontrado")
                boton_confirma.click()
                time.sleep(3)
        except ElementClickInterceptedException as exception:
            print("Probablemente ya está enviado")
        #Se abre modal de nuevo
        boton_status = self.driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[7]/span/i')
        if boton_status is not None:
            print("Botón para cambiar de status encontrado")
            boton_status.click()
            time.sleep(3)
        #Se intenta hace click en la palomita 
        try:
            boton_confirmarrr = self.driver.find_element_by_xpath('//*[@id="confirmedOrderOptn"]')
            if boton_confirmarrr is not None:
                print("Botón de estado 'Confirmar (Palomita)', encontrado")
                boton_confirmarrr.click()
                time.sleep(3)
        except ElementClickInterceptedException as exception:
            print("La orden va un paso más adelante que la confirmación de orden")
            time.sleep(2)
        #Cerrar modal con "Confirmar"
        boton_confirma = self.driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
        if boton_confirma is not None:
            print("Botón confirmar (para cerrar) encontrado")
            boton_confirma.click()
            time.sleep(2)
        #Se abre modal de nuevo
        boton_status = self.driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[7]/span/i')
        if boton_status is not None:
            print("Botón para cambiar de status encontrado")
            boton_status.click()
            time.sleep(3)
        #Se intenta hacer click en el carrito (programar envío)
        try:  
            boton_programada = self.driver.find_element_by_xpath('//*[@id="scheduledToShipOrderOptn"]')
            if boton_programada is not None:
                print("Se encontró el botón para programar el envío de la orden")
                boton_programada.click()
                time.sleep(2)
            campoGuia = self.driver.find_element_by_id("shippingGuide")
            if campoGuia is not None:
                print("Se encontró el campo para la guía de envío")
            campoMensajero=self.driver.find_element_by_xpath('//*[@id="shippingCarrier"]')
            if campoMensajero is not None:
                print("Se encontró el campo para la mensajería")
            campoLink = self.driver.find_element_by_xpath('//*[@id="shippingLink"]')
            if campoLink is not None:
                print("Se encontró el campo para el link de seguimiento")
            campoConductor = self.driver.find_element_by_xpath('//*[@id="shippingDriver"]')
            if campoConductor is not None:
                print("Se encontró el campo para el nombre del Conductor")
            campo_ruta = self.driver.find_element_by_xpath('//*[@id="shippingRoute"]')
            if campo_ruta is not None:
                print("Se encontró el campo para la ruta del paquete")
            try:
                campoGuia.send_keys("GM99999999999")
                campoMensajero.send_keys("DHL")
                campoLink.send_keys("https://www.unam.mx/")
                #Cerrar modal con "Confirmar"
                boton_confirma = self.driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
                if boton_confirma is not None:
                    print("Botón confirmar (para cerrar) encontrado")
                    boton_confirma.click()
                    time.sleep(2)
            except ElementNotInteractableException as exception:
                print("No se encontró, campo de guía, entonces es local!")
                campoConductor.send_keys("Juanito Pérez")
                campo_ruta.send_keys("La Huasteca")
                #Cerrar modal con "Confirmar"
                boton_confirma = self.driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
                if boton_confirma is not None:
                    print("Botón confirmar (para cerrar) encontrado")
                    boton_confirma.click()
                    time.sleep(2)
        except ElementClickInterceptedException as exception:
            print("La orden va un paso más adelante que la programación de envío")
        #Se abre modal de nuevo
        boton_status = self.driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[7]/span/i')
        if boton_status is not None:
            print("Botón para cambiar de status encontrado")
            boton_status.click()
            time.sleep(3)
        #Se intenta hace click en construyendo 
        try:
            boton_construyendo = self.driver.find_element_by_xpath('//*[@id="inConstructionOrderOptn"]')
            if boton_construyendo is not None:
                print("Botón de estado construyendo (paquetito) encontrado")
                boton_construyendo.click()
                time.sleep(3)
        except ElementClickInterceptedException as exception:
            print("La orden va un paso más adelante que construyendo Orden")
            time.sleep(3)
        #Cerrar modal con "Confirmar"
        boton_confirma = self.driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
        if boton_confirma is not None:
            print("Botón confirmar (para cerrar) encontrado")
            boton_confirma.click()
            time.sleep(3)
        #Se abre modal de nuevo
        boton_status = self.driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[7]/span/i')
        if boton_status is not None:
            print("Botón para cambiar de status encontrado")
            boton_status.click()
            time.sleep(3)
        #Se intenta hace click en Entregado
        try:
            try:
                boton_entregado = self.driver.find_element_by_xpath('//*[@id="deliveredOrderOptn"]')
                if boton_entregado is not None:
                    print("Botón de estado entregado (monito) encontrado")
                    time.sleep(2)
                    boton_entregado.click()
                    time.sleep(3)
            except ElementClickInterceptedException as exception:
                print("La orden ya se entregó o está cancelada")
                time.sleep(2)
            #Cerrar modal con "Confirmar"
            boton_confirma = self.driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
            if boton_confirma is not None:
                print("Botón confirmar (para cerrar) encontrado")
                boton_confirma.click()
                time.sleep(2)
        except ElementNotInteractableException as expepction:
            print("No se puede ver")
    def tearDown(self):
        driver.quit()
  

if __name__ == "__main__":
   unittest.main()
