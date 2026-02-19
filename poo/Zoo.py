class Zoo:
    def __init__(self,nombre):
        self.nombre=nombre
        self.listaGatos=[]
    def addFelino(self,gato):
        #self.gato=gato
        self.listaGatos.append(gato)
    def verGatos(self):
        return self.listaGatos
