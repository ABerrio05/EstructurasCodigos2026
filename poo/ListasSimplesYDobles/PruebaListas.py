from ListasSimples import ListaSimple
from ListasDobles import ListaDoble

# Prueba de Lista Simple
print("=== LISTA SIMPLE ===")
ls = ListaSimple()
ls.insertar_nodo(3)
ls.mostrar()
ls.insertar_nodo(2)
ls.mostrar()
ls.insertar_nodo(1)
ls.mostrar() 
ls.insertar_fila(4)       
ls.insertar_fila(5)       
ls.mostrar()

# Prueba de Lista Doble
print("\n=== LISTA DOBLE ===")
ld = ListaDoble()
ld.insertar_inicio(3)
ld.insertar_inicio(2)
ld.insertar_final(1)
print("Adelante:", end=" ")
ld.mostrar_adelante()
print("Atrás:", end=" ")
ld.mostrar_atras()