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

class dashboardTestClass (unittest.TestCase):
    """def __init__(self,driver):
        
        self.driver=driver"""
    def setUp(self):
        global driver
        #driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
        #Cerrar modal
        try:
            esperaModalMolesto = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="PopupSignupForm_0"]/div[2]/div[1]'))).click()
            print("Se hizo click en el modal molesto del newsletter")
            print("<br>")
        except ElementNotInteractableException as exception:
            print("No se encontraron modales molestos de newsletter")
            print("<br>")
        #Termina manejo de modal
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
    def test_specificDashboard(self):
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
            time.sleep(3)
            
        print("Para continuar, es necesario tener  role de profile_owner")
        print("<br>")
        driver.get("https://gobstore-qa.firebaseapp.com/carnesramos/dashboard")
        time.sleep(2)
        print("El usuario tiene permisos de profile_owner")
        print("<br>")
        semana_buscar= driver.find_element_by_xpath('//*[@id="btnSearchData"]')
        if semana_buscar is not None:
            semana_buscar.click()
            time.sleep(4)
            print("Se ha hecho la busqueda de datos de los ultimos 7 dias:")
            print("<br>")
            datepicker_from = driver.find_element_by_xpath('//*[@id="inputDateMin"]').get_attribute("value")
            datepicker_to=driver.find_element_by_xpath('//*[@id="inputDateMax"]').get_attribute("value")
            #Tabla
            #Resumen
            clientes_ordenes= driver.find_element_by_xpath('//*[@id="totalClients"]').text
            local_orders=driver.find_element_by_xpath('//*[@id="localOrdersLenght"]').text 
            national_orders=driver.find_element_by_xpath('//*[@id="nationalOrdersLenght"]').text
            #nuevos_clientes = driver.find_element_by_xpath('//*[@id="newClients"]').get_atrribute("value")
            nuevos_clientes = driver.find_element_by_xpath('//*[@id="newClients"]').text
            ingreso=driver.find_element_by_xpath('//*[@id="profit"]').text
            comision=driver.find_element_by_xpath('//*[@id="profitComission"]').text
            embalaje=driver.find_element_by_xpath('//*[@id="profitPackaging"]').text
            avTicket=driver.find_element_by_xpath('//*[@id="averageTicket"]').text
            #Top
            first=driver.find_element_by_xpath('//*[@id="ulTop5Products"]/li[1]/div/h6').text
            second=driver.find_element_by_xpath('//*[@id="ulTop5Products"]/li[2]/div/h6').text
            third=driver.find_element_by_xpath('//*[@id="ulTop5Products"]/li[3]/div/h6').text
            print("<br>")
            print("<b>Se imprimen los valores del dia ", datepicker_from)
            print("Hasta el dia  : ", datepicker_to)
            print("</b>")
            print("<br>")
            print("<br>")
            uno=('              ._ o o')
            dos=('               \_`-)|_')
            tres=('           ,""       \ ')
            cuatro=('    ,"  ## |   ಠ ಠ. ')
            cinco=('     ," ##   ,-\__    `.')
            seis=('      ,"       /     `--._;)')
            siete=('  ,"     ## /')
            ocho=(' ,"   ##    /')
            print(uno.encode("utf-8"))
            print("</br>")
            print(dos.encode("utf-8"))
            print("</br>")
            print(tres.encode("utf-8"))
            print("</br>")
            print(cuatro.encode("utf-8"))
            print("</br>")
            print(cinco.encode("utf-8"))
            print("</br>")
            print(seis.encode("utf-8"))
            print("</br>")                                       
            print(siete.encode("utf-8"))
            print("</br>")
            print(ocho.encode("utf-8"))
            print("</br>")   
            print("<br>")
            print('<table style= "width:100%">')
            #Header
            print('<tr>')
            print('<th>Clientes que hicieron ordenes</th>')    
            print('<th>Ordenes locales</th>')
            print(' <th>Ordenes nacionales</th>')
            print(' <th>Clientes nuevos</th>')
            print(' <th>Ingreso</th>')
            print(' <th>Comision</th>')
            print(' <th>Embalaje</th>')
            print(' <th>Ticket Promedio</th>')
            print(' </tr>')
            #Cuerpo tabla informacion resumen
            print('<tr>')
            print('<td>',clientes_ordenes,'</td>')
            print('<td>',local_orders,'</td>')
            print('<td>',national_orders,'</td>')
            print('<td>',nuevos_clientes,'</td>')
            print('<td>',ingreso,'</td>')
            print('<td>',comision,'</td>')
            print('<td>',embalaje,'</td>')
            print('<td>',avTicket,'</td>')
            print(' </tr>')
            print("</table>")
            print("<br>")
            #Tabla siguiente (top 3)
            print('<table style= "width:100%">')
            print('<tr>')
            print('<th style= "width:100%">Productos Estrella/TOP 3</th>')
            print(' </tr>')
            print("</table>")
            print("<br>")
            #Brinco row
            #print('<tr>')
            print('<table style= "width:100%">')
            print('<th>Primer lugar</th>')
            print('<th>Segundo lugar</th>')
            print('<th>Tercer lugar</th>')
            #print(' </tr>')
            print("<br>")
            #Informacion productos
            print('<tr>')
            print('<td>',first,'</td>')
            print('<td>',second,'</td>')
            print('<td>',third,'</td>')
            print('</tr>')
            
            print("</table>")
        
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
