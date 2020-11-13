#For con listas
for i in [1,2,3]:
    print(i)

for i in ["Primavera","Verano","Otoño","Invierno"]:
    print(i)

#Strings, range(), notaciones especiales con print
for i in ["Ingenieria","Sistemas",3]:
    #end hace que todo el resultado aparezca en una sola linea. Se puede dar espacios, comas, etc (dentro de las comillas)
    print("Hola",end=" ")

email=False
miEmail=input("Introduce tu dirección de email: ")
for i in miEmail:
    if (i=="@"):
        email=True
if email:
    print("Email es correcto")
else:
    print("Email es incorrecto")

#range()    
for i in range(5):
    #f es para utilizar notaciones especiales, funciones tipo F. Sirve para unir texto con variables
    print(f"Hola {i}")

# while
i=1
while i <=10:
    print("Ejecución " + str(i))
    i=i+1
print("Fin ejecución")

#Otro ejemplo de while
edad=int(input("Introduzca su edad: "))
while edad<5 or edad>100:
    print("la edad debe ser mayor que 5 o menor a 100")
    edad=int(input("Introduce tu edad: "))
print("Gracias por participar :)")
print("Tu edad es: " + str(edad))

#Otro ejemplo de while
import math
print("Programa de calculo de raíz cuadrada")
print("Tienes 3 intentos")
numero=int(input("Introduce un número por favor: "))
intentos=0
while numero<0:
    print("No se puede hallar la raíz de un número negativo. Intento " + str(intentos+1))
    if intentos==2:
        print("Has consumido demasiados intentos, El programa ha finalizado")
        break
    numero=int(input("Introduce un número por favor: "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    #math es una clase que se tiene que importar
    #sqrt es un función para sacar la raíz cuadrada de un número
    solucion=math.sqrt(numero)
    print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))

# Continue, pass, else
for letra in "Python":
    if letra=="h":
        continue
    # "continue" excluye la letra h y donde aparace el print
    print("Viendo la letra: " + letra)

#Ejemplo de continue: validar nombre sin contar el espacio
nombre="Cesar Jauregui"
contador=0
for i in nombre:
    if i==" ":
        continue
    contador+=1
print(contador)


