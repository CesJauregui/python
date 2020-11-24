'''
¡Documentación importante!: https://docs.python.org/3.3/library/tk.html

línea para importar toda la libreria tkinter
from tkinter import *
Si se importara toda la libreria, daría error (Visual Studio Code)
'''
#Aquí se utiliza sólo estas dos
from tkinter import mainloop
from tkinter import Tk
from tkinter import Frame

#Construcción de la raíz
raiz=Tk()

#Poner título a la ventana
raiz.title("Ventana de pruebas")

#redimencionar la ventana
#resizable sólo permite parámetros booleanos(True o False) que es igual a (1 y 0)
raiz.resizable(1,1) #resizable(width,height)

#icono en la ventana
raiz.iconbitmap("../Python/Interfaces_gráficas/logo.ico")

#Ancho y alto de la ventana
raiz.geometry("650x350")

#color de fondo de la ventana
raiz.config(bg="skyblue")

#-------------------Frame-----------------------
#Creación del Frame
miFrame=Frame()
#Dar la posición del frame (left,right,bottom,top)
miFrame.pack(side="right", anchor="s") #anchor: recibe "n" o "s" (arriba o abajo)

#Rellenado de todo el frame
#miFrame.pack(fill="both", expand="True")

#Visualizar el frame
miFrame.config(bg="red")

#Dar tamaño al frame
miFrame.config(width="650", height="350")

#Dar un borde
miFrame.config(bd="20")#grosor del borde
miFrame.config(relief="groove")

#cambiar cursor
miFrame.config(cursor="pirate")

#Ejecución del programa
raiz.mainloop()