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
import string
import random
from random import choice
from string import ascii_uppercase
from string import ascii_lowercase
animals= ["'perrito', 'carne','animal','jugo','gato', 'Halcón','Hiena','Hipopótamo','Hormiga','Hurón','Hámster',Aardvark","Albatross","Alligator","Alpaca","Ant","Anteater","Antelope","Ape","Armadillo","Donkey","Baboon","Badger","Barracuda","Bat","Bear","Beaver","Bee","Bison","Boar","Buffalo","Butterfly","Camel","Capybara","Caribou","Cassowary","Cat","Caterpillar","Cattle","Chamois","Cheetah","Chicken","Chimpanzee","Chinchilla","Chough","Clam","Cobra","Cockroach","Cod", "Cormorant","Coyote","Crab","Crane","Crocodile","Crow","Curlew","Deer","Dinosaur","Dog","Dogfish","Dolphin","Dotterel","Dove","Dragonfly","Duck","Dugong","Dunlin","Eagle","Echidna","Eel","Eland","Elephant","Elk","Emu","Falcon","Ferret","Finch","Fish","Flamingo","Fly","Fox","Frog","Gaur","Gazelle","Gerbil","Giraffe","Gnat","Gnu","Goat","Goldfinch","Goldfish","Goose","Gorilla","Goshawk","Grasshopper","Grouse","Guanaco","Gull","Hamster","Hare","Hawk","Hedgehog","Heron","Herring","Hippopotamus","Hornet","Horse","Human","Hummingbird","Hyena","Ibex","Ibis","Jackal","Jaguar","Jay","Jellyfish",
    "Kangaroo","Kingfisher","Koala","Kookabura","Kouprey","Kudu","Lapwing","Lark","Lemur","Leopard","Lion","Llama","Lobster","Locust""Loris","Louse","Lyrebird","Magpie","Mallard","Manatee","Mandrill","Mantis","Marten","Meerkat","Mink","Mole","Mongoose","Monkey","Moose","Mosquito","Mouse","Mule","Narwhal","Newt","Nightingale","Octopus",
    "Okapi","Opossum","Oryx","Ostrich","Otter","Owl","Oyster","Panther","Parrot","Partridge","Peafowl","Pelican","Penguin","Pheasant","Pig","Pigeon","Pony","Porcupine","Porpoise","Quail","Quelea","Quetzal","Rabbit","Raccoon","Rail","Ram","Rat","Raven","Red deer",
    "Red panda","Reindeer","Rhinoceros","Rook","Salamander","Salmon","Sand Dollar","Sandpiper","Sardine","Scorpion","Seahorse","Seal","Shark","Sheep","Shrew","Skunk","Snail","Snake","Sparrow","Spider","Spoonbill","Squid","Squirrel","Starling","Stingray","Stinkbug","Stork","Swallow","Swan","Tapir","Tarsier","Termite","Tiger","Toad","Trout","Turkey",
    "Turtle","Viper","Vulture","Wallaby","Walrus""Wasp","Weasel","Whale","Wildcat","Wolf","Wolverine","Wombat","Woodcock","Woodpecker","Worm","Wren","Yak","Zebra"]
def randomGen(tipo):
    if tipo == 'sku':
        first=(''.join(choice(ascii_uppercase) for i in range(4)))
        num = str(random.randint(-1000,1000))
        second=(''.join(choice(ascii_uppercase) for i in range(4)))
        randSku= first + num + second
        print(randSku)
        return randSku
    if tipo == 'desc':
        description=(' '.join(choice(animals) for i in range(10)))
        print(description)
        return description
    if tipo == 'nombre':
        name_only=('-'.join(choice(animals) for i in range(2)))
        num = str(random.randint(-10,10))
        finalname=name_only+num
        print(finalname)
        return finalname
    if tipo =='categoria':
        initial=(''.join(choice(ascii_lowercase) for i in range(2)))
        animalword=name_only=('-'.join(choice(animals) for i in range(1)))
        finalcat=initial+animalword
        print(finalcat)
        return finalcat
class productCreation(unittest.TestCase):
    def setUp(self):
        global driver
        options = Options()##para guardar archivos sin preguntar
        options.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
        #driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\Users\\Username\\Downloads\\chromedriver.exe")
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
    ##Con sesión iniciada
    #Creación de producto
    def test_creacionProducto(self):
        driver.get("https://gobstore-qa.firebaseapp.com/michoselenium/")
        time.sleep(2)
        driver.get("https://gobstore-qa.firebaseapp.com/michoselenium/config/products")
        time.sleep(2)
        botonNuevoProducto=driver.find_element_by_xpath('//*[@id="newProduct"]')
        acceptcookies=driver.find_element_by_id('acceptCookieAgreement')
        if acceptcookies is not None:
            acceptcookies.click()
            print('Cookies aceptadas')
        if botonNuevoProducto is not None:
            print('Botón de producto nuevo encontrado')
            botonNuevoProducto.click()
        skuCampo= driver.find_element_by_xpath('//*[@id="inputProdSku"]')
        if skuCampo is not None:
            print('Generando sku random')
            skurand=randomGen('sku')
            skuCampo.send_keys(skurand)
            print('Escribiendo Sku')
        nombreCampo= driver.find_element_by_xpath('//*[@id="inputProdName"]')
        if nombreCampo is not None:
            print('Generando nombre random')
            namerand=randomGen('nombre')
            nombreCampo.send_keys(namerand)
            print('Escribiendo nombre')            
        categoriaCampo= driver.find_element_by_xpath('//*[@id="inputProdCategory"]')
        if categoriaCampo is not None:
            print('Generando categoria random')
            categorand=randomGen('categoria')
            categoriaCampo.send_keys(categorand)
            print('Escribiendo categoria')      
        min_input= driver.find_element_by_xpath('//*[@id="inputProdMin"]')
        if min_input is not None:
            min_input.send_keys('1')
            print('Mínimo: 1')
        max_input= driver.find_element_by_xpath('//*[@id="inputProdMax"]')
        if min_input is not None:
            max_input.send_keys('10')
            print('Máximo: 10')
        sectionselector= driver.find_element_by_class_name('ms-options-wrap')
        if sectionselector is not None:
            sectionselector.click()
            print('Se hace click en el selector de secciones')
            time.sleep(1)
        selectorVal= driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[3]/div[1]/div/div/ul/li')
        if selectorVal is not None:
            selectorVal.click()
            print('Se hace click en el valor "default"')
            time.sleep(1)
        #proveedor
        sectionselector2= driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[3]/div[2]/div')
        if sectionselector2 is not None:
            sectionselector2.click()
            print('Se hace click en el selector de secciones')
            time.sleep(1)
        selectorVal2= driver.find_element_by_id('ms-opt-2')
        if selectorVal2 is not None:
            selectorVal2.click()
            print('Se hace click en el valor "grillonbox"')
            time.sleep(1)
        descripcionCampo= driver.find_element_by_id('inputProdDesc')
        if descripcionCampo is not None:
            print('Calculando la descripcion del rango random')
            camporand=randomGen('desc')
            print('La descripción random generada es: ', camporand)
            descripcionCampo.send_keys(camporand)
            time.sleep(2)
        driver.execute_script("window.scrollTo(0,1200)")
        imgCampo=driver.find_element_by_class_name('addModelImgInput')
        if imgCampo is not None:
            print('Campo para imágenes encontrado')
            imgCampo.send_keys(os.path.abspath("C:/Users/DELL/Documents/Scripts de python/selenium_python/Automatic_Testing/pokemon1.png"))
            print('Se relacionó imagen de pokemon en el input')
            time.sleep(2)
        ancho=driver.find_element_by_id('inputProdX').send_keys('10')
        largo=driver.find_element_by_id('inputProdY').send_keys('10')
        alto=driver.find_element_by_id('inputProdZ').send_keys('10')
        grs=driver.find_element_by_id('inputProdWeight').send_keys('100')
        price=driver.find_element_by_id('inputProdBasePrice').send_keys('100')
        time.sleep(2)
        tagpropuesta=randomGen('nombre')
        tags=driver.find_element_by_id('inputKeywords').send_keys(tagpropuesta)
        time.sleep(1)
        unitTypeSelector=driver.find_element_by_id('unitType')
        if unitTypeSelector is not None:
            print('Selector para unidades encontrado')
            unitTypeSelector.click()
            print('Seleccionando un valor')
        selectorvalue1=driver.find_element_by_xpath('//*[@id="unitType"]/option[2]')
        if selectorvalue1 is not None:
            selectorvalue1.click()
            print('Click exitoso')
        saveButton=driver.find_element_by_id('saveProductChanges')
        if saveButton is not None:
            saveButton.click()
            print('Guardando...')
        time.sleep(15)
            

    def tearDown(self):
        driver.quit()
        


if __name__ == "__main__":
   unittest.main()
