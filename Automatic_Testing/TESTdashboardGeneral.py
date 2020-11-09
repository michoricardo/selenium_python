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
import TESTemailLogin as el #Archivo para iniciar sesión en email
#Para desidentar: CTRL + SHIFT + BRACKET IZQ
class generalDashboardTestClass (unittest.TestCase):
    def setUp(self):
        global driver
        #driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
        driver = webdriver.Firefox(executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")
        el.loginFromEmailClass().test_emailLog(driver)
    def test_generalDashboard(self):
        #Dashboard general
        print("Para continuar, es necesario tener  role de administrador")
        print("<br>")
        driver.get("https://gobstore-qa.firebaseapp.com/admin/dashboard")
        time.sleep(2)
        print("El usuario tiene permisos de administrador")
        print("<br>")
        canalesDisponibles=[]
        time.sleep(2)
        selectorCanales=driver.find_element_by_id('profileSelector')
        if selectorCanales is not None:
            selectorCanales.click()
            opcionesDisponibles=selectorCanales.find_elements_by_tag_name("option")
            print("las opciones disponibeles son:     ")
            for x in opcionesDisponibles:
                print("<h2>")
                print("<b>")
                print("Canal: ",x.get_attribute("value"))
                print("<b>")
                print("</h2>")
                print("<br>")
                selectorCanales.click()
                x.click()
                #Búsqueda de última semana
                semana_buscar= driver.find_element_by_xpath('//*[@id="btnSearchData"]')
                if semana_buscar is not None:
                    semana_buscar.click()
                    time.sleep(4)
                    print("<h2>")
                    print("Se ha hecho la busqueda de datos de los ultimos 7 dias:")
                    print("</h2>")
                    print("<br>")
                    datepicker_from = driver.find_element_by_xpath('//*[@id="inputDateMin"]').get_attribute("value")
                    datepicker_to=driver.find_element_by_xpath('//*[@id="inputDateMax"]').get_attribute("value")
                    #Tabla
                    #Resumen
                    clientes_ordenes= driver.find_element_by_xpath('//*[@id="totalClients"]').text
                    total_orders=driver.find_element_by_xpath('//*[@id="ordersTotal"]').text
                    local_orders=driver.find_element_by_xpath('//*[@id="localOrdersLenght"]').text 
                    national_orders=driver.find_element_by_xpath('//*[@id="nationalOrdersLenght"]').text
                    nuevos_clientes = driver.find_element_by_xpath('//*[@id="newClients"]').text
                    ingreso_total=driver.find_element_by_xpath('//*[@id="totalIncome"]').text
                    income_shipping=driver.find_element_by_xpath('//*[@id="incomeShipping"]').text
                    comision=driver.find_element_by_xpath('//*[@id="profitComission"]').text
                    embalaje=driver.find_element_by_xpath('//*[@id="profitPackaging"]').text
                    partner_payment=driver.find_element_by_xpath('//*[@id="partnerPayment"]').text
                    avTicket=driver.find_element_by_xpath('//*[@id="averageTicket"]').text
                    #Top
                    try:
                        first=driver.find_element_by_xpath('//*[@id="ulTop5Products"]/li[1]/div/h6').text
                        second=driver.find_element_by_xpath('//*[@id="ulTop5Products"]/li[2]/div/h6').text
                        third=driver.find_element_by_xpath('//*[@id="ulTop5Products"]/li[3]/div/h6').text
                    except NoSuchElementException as exception:
                        first="Sin datos"
                        second="Sin datos"
                        third="Sin datos"
                    print("<h4>")   
                    print("<br>")
                    print("<b>Se imprimen los valores del dia ", datepicker_from)
                    print("Hasta el dia  : ", datepicker_to)
                    print("</b>")
                    print("</h4>")

                    headers= "<table style='background-color:#50B7FF; border-style:dashed;'><tr><th> Clientes que hicieron ordenes </th><th> Total de ordenes </th><th> Ordenes locales </th><th> ordenes nacionales </th><th> clientes nuevos </th><th> Ingreso Total </th><th> Ingreso por envio </th><th> comision </th><th> embalaje </th><th> Pago a socio </th><th>Ticket Promedio </th></tr></table"
                    content="<table style='background-color:#50B7FF; border-style:dashed;'><tr><td>"+str(clientes_ordenes)+ "</td><td>"+str(total_orders)+"</td><td>"+str(local_orders)+"</td><td>"+str(national_orders)+"</td><td>"+str(nuevos_clientes)+"</td><td>"+str(ingreso_total)+"</td><td>"+str(income_shipping)+"</td><td>"+str(comision)+"</td><td>"+str(embalaje)+"</td><td>"+str(partner_payment)+"</td><td>"+str(avTicket)+"</td></tr></table>"        
                    table1=headers+content
                    print(table1)
                    inici="<h4><b> Productos Estrella TOP 3 </b><h4>"
                    #inici= "<table style='background-color:#50B7FF; border-style:dashed;'><tr><th>Productos Estrella TOP 3</th></tr></table>"
                    print(inici)
                    headers2= "<table style='background-color:#50B7FF; border-style:dashed;'><tr><th> Primer Lugar </th><th> Segundo Lugar </th><th> Tercer Lugar </th></tr></table>"
                    content2="<table style='background-color:#50B7FF; border-style:dashed;'><tr><td>"+str(first)+ "</td><td>"+str(second)+"</td><td>"+str(third)+"</td></tr></table>"
                    table2=headers2+content2
                    print(table2)
                    print("<p> =========================================================================================================================================</p>")
    
        
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
