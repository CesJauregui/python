#Estructura de datos que nos permite almacenar valores de diferentes tipos, listas, y otros diccionarios
#No importa el orden que estén declarados
midiccionario={
    "Alemania":"Berlín",
    "Francia":"París",
    "Reino Unido":"londres",
    "España":"Madrid"
}
#Agregar un elemento al diccionario
midiccionario["Italia"]="Lisboa"
#Imprimir todo el diccionario
print(midiccionario)
#Modificar el diccionario
midiccionario["Italia"]="Roma"
#Imprimir el diccionario modificado
print(midiccionario)
#Eliminar un elemento del diccioanrio
del midiccionario["Reino Unido"]
print(midiccionario)

#Imprimir la capital de Francia
print(midiccionario["Francia"])

#Imprimir todas la claves del diccionario
print(midiccionario.keys())

#Imprimir todos los valores del diccionario
print(midiccionario.values())

#Imprimir la longitud del diccionario
print(len(midiccionario))
