import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
#from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class Espera(unittest.TestCase):

    while True:
        global errors
        errors ={'error':'Tipo de error','Fecha de inicio':time.asctime(),'Duracion en segundos':time.asctime()}
        try:
            tiempoinicial = time.time()
            inicial_asc = time.asctime()
    
            def setUp(self):
                global driver
                driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
            
                #driver.implicitly_wait(15)
        
                driver.get("http://goodstartbook.com/pruebas/")

            def test1(self):
                espera = WebDriverWait(driver, 10)
                boton = espera.until(EC.element_to_be_clickable((By.ID,"proceed")))
                if boton is not None:
                    boton.click()
                    print("Ecsitosa")
                    time.sleep(3)
        except KeyboardInterrupt:
            print("Salemossss")
            final = time.time()
            difference = final-tiempoinicial
            errors.update({'error':'Interrupción de teclado','Fecha de inicio':inicial_asc,'Duracion en segundos':difference})
            with open("mailAuth.txt","a") as f:
                print(errors,file = f)
                print('\n', file = f)
            break
        except (ElementClickInterceptedException) as e:
            #raise ValueError("No se pudo hacer click en un elemento") from e
            print("No se pudo hacer click en un elemento")
            final = time.time()
            difference = final-tiempoinicial
            errors.update({'error':'Elemento no clickeable','Fecha de inicio':inicial_asc,'Duracion en segundos':difference})
            print(errors,"\n")
            with open("mailAuth.txt","a") as f:
                #print(23*"=",file = f)
                print(errors,file = f)
                print('\n', file = f)
        except (TimeoutException) as e:
            print("Pasó más del tiempo de espera para encontrar un elemento")
            final = time.time()
            difference = final-tiempoinicial
            errors.update({'error':'Tiempo de espera agotado','Fecha de inicio':inicial_asc,'Duracion en segundos':difference})
            print(errors,"\n")
            with open("mailAuth.txt","a") as f:
                print(errors, file = f)
                print('\n', file = f)
        except (NoSuchElementException) as e:
            print("No se encontró el elemento")
            final = time.time()
            difference = final-tiempoinicial
            errors.update({'error':'No se encontró un elemento','Fecha de inicio':inicial_asc,'Duracion en segundos':difference})
            print(errors,"\n")
            with open("mailAuth.txt","a") as f:
                print(errors, file = f)
                print('\n', file = f)
        except:
            print("Ocurrió error desconocido de selenium o de plataforma")
            final = time.time()
            difference = final-tiempoinicial
            errors.update({'error':'De plataforma/selenium desconocido','Fecha de inicio':inicial_asc,'Duracion en segundos':difference})
            print(errors,"\n")
            with open("mailAuth.txt","a") as f:
                print(errors, file = f)
                print('\n', file = f)
        else:
            print ("Nada detuvo el script")
            final = time.time()
            print("El tiempo de prueba en segundos fue: ", final-tiempoinicial)
            with open("mailAuth.txt","a") as f:
                #print(23*"=",file = f)
                print("Prueba exitosa!! "+ "Tiempo de inicio: ", inicial_asc, " El tiempo en segundos fue:", final-tiempoinicial ,file = f)
                print('\n',file = f)
        
    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/ricar/Documents/GrillOnBox/PythonScripts/HtmlTestRunner'))
