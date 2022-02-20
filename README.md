# LFP_PR_9017323

Lenguajes Formales y de Programación - Práctica

Lino Antonio García Vallejo.  
Carnet 9017323

Lenguajes Formales y de Programación - Sección B

Generador de Reportes de Ventas

Configuración de ambiente de desarrollo:

* Clonar el repositorio:
```git@github.com:linovallejo/LFP_PR_9017323.git```
* Instalar Python 3.8
* Instalar pip3

* Instalar paquetes requeridos

  * pip3 install tkinter
  * pip3 install console-menu
  * pip3 install -U matplotlib

* Ejecutar aplicación
  ```python3 app.py```

-----------------------------------------------------
  Problemas Conocidos
  * El paso 3 - Analizar no se ejecuta con exito en MacOS. Aparentemente una incompatibilidad entre las versiones de tkinter y matplotlib utilizadas.
  * EL paso 4 - Reporte no se ejecuta con éxito en Ubuntu. Aparentemente problemas de permisos para webbrowser. 
  * El siguiente mensaje es reportado a la consola en el paso 3 (cualquier plataforma).  Aparentemente es un problema derivado del hecho que matplotlib no es thread-safe (https://matplotlib.org/3.1.0/faq/howto_faq.html#working-with-threads).