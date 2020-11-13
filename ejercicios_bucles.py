#Ejercicio 1: Crea un programa que muestre los números impares del 1 al 100. Los números deberán aparecer una al lado del otro sin salto de línea
for i in range(1,100,2):
    print(i, end=" ")

#Ejercicio 2: Crea un programa que pida por teclado introducir una contraseña. La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta, el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña errónea”
contrasena=input("Introduzca su contraseña: ")
contador=0
for i in range(len(contrasena)):
    if contrasena[i]==" ":
        contador=1
if len(contrasena)<8 or contador>0:
    print("Contraseña errónea")
else:
    print("Contraseña OK")

#Ejercicio 3:  Crea un programa que evalúe si una dirección de correo electrónico es válida o no en función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera correcta si solo tiene una “@” y si tiene uno o más “.”
correo=input("Introduce email: ")
contadorArroba=0
contadorPunto=0
for i in range(len(correo)):
    if correo[i]=="@": 
        contadorArroba=contadorArroba+1
    if correo[i]==".":
        contadorPunto=1
if contadorPunto==0 or contadorArroba!=1:
    print("incorrecto")
else:
    print("correcto")