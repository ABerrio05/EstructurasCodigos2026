class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

class Lista:
    def __init__(self):
        self.primero=None
            
    def adicionar(self,dato):
        nuevo=Nodo(dato)
        if self.primero==None:
            self.primero=nuevo
        else:
           actual=self.primero
           while actual.siguiente:
               actual=actual.siguiente
           actual.siguiente=nuevo
    
    def mostrar(self):
        actual=self.primero
        while actual:
            print(actual.dato)
            actual=actual.siguiente      

    def eliminar(self, valor):
        if self.primero == None:
            return
        
        if self.primero.dato == valor:
            self.primero = self.primero.siguiente
            return
        
        actual = self.primero
        while actual.siguiente:
            if actual.siguiente.dato == valor:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

listado=Lista()
listado.adicionar(24)
listado.adicionar(11)
listado.adicionar(2)
listado.adicionar(9)
listado.mostrar()
x=int(input("Ingrese el numero q desee eliminar de la lista: "))
listado.eliminar(x)
listado.mostrar()
