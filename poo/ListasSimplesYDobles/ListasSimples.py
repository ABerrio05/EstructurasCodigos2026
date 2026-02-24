class NodoSimple:    
    def __init__(self,dato):
        self.dato=dato 
        self.siguiente=None
    
class ListaSimple:
    def __init__(self):
        self.cabeza=None

    def insertar_nodo(self, dato):
        nuevo_nodo = NodoSimple(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_fila(self, dato):
        nuevo_nodo = NodoSimple(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return 
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")