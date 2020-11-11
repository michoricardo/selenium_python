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

#Funciones para llamar cada uno de los testsuite de las pruebas
def  TDD(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_TESTcompraTarjeta.py')
    time.sleep(3)
    Lb1.insert(1,"Compra  TDC")
def  oxxo(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_TESTcompraOxxo.py')
    time.sleep(3)
    Lb1.insert(1,"Compra  OXXO")
def  spei(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_TESTcompraSpei.py')
    time.sleep(3)
    Lb1.insert(1,"Compra  SPEI")
def  institucional(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_TESTcompraInstitucional.py')
    time.sleep(3)
    Lb1.insert(1,"Compra Insitucional")
def  stock(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_TESTresurtidoInventario.py')
    time.sleep(3)
    Lb1.insert(1,"Stock Restore")
def  csv(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_TESTcsvOrdenes.py')
    time.sleep(3)
    Lb1.insert(1,"Prueba CSV")
def  dashboard(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python trigger_testsuite_TESTdashboardCanal.py')
    time.sleep(3)
    Lb1.insert(1,"Dashboard Canal")
def  htmlmerge(nombreprueba):
    print("Corriendo:  " + nombreprueba)
    os.system('python TESTscrapEstadisticasPruebas.py')
    time.sleep(3)
    Lb1.insert(1,"Stats de pruebas")
def scrap_sendMail(nombreprueba):
    print("Corriendo: " + nombreprueba)
    os.system('python TESTscrapResumenEnvioMailAutomatico.py')
    time.sleep(3)
    Lb1.insert(1, "Resumen y Mail")
def metodo_pago(nombreprueba):
    print("Corriendo: " + nombreprueba)
    os.system('python trigger_testsuite_TESTagregarMetodosPago.py')
    time.sleep(3)
    Lb1.insert(1, "Agregar M de pago")
def dashboard_general(nombreprueba):
    print("Corriendo: " + nombreprueba)
    os.system('python trigger_testsuite_TESTdashboardGeneral.py')
    time.sleep(3)
    Lb1.insert(1, "Test GEN dashboard")
def nuevo_producto(nombreprueba):
    print("Corriendo: " + nombreprueba)
    os.system('python trigger_testsuite_TESTcreateNewProduct.py')
    time.sleep(3)
    Lb1.insert(1, "Crear nuevo prod")    
botonTDD = tkinter.Button(ventana,text="Tarjeta de crédito",bg="black",fg="white",command = lambda : TDD ("Tarjeta de crédito"))
botonTDD.place(relx=0.02,rely=0.05,relwidth=0.27,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="OXXO",bg="black",fg="white",command = lambda : oxxo ("OXXO"))
botonTDD.place(relx=0.3,rely=0.05,relwidth=0.2,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="SPEI",bg="black",fg="white",command = lambda : spei ("SPEI"))
botonTDD.place(relx=0.52,rely=0.05,relwidth=0.2,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="institucional",bg="black",fg="white",command = lambda : institucional ("Compra institucional"))
botonTDD.place(relx=0.73,rely=0.05,relwidth=0.27,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Resurtivo Inv",bg="black",fg="white",command = lambda : stock ("Resurtido Inv"))
botonTDD.place(relx=0.02,rely=0.35,relwidth=0.27,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Prueba CSV",bg="black",fg="white",command = lambda : csv ("Prueba CSV"))
botonTDD.place(relx=0.3,rely=0.35,relwidth=0.2,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Dashboard Canal",bg="black",fg="white",command = lambda : dashboard ("Dashboard Canal"))
botonTDD.place(relx=0.52,rely=0.35,relwidth=0.2,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Agregar M Pago",bg="black",fg="white",command = lambda : metodo_pago ("Metodo pago"))
botonTDD.place(relx=0.73,rely=0.35,relwidth=0.27,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Dashboard General",bg="black",fg="white",command = lambda : dashboard_general ("Dashboard General"))
botonTDD.place(relx=0.02,rely=0.6,relwidth=0.27,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Nuevo Producto",bg="black",fg="white",command = lambda : nuevo_producto ("Nuevo Producto"))
botonTDD.place(relx=0.3,rely=0.6,relwidth=0.2,relheight=0.1)
#últimas siempre
botonTDD = tkinter.Button(ventana,text="Stats Pruebas",bg="black",fg="white",command = lambda : htmlmerge ("Stats de pruebas"))
botonTDD.place(relx=0.22,rely=0.9,relwidth=0.2,relheight=0.1)
botonTDD = tkinter.Button(ventana,text="Resumen/Mail",bg="black",fg="white",command = lambda : scrap_sendMail ("Resumen y mail"))
botonTDD.place(relx=0.43,rely=0.9,relwidth=0.27,relheight=0.1)
ventana.mainloop() #Registro de todo lo que sucede en la ventana
