'''
    Ejecución de raise
    para manejo de error y excepciones
'''
def evaluaEdad(edad):
    if edad<0:
        raise TypeError("No se permiten edades negativas")
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuídate"
    
print(evaluaEdad(70))