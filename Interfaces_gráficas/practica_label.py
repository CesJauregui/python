from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import PhotoImage
root=Tk()

#Creación de frame
miFrame=Frame(root, width=500, height=400)
miFrame.pack()

#Creación del label de imagen y Posición del label
miImagen=PhotoImage(file="../Python/Interfaces_gráficas/logo.png")
Label(miFrame, image=miImagen).place(x=100,y=100)

#Creación del label de texto y Posición del label
Label(miFrame,text="Hola mundo",fg="red", font=("Comic Sans MS",18)).place(x=100,y=200)

root.mainloop()