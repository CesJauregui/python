from tkinter import Tk
from tkinter import Button
from tkinter import Menu
from tkinter import Label
from tkinter import Text
from tkinter import Grid
from tkinter import Frame
from tkinter import Entry
import tkinter.scrolledtext as scrolledtext
from tkinter import StringVar
import sqlite3
from tkinter import messagebox
import traceback

root=Tk()
root.title("Práctica CRUD")
root.geometry("300x305")

frame=Frame(root)
frame.pack()

menu=Menu(frame)
root.config(menu=menu, width=450,height=700)

#--------------FUNCIONES-----------------
#------------Funciones GUI---------------
def salirApp():
    mensaje=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
    if mensaje=="yes":
        root.destroy()

def limpiarCampos():
    global idParam
    global nombreParam
    global apellidoParam
    global direccionParam
    global usuarioParam
    global passw
    idParam.set("")
    nombreParam.set("")
    apellidoParam.set("")
    direccionParam.set("")
    usuarioParam.set("")
    passw.set("")

#---------Funciones Base de datos-----------
def conectar():
    conect=sqlite3.connect("usuarios")
    cursor=conect.cursor()
    try:
        cursor.execute('''
           CREATE TABLE users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100),
                apellido VARCHAR(100),
                direccion VARCHAR(100),
                usuario VARCHAR(100),
                passwor VARCHAR(100)
            )
            ''')
        messagebox.showinfo("Conexión", "Conexión exitosa")
        conect.commit()
    except:
        messagebox.showwarning("Conexión","La base de datos ya existe")
    conect.close()

def agregarUsuario(nombre,apellido,direccion,usuario,passw):
    conect=sqlite3.connect("usuarios")
    cursor=conect.cursor()
    try:
        cursor.execute("INSERT INTO users VALUES(NULL,?,?,?,?,?)",(nombre,apellido,direccion,usuario,passw))
        messagebox.showinfo("Creación", "Se creó un usuario nuevo")
        limpiarCampos()
        conect.commit()
    except:
        print("No se pudo crear un nuevo usuario")
        traceback.print_exc()
        conect.rollback()
    conect.close()

def leerUsuario(idu):
    conect=sqlite3.connect("usuarios")
    cursor=conect.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE id = ? ",(idu,))
        usuarios=cursor.fetchall()
        global nombreParam
        global apellidoParam
        global direccionParam
        global usuarioParam
        global passw
        if usuarios:
            for usuario in usuarios:
                nombreParam.set(usuario[1])
                apellidoParam.set(usuario[2])
                direccionParam.set(usuario[3])
                usuarioParam.set(usuario[4])
                passw.set(usuario[5])
        else:
            messagebox.showinfo("Mensaje","No se encontraron registros")
        print(usuarios)
    except:
        messagebox.showerror("Mensaje","No se encontraron registros")
        traceback.print_exc()
    conect.close()

def actualizarUsuarios():
    conect=sqlite3.connect("usuarios")
    cursor=conect.cursor()
    try:
        global nombreParam
        global apellidoParam
        global direccionParam
        global usuarioParam
        global passw
        cursor.execute("UPDATE users set nombre = ?, apellido = ?, direccion = ?, usuario = ?, passwor = ? WHERE id = ?",(str(nombreParam.get()),str(apellidoParam.get()),str(direccionParam.get()),str(usuarioParam.get()),str(passw.get()),str(idU.get())))
        messagebox.showinfo("Mensaje","Se actualizó el registro")
        conect.commit()
    except:
        print("No se pudo actualizar el registro")
        traceback.print_exc()
    conect.close()

def borrarUsuario(idu):
    conect=sqlite3.connect("usuarios")
    cursor=conect.cursor()
    try:
        mensaje=messagebox.askquestion("Borrar Usuario","¿Seguro que quiere eliminar a este usuario?")
        if mensaje=="yes":
            cursor.execute("DELETE FROM users WHERE id = ?",idu)
            limpiarCampos()
            messagebox.showwarning("Información","Se eliminó el registro")
        conect.commit()
    except:
        print("No se pudo eliminar el registro")
        traceback.print_exc()
    conect.close()

#-----------------MENU-------------------
#-------------Pestaña BBDD---------------
menuBBDD=Menu(frame, tearoff=0)
menuBBDD.add_command(label="Conectar", command=conectar)
menuBBDD.add_command(label="Salir", command=salirApp)

#-------------Pestaña Borrar-------------
menuBorrar=Menu(frame,tearoff=0)
menuBorrar.add_command(label="Limpiar campos", command=limpiarCampos)

#-------------Pestaña CRUD---------------
menuCRUD=Menu(frame,tearoff=0)
menuCRUD.add_command(label="Crear",command=lambda:agregarUsuario(str(nombree.get()),str(apellido.get()),str(direccion.get()),str(usuario.get()),str(password.get())))
menuCRUD.add_command(label="Mostrar",command=lambda:leerUsuario(idU.get()))
menuCRUD.add_command(label="Editar",command=lambda:actualizarUsuarios())
menuCRUD.add_command(label="Eliminar",command=lambda:borrarUsuario(idU.get()))

#-------------Pestaña Ayuda---------------
menuAYUDA=Menu(frame, tearoff=0)
menuAYUDA.add_command(label="Licencia")

#----------Opciones de pestañas-----------
menu.add_cascade(label="BBDD", menu=menuBBDD)
menu.add_cascade(label="Borrar", menu=menuBorrar)
menu.add_cascade(label="CRUD", menu=menuCRUD)
menu.add_cascade(label="Ayuda", menu=menuAYUDA)

#---------------Etiquetas-----------------
idLabel=Label(frame,text="ID:")
idLabel.grid(row=0, column=0, sticky="w",padx=10, pady=10, columnspan=2)
nombreLabel=Label(frame,text="Nombre:")
nombreLabel.grid(row=1,column=0, sticky="w",padx=10, pady=10, columnspan=2)
apellidosLabel=Label(frame,text="Apellidos:")
apellidosLabel.grid(row=2,column=0, sticky="w",padx=10, pady=10, columnspan=2)
direccionLabel=Label(frame,text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="w",padx=10, pady=10, columnspan=2)
usuarioLabel=Label(frame,text="Nombre Usuario:")
usuarioLabel.grid(row=4, column=0, sticky="w",padx=10, pady=10, columnspan=2)
passwordLabel=Label(frame,text="Contraseña:")
passwordLabel.grid(row=5, column=0, sticky="w",padx=10, pady=10, columnspan=2)

#-------------Campos de texto--------------
idParam=StringVar()
idU=Entry(frame,width=8, textvariable=idParam)
idU.grid(row=0, column=2, columnspan=2)

nombreParam=StringVar()
nombree=Entry(frame, textvariable=nombreParam)
nombree.grid(row=1, column=2, columnspan=2)

apellidoParam=StringVar()
apellido=Entry(frame, textvariable=apellidoParam)
apellido.grid(row=2, column=2, columnspan=2)

direccionParam=StringVar()
direccion=Entry(frame, textvariable=direccionParam)
direccion.grid(row=3, column=2, columnspan=2)

usuarioParam=StringVar()
usuario=Entry(frame, textvariable=usuarioParam)
usuario.grid(row=4, column=2, columnspan=2)

passw=StringVar()
password=Entry(frame, textvariable=passw)
password.grid(row=5, column=2, columnspan=2)
password.config(show="*")

#----------------Botones------------------

crear=Button(frame,text="Crear",command=lambda:agregarUsuario(str(nombree.get()),str(apellido.get()),str(direccion.get()),str(usuario.get()),str(password.get())))
crear.grid(row=6,column=0,padx=5, pady=10)
mostrar=Button(frame,text="Mostrar",command=lambda:leerUsuario(idU.get()))
mostrar.grid(row=6,column=1,padx=5, pady=10)
editar=Button(frame,text="Editar",command=lambda:actualizarUsuarios())
editar.grid(row=6,column=2,padx=5, pady=10)
eliminar=Button(frame,text="Eliminar",command=lambda:borrarUsuario(idU.get()))
eliminar.grid(row=6,column=3,padx=5, pady=10)

root.mainloop()