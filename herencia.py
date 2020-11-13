#Creación de clase Vehiculos
class Vehiculos:
    #constructor
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    #Métodos
    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo:", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

#Crear la clase Moto y heredar la clase vehiculos
class Moto(Vehiculos):
    hcaballito=""
    #sobreescribiendo un método
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito!"
    #Sobreescribiendo el método estado para agregar el caballito
    def estado(self):
        print("Marca: ", self.marca, "\nModelo:", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\nme ", self.hcaballito)

miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

#Creación de clase Furgoneta
class Furgoneta(Vehiculos):
    def carga(self, carga):
        self.cargado=carga
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

miFurgoneta = Furgoneta("Renault","Kango")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class VeElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        self.autonomia=100
    def cargaEnergia(self):
        self.cargando=True
#Herencia multiple
class BicicletaElectrica(VeElectricos,Vehiculos):
   pass 
#Depende del orden que heredamos, se da preferencia a la primera clase heredada
miBici = BicicletaElectrica("Orbea","th3")