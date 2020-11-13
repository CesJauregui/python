#------------Ejercicio 1------------
# Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos
n1=(int(input("Ingrese un número: ")))
n2=(int(input("Ingrese otro número: ")))
def DevuelveMax(numero1,numero2):
    if numero1>numero2:
        print(numero1)
    elif numero2>numero1:
        print(numero2)
    else:
        print("Son iguales")
print("El número más alto es: ")
DevuelveMax(n1,n2)

#------------Ejercicio 2------------
#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado)
nombre=input("Ingrese su nombre: ")
direccion=input("Ingrese su dirección: ")
telefono=input("Ingrese su teléfono: ")

lista=[nombre,direccion,telefono]

print("Los datos personales son: ")
print(lista[:])

#------------Ejercicio 3------------
#Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmética de los números introducidos.
n1=(int(input("Primer número: ")))
n2=(int(input("Segundo número: ")))
n3=(int(input("Tercer número: "))) 

print((n1+n2+n3)/3)

#La función str() hace que concatene el string con el int