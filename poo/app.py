# import Animal
from Animal import Animal
from Felino import Felino

ob=Animal("Pantera")
ob1=Animal("Gato")
ob1.setNombre("Lince")
print(ob1.getNombre())
e1=Felino("Felino","Leon")
print(e1.getNombre())
print(e1.getEspecie())