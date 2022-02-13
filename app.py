# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
import tkinter as tk
from tkinter import filedialog as fd


def AbrirArchivoData():
    filetypes = [("Archivos de Data", "*.data")]
    nombreArchivo = fd.askopenfilename(filetypes=filetypes, title="Seleccione un archivo .data")
    if nombreArchivo == '':
        return
    tf = open(nombreArchivo, 'r')
    contenido = tf.read()
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

menu = ConsoleMenu("Generador de Reportes de Ventas", exit_option_text="Salir")

menu_item = MenuItem("Menu Item")

function_item_cargar_datos = FunctionItem("Cargar Data", AbrirArchivoData)
function_item_cargar_instrucciones = FunctionItem("Cargar Instrucciones", AbrirArchivoInstrucciones)
function_item_analizar = FunctionItem("Analizar", Analizar)

menu.append_item(function_item_cargar_datos)
menu.append_item(function_item_cargar_instrucciones)
menu.append_item(function_item_analizar)

menu.show()

