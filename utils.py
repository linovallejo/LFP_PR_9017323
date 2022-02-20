from tkinter import messagebox as mb
import re

def is_float(n):
    try:
        float(n) 
    except ValueError:
        return False
    return True

def is_positive_integer(n):
    try:
        val = int(n)
        if int(n) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False 

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

def format_money(s):
    s = "%.2f" % float(s)
    integer, decimal = s.split(".")
    integer = re.sub(r"\B(?=(?:\d{3})+$)", ",", integer)
    return 'Q. ' + integer + "." + decimal
