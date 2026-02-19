class Animal:
    def __init__(self,nombre):
        #pass
        #print("se activo el constructor")
        self.nombre=nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre