# Ejercicio 4
familia = {}
for i in range(1, 5):
    print(f"Ingrese los datos de la persona {i}:")
    persona = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "dni": input("DNI: "),
        "email": input("Email: "),
        "fecha_nacimiento": input("Fecha de nacimiento: ")
    }
    familia[f"persona_{i}"] = persona

print("Datos de la familia:", familia)