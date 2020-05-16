#Imports de testing/selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#Se importan las páginas creadas
from paginas.agregar_domicilio_mty import domicilioMTY
from paginas.agregar_domicilio_cdmx import domicilioCDMX
from paginas.agregar_metodos_pago_conekta import metodosDePagoConekta
from paginas.compra_Ramos_TDDTDC import shoppingRamosTDDTDC
from paginas.compra_Ramos_OXXO import shoppingRamosOXXO
from paginas.compra_Ramos_SPEI import shoppingRamosSPEI
from paginas.compra_Ramos_TDD_GOBSTORE_LOCAL import shoppingRamosLocally
from paginas.find_order_details import findOrder
from paginas.googleAuth import googleOauth
from paginas.mailAuth import correoauth
from paginas.proceso_completo_orden import ProcessOrder
#Imports comunes python
import sys
import time
#Para desidentar: CTRL + SHIFT + BRACKET IZQ
class ClickSendKeys(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
        driver.get("https://gobstore-qa.firebaseapp.com/")
        print("abriendo la página principal") 
        driver.implicitly_wait(50)
    def testID(self):
        print("Iniciando sesión con correo automáticamente")
        inicioCCorreo = correoauth(driver)
        inicioCCorreo.inicioConCorreo()
        n=0
        while n==0:
            print("""¿Que automatizacion quieres correr?
            1.-Iniciar sesión con Google
            2.- Agregar un domicilio de Monterrey
            3.- Agregar un domicilio de Ciudad de Mexico
            4.-Agregar métodos de pago (Visa correcta, Mastercard correcta, American Express Correcta,
            Tarjeta declinada, Tarjeta fondos insuficientes, Tarjeta MSI error)
            5.-Comprar unos chicharroncitos Ramos con tarjeta de crédito (verificar tu dirección)
            6.-Comprar unos chicharroncitos Ramos con OXXO pago(verificar tu dirección)
            7- Comprar unos chicharroncitos Ramos con SPEI pago (verificar tu dirección)
            8.-Comprar unos chicharroncitos Ramos con TDD recogiendo en GOBSTORE MTY
            9.-Encontrar una orden
            10.-Hacer el proceso de una orden en producción (no canceladas)
            11.-Salir
                    """)
            opcion = input()
            if opcion == "1":
                print("Iniciar sesión con Google")
                googleinit = googleOauth(driver)
                googleinit.inicioConGoogle()
            elif opcion =="2":
                print("Domicilio MTY")
                paginamonterrey = domicilioMTY(driver)
                paginamonterrey.altamty("Ricardo García Monterrey","8441206120","64849","Av. Eugenio Garza Sada","2501","1","Revolución y filósofos","Mi alma mater")
            elif opcion =="3":
                print("Domicilio CDMX")
                paginaCiudadDeMexico = domicilioCDMX(driver)
                paginaCiudadDeMexico.altaCDMX("Ricardo García CDMX","5556221625","04510","Cto. Interior S/N","0","1","Av Universidad e Insurgentes","Es mi nueva alma mater")
            elif opcion =="4":
                print("Agregar métodos de pago")
                tarjetaObjectVisaCorrecta = metodosDePagoConekta(driver)
                tarjetaObjectVisaCorrecta.altaTarjeta("Visa Correcta","4242424242424242","200","10","22")
                time.sleep(3)
                default=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/button[2]').click()
                #Set as default
                time.sleep(4)
                tarjetaObjectMasterCorrecta = metodosDePagoConekta(driver)
                tarjetaObjectMasterCorrecta.altaTarjeta("Mastercard Correcta","5555555555554444" ,"200","10","22")
                time.sleep(4)
                tarjetaObjectAmexCorrecta = metodosDePagoConekta(driver)
                tarjetaObjectAmexCorrecta.altaTarjeta("American Express Correcta","378282246310005" ,"200","10","22")
                time.sleep(4)
                tarjetaObjectDeclined = metodosDePagoConekta(driver)
                tarjetaObjectDeclined.altaTarjeta("Tarjeta Declinada","4000000000000002" ,"200","10","22")
                time.sleep(4)
                tarjetaObjectInsufficient = metodosDePagoConekta(driver)
                tarjetaObjectInsufficient.altaTarjeta("Tarjeta Insuficientes","4000000000000127" ,"200","10","22")
                time.sleep(4)
                tarjetaObjectMSI_error = metodosDePagoConekta(driver)
                tarjetaObjectMSI_error.altaTarjeta("Tarjeta MSI Error","4111111111111111" ,"200","10","22")
            elif opcion == "5":
                print("Comprar unos chicharroncitos Ramos con tarjeta de crédito(Verifica tu dirección)")
                chicha = shoppingRamosTDDTDC(driver)
                chicha.compraChicharron()
            elif opcion == "6":
                print("Comprar unoschicharroncitos Ramos con OXXO pago (verifica tu dirección)")
                chichaOXXO = shoppingRamosOXXO(driver)
                chichaOXXO.compraChicharron()
            elif opcion == "7":
                print("Comprar unoschicharroncitos Ramos con SPEI pago (verifica tu dirección)")
                chichaSPEI = shoppingRamosSPEI(driver)
                chichaSPEI.compraChicharron()
            elif opcion == "8":
                print("Comprar unos chicharroncitos Ramos con TDD recogiendo en GOBSTORE MTY")
                chichaGobstoreLocal = shoppingRamosLocally(driver)
                chichaGobstoreLocal.compraChicharronLocally("8441206120")
            elif opcion == "9":
                print("Encontrar una orden")
                orderSearcher = findOrder(driver)
                orderSearcher.encontrarOrden()
            elif opcion == "10":
                print("Hacer el proceso de una orden en producción no canceladas")
                orderProduction = ProcessOrder(driver)
                orderProduction.OrdenDeProceso()
            elif opcion =="11":
                print("Nos vemos pronto")
                despedida = ClickSendKeys()
                despedida.tearDown()
            else:
                print("opcion invaida")
    def tearDown(self):
        driver.quit()
        sys. exit()
            #exit(0)

if __name__ == "__main__":
   unittest.main()
