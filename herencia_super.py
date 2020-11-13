
#Uso de super() e isinstance()

class Persona:
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_e, edad_e, residencia_e):
        super().__init__(nombre_e, edad_e, residencia_e)
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "\nAntiguedad: " ,self.antiguedad)
Manuel = Persona("Manuel",55,"Perú")
Manuel.descripcion()

#isinstance(): sirve para ver si Manuel es una instancia o no(devuelve True o False)

#print(isinstance(Manuel,Persona)

print(isinstance(Manuel,Empleado))
