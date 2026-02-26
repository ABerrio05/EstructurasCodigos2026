class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

a=Nodo(100)
b=Nodo(1000)
c=Nodo(1)
d=Nodo(10)

a.siguiente=b
b.siguiente=c
c.siguiente=d
d.siguiente=None

actual=a
while actual:
    print(actual.dato)
    actual=actual.siguiente