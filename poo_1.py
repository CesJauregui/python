class Coche:
#Creación de un constructor / estado inicial de la clase
    def __init__(self):
        self.largoChasis=250
        self.largoChasis=250
        self.anchoChasis=120
        #la variable rueda no es accesible desde fuera de la clase por los "__", es decir, al momento de instanciar. No se puede cambiar el valor
        self.__ruedas=4
        self.enMarcha=False

    #self hace referencia a la misma instancia u objeto es igual al this
    #es obligatoria ponerlo en python
    def arrancarCoche(self,arrancamos):
        self.enMarcha=arrancamos

        if self.enMarcha:
            chequeo=self.__chequeInterno()

        if self.enMarcha and chequeo:
            return "El coche está en marcha"
        elif self.enMarcha and chequeo==False:
            return "Algo ha ido mal en el chequeo, no se puede arrancar"
        else:
            return "El coche está parado"
        self.enMarcha=True
        
    def estadoCoche(self):
        #Dentro de la clase tambien se le debe poner los dos guiones "__" a la varible rueda
        print("El coche tiene " , self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)

    #Método encapsulado
    def __chequeInterno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False

#Instanciar una clase
#NO se utiliza el new
miCoche = Coche()
#si arrancarCoche() no está instanciado y es False, el valor será none, osea el coche está parado
print(miCoche.arrancarCoche(True))

miCoche.estadoCoche()

print("---------A continuación creamos el segundo objeto!-----------")

miCoche2 = Coche()
#si arrancarCoche() no está instanciado, el valor será none, osea el coche está parado
print(miCoche2.arrancarCoche(False))

miCoche2.estadoCoche()