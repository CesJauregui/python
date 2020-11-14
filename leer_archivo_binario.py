#importamos la libreria
import pickle

# "rb": leer de forma binaria
fichero=open("lista_nombres","rb")

#carga de fichero y lectura
lista=pickle.load(fichero)

#mostrar en consola
print(lista)
