#No permite añadir, eliminar, mover elementos etc
#Son inmutables, no se puede modificar despues de su creación
mitupla=("Juan",13,1,1995)
#Convertir a lista
milista=list(mitupla)
#Buscar Juan en la lista
print("Juan" in milista)
#Contar la cantidad de datos
print(milista.count(13))
#cantidad de elementos en la lista
print(len(milista[:]))
#Desempaquetado de tuplas
nombre,dia,mes,anio=mitupla
print(nombre)
print(dia) # ...