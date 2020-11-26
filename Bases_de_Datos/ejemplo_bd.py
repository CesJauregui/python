import sqlite3

#Creación del archivo de la base de datos
conexion=sqlite3.connect("FirstDB")

#Creación del cursor
cursor=conexion.cursor()

''' Creación de tabla 
cursor.execute("CREATE TABLE productos (NOMBRE_ARTICULO VARCHAR(50), PRECIO INT, SECCION VARCHAR(20))")
'''

''' Creación individual de los productos (fila por fila)
cursor.execute("INSERT INTO productos VALUES('Balón',15,'Deportes')")
'''

''' Inserción de varios productos 
productos=[
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería")
]
'''

''' Ejecución de la inserción de varios productos
cursor.executemany("INSERT INTO productos VALUES(?,?,?)",productos)
'''

 #Leer la tabla productos y mostrar en consola
cursor.execute("SELECT * FROM productos")
productos=cursor.fetchall()#Devuelve una lista de la consulta
for producto in productos:
    print("Nombre artículo: ", producto[0], " Sección: ", producto[2])


conexion.commit()
conexion.close()