import sqlite3

conexion=sqlite3.connect("GestionProductos")

cursor=conexion.cursor()

cursor.execute('''
    CREATE TABLE productos(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
''')

productos=[
    ("pelota", 20, "juguetería"),
    ("pantalón", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica"),
]

cursor.executemany("INSERT INTO productos VALUES(NULL,?,?,?)", productos)

conexion.commit()

conexion.close()