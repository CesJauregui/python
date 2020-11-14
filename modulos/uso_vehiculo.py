from modulo_vehiculos import *

miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miCoche=Vehiculos("Mazda", "MX65")

miCoche.estado()

miFurgoneta = Furgoneta("Renault","Kango")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
