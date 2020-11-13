'''def generaPares(limite):
    num=1

    while num<limite:
        yield num*2
        num+=1
devuelvePares=generaPares(10)

print(next(devuelvePares))
print("Más código")
print(next(devuelvePares))
print("Más código")
print(next(devuelvePares))
'''
#bucles anidados
# el "*" es para indicar que vamos a ingresar un numero indeterminados de argumentos en forma de tuplas.
def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
        #el "yield from" reemplaza a otro for anidado, asi se evita otro for
            yield from elemento 

ciudades_devueltas=devuelveCiudades("Madrid","Barcelona","Bilbao","Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
