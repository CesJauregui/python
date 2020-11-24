from tkinter import Tk
from tkinter import filedialog
from tkinter import Button
root=Tk()
def abrirFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:")#initialdir="C:" cambia la dirección de carpetas inicial
    print(fichero)

Button(root, text="abrir fichero", command=abrirFichero).pack()
root.mainloop()