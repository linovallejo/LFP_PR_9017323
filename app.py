# Import the necessary packages
from tokenize import Number
from consolemenu import *
from consolemenu.items import *
import tkinter as tk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
from decimal import *

meses = {'ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE'}
simbolos = {'dos_puntos': ':', 'igual':'=', 'parentesis_abierto':'(', 'parentesis_cerrado': ')', 'corchete_abierto':'[', 'comilla':'"', 'coma':',', 'punto_coma':';', 'corchete_cerrado':']'}
mes = None
anio = None
errores = []
productos = []
ventas = []

def is_float(n):
    try:
        float(n) 
    except ValueError:
        return False
    return True

def AbrirArchivoData():
    filetypes = [("Archivos de Data", "*.data")]
    nombreArchivo = fd.askopenfilename(filetypes=filetypes, title="Seleccione un archivo .data")
    if nombreArchivo == '':
        return
    tf = open(nombreArchivo, 'r')
    contenido = tf.readlines()
    for linea in contenido:
        precio = 0
        cantidad = 0
        monto_ventas = 0
        if ((simbolos['dos_puntos'] in linea) and (simbolos['igual']) and (simbolos['parentesis_abierto'])):
            linea = linea.split()
            if (linea[0].upper() in meses):
                mes = linea[0].upper()
            else:
                errores.append('Mes invalido')
            if (linea[2].isdigit()):                
                anio = linea[2]
            else:
                errores.append('Anio invalido')
            if mes is None or anio is None:
                errores.append('Mes o anio son invalidos')
            if mes is None and anio is None:
                errores.append('Ambos mes y anio son invalidos')
        
        if ((simbolos['corchete_abierto'] in linea) and (simbolos['punto_coma'] in linea) and (simbolos['corchete_cerrado'] in linea)):
            linea = linea.replace(simbolos['comilla'],'')
            linea = linea.replace(simbolos['corchete_abierto'],'')
            linea = linea.replace(simbolos['corchete_cerrado'],'')
            linea = linea.replace(simbolos['punto_coma'],'')
            linea = linea.split(simbolos['coma'])
            if linea[0].strip() != '':
                productos.append(linea[0].strip())
            else:
                errores.append('Nombre de producto faltante')
            
            if linea[1].strip() == '':
                precio = 0
            else:
                if is_float(linea[1].strip()):
                    precio = float(linea[1].strip())
                else:
                    errores.append('Precio invalido')
            if linea[2].strip() == '':
                cantidad = 0
            else:
                if linea[2].strip().isnumeric():
                    cantidad = int(linea[2].strip())
                else:
                    errores.append('Cantidad invalido')

            monto_ventas = precio * float(cantidad)
            
            ventas.append(round(monto_ventas,2))


    tf.close()

def AbrirArchivoInstrucciones():
    filetypes = [("Archivos de Instruccionese", "*.lfp")]
    nombreArchivo = fd.askopenfilename(filetypes=filetypes, title="Seleccione un archivo .lfp")
    if nombreArchivo == '':
        return
    tf = open(nombreArchivo, 'r')
    contenido = tf.read()
    tf.close()


def Analizar():
    print('Analizar')

def GraficaPie():
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

menu = ConsoleMenu("Generador de Reportes de Ventas", exit_option_text="Salir")

menu_item = MenuItem("Menu Item")

function_item_cargar_datos = FunctionItem("Cargar Data", AbrirArchivoData)
function_item_cargar_instrucciones = FunctionItem("Cargar Instrucciones", AbrirArchivoInstrucciones)
function_item_analizar = FunctionItem("Analizar", Analizar)
function_item_grafica = FunctionItem("Grafica", GraficaPie)

menu.append_item(function_item_cargar_datos)
menu.append_item(function_item_cargar_instrucciones)
menu.append_item(function_item_analizar)
menu.append_item(function_item_grafica)

menu.show()

