#se llama al archivo donde están las funciones a reutilizar

#importar el módulo (primera forma)
#import funciones_matematicas

#otra forma de llamar a un archivo (segunda forma)
#manera de importar sólo un método(o lo que se quiera)
#from funciones_matematicas import suma #(resta o multiplicacion)

#manera de importar todo
from funciones_matematicas import *

#primera forma de utilización de las funciones
'''
funciones_matematicas.sumar(5,5)
funciones_matematicas.restar(10,5)
funciones_matematicas.multiplicar(5,4)
'''
#otra forma de utilizar las funciones
#
sumar(7,5)
restar(10,8)
multiplicar(6,4)