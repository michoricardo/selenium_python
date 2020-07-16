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
from selenium.webdriver.firefox.options import Options ##para guardar archivos sin preguntar
import csv
class csvModule(unittest.TestCase):
    """def __init__(self,driver):
        
        self.driver=driver"""
    def setUp(self):
        global driver
        options = Options()##para guardar archivos sin preguntar
        options.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
        #options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/csv")
        #driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
        #driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\Users\\Username\\Downloads\\chromedriver.exe")
        driver = webdriver.Firefox(firefox_options=options,executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
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
    ##Con sesión iniciada
    def test_modulocsv(self):
        driver.get("https://gobstore-qa.firebaseapp.com/admin/orders/all")
        time.sleep(4)
        orderDateFilter = WebDriverWait(driver,40).until(EC.presence_of_element_located((By.ID,'typeOfSearchSelect')))
        if orderDateFilter is not None:
            print("Selector para fechas encontrado")
            print("<br>")
            orderDateFilter.click()
            botonEnviadas = driver.find_element_by_xpath('//*[@id="typeOfSearchSelect"]/option[1]')
            print("Boton enviadas encontrado")
            print("<br>")
            botonEnviadas.click()
            print("Clickeado")
            print("<br>")
            searchOrdersBtn = driver.find_element_by_id('searchOrdersBtn')
            if searchOrdersBtn is not None:
                searchOrdersBtn.click()
                print("Se hizo click para buscar ordenes")
                print("<br>")
                time.sleep(8)
            howmanyInfo = WebDriverWait(driver,400).until(EC.presence_of_element_located((By.CLASS_NAME,'pagination-info')))
            #Pie de página para contar Rows
            try:
                if howmanyInfo is not None:
                    print('si llego al how many')
                    howmanyInfoValue = howmanyInfo.text
                    print("<br>")
                    rows=howmanyInfoValue.split()
                    print("se encontraron", rows[5], "ordenes")
                    print('<br>')
                btnCsvExport = driver.find_element_by_id('exportExcelBtn')
                btnCsvExport.click()
                print("Se hace click en exportar ordenes")
            except:
                print("No se encontraron ordenes o elemento de pie de tabla")
            #wait for download complete
            wait = True
            while(wait==True):
                for fname in os.listdir('C:/Users/ricar/Downloads'):
                    if ('orders') in fname:
                        print('se encontro un archivo csv')
                        print('<br>')
                        time.sleep(1)
                        with open('C:/Users/ricar/Downloads/orders.csv') as csvfile:
                            readCSV = csv.reader(csvfile, delimiter=',')
                            folio_nuevo = None
                            for row in readCSV:
                                foliocurrent = row[0]
                                if folio_nuevo == foliocurrent:
                                    print(row[24],row[25])
                                    print('<br>')
                                    
                                elif folio_nuevo != foliocurrent:
                                    print('*******************************************')
                                    print('<br>')
                                    print(row[0])
                                    print('<br>')
                                    print(row[24],row[25])
                                    print('<br>')
                                folio_nuevo = foliocurrent
                        print("--------------------------------------------------------------------")
                        print('<br>')
                        print("--------------------------------------------------------------------")
                        print('<br>')
                    else:
                        wait=False
            print('FIN DE LOS ARCHIVOS ENCONTRADOS')
                            

    def tearDown(self):
        driver.quit()
        


if __name__ == "__main__":
   unittest.main()
