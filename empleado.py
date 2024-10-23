import json
from validaciones import *

inasistencias = []
personas = []
mDia = 33.33

def registrarEmpleado():
    global personas
    personas.clear()  # Limpiamos la lista antes de registrar nuevos empleados

    ID = validarNumero("Por favor digite el ID del empleado: ")
    nombre = validarPalabra("El nombre del empleado es: ")
    cargo = validarPalabra("Su cargo en la empresa es: ")
    salarioEm = validarNumero("Su salario actual es: ")

    empleadoData = {
        "ID": ID,
        "nombre": nombre,
        "cargo": cargo,
        "salario": salarioEm,
        "inasistencias": [],
        "nomina": {
            "salario_actual": salarioEm,
            "dias_trabajados": 0,
            "bonos": []
        }
    }

    personas.append(empleadoData)

    # Guardar empleado en su archivo JSON
    with open(f"empleado_{ID}.json", 'w') as file:
        json.dump(empleadoData, file, indent=4)

    print("Se registró el empleado correctamente!")
    print(f"Id: {ID} Nombre: {nombre} Cargo: {cargo} Salario: {salarioEm} \n")

def ingresarInasistencias():
    global personas

    if not personas:
        print("( X ) No hay empleados registrados.")
        return

    ID = validarNumero("Por favor digite el Id del empleado: ")

    for emple in personas:
        if ID == emple["ID"]:
            cantidad = validarNumero("Digite la cantidad de inasistencias:")
            inasistencias.append(cantidad)
            emple["salario"] -= (cantidad * mDia)  # Actualizar salario
            emple["inasistencias"].append(cantidad)  # Actualizar inasistencias

            # Guardar actualizaciones en el archivo JSON del empleado
            with open(f"empleado_{ID}.json", 'w') as file:
                json.dump(emple, file, indent=4)

            print("Se registró de manera correcta las inasistencias!")
            print(f"El empleado {emple['nombre']} tiene {inasistencias[-1]} inasistencias y su salario actual es: {emple['salario']}")
            return

    print("ID inválido, no se encontró el empleado.")
