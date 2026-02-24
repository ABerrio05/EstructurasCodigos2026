def suma_lista(lista):
    #caso base
    if not lista:
        return  0
    #caso recursivo
    else:
        return lista[0] + suma_lista(lista[1:])
    
print(f"Suma de [1,2,3,4,5]:{suma_lista([1,2,3,4,5])}")

def invertir_cadena(cadena):
    if len(cadena)<=1:
        return cadena
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]
    
print(f"Cadena invertida 'Hola': {invertir_cadena('Hola')}")
