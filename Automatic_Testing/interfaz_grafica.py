#import tkinter
import tkinter
from tkinter import *
import os
import time
from PIL import Image, ImageTk
#import tkMessageBox

ventana = tkinter.Tk()
ventana.title("Pruebas automatizadas Micho")
ventana.geometry("500x500") #para redimensionar la ventana
image = Image.open('cho2.jpg')
photo_image = ImageTk.PhotoImage(image)
label = tkinter.Label(ventana, image = photo_image)
label.pack() #Label de imagen de fondo
Lb1 = Listbox(ventana,selectmode=BROWSE,height=20)
Lb1.place(relx=0.0,rely=0.80,relwidth=0.2,relheight=0.7)
already= tkinter.Label(text="Pruebas corridas",bg="black",fg="white")
already.place(relx=0.0,rely=0.75,relwidth=0.2)


def  TDD(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_compraTDD.py')
    time.sleep(3)
    Lb1.insert(1,"Compra  TDC")
def  oxxo(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_compraOXXO.py')
    time.sleep(3)
    Lb1.insert(1,"Compra  OXXO")
def  spei(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_compraSPEI.py')
    time.sleep(3)
    Lb1.insert(1,"Compra  SPEI")
def  institucional(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_compraINSTITUCIONAL.py')
    time.sleep(3)
    Lb1.insert(1,"Compra Insitucional")
def  stock(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_stockRestore.py')
    time.sleep(3)
    Lb1.insert(1,"Stock Restore")
def  csv(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_exportCsvModule.py')
    time.sleep(3)
    Lb1.insert(1,"CSV Export")
def  dashboard(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_DashboardTest.py')
    time.sleep(3)
    Lb1.insert(1,"Dashboard Data")
def  htmlmerge(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('HTML_ScrapAndMerge.py')
    time.sleep(3)
    Lb1.insert(1,"HTML Merge")
def scrap_sendMail(nombreprueba):
    print("Corriendo: " + nombreprueba)
    os.system('scrap_summary_MIMEMAIL.py')
    time.sleep(3)
    Lb1.insert(1, "scrapSumMail")
botonTDD = tkinter.Button(ventana,text="Compra Tarjeta Crédito",bg="black",fg="white",command = lambda : TDD ("Tarjeta de crédito"))
botonTDD.place(relx=0.02,rely=0.05,relwidth=0.27,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Compra OXXO",bg="black",fg="white",command = lambda : oxxo ("OXXO"))
botonTDD.place(relx=0.3,rely=0.05,relwidth=0.2,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Compra SPEI",bg="black",fg="white",command = lambda : spei ("SPEI"))
botonTDD.place(relx=0.52,rely=0.05,relwidth=0.2,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Compra institucional",bg="black",fg="white",command = lambda : institucional ("Compra institucional"))
botonTDD.place(relx=0.73,rely=0.05,relwidth=0.27,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Agregar Stock",bg="black",fg="white",command = lambda : stock ("Stock Restore"))
botonTDD.place(relx=0.02,rely=0.35,relwidth=0.27,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Export CSV",bg="black",fg="white",command = lambda : csv ("Export CSV"))
botonTDD.place(relx=0.3,rely=0.35,relwidth=0.2,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Dashboard Data",bg="black",fg="white",command = lambda : dashboard ("Dashboard Data"))
botonTDD.place(relx=0.52,rely=0.35,relwidth=0.2,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="HTML Merge",bg="black",fg="white",command = lambda : htmlmerge ("HTML Merge"))
botonTDD.place(relx=0.73,rely=0.35,relwidth=0.27,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Scrap Sum Mail",bg="black",fg="white",command = lambda : scrap_sendMail ("Scrap Sum Mail"))
botonTDD.place(relx=0.02,rely=0.6,relwidth=0.27,relheight=0.1)
ventana.mainloop() #Registro de todo lo que sucede en la ventana
