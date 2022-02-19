# Import the necessary packages
from distutils.log import error
from fileinput import filename
from hashlib import new
import this
from tokenize import Number
from consolemenu import *
import consolemenu
from consolemenu.items import *
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import utils
import webbrowser
import os
import graphs

meses = {'ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE'}
simbolos = {'dos_puntos': ':', 'igual':'=', 'parentesis_abierto':'(', 'parentesis_cerrado': ')', 'corchete_abierto':'[', 'comilla':'"', 'coma':',', 'punto_coma':';', 'corchete_cerrado':']','apertura_instrucciones':'<¿','cierre_instrucciones':'?>'}
mes = None
anio = None
errores = []
productos = []
ventas = []
nombrearchivografica = ''
tipografica = ''
titulografica=''
titulox=''
tituloy=''
carpetagraficas = 'imagenes'
fullpathgraficas = f'{os.getcwd()}/{carpetagraficas}/'
extensionarchivografica = '.png'
carpetareportes = 'reportes'
plantillahtml = 'plantilla.html'
plantillahtmlpath = f'{os.getcwd()}/{carpetareportes}/{plantillahtml}'
instrucciones = {'nombre': 'Nombre:', 'grafica' : 'Grafica:', 'titulo':'Titulo:', 'titulox':'Titulox:', 'tituloy':'Tituloy'}
productomasvendido = ''
productomenosvendido = ''
fullpathreportes = f'{os.getcwd()}/{carpetareportes}/'
nombreestudiante = 'Lino Antonio Garcia Vallejo'
carnetestudiante = '9017323'
errorcritico = False


def AbrirArchivoData():
    global mes, anio, errores, productos, ventas
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
            if mes is not None and anio is not None:
                titulografica = f'Reporte de Ventas {mes}-{anio} '
        
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
                if utils.is_float(linea[1].strip()):
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
    contenido = tf.readlines()
    for linea in contenido:
        if (simbolos['apertura_instrucciones'] in linea):
            apertura = True
            if (instrucciones['nombre'] in linea):
                nombrearchivografica = linea.split(':')[1].strip().replace('"','')
            elif (instrucciones['grafica'] in linea):
                tipografica = linea.split(':')[1].strip().replace('"','').upper()
            elif (instrucciones['titulo'] in linea):
                titulografica = linea.split(':')[1].strip().replace('"','')
            elif (instrucciones['titulox'] in linea):
                titulox = linea.split(':')[1].strip().replace('"','')
            elif (instrucciones['tituloy'] in linea):
                tituloy = linea.split(':')[1].strip().replace('"','')

        if (simbolos['cierre_instrucciones'] in linea):
            cierre = True
        
        if not (apertura and cierre):
            errores.append('Formato de archivo de instrucciones es invalido')
            errorcritico = True
    
    if not nombrearchivografica:
        errores.append('Nombre de archivo de grafica es un parametro obligatorio')
        errorcritico = True

    if not tipografica:
        errores.append('Tipo de grafica es un parametro obligatorio')
        errorcritico = True
    elif (tipografica != 'BARRAS' and tipografica != 'LINEAS' and tipografica != 'PIE'):
        errores.append('Tipo de grafica invalido')
        errorcritico = True


    tf.close()


        

def Reporte():
    if not errorcritico:
        #filename = "file:///home/linovallejo/Projects/LFP_PR_9017323/report.html"
        #webbrowser.open(fullpathreportes)
        htmlapertura = """<div class="row">
                    <div class="cell">"""
        htmlcolumna = """</div><div class="cellright">"""
        htmlcierre = """
                    </div></div>"""
        htmltablaproductos = ''
        datos = {}
        datos = utils.combina_ordena_datos(productos, ventas)
        productomasvendido = datos[0]
        productomenosvendido = datos[-1]
        for producto in datos:
            htmltablaproductos = htmltablaproductos + htmlapertura + producto[0] + htmlcolumna + producto[1] + htmlcierre

        archivoplantilla = open(plantillahtmlpath)
        html = archivoplantilla.read()
        archivoplantilla.close()

        html = html.replace('{nombreestudiante}', nombreestudiante)
        html = html.replace('{carnetestudiante}', carnetestudiante)
        html = html.replace('{tituloreporte}', titulografica)
        html = html.replace('{tablaventas}', htmltablaproductos)
        html = html.replace('{productomasvendido}', productomasvendido)
        html = html.replace('{productomenosvendido}', productomenosvendido)

        archivohtmlreporte = fullpathreportes + nombrearchivografica + ".html"

        if (os.path.exists(archivohtmlreporte)):
            os.remove(archivohtmlreporte)

        with open(archivohtmlreporte, 'w') as rep:
            try:
                rep.write(html)
            except:
                errores.append('No se pudo crear el reporte. Contacte a soporte tecnico ;-).')
                return False

        webbrowser.open(archivohtmlreporte) 


def Analizar():
    if not errorcritico:
        fullpathgraficas = fullpathgraficas + nombrearchivografica + extensionarchivografica
        if tipografica == 'BARRAS':
            graphs.GraficaBarras(productos, ventas)
        elif tipografica == 'LINEAS':
            graphs.GraficaLineas(productos, ventas)
        elif tipografica == 'PIE':
            graphs.GraficaPie(productos, ventas)


menu = ConsoleMenu("Generador de Reportes de Ventas", exit_option_text="Salir")

menu_item = MenuItem("Menu Item")

def EscribirConsola():
    #menu.screen.println('Testing')
    #consolemenu.clear_terminal
    #consolemenu.Screen.clear
    #mb.showerror('Que pumas')
    consolemenu.PromptUtils.clear()
    #consolemenu.PromptUtils.validate_input


function_item_cargar_datos = FunctionItem("Cargar Data", AbrirArchivoData)
function_item_cargar_instrucciones = FunctionItem("Cargar Instrucciones", AbrirArchivoInstrucciones)
function_item_analizar = FunctionItem("Analizar", Analizar)
function_item_reporte = FunctionItem("Reportes", EscribirConsola)

menu.append_item(function_item_cargar_datos)
menu.append_item(function_item_cargar_instrucciones)
menu.append_item(function_item_analizar)
menu.append_item(function_item_reporte)

menu.show()

