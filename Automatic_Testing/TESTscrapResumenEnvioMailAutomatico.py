import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import bs4
import os
import html5lib
from selenium import webdriver
import unittest
import pdfkit
#Para desidentar: CTRL + SHIFT + BRACKET IZQ
names=[]
infos=[]
def durationToMin(duracionSegundos):
    mins = 0
    if duracionSegundos <60:
        restante = duracionSegundos
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
    print(minsCalc, "minutos con ", secCalc, "segundos")
    return minsCalc, "minutos con ", secCalc, "segundos"
def  main():
    global driver
    #password = input("Escribe tu contraseña por favor (del mail quien envía: ")
    password='C0business.'
    #driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
    driver = webdriver.Firefox(executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")
    driver.get("file:///C:/Users/DELL/Documents/Scripts%20de%20python/selenium_python/Automatic_Testing/allReports.html")
    viewButtons = driver.find_elements_by_css_selector(".btn-default")
    for button in viewButtons:
        button.click()
    nombresPruebas=driver.find_elements_by_css_selector("th")
    for tags in nombresPruebas:
        #if ("_") in tags.text or ("csv") in tags.text:
        if ("TEST") in tags.text or ("csv") in tags.text:
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
    emailfrom = "sistemasgobstore@gmail.com"
    emailto = "axolotlcode@gmail.com"
    fileToSend = "allreports.html"
    username = "sistemasgobstore@gmail.com"
    #password = input("Escribe tu contraseña por favor: ")

    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = "Resultados de pruebas automatizadas"
    msg.preamble = "Pruebas automatizadas de python"
    #Texto inicial
    text = "Espero que estés teniendo un excelente día, te dejo un resumen de las pruebas automatizadas\n"
    estiloTabla = 'border: 1px solid black'
    #Tabla 1 en HTML
    strTable = "<html><table style='background-color:#50B7FF; border-style:dashed;'><tr><th>Nombre de prueba</th><th>Pruebas corridas</th><th>Pasadas</th><th>Errores</th><th>Duración (Seg)</th></tr>"
    for i in range(0,len(namesList)):
     strRW = "<tr style='border-style:dashed;'><td>"+str(namesList[i])+ "</td><td>"+str(totalList[i])+"</td><td>"+str(passedList[i])+"</td><td>"+str(errorList[i])+"</td><td>"+str(durationList[i])+"</td></tr>"
     strTable = strTable+strRW
    strTable = strTable+"</table><br></html>"
     #Texto de resumen
    textSummary = "A continuación, te comparto el resumen de todas las pruebas\n"
     #Tabla de resumenes en HHTML
    summaryTable = "<html><table style='background-color:#0083DE; border-style:dashed;'><th>Total de pruebas</th><th>Total de pruebas pasadas</th><th>Total de Errores</th><th>Duración Total</th></tr>"
    summaryStrRW = "<tr><td>"+str(totalIntTotal)+ "</td><td>"+str(passedIntTotal)+"</td><td>"+str(totalIntError)+"</td><td>"+str(durationToMin(durationIntTotal))+"</td></tr>"
    summaryTable = summaryTable+summaryStrRW
    summaryTable = summaryTable + "</table><br></html>"
    #Imagen chistosa
    imagen_firma='<html><body><img src="https://styles.redditmedia.com/t5_3kq89/styles/profileIcon_urodwn335xc01.jpg?width=256&height=256&crop=256:256,smart&s=247ffc7c78c428cf37769d6f5181b531c9866507" alt="chocho"><br><h3><i><b>Ricardo García <i></b>Software Tester</h3></body></html>'
    # ponemos las variables de MIME como texto plano y como html para poderle hacer attach al .msg
    part1 = MIMEText(text, 'plain')
    part2=MIMEText(strTable,'html')
    part3=MIMEText(textSummary,'plain')
    part4=MIMEText(summaryTable,'html')
    part5=MIMEText(imagen_firma,'html')
    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)
    msg.attach(part1)
    msg.attach(part2)
    msg.attach(part3)
    msg.attach(part4)
    msg.attach(part5)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username,password)
    #el sendmail tiene tres argumentos (de donde sale, a donde va y el mensaje)
    server.sendmail(emailfrom, emailto, msg.as_string())

    print("mensaje enviado")
    server.quit()
def tearDown(self):
    driver.quit()
if __name__ == "__main__":
    main()

