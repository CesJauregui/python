from tkinter import Tk
from tkinter import Entry
from tkinter import Frame
from tkinter import Label
from tkinter import Grid
from tkinter import Text
import tkinter.scrolledtext as scrolledtext
from tkinter import Button

raiz=Tk()

#Creación de frame
miFrame=Frame(raiz,width=1200, height=600)
#Empaquetamos al frame
miFrame.pack()

#-----------Label del nombre------------
nombreLabel=Label(miFrame)
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

#Creación del campo de texto
cuadroNombre=Entry(miFrame)
#Posición del campo de texto
#cuadroTexto.place(x=200,y=100)

#Posición del campo de texto con grid
cuadroNombre.grid(row=0, column=1, sticky="e", padx=10, pady=10)

#----------------Label del apellido------------
apellidoLabel=Label(miFrame,text="Apellidos:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

#Creación del campo de texto
cuadroApellido=Entry(miFrame)
#Posición del campo de texto
#cuadroTexto.place(x=200,y=100)

#Posición del campo de texto con grid
cuadroApellido.grid(row=1, column=1, sticky="e", padx=10, pady=10)

#---------------Label de contraseña-----------
contrasenaLabel=Label(miFrame,text="Contraseña:")
contrasenaLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

#Creación del campo de texto
cuadroContrasena=Entry(miFrame)
#Posición del campo de texto
#cuadroTexto.place(x=200,y=100)

#Posición del campo de texto con grid
cuadroContrasena.grid(row=2, column=1, sticky="e", padx=10, pady=10)
#Poner modo contraseña al campo de texto
cuadroContrasena.config(show="*")

#---------------Label de dirección-----------
direccionLabel=Label(miFrame,text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

#Creación del campo de texto
cuadroDireccion=Entry(miFrame)
#Posición del campo de texto
#cuadroTexto.place(x=200,y=100)

#Posición del campo de texto con grid
cuadroDireccion.grid(row=3, column=1, sticky="e", padx=10, pady=10)

#---------------Label de Comentarios---------
comentariosLabel=Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

#Creación del campo de texto extenso
#scroll para el campo de texto extense
scrollVert=scrolledtext.ScrolledText(miFrame, width=13, height=10)
scrollVert.grid(row=4, column=1)

#Creación de botón 
botonEnvio=Button(raiz, text="Enviar")
botonEnvio.pack()

raiz.mainloop()