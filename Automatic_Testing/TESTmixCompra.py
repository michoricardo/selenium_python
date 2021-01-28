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
import TESTemailLoginDev as el #Archivo para iniciar sesión en email en dev
class shoppingMixClass(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Firefox(executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")
        el.loginFromEmailClassDev().test_emailLog(driver)
    def test_compraMix(self):
        arregloExtras = ["'oQ0JXRH272Wr5ZfUCdcY'","'yOC2OdW19WPQrsyvunPN'","'ffXuw5WGxtGx9oAnSqpA'","'EUKRqXcreRY6XIxjSeUl'","'7Xckm3LDgOHUXlcnSgb5'","'MX3QgHH6ub0xHabneL2Y'"]
        driver.get("https://gobstoredev.firebaseapp.com/bearsinthekitchen")
        global codigoPostal
        #codigoPostal= "25204"
        codigoPostal=75201
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
        btn_mix1 = driver.find_element_by_css_selector("[data-mix-sku='TESTHK1']")
        if btn_mix1 is not None:
            print("Clickeando imagen del mix para agregar a cart")
            print("<br>")
            btn_mix1.click()
            driver.implicitly_wait(10)
            time.sleep(2)
        #Elegir toppings
        sirloin = driver.find_element_by_css_selector("[data-topping-id='Xx2ZTMHPC5d3GgTdrshH']").find_element_by_css_selector(".incrementToppingQty ")
        if sirloin is not None:
            print("Eligiendo sirloin")
            print("<br>")
            sirloin.click()
            time.sleep(1)
        pollo = driver.find_element_by_css_selector("[data-topping-id='U4crmvV8B6Lu1UAvpM7E']").find_element_by_css_selector(".incrementToppingQty ")
        if pollo is not None:
            print("Eligiendo pollo")
            print("<br>")
            pollo.click()
            time.sleep(1)
        tortillas = driver.find_element_by_css_selector("[data-topping-id='5sGpEyl4naOB2y7PNFuo']").find_element_by_css_selector(".form-check-input ")
        if tortillas is not None:
            print("Eligiendo tortillas")
            print("<br>")
            tortillas.click()
            time.sleep(1)
        salsa_roja = driver.find_element_by_css_selector("[data-topping-id='uFjbuk3Xm8J0O90bixFo']").find_element_by_css_selector(".mix-topping-optn ")
        if salsa_roja is not None:
            print("Eligiendo salsa roja")
            print("<br>")
            salsa_roja.click()
            time.sleep(1)
        salsa_tatemada = driver.find_element_by_css_selector("[data-topping-id='XjKaeNIoFE2JfHZviTpJ']").find_element_by_css_selector(".mix-topping-optn ")
        if salsa_roja is not None:
            print("Eligiendo salsa tatemada")
            print("<br>")
            salsa_tatemada.click()
            time.sleep(1)
        salsa_verde = driver.find_element_by_css_selector("[data-topping-id='bWKx0KKak2SupZwARdaC']").find_element_by_css_selector(".mix-topping-optn ")
        if salsa_verde is not None:
            print("Eligiendo salsa verde")
            print("<br>")
            salsa_verde.click()
            time.sleep(1)
        charro_beans = driver.find_element_by_css_selector("[data-topping-id='O5l3NMYDOzsKwJB7Vfzx']").find_element_by_css_selector(".incrementToppingQty ")
        if sirloin is not None:
            print("Eligiendo frijoles charrros")
            print("<br>")
            charro_beans.click()
            time.sleep(1)
        fried_beans = driver.find_element_by_css_selector("[data-topping-id='7hP6gCA2NIAvW1KaSGPj']").find_element_by_css_selector(".incrementToppingQty ")
        if sirloin is not None:
            print("Eligiendo frijoles refritos")
            print("<br>")
            fried_beans.click()
            time.sleep(1)
        for producto in arregloExtras:
            articulo = driver.find_element_by_css_selector("[data-topping-id={}]".format(producto)).find_element_by_css_selector(".incrementToppingQty ")
            articulo.click()
            time.sleep(1)
        addToCart = driver.find_element_by_id('btnAddMixToCart').click()
        time.sleep(3)
        driver.get("https://gobstoredev.firebaseapp.com/checkout/bearsinthekitchen")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,1200)")
        #driver.execute_script("window.scrollTo(0,700)")
        for i in range(2):
            try:
                #MANEJO DE DATEPICKER
                datepicker = driver.find_element_by_xpath('//*[@id="deliveryDatetimepicker"]')
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
            except NoSuchElementException as exception:
                    print("No se pudo manejar el datepicker")
            pedir=driver.find_element_by_css_selector('.btn.btn-primary.btn-lg.btn-block')
            if pedir is not None:
                print("ordenando")
                pedir.click()
            #RECUPERANDO URL COMPRA EN HTML
            time.sleep(10)
        urlcompra = driver.current_url
        if urlcompra is not None:
            if "thankyou?order=" in urlcompra:
                print("Enlace de compra:")
                print("<br>")
                print(urlcompra)
                print("<br>")
                print("<a href=")
                print(urlcompra)
                print(">")
                print(urlcompra)
                print("</a>")
        
        
        

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
