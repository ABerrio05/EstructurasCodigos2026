from Paciente import Paciente

class PacienteMetodos:
    class NodoSimple:
        def __init__(self, paciente):
            self.paciente = paciente
            self.siguiente = None
    
    class ListaSimple:
        def __init__(self):
            self.cabeza = None

        def agregar(self, paciente):
            nuevo = PacienteMetodos.NodoSimple(paciente)
            if not self.cabeza:
                self.cabeza = nuevo
            else:
                actual = self.cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = nuevo

        def buscar(self, id):
            actual = self.cabeza
            while actual:
                if actual.paciente.id == id:
                    return actual.paciente
                actual = actual.siguiente
            return None

        def mostrar(self):
            actual = self.cabeza
            while actual:
                print(f"ID: {actual.paciente.id} - Nombre: {actual.paciente.nombre}")
                actual = actual.siguiente
    
    class NodoDoble:
        def __init__(self, paciente):
            self.paciente = paciente
            self.siguiente = None
            self.anterior = None
    
    class ListaDoble:
        def __init__(self):
            self.cabeza = None
            self.cola = None

        def agregar(self, paciente):
            nuevo = PacienteMetodos.NodoDoble(paciente)
            if not self.cabeza:
                self.cabeza = self.cola = nuevo
            else:
                self.cola.siguiente = nuevo
                nuevo.anterior = self.cola
                self.cola = nuevo

        def atender(self):
            if not self.cabeza:
                print("No hay pacientes en espera")
                return

            print(f"Atendiendo a: {self.cabeza.paciente.nombre}")
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None

        def mostrar_adelante(self):
            actual = self.cabeza
            while actual:
                print(actual.paciente.nombre)
                actual = actual.siguiente

        def mostrar_atras(self):
            actual = self.cola
            while actual:
                print(actual.paciente.nombre)
                actual = actual.anterior