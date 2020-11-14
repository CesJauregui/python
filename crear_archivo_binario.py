#importamos la libreria
import pickle

lista_nombre=["Pedro", "Ana", "Maria", "Isabel"]
# "wb": escritura binaria
fichero_binario=open("lista_nombres","wb")
#volcado de datos de la lista
pickle.dump(lista_nombre, fichero_binario)
#cerrar el fichero
fichero_binario.close()

#borrar de la memoria
del (fichero_binario)