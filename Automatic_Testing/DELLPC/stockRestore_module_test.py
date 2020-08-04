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

class stockRestoreClass (unittest.TestCase):
    """def __init__(self,driver):
        
        self.driver=driver"""
    def setUp(self):
        global driver
        #driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
        driver = webdriver.Firefox(executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")
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
        #INICIO DE SESIÓN TERMINA
    def test_stockRestore(self):
        #RAMOS CANAL
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
            print("No se agrega Codigo postal porque ya existia una sesion activa")
            print("<br>")
            print("Intentando entrar a pagina de stock superadmin")
            time.sleep(3)
        driver.get("https://gobstore-qa.firebaseapp.com/carnesramos/config/stock")        
        print("Se entro a la pagina de stock")
        print("<br>")
        time.sleep(2)        
        print("El usuario tiene permisos de superadmin")
        print("<br>")
        selectorOp = driver.find_element_by_xpath('//*[@id="inputGroupOpSelector"]')
        if selectorOp is not None:
            selectorOp.click()
            opMty=driver.find_element_by_xpath('//*[@id="inputGroupOpSelector"]/option[1]')
            opMty.click()
            print('Eligiendo operativo de Monterrey')
            print("<br>")
            time.sleep(3)
        quantities=driver.find_elements_by_css_selector(".inputIncrement")   
        buttons=driver.find_elements_by_css_selector(".inputIncrementBtn")
        quantitieslength=len(quantities)
        print(quantitieslength)
        cookiebanner=driver.find_element_by_xpath(' //*[@id="acceptCookieAgreement"]')
        if cookiebanner is not None:
            cookiebanner.click()
            print("cookies aceptadas")
            print("<br>")
        #driver.execute_script("window.scrollTo(0,1200)")
        for al in range(quantitieslength):
            tempBox=driver.find_element_by_xpath('//*[@id="productsStockTable"]/tbody/tr['+str(al+1)+']/td[13]/input')
            tempButton=driver.find_element_by_xpath('//*[@id="productsStockTable"]/tbody/tr['+str(al+1)+']/td[14]/button')
            print("Elemento #"+str(al+1)+"con 5 productos extra en stock")
            print("<br>")
            time.sleep(1)
            tempBox.send_keys('5')
            tempButton.click()
            time.sleep(3)
        
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
