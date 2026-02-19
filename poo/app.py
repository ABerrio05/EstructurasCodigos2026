# import Animal
from Animal import Animal
from Felino import Felino
from Zoo import Zoo
from Fabric import Fabrica

#ob=Animal("Pantera")
#ob1=Animal("Gato")
#ob1.setNombre("Lince")
#print(ob1.getNombre())
gato1=Felino("Felino","Leon")
gato2=Felino("Felino","Tigre")
z1=Zoo("udec")
z1.addFelino(gato1)
z1.addFelino(gato2)
#print(z1.verGatos())
for ob in z1.verGatos():
    print(ob.getEspecie)

del z1
print(type(gato1))

zz=Fabrica("minitoy")
zz.makeToy("puma")
zz.makeToy("lince")
zz.makeToy("jaguar")

for peluche in zz.verCatalogo():
    print(peluche.getEspecie())




#print(e1.getNombre())
#print(e1.getEspecie())

#l1=[10,20,"udec",5]
#l1.append(100)
#print(l1)
#l2=list()
