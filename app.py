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

archivodatoscargado = False
archivoinstruccionescargado =  False
analisisrealizado = False
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
pathrelativograficas = f'../{carpetagraficas}'
extensionarchivografica = '.png'
carpetareportes = 'reportes'
plantillahtml = 'plantilla.html'
plantillahtmlpath = f'{os.getcwd()}/{carpetareportes}/{plantillahtml}'
instrucciones = {'nombre': 'Nombre:', 'grafica' : 'Grafica:', 'titulo':'Titulo:', 'titulox':'TituloX:', 'tituloy':'TituloY'}
productomasvendido = ''
productomenosvendido = ''
fullpathreportes = f'{os.getcwd()}/{carpetareportes}/'
nombreestudiante = 'Lino Antonio Garcia Vallejo'
carnetestudiante = '9017323'


def AbrirArchivoData():
    global mes, anio, errores, productos, ventas, archivodatoscargado, titulografica
    filetypes = [("Archivos de Data", "*.data")]
    root = tk
    archivodatos = fd.askopenfilename(filetypes=filetypes, title="Seleccione un archivo .data")
    if archivodatos is None or archivodatos == ():
        archivodatoscargado = False
        return
    else:
        tf = open(archivodatos, 'r')
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
                    utils.manejador_errores(mensaje='Mes invalido en el archivo de datos. Corrijalo y vuelva a cargar el archivo.')
                    archivodatoscargado = False
                    return
                if (linea[2].isdigit()):                
                    anio = linea[2]
                else:
                    utils.manejador_errores(mensaje='Anio invalido en el archivo de datos. Corrijalo y vuelva a cargar el archivo.')
                    archivodatoscargado = False
                    return
                if mes is None or anio is None:
                    utils.manejador_errores(mensaje='El Mes o el Anio es(son) invalido(s) en el archivo de datos. Corrijalo(s) y vuelva a cargar el archivo.')
                    archivodatoscargado = False
                    return
                    
                if mes is None and anio is None:
                    utils.manejador_errores(mensaje='Ambos Mes y Anio son invalidos en el archivo de datos. Corrijalos y vuelva a cargar el archivo.')
                    archivodatoscargado = False
                    return
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

    archivodatoscargado = True
    tf.close()


def AbrirArchivoInstrucciones():
    global nombrearchivografica, tipografica, titulografica, titulox, tituloy, archivoinstruccionescargado
    apertura = False
    cierre = False
    tiposgrafica = ['BARRAS','LINEAS','PIE']
    if not archivodatoscargado:
        utils.manejador_errores(mensaje='El archivo de datos aun no ha sido cargado. Utilice la opcion 1 en el menu para cargarlo y luego vuelva a intentar esta operacion.')
    else:
        filetypes = [("Archivos de Instruccionese", "*.lfp")]
        archivoinstrucciones = fd.askopenfilename(filetypes=filetypes, title="Seleccione un archivo .lfp")
        if archivoinstrucciones is None or archivoinstrucciones == ():
                archivoinstruccionescargado = False
                return
        else:
            tf = open(archivoinstrucciones, 'r')
            contenido = tf.readlines()
            for linea in contenido:
                if (simbolos['apertura_instrucciones'] in linea):
                    apertura = True
                if (instrucciones['nombre'] in linea):
                    nombrearchivografica = linea.split(':')[1].strip().replace('"','').replace(",","")
                elif (instrucciones['grafica'] in linea):
                    tipografica = linea.split(':')[1].strip().replace('"','').replace(',','').upper()
                elif (instrucciones['titulo'] in linea):
                    titulografica = linea.split(':')[1].strip().replace('"','').replace(",","")
                elif (instrucciones['titulox'] in linea):
                    titulox = linea.split(':')[1].strip().replace('"','').replace(",","")
                elif (instrucciones['tituloy'] in linea):
                    tituloy = linea.split(':')[1].strip().replace('"','').replace(",","")

                if (simbolos['cierre_instrucciones'] in linea):
                    cierre = True
                
            if not (apertura and cierre):
                utils.manejador_errores(mensaje='Formato de archivo de instrucciones es invalido. Corrijalo y vuelva a intentar esta operacion.')
                archivoinstruccionescargado = False
                return
            
            if not nombrearchivografica:
                utils.manejador_errores(mensaje='Nombre de archivo de grafica es un parametro obligatorio')
                archivoinstruccionescargado = False
                return

            if not tipografica:
                utils.manejador_errores(mensaje='Tipo de grafica es un parametro obligatorio')
                archivoinstruccionescargado = False
                return
            elif (tipografica not in tiposgrafica):
                utils.manejador_errores(mensaje='Tipo de grafica es invalido')
                archivoinstruccionescargado = False
                return

            archivoinstruccionescargado = True

            tf.close()




def Analizar():
    global fullpathgraficas, analisisrealizado, nombrearchivografica, extensionarchivografica
    if not archivodatoscargado and not archivoinstruccionescargado:
        utils.manejador_errores(mensaje='Debe cargar tanto el archivo de datos como el de instrucciones antes de Analizar. Utilice las opciones 1 y 2 en el menu para cargarlos y luego vuelva a intentar esta operacion.')
    else:
        fullpathgraficas = fullpathgraficas + nombrearchivografica + extensionarchivografica
        if tipografica == 'BARRAS':
            graphs.GraficaBarras(productos, ventas, fullpathgraficas)
        elif tipografica == 'LINEAS':
            graphs.GraficaLineas(productos, ventas, fullpathgraficas)
        elif tipografica == 'PIE':
            graphs.GraficaPie(productos, ventas, fullpathgraficas)
        analisisrealizado = True


def Reporte():
    global plantillahtmlpath, pathrelativograficas, nombrearchivografica, extensionarchivografica
    if not archivodatoscargado and not archivoinstruccionescargado and not analisisrealizado:
        utils.manejador_errores(mensaje='Debe cargar tanto el archivo de datos como el de instrucciones y analizar la informacion antes de generar el Reporte. Utilice las opciones 1, 2, y 3 en el menu para cargarlos y Analizar; luego vuelva a intentar esta operacion.')
    else:
        htmlapertura = "<tr><td>"
        htmlcolumna = "</td><td align='right'>"
        htmlcierre = "</td></tr>"
        htmltablaproductos = ''
        datos = {}
        datos = utils.combina_ordena_datos(productos, ventas)
        totalventas = float(sum(ventas))
        #totalventas = "%.2f" % totalventas
        totalventas = utils.format_float(totalventas)
        productomasvendido = datos[0]
        productomenosvendido = datos[-1]
        ventaproducto = 0
        for producto in datos:
            ventaproducto = utils.format_float(producto[1])
            htmltablaproductos = htmltablaproductos + htmlapertura + producto[0] + htmlcolumna + str(ventaproducto) + htmlcierre

        archivoplantilla = open(plantillahtmlpath)
        html = archivoplantilla.read()
        archivoplantilla.close()

        archivografica = f'{pathrelativograficas}/{nombrearchivografica}{extensionarchivografica}'

        html = html.replace('{nombreestudiante}', nombreestudiante)
        html = html.replace('{carnetestudiante}', carnetestudiante)
        html = html.replace('{tituloreporte}', titulografica)
        html = html.replace('{tablaventas}', htmltablaproductos)
        html = html.replace('{totalventas}', str(totalventas))
        html = html.replace('{productomasvendido}', productomasvendido[0])
        html = html.replace('{productomenosvendido}', productomenosvendido[0])
        html = html.replace('{archivografica}', archivografica)

        archivohtmlreporte = fullpathreportes + nombrearchivografica + ".html"

        if (os.path.exists(archivohtmlreporte)):
            os.remove(archivohtmlreporte)

        with open(archivohtmlreporte, 'w') as rep:
            try:
                rep.write(html)
            except:
                utils.manejador_errores(mensaje='No se pudo crear el reporte. Contacte a soporte tecnico ;-).')
                return False

        #webbrowser.open(archivohtmlreporte) 

menu = ConsoleMenu("Generador de Reportes de Ventas", exit_option_text="Salir")

menu_item = MenuItem("Menu Item")

function_item_cargar_datos = FunctionItem("Cargar Data", AbrirArchivoData)
function_item_cargar_instrucciones = FunctionItem("Cargar Instrucciones", AbrirArchivoInstrucciones)
function_item_analizar = FunctionItem("Analizar", Analizar)
function_item_reporte = FunctionItem("Reportes", Reporte)

menu.append_item(function_item_cargar_datos)
menu.append_item(function_item_cargar_instrucciones)
menu.append_item(function_item_analizar)
menu.append_item(function_item_reporte)

menu.show()

