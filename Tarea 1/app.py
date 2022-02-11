import tkinter as tk
from tkinter import filedialog as fd
import re as re
import sys

root = tk.Tk()
root.title('Abrir Archivo')
root.resizable(False, False)
root.geometry('300x300')

filetypes = [("Archivos de Entrada", "*.txt")]
def AbrirArchivo():
    nombreArchivo = fd.askopenfilename(filetypes=filetypes, title="Seleccione un archivo .txt")
    if nombreArchivo == '':
        return
    tf = open(nombreArchivo, 'r')
    contenido = tf.read()
    tf.close()
    patron = '[A-Z]{1}';
    print('Total de Letras:', len(re.findall(patron, contenido)));
    patron = '\d'
    print('Total de Dígitos:', len(re.findall(patron, contenido)));
    patron = '[^a-zA-Z\d\n\s|]';
    print('Total de Símbolos:', len(re.findall(patron, contenido)));
    sys.exit()


errmsg = 'Error!'
tk.Button(text='Click para seleccionar archivo de entrada', command=AbrirArchivo).pack(fill=tk.X)
tk.mainloop()

