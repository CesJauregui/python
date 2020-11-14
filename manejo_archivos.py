#importar la libreria de archivos
from io import open
'''
    Creación de archivo externo

    "r" : lectura
    "w" : escritura
    "a" : abrir el archivo y escribir
    "r+": lectura y escritura
'''
archivo_texto=open("archivo.txt","w")
# "archivo.txt" : es el nombre del archivo que vamos a utilizar
# "w" : es el modo del que vamos a utilizar el archivo. 

frase="Hola mundo \n ¡Bienvenidos!"

#Utilizamos el método write() para escribir el texto en el archivo.txt
archivo_texto.write(frase)

#Cerramos el archivo (de la memoria ram)
archivo_texto.close()

'''
    Leer el archivo creado
'''
archivo_texto=open("archivo.txt","r")

#Lear lo que hay en archivo.txt y que lo guarde en la variable text
text=archivo_texto.read()

archivo_texto.close()

print(text)

'''
    Añadir información al archivo.txt
'''
archivo_texto=open("archivo.txt","a")

archivo_texto.write("\n sigue aprendiendo")








