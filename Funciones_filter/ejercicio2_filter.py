class Empleado:
    def __init__(self, nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {}, tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)
    
listaEmpleados=[
    Empleado("Pedro","Jefe",2500),
    Empleado("Juana","Directora",4500),
    Empleado("Oscar","Supervisor",2000),
    Empleado("Maria","Gerente", 3500)
]
#Uso de la función filter
salarios_altos=filter(lambda empleado: empleado.salario>2800,listaEmpleados)
print("---Reporte de salarios mayores a 2800---")
for salarios in salarios_altos:
    print(salarios)