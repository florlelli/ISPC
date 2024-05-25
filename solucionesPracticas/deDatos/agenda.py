# Parte 2: Agenda
agenda = {}

def agregar_persona():
    dni = input("Ingrese el DNI: ")
    if dni in agenda:
        print("La persona ya existe en la agenda.")
    else:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "telefono": telefono
        }
        print("Persona agregada.")

def modificar_persona():
    dni = input("Ingrese el DNI de la persona a modificar: ")
    if dni in agenda:
        nombre = input(f"Nuevo nombre ({agenda[dni]['nombre']}): ") or agenda[dni]['nombre']
        apellido = input(f"Nuevo apellido ({agenda[dni]['apellido']}): ") or agenda[dni]['apellido']
        email = input(f"Nuevo email ({agenda[dni]['email']}): ") or agenda[dni]['email']
        telefono = input(f"Nuevo teléfono ({agenda[dni]['telefono']}): ") or agenda[dni]['telefono']
        agenda[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "telefono": telefono
        }
        print("Persona modificada.")
    else:
        print("La persona no existe en la agenda.")

def eliminar_persona():
    dni = input("Ingrese el DNI de la persona a eliminar: ")
    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada.")
    else:
        print("La persona no existe en la agenda.")

def mostrar_agenda():
    if agenda:
        for dni, datos in agenda.items():
            print(f"DNI: {dni}")
            for clave, valor in datos.items():
                print(f"  {clave}: {valor}")
    else:
        print("La agenda está vacía.")

def menu():
    while True:
        print("\n--- Agenda Telefónica ---")
        print("1. Agregar una persona")
        print("2. Modificar una persona")
        print("3. Eliminar una persona")
        print("4. Mostrar todos la agenda")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            agregar_persona()
        elif opcion == "2":
            modificar_persona()
        elif opcion == "3":
            eliminar_persona()
        elif opcion == "4":
            mostrar_agenda()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()
