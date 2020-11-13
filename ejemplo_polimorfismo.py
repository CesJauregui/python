class Coche:
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto:
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion:
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")
'''
#Sin Polimorfismo

miVehiculo=Moto()
miVehiculo.desplazamiento()

miVehiculo2=Coche()
miVehiculo2.desplazamiento()

miVehiculo3=Camion()
miVehiculo3.desplazamiento()
'''

#Con Polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Coche()#Puede ser Moto o Camion tambien

desplazamientoVehiculo(miVehiculo)
