from tkinter import Tk
from tkinter import Frame
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
raiz=Tk()
raiz.title("Calculadora CJ")
raiz.geometry("300x195")
raiz.resizable(0,0)

frame=Frame(raiz,bg="#102B42")
frame.pack()

operacion=""

reset_pantalla=False

resultado=0
#---------------Pantalla-------------
numero=StringVar()


pantalla=Entry(frame, textvariable=numero)
pantalla.grid(row=1,column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

#--------Captura de números------
def numeroPulsado(num):
	global operacion
	global reset_pantalla
	if reset_pantalla!=False:
		numero.set(num)
		reset_pantalla=False
	else:
		numero.set(numero.get()+num)

#----------Función suma--------------
def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado+=float(num)
    operacion="suma"
    reset_pantalla=True
    numero.set(resultado)

num1=0
contador_resta=0
def resta(num):
	global operacion
	global resultado
	global num1
	global contador_resta
	global reset_pantalla
	if contador_resta==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_resta==1:
			resultado=num1-float(num)
		else:
			resultado=float(resultado)-float(num)	
		numero.set(resultado)
		resultado=numero.get()
	contador_resta=contador_resta+1
	operacion="resta"
	reset_pantalla=True

#-------------funcion multiplicacion---------------------
contador_multi=0
def multiplica(num):
	global operacion
	global resultado
	global num1
	global contador_multi
	global reset_pantalla
	if contador_multi==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_multi==1:
			resultado=num1*float(num)
		else:
			resultado=float(resultado)*float(num)	
		numero.set(resultado)
		resultado=numero.get()
	contador_multi=contador_multi+1
	operacion="multiplicacion"
	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):
	global operacion
	global resultado
	global num1
	global contador_divi
	global reset_pantalla
	if contador_divi==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_divi==1:
			resultado=num1/float(num)
		else:
			resultado=float(resultado)/float(num)	
		numero.set(resultado)
		resultado=numero.get()
	contador_divi=contador_divi+1
	operacion="division"
	reset_pantalla=True

#--------- Función resultado---------
def resultadoTotal():
	global resultado
	global operacion
	global contador_resta
	global contador_multi
	global contador_divi
	if operacion=="suma":
		numero.set(resultado+float(numero.get()))
		resultado=0
	elif operacion=="resta":
		numero.set(float(resultado)-float(numero.get()))
		resultado=0
		contador_resta=0
	elif operacion=="multiplicacion":
		numero.set(float(resultado)*float(numero.get()))
		resultado=0
		contador_multi=0
	elif operacion=="division":
		numero.set(float(resultado)/float(numero.get()))
		resultado=0
		contador_divi=0
    
#---------------Fila 1---------------
boton7=Button(frame,text="7", width=3, command=lambda:numeroPulsado("7"),activebackground="grey")
boton7.grid(row=2, column=1, pady=5)
boton8=Button(frame,text="8", width=3, command=lambda:numeroPulsado("8"), activebackground="grey")
boton8.grid(row=2, column=2, pady=5)
boton9=Button(frame,text="9", width=3, command=lambda:numeroPulsado("9"), activebackground="grey")
boton9.grid(row=2, column=3, pady=5)
dividir=Button(frame,text="/", width=3,activebackground="grey", command=lambda:divide(numero.get()))
dividir.grid(row=2, column=4, pady=5)

#---------------Fila 2---------------
boton4=Button(frame,text="4", width=3, command=lambda:numeroPulsado("4"), activebackground="grey")
boton4.grid(row=3, column=1, pady=5)
boton5=Button(frame,text="5", width=3, command=lambda:numeroPulsado("5"), activebackground="grey")
boton5.grid(row=3, column=2, pady=5)
boton6=Button(frame,text="6", width=3, command=lambda:numeroPulsado("6"), activebackground="grey")
boton6.grid(row=3, column=3, pady=5)
multiplicar=Button(frame,text="*", width=3,  activebackground="grey", command=lambda:multiplica(numero.get()))
multiplicar.grid(row=3, column=4, pady=5)

#---------------Fila 3---------------
boton1=Button(frame,text="1", width=3, command=lambda:numeroPulsado("1"), activebackground="grey")
boton1.grid(row=4, column=1, pady=5)
boton2=Button(frame,text="2", width=3, command=lambda:numeroPulsado("2"), activebackground="grey")
boton2.grid(row=4, column=2, pady=5)
boton3=Button(frame,text="3", width=3, command=lambda:numeroPulsado("3"), activebackground="grey")
boton3.grid(row=4, column=3, pady=5)
restar=Button(frame,text="-", width=3, activebackground="grey", command=lambda:resta(numero.get()))
restar.grid(row=4, column=4, pady=5)

#---------------Fila 4---------------
limpiarPantalla=Button(frame,text="0", width=3, command=lambda:numeroPulsado("0"),activebackground="grey")
limpiarPantalla.grid(row=5, column=1, pady=5)
boton0=Button(frame,text=",", width=3,command=lambda:numeroPulsado("."), activebackground="grey")
boton0.grid(row=5, column=2, pady=5)
botonResultado=Button(frame,text="=", width=3, activebackground="grey", command=lambda:resultadoTotal())
botonResultado.grid(row=5, column=3, pady=5)
sumar=Button(frame,text="+", width=3,activebackground="grey", command=lambda:suma(numero.get()))
sumar.grid(row=5, column=4, pady=5)


raiz.mainloop()