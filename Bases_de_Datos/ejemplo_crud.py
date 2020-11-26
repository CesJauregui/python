import sqlite3

conexion=sqlite3.connect("GestionProductos")

cursor=conexion.cursor()

#READ
'''cursor.execute("SELECT * FROM productos WHERE SECCION='confección'")
productos=cursor.fetchall()
print(productos)
'''
#UPDATE
cursor.execute("UPDATE productos SET precio=35 WHERE NOMBRE_ARTICULO='pelota'")

#DELETE
cursor.execute("DELETE FROM productos WHERE ID=4")
conexion.commit()

conexion.close()