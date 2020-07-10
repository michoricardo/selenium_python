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
import os

class processOrder(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
        driver.get("https://gobstore-qa.firebaseapp.com/")
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
    def test_OrdenDeProceso(self):
        driver.get("https://gobstore-qa.firebaseapp.com/admin/orders/all")
        time.sleep(2)
        selectorOperativos = driver.find_element_by_id("inputGroupOpSelectorQuery")
        if selectorOperativos is not None:
            print("Se encontró el selector de operativos")
            selectorOpcion = driver.find_element_by_xpath('//*[@id="inputGroupOpSelectorQuery"]/option[1]')
            print("Se encontró la opción 'Todos'")
            selectorOpcion.click()
            print("Seleccionando Todos")
        print("Las fechas de la búsqueda son por default")
        time.sleep(2)
        selectorFechaQuery = driver.find_element_by_id("typeOfSearchSelect")
        if selectorFechaQuery is not None:
            print("Se encontró el selector de búsqueda de fecha")
            selectorOpcionCreacion = driver.find_element_by_xpath('//*[@id="typeOfSearchSelect"]/option[2]')
            print("Seleccionando buscar por fecha de creación")
            selectorOpcionCreacion.click()
            time.sleep(2)
        dropDownEstado = driver.find_element_by_id("dropdownMenuButton")
        if dropDownEstado is not None:
            print("dropdown encontrado")
            dropDownEstado.click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0,400)")
            selector_confirmed = driver.find_element_by_id("optionStatusConfirmed")
            if selector_confirmed is not None:
                selector_confirmed.click()
                print("Des seleccionando conirmadas")
            driver.find_element_by_id("optionStatusInConstruction").click
            print("Des seleccionando en construccion")
            driver.find_element_by_id("optionStatusBuilt").click
            print("Des seleccionando en construida")
            driver.find_element_by_id("optionStatusScheduledToShip").click
            print("Des seleccionando programada")
            driver.find_element_by_id("optionStatusSent").click
            print("Des seleccionando enviada")
            driver.find_element_by_id("optionStatusDelivered").click
            print("Des seleccionando entregada")            
        btn_query_search = driver.find_element_by_id("searchOrdersBtn")
        if btn_query_search is not None:
            print("Botón buscar encontrado")
            btn_query_search.click()
            print("Pulsando...")
            time.sleep(6)
        userOnlySearcher = driver.find_element_by_xpath("/html/body/div[2]/div[7]/div[1]/div[1]/div[3]/div/input")
        if userOnlySearcher is not None:
            print("Buscador contra tabla encontrado")
            userOnlySearcher.send_keys("micho")

        #Empieza proceso de cambios de estado
        #boton_status = driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[7]/span/i')
        boton_status= driver.find_element_by_class_name('btnChangeOrderStatus ')  
        if boton_status is not None:
            print("Botón para cambiar de status encontrado")
            boton_status.click()
            time.sleep(3)
        try:
            boton_nueva = driver.find_element_by_xpath('//*[@id="placedOrderOptn"]')
            if boton_nueva is not None:
                print("Botón para confirmar (Campanita) orden encontrado")
                boton_nueva.click()
                time.sleep(3)
        except ElementClickInterceptedException as exception:
            print("La orden va un paso más adelante que ser nueva")
            time.sleep(2)
        #Cerrar modal con "CONFIRMAR"
        try:
            boton_confirma = driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
            if boton_confirma is not None:
                print("Botón confirmar (para cerrar) encontrado")
                boton_confirma.click()
                time.sleep(3)
        except ElementClickInterceptedException as exception:
            print("Probablemente ya está enviado")
        #Se abre modal de nuevo
        boton_status = driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[7]/span/i')
        if boton_status is not None:
            print("Botón para cambiar de status encontrado")
            boton_status.click()
            time.sleep(3)
        #Se intenta hace click en la palomita 
        try:
            boton_confirmarrr = driver.find_element_by_xpath('//*[@id="confirmedOrderOptn"]')
            if boton_confirmarrr is not None:
                print("Botón de estado 'Confirmar (Palomita)', encontrado")
                boton_confirmarrr.click()
                time.sleep(3)
        except ElementClickInterceptedException as exception:
            print("La orden va un paso más adelante que la confirmación de orden")
            time.sleep(2)
        #Cerrar modal con "Confirmar"
        boton_confirma = driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
        if boton_confirma is not None:
            print("Botón confirmar (para cerrar) encontrado")
            boton_confirma.click()
            time.sleep(2)
        #Se abre modal de nuevo
        boton_status = driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[7]/span/i')
        if boton_status is not None:
            print("Botón para cambiar de status encontrado")
            boton_status.click()
            time.sleep(3)
        #Se intenta hacer click en el carrito (programar envío)
        try:  
            boton_programada = driver.find_element_by_xpath('//*[@id="scheduledToShipOrderOptn"]')
            if boton_programada is not None:
                print("Se encontró el botón para programar el envío de la orden")
                boton_programada.click()
                time.sleep(2)
            campoGuia = driver.find_element_by_id("shippingGuide")
            if campoGuia is not None:
                print("Se encontró el campo para la guía de envío")
            campoMensajero=driver.find_element_by_xpath('//*[@id="shippingCarrier"]')
            if campoMensajero is not None:
                print("Se encontró el campo para la mensajería")
            campoLink = driver.find_element_by_xpath('//*[@id="shippingLink"]')
            if campoLink is not None:
                print("Se encontró el campo para el link de seguimiento")
            campoConductor = driver.find_element_by_xpath('//*[@id="shippingDriver"]')
            if campoConductor is not None:
                print("Se encontró el campo para el nombre del Conductor")
            campo_ruta = driver.find_element_by_xpath('//*[@id="shippingRoute"]')
            if campo_ruta is not None:
                print("Se encontró el campo para la ruta del paquete")
            try:
                campoGuia.send_keys("GM99999999999")
                campoMensajero.send_keys("DHL")
                campoLink.send_keys("https://www.unam.mx/")
                #Cerrar modal con "Confirmar"
                boton_confirma = driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
                if boton_confirma is not None:
                    print("Botón confirmar (para cerrar) encontrado")
                    boton_confirma.click()
                    time.sleep(2)
            except ElementNotInteractableException as exception:
                print("No se encontró, campo de guía, entonces es local!")
                campoConductor.send_keys("Juanito Pérez")
                campo_ruta.send_keys("La Huasteca")
                #Cerrar modal con "Confirmar"
                boton_confirma = driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
                if boton_confirma is not None:
                    print("Botón confirmar (para cerrar) encontrado")
                    boton_confirma.click()
                    time.sleep(2)
        except ElementClickInterceptedException as exception:
            print("La orden va un paso más adelante que la programación de envío")
        #Se abre modal de nuevo
        boton_status = driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[7]/span/i')
        if boton_status is not None:
            print("Botón para cambiar de status encontrado")
            boton_status.click()
            time.sleep(3)
        #Se intenta hace click en construyendo 
        try:
            boton_construyendo = driver.find_element_by_xpath('//*[@id="inConstructionOrderOptn"]')
            if boton_construyendo is not None:
                print("Botón de estado construyendo (paquetito) encontrado")
                boton_construyendo.click()
                time.sleep(3)
        except ElementClickInterceptedException as exception:
            print("La orden va un paso más adelante que construyendo Orden")
            time.sleep(3)
        #Cerrar modal con "Confirmar"
        boton_confirma = driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
        if boton_confirma is not None:
            print("Botón confirmar (para cerrar) encontrado")
            boton_confirma.click()
            time.sleep(3)
        #Se abre modal de nuevo
        boton_status = driver.find_element_by_xpath('//*[@id="ordersTableBody"]/tr/td[7]/span/i')
        if boton_status is not None:
            print("Botón para cambiar de status encontrado")
            boton_status.click()
            time.sleep(3)
        #Se intenta hace click en Entregado
        try:
            try:
                boton_entregado = driver.find_element_by_xpath('//*[@id="deliveredOrderOptn"]')
                if boton_entregado is not None:
                    print("Botón de estado entregado (monito) encontrado")
                    time.sleep(2)
                    boton_entregado.click()
                    time.sleep(3)
            except ElementClickInterceptedException as exception:
                print("La orden ya se entregó o está cancelada")
                time.sleep(2)
            #Cerrar modal con "Confirmar"
            boton_confirma = driver.find_element_by_xpath('//*[@id="btnModalChangeOrderStatus"]')
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
