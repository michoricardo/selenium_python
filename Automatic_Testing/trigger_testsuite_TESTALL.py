#Imports de testing/selenium
import unittest
from unittest import TestLoader,TestSuite,TextTestRunner
import HtmlTestRunner

#Imports de archivos para correr todos de golpe
from TESTagregarMetodosPago  import misMetodosPago #Archivo para agregar métodos de pago
from TESTcsvOrdenes import csvModule #Archivo para checar csv de órdenes
from TESTcompraSpei import shoppingRamosSPEI #archivo para comprar spei
from TESTdashboardCanal import dashboardTestClass #archivo para checar dashboard de canal

#Imports comunes python
import sys
import time
import os
#Para desidentar: CTRL + SHIFT + BRACKET IZQ
#Arreglo de clases que fueron importadas desde los archivos
clasesDeArchivos = [dashboardTestClass,shoppingRamosSPEI]

#Para imprimir con los colores reservados de IDLE python
try: color = sys.stdout.shell
#except AttributeError: raise RuntimeError("Use IDLE")
except:
  print("No pudimos imprimir al no correr en IDLE")

if __name__ == "__main__":
  #Texto importante de colores
   color.write("-----------Consideraciones antes de correr pruebas---------- \n\n","KEYWORD")
   color.write("1.-Checar que el ambiente de qa tenga una dirección válida (Saltillo) \n","COMMENT")
   color.write("2.-Checar contraseñas (para login y para envío de email) \n","STRING")
   color.write("3.-Checar que todos los archivos estén presentes (Leer readme) \n","KEYWORD")
   color.write("4.-Las pruebas se correrán en un orden conveniente (primero resurtir stock y luego comprar, por ejemplo) \n","COMMENT")
   color.write("5.-Al final de las pruebas, se hace un resumen (verificar que las pruebas estén en la misma carpeta que  los resultados \n","STRING")
   color.write("6.-Checar que el mail desde el cual se envía el resumen tenga autorizada la opción de permitir apps menos seguras (en su cuenta de gmail) \n","KEYWORD")
   color.write("7.-Checar que todos los archivos con sus clases estén en este .py al igual que en la interfaz gráfica para poder decir que el set de pruebas está completo \n","COMMENT")
   print("\n")
   test_classes_to_run = []
   veces=input("¿Cuantas veces quieres correr el set completo de pruebas? : ")
   vecesnum= int(veces)
   for i in range(0,vecesnum): #Por cada vez que se quiso correr la prueba
      for claseIterativa in clasesDeArchivos: #Se agregan las clases al arreglo de clases por correr
         test_classes_to_run.append(claseIterativa)
   print(test_classes_to_run)
   print("debería de verse : ", vecesnum, "veces")
   
#Segunda parte del tutorial en stackoverflow
   loader = TestLoader()
   suites_list = []
   for test_class in test_classes_to_run:
      suite = loader.loadTestsFromTestCase(test_class) #Se agregan las clases por correr desde  el arreglo de clases, antes era manual
      suites_list.append(suite)
   big_suite = unittest.TestSuite(suites_list)
   runner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/DELL/Documents/Scripts de python/selenium_python/Automatic_Testing')
   #runner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/ricar/Documents/GrillOnBox/PythonScripts')
   runner.run(big_suite)
   #Web scrapping, resumen y envío por email
   print("Haciendo el merge de los archivos generados")
   os.system('python TESTscrapEstadisticasPruebas.py')
   print("Checando resumen y enviando por correo automáticamente")
   os.system('python TESTscrapResumenEnvioMailAutomatico.py')

