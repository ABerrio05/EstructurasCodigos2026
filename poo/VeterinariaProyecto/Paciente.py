from Animales import Animales

class Paciente(Animales):
    def __init__(self, nombre,especie,raza,id,vacunas,alergias):
        super().__init__(nombre,especie,raza)
        self.id=id
        self.vacunas=vacunas
        self.alergias=alergias
