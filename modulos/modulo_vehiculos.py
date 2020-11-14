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

#Creación de clase Furgoneta
class Furgoneta(Vehiculos):
    def carga(self, carga):
        self.cargado=carga
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
