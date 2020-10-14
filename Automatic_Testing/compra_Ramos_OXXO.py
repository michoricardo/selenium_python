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

class shoppingRamosOXXO(unittest.TestCase):
    """def __init__(self,driver):
        
        self.driver=driver"""
    def setUp(self):
        global driver
        #driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
        driver = webdriver.Firefox(executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")
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

    def test_compraChicharron(self):
        driver.get("https://gobstore-qa.firebaseapp.com/carnesramos")
        global codigoPostal
        codigoPostal= "64849"
        time.sleep(3)
        try:
            modal = WebDriverWait(driver,40).until(EC.presence_of_element_located((By.XPATH,'//*[@id="postalCodeModal"]/div/div')))
            if modal is not None:
                blank_cp = driver.find_element_by_id("inputPostalCode")
                if blank_cp is not None:
                    print("Agregando CP")
                    print("<br>")
                    blank_cp.send_keys(codigoPostal)
                    vertienda = driver.find_element_by_id("btnGetOpByPostalCode")
                    vertienda.click()
                    time.sleep(4)
        except ElementNotInteractableException as exception:
            print("No tenias que poner CP porque ya habías comprado :)")
            print("<br>")
        time.sleep(3)
        btn_chicharron = driver.find_element_by_xpath('//*[@id="customSectionsWrapper"]/div/div[2]/div[2]/div[1]')
        if btn_chicharron is not None:
            print("Clickeando imagen de chicharron para agregar a cart")
            print("<br>")
            btn_chicharron.click()
            driver.implicitly_wait(10)
            time.sleep(2)    
        btn_addToCart = driver.find_element_by_id("btnAddItemToCard")
        if btn_addToCart is not None:
            print("Haciendo click en Agregar al carrito/ QTY default (1)")
            print("<br>")
            btn_addToCart.click()
            driver.implicitly_wait(10)
            time.sleep(2)
        """
        btn_checkCart = driver.find_element_by_xpath('/html/body/header/div/div/section/button[3]/span')
        if btn_checkCart is not None:
            print("Haciendo click para consultar carrito")
            print("<br>")
            btn_checkCart.click()
            driver.implicitly_wait(10)
            time.sleep(8)
        btn_proceedCheckout = driver.find_element_by_id("proceedToCheckout")
        if btn_proceedCheckout is not None:
            print("Haciendo click para proceder a checkout")
            btn_proceedCheckout.click()
            driver.implicitly_wait(10)
            time.sleep(8)"""
        cambio_pagina =driver.get("https://gobstore-qa.firebaseapp.com/carnesramos/checkout")
        print("Llendo a checkout")
        print("<br>")
        time.sleep(5)
        btn_OXXO = driver.find_element_by_xpath('//*[@id="paymentTypeSelector"]/li[2]/a')
        if btn_OXXO is not None:
            print("Eligiendo metodo de pago OXXO")
            print("<br>")
            btn_OXXO.click()
            driver.implicitly_wait(10)
            time.sleep(8)
        driver.execute_script("window.scrollTo(0,400)")
        time.sleep(3)
        disclaimerCheck = driver.find_element_by_xpath('//*[@id="paymentTypeAgreementMessageLabel"]')
        if disclaimerCheck is not None:
            print("Checkbox disclaimer encontrado")
            print("<br>")
            time.sleep(2)
            disclaimerCheck.click()
        driver.execute_script("window.scrollTo(0,1200)")
        #MANEJO DE DATEPICKER
        datepicker = driver.find_element_by_xpath('//*[@id="inputDate"]')
        if datepicker is not None:
            print("Date picker encontrado")
            print("<br>")
            time.sleep(2)
            actions= ActionChains(driver)
            actions.move_to_element(datepicker).click().perform()
            time.sleep(3)
            print("<br>")
            print("<br>")
            tabla = driver.find_element_by_xpath('//*[@id="deliveryDatetimepicker"]/div[1]/ul/li[1]/div/div[1]/table/tbody')
            if tabla is not None:
                print("Se encontro la tabla")
                activo = tabla.find_element_by_css_selector("#deliveryDatetimepicker td.day:not(.disabled)")
                if activo is not None:
                    print("se encontro activo en tabla")
                    print("<br>")
                    print("valor: ",activo.get_attribute("value"))
                    print("<br>")
                    print("texto: ",activo.text)
                    print("<br>")
                    activo.click()
                    print("eligiendo dia activo")
            time.sleep(1)
            print("<br>")
            #TERMINA MANEJO DE DATEPICKER
        falto_algo=driver.find_element_by_xpath('//*[@id="extraComments"]').send_keys("No faltó nada")
        time.sleep(1)
        ordenar_btn=driver.find_element_by_xpath('//*[@id="handlePlaceOrder"]')
        if ordenar_btn is not None:
            print("Ordenando ...")
            print("<br>")
            ordenar_btn.click()
            time.sleep(5)
            alert_obj = driver.switch_to.alert
            alert_obj.accept()
            print("alerta aceptada")
            time.sleep(20)
        urlcompra = driver.current_url
        print("llego aqui")
        if urlcompra is not None:
            if "thankyou?order=" in urlcompra:
                print("Enlace de compra:")
                print("<br>")
                print(urlcompra)
                print("<br>")
                #<a href="quien-soy.html">Quién soy</a>
                print("<a href=")
                print(urlcompra)
                print(">")
                print(urlcompra)
                print("</a>")
                #print('<a href="','"',urlcompra,'"'>urlcompra,'</a>')
            
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
