class Nodo:
    def __init__(self, titulo, procesos):
        self.titulo = titulo
        self.procesos = procesos  
        self.completado = False   
        self.siguiente = None
        self.anterior = None      

class ListaSimpleCircular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, titulo, procesos):
        nuevo = Nodo(titulo, procesos)
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.siguiente = self.cabeza
        print(f"Etapa '{titulo}' añadida a Producción.")

    def validar_etapa(self, titulo):
        if not self.cabeza: return False
        temp = self.cabeza
        while True:
            if temp.titulo.lower() == titulo.lower():
                temp.completado = True
                return True
            temp = temp.siguiente
            if temp == self.cabeza: break
        return False

    def mostrar(self):
        if not self.cabeza:
            print("\n[!] Producción vacía.")
            return
        temp = self.cabeza
        print("\n--- ESTADO DE PRODUCCIÓN ---")
        while True:
            estado = "COMPLETADO" if temp.completado else "PENDIENTE"
            print(f"{temp.titulo} [{estado}]")
            for p in temp.procesos:
                print(f"   - {p}")
            temp = temp.siguiente
            if temp == self.cabeza: break

class ListaDobleCircular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, titulo, procesos):
        nuevo = Nodo(titulo, procesos)
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
            nuevo.anterior = self.cabeza
        else:
            ultimo = self.cabeza.anterior
            ultimo.siguiente = nuevo
            nuevo.anterior = ultimo
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
        print(f"Punto '{titulo}' añadido a Distribución.")

    def mostrar(self):
        if not self.cabeza:
            print("\n[!] Distribución vacía.")
            return
        temp = self.cabeza
        print("\n--- ESTADO DE DISTRIBUCIÓN ---")
        while True:
            print(f"{temp.titulo} (Ant: {temp.anterior.titulo} | Sig: {temp.siguiente.titulo})")
            for p in temp.procesos:
                print(f"   - {p}")
            temp = temp.siguiente
            if temp == self.cabeza: break

class SistemaMermelada:
    def __init__(self):
        self.produccion = ListaSimpleCircular()
        self.distribucion = ListaDobleCircular()
        
        self.opciones_prod = {
            "1": ("Producción Agrícola", ["Agricultura agroecológica", "Sensores de cultivo"]),
            "2": ("Cosecha", ["Clasificación automática", "Lavado y desinfección"]),
            "3": ("Transformación e Innovación", ["Nuevos sabores", "Endulzado natural"]),
            "4": ("Empaque y Valor Agregado", ["Frascos biodegradables", "Trazabilidad QR"])
        }
        self.opciones_dist = {
            "1": ("Comercialización", ["Redes sociales", "Mercados locales"]),
            "2": ("Experiencia Cliente", ["Feedback directo", "Calidad y Origen"])
        }

    def menu(self):
        while True:
            print("\n" + "="*50)
            print("   GESTOR DE CALIDAD: MERMELADA DE MORA")
            print("="*50)
            print("1. AGREGAR etapa a Producción (Simple Circular)")
            print("2. AGREGAR punto a Distribución (Doble Circular)")
            print("3. VALIDAR/COMPLETAR una etapa")
            print("4. VER TODO el proceso y estados")
            print("5. Salir")
            
            opc = input("\nSeleccione una opción: ")

            if opc == "1":
                print("\n--- Opciones de Producción ---")
                for k, v in self.opciones_prod.items(): print(f"{k}. {v[0]}")
                sel = input("Seleccione: ")
                if sel in self.opciones_prod:
                    t, p = self.opciones_prod[sel]
                    self.produccion.agregar(t, p)

            elif opc == "2":
                print("\n--- Opciones de Distribución ---")
                for k, v in self.opciones_dist.items(): print(f"{k}. {v[0]}")
                sel = input("Seleccione: ")
                if sel in self.opciones_dist:
                    t, p = self.opciones_dist[sel]
                    self.distribucion.agregar(t, p)

            elif opc == "3":
                self.produccion.mostrar()
                nombre = input("\nEscriba el nombre de la etapa a validar: ")
                if self.produccion.validar_etapa(nombre):
                    print(f"Etapa '{nombre}' validada correctamente.")
                else:
                    print("No se encontró o no existe esa etapa.")

            elif opc == "4":
                self.produccion.mostrar()
                self.distribucion.mostrar()

            elif opc == "5":
                break

if __name__ == "__main__":
    app = SistemaMermelada()
    app.menu()