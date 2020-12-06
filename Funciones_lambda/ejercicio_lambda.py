#Función tradicional
def area_triangulo(base,altura):
    return (base*altura)/2
print("------Función tradicional, área de un triángulo------")
print(area_triangulo(5,7))

#Con función lambda
#NO es recomendable realizar funciones lambda para funciones más complejas, que contengan bucles, condiciopnales, etc.
triangulo_a=lambda base,altura: (base*altura)/2
print("------Función con lambda, área de un triángulo-------")
print(triangulo_a(8,9))

#Función con lambda para sacar el cubo de un número
#pow() es una función matemática para elevar al cuadrado, al cubo, etc.
al_cubo=lambda numero: pow(numero,3)
print("------Función con lambda, sacar el cubo de un número-------")
print(al_cubo(13))

#Función para mostrar la comisión en dolares
destacar_valor=lambda comision: "¡{}! $".format(comision)
comision_sandra=15200
print("------Función lambda, mostrar la comisión en dolares-------")
print(destacar_valor(comision_sandra))