class NodoDoble:
    def __init__(self,dato):
        self.dato=dato
        self.anterior=None
        self.siguiente=None

class ListaDoble:
    def __init__(self):
        self.cabeza=None
        self.cola=None

    def insertar_inicio(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
    
    def insertar_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
    
    def mostrar_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")
    
    def mostrar_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.anterior
        print("None")