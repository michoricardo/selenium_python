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
from selenium.webdriver.common.keys import Keys
from reportlab.pdfgen import canvas
class reportGenerator:
    def __init__(self,driver):
        self.driver=driver
    def generandoReporte(self):
        
        exitosas=0
        interrupcion = 0
        clickInterrumpido = 0
        timeout = 0
        noElemento = 0
        selenium_platform = 0
        with open('mailAuth.txt') as fobj:
            
            lectura = fobj.readlines()
            for line in lectura:
                if "exitosa!!" in line:
                    exitosas = exitosas+1
                elif 'teclado' in line:
                    interrupcion = interrupcion+1
                elif 'clickeable' in line:
                    clickInterrumpido = clickInterrumpido+1
                elif 'agotado' in line:
                    timeout = timeout+1
                elif 'encontró' in line:
                    noElemento = noElemento+1
                elif 'plataforma' in line:
                    selenium_platform =selenium_platform+1
            """print("Las exitosas fueron: ", exitosas)
            print("Se interrumpieron :", interrupcion)
            print("No se pudo hacer click" ,clickInterrumpido)
            print("Se agotó el tiempo de espera: ",timeout)
            print("No se encontró al elemento: ",noElemento)
            print("Otros errores: ", selenium_platform)"""
        with open ("mailAuthResumen.txt", "a") as f:
            print("Se genera reporte el: ",time.asctime(),file = f)
            print('\n', file = f)
            print(23*"=",file = f)
            print('\n', file = f)
            print("Las exitosas fueron: ",exitosas, file = f)
            print('\n', file = f)
            print("Se interrumpieron :",interrupcion,file = f)
            print('\n', file = f)
            print("No se pudo hacer click" ,clickInterrumpido, file = f)
            print('\n', file = f)
            print("Se agotó el tiempo de espera: ",timeout, file = f)
            print('\n', file = f)
            print("No se encontró al elemento: ",noElemento, file = f)
            print('\n', file = f)
            print("Otros errores: ",selenium_platform, file = f)
            print('\n', file = f)
        time.sleep(5)
        with open('mailAuthResumen.txt') as fobj:
            lecturaResumen = fobj.readlines()
            fobj.close()
            c= canvas.Canvas("Reporte1")
            from reportlab.lib import colors
            text = c.beginText(40, 680)
            text.setFont("Courier", 18)
            text.setFillColor(colors.blue)
            for line in lecturaResumen:
                line.split('\n')
                text.textLine(line)

            c.drawText(text)            
            #c.setFont('Helvetica',12)
            #c.drawString(0,200,lecturaResumen)
            c.save()
    def tearDown(self):
        driver.quit()
  

if __name__ == "__main__":
   unittest.main()
