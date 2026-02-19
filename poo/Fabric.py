from Felino import Felino
class Fabrica:
    def __init__(self,nombre):
        self.nombre=nombre
        self.listaPeluches=list()
    def makeToy(self,especie):
        f=Felino("gatos",especie)
        self.listaPeluches.append(f)
    def verCatalogo(self):
        return self.listaPeluches