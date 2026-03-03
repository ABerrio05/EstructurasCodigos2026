from Paciente import Paciente
from PacienteMetodos import PacienteMetodos

registro = PacienteMetodos.ListaSimple()
cola_atencion = PacienteMetodos.ListaDoble()

while True:
    print("\n Veterinaria Animales Felices")
    print("1. Buscar mascota por ID")
    print("2. Registrar nueva mascota")
    print("3. Mostrar mascotas registradas")
    print("4. Ver cola de atención")
    print("5. Atender paciente")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_buscar = input("Ingrese ID: ")
        paciente = registro.buscar(id_buscar)
        if paciente:
            print("Mascota encontrada:", paciente.nombre)
            cola_atencion.agregar(paciente)
        else:
            print("No existe esa mascota")

    elif opcion == "2":
        nombre = input("Nombre: ")
        especie = input("Especie: ")
        raza = input("Raza: ")
        id = input("ID: ")
        vacunas = input("Vacunas: ")
        alergias = input("Alergias: ")

        nuevo = Paciente(nombre, especie, raza, id, vacunas, alergias)
        registro.agregar(nuevo)
        print("Mascota registrada correctamente")

    elif opcion == "3":
        registro.mostrar()

    elif opcion == "4":
        cola_atencion.mostrar_adelante()

    elif opcion == "5":
        cola_atencion.atender()

    elif opcion == "6":
        break