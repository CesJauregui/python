from tkinter import Tk
from tkinter import Radiobutton
from tkinter import IntVar
from tkinter import Label

root=Tk()
varOption=IntVar()

def imprimir():
    if varOption.get()==1:
        etiqueta.config(text="Has elegido Masculino")
    else:
        etiqueta.config(text="Has elegido Femenino")

Label(root,text="Género: ").pack()
Radiobutton(root,text="Masculino", variable=varOption, value=1, command=imprimir).pack()
Radiobutton(root,text="Femenino", variable=varOption, value=2, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()