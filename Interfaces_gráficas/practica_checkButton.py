from tkinter import Tk
from tkinter import Checkbutton
from tkinter import IntVar
from tkinter import Label

root=Tk()
root.title("Práctica")
root.geometry("150x180")

costa=IntVar()
sierra=IntVar()
selva=IntVar()

def opcionesDestino():
    opcionSeleccionada=""
    if costa.get()==1:
        opcionSeleccionada+="Costa\n"
    if sierra.get()==1:
        opcionSeleccionada+="Sierra\n"
    if selva.get()==1:
        opcionSeleccionada+="Selva\n"
    opciones.config(text=f"Usted ha elegido:\n {opcionSeleccionada}")

Label(root,text="Eliga uno o más destinos: ").pack()

Checkbutton(root,text="Costa", variable=costa, onvalue=1, offvalue=0, command=opcionesDestino).pack()
Checkbutton(root,text="Sierra", variable=sierra, onvalue=1, offvalue=0, command=opcionesDestino).pack()
Checkbutton(root,text="Selva", variable=selva, onvalue=1, offvalue=0, command=opcionesDestino).pack()

opciones=Label(root)
opciones.pack()

root.mainloop()