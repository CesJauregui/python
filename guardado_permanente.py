import pickle
#Creación de la clase Persona
class Persona:
    #Definiendo el constructor
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona con el nombre de ",self.nombre)

    #Método especial para convetir en cadena de texto la información de un objeto
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    personas=[]
    def __init__(self):
        # "ab": agregar información binaria
        listaDePersonas=open("ficheroExterno","ab+")
        #cursor al principio
        listaDePersonas.seek(0)
        #volcado de información
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del (listaDePersonas)

    def agregarPersona(self,p):
        self.personas.append(p)
        self.guardarPersonas()
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonas(self):
        listaDePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()

persona=Persona("Sandra", "Femenino", 20)
miLista.agregarPersona(persona)

miLista.mostrarInfoFicheroExterno()