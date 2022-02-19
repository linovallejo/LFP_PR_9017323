from tkinter import messagebox as mb
import re

def is_float(n):
    try:
        float(n) 
    except ValueError:
        return False
    return True

def combina_ordena_datos(productos, ventas):
    dict = {}
    for p in productos:
	    dict[p] = (ventas[productos.index(p)])
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict

def manejador_errores(mensaje, iswarning=False):
    titulo = ''
    if iswarning:
        titulo = 'Precaucion'
        mb.showwarning(titulo, mensaje)
    else:
        titulo='Error'
        mb.showerror(titulo,mensaje)
    return

def format_float(s):
    s = "%.2f" % float(s)
    integer, decimal = s.split(".")
    integer = re.sub(r"\B(?=(?:\d{3})+$)", ",", integer)
    return integer + "." + decimal
