import bs4
import os
import html5lib
from selenium import webdriver
import unittest
import pdfkit
import TESTmergeArchivos as ma #Archivo para ihacer el merge de Archivos HTML con Beautiful Soup
#Para desidentar: CTRL + SHIFT + BRACKET IZQ
names=[]
infos=[]
def durationToMin(duracionSegundos):
    mins=0
    if duracionSegundos<60:
        minsCalc=mins
        #secCalc=duracionSegundos
        restante = duracionSegundos
        return "Se calcularon: ", minsCalc, "minutos con ", secCalc, "segundos"
    while duracionSegundos >60.0 or duracionSegundos==60:
        print("segundos antes de  dividir: ",duracionSegundos)
        duracionSegundos=duracionSegundos-60
        print("segundos restantes",duracionSegundos)
        mins=mins+1
        if duracionSegundos<60:
            restante=duracionSegundos
            print("El restante es: ",restante)
            break
    minsCalc=mins
    secCalc=round(restante,2)
    print("Se calcularon: ", minsCalc, "minutos con ", secCalc, "segundos")
    return "Se calcularon: ", minsCalc, "minutos con ", secCalc, "segundos"     
def  main():
    ma.reportesJuntosClass().test_allReportsGenerating()
    global driver
    #driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
    driver = webdriver.Firefox(executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")
    driver.get("file:///C:/Users/DELL/Documents/Scripts%20de%20python/selenium_python/Automatic_Testing/allReports.html")
    viewButtons = driver.find_elements_by_css_selector(".btn-default")
    for button in viewButtons:
        button.click()
    nombresPruebas=driver.find_elements_by_css_selector("th")
    #nombresPruebas=driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/table/thead/tr/th[1]")
    for tags in nombresPruebas:
        if ("_") in tags.text or ("csv") in tags.text:
            print(tags.text)
            names.append(tags.text)
    with open('allReports_openlogs.html', 'w') as f:
        f.write(driver.page_source)
    resumenes=driver.find_elements_by_css_selector("td")
    for tagz in resumenes:
        if ("Duration") in tagz.text:
            print(tagz.text)
            infos.append(tagz.text)
    #print(names)
    #print(infos)
    passedIntTotal= 0
    totalIntTotal=0
    durationIntTotal=0
    passedList=[]
    totalList=[]
    durationList=[]
    errorList=[]
    namesList=[]
    for x in range(len(names)):
        totales=infos[x]
        total=totales[7:10].replace(',','')
        passedPos=infos[x].find("Pass:")
        #passed=(totales[passedPos+6:passedPos+8]).replace("[',]",'')
        passed=(totales[passedPos+6:passedPos+8]).replace(",",'')
        durationPos=infos[x].find("Duration:")
        durations=(totales[durationPos+9:durationPos+19]).replace("s",'')
        print('La prueba de nombre: ',names[x],'paso :' ,passed, 'de un total de: ',total,'pruebas', 'con una duracion total de: ', durations, 'segundos')
        print("TIPOS DE VARIABLES")
        print(type(passed))
        print(type(total))
        print(type(durations))
        print(passed)
        eachError=(int(total)-int(passed))
        namesList.append(names[x])
        passedList.append(passed)
        totalList.append(total)
        durationList.append(durations)
        errorList.append(eachError)
        passedIntTotal=passedIntTotal+int(passed)
        totalIntTotal=totalIntTotal+int(total)
        durationIntTotal=round(durationIntTotal+float(durations),2)
        totalIntError=totalIntTotal-passedIntTotal
    print("PASADAS TOTALES: ",passedIntTotal)
    print("TOTALES TOTALES: ",totalIntTotal)
    print("ERRORES TOTALES:",totalIntError)
    print("duracion TOTALES: ",durationIntTotal)
    print(durationToMin(durationIntTotal))
    print('arreglo de pasadas',passedList)
    print('arreglo de errores',errorList)
    print('arreglo de duraciones',durationList)
    print('arreglo totales',totalList)
    print('arreglo de nombres',namesList)
def tearDown(self):
    driver.quit()
if __name__ == "__main__":
    main()







