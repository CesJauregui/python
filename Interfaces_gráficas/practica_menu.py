from tkinter import Tk
from tkinter import Menu
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo("Proyecto CJ","Practica de Python por CJ")

def avisoLicencia():
    messagebox.showwarning("Licencia","Proyecto open source")

def salirAplicacion():
    valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
    if valor=="yes":
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar","No es posible cerrar. Documento bloqueado")
    if valor==False:
        root.destroy()
        
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

menuArchivo=Menu(barraMenu,tearoff=0)#tearoff=0 es para que no apararezca el separador al inicio del menu
menuArchivo.add_command(label="Nuevo")
menuArchivo.add_command(label="Guardar")
menuArchivo.add_command(label="Guardar como...")
menuArchivo.add_separator()#Agrega un separador
menuArchivo.add_command(label="Cerrar", command=cerrarDocumento)
menuArchivo.add_command(label="Salir", command=salirAplicacion)

menuEdicion=Menu(barraMenu,tearoff=0)
menuEdicion.add_command(label="Copiar")
menuEdicion.add_command(label="Cortar")
menuEdicion.add_command(label="Pegar")

menuHerramienta=Menu(barraMenu,tearoff=0)

menuAyuda=Menu(barraMenu,tearoff=0)
menuAyuda.add_command(label="Licencia", command=avisoLicencia)
menuAyuda.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Edición", menu=menuEdicion)
barraMenu.add_cascade(label="Herramientas", menu=menuHerramienta)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
root.mainloop()

