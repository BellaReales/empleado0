from modulos.empleado import *
from validaciones import *

salarioMin = 1000000
salud = 40.000
pension = 40.000
auxilio = 100.000
salarioTotal = []
emplead0 = []  # Lista para almacenar empleados en memoria

def cargarEmpleados():
    global personas
def bonosExtra(personas):  
    ID = validarNumero("Por favor ingrese el ID del empleado: ")
    for emple in personas:
        if ID == emple["ID"]:
            cantidad = validarNumero("¿Cuántos bonos extra desea generar?: ")
            if cantidad <= 2:
                for _ in range(cantidad):
                    tipo = validarPalabra("Ingrese el concepto de bono extra: ")
                    valor = validarNumero("Ingrese el valor del bono extra: ")
                    emple["salario"] += valor  # Actualizar salario
                    emple["nomina"]["bonos"].append({"tipo": tipo, "valor": valor})  # Agregar bono

                    print(f"Se ha generado un bono extra a {emple['nombre']} por: {tipo} con un valor de: {valor}")

                # Guardar cambios en el archivo JSON del empleado
                with open(f"empleado_{ID}.json", 'w') as file:
                    json.dump(emple, file, indent=4)

            else:
                print("Solo puede generar dos bonos extra por empleado.")
            return
    print("ID inválido, no se encontró el empleado.")


def sacarNomina():

    ID = validarNumero("Por favor ingrese el ID del empleado: ")
    for emple in personas:
        if ID == emple["ID"]:
            print(f"Su salario actual es: {emple['salario']}")
            if emple["salario"] < 2000000:
                print(f"Su salario: {emple['salario']} es menor a la mínima, por lo tanto se le dará un auxilio de: {auxilio}")
                emple["salario"] += auxilio
                print(f"Se le ha aplicado el auxilio y su salario actual es: {emple['salario']}")
            else:
                print(f"Su salario {emple['salario']} es mayor o igual a la mínima, por lo tanto no se le dará un auxilio.")

            emple["salario"] -= salud  # Descontar salud
            emple["salario"] -= pension  # Descontar pensión
            salarioTotal.append(emple["salario"])

            # Crear un resumen de la nómina
            nominaData = {
                "salario_total": emple["salario"],
                "descuento_salud": salud,
                "descuento_pension": pension,
                "bonos": emple["nomina"]["bonos"],
                "inasistencias": emple["inasistencias"]
            }

            print(f"Se le ha descontado salud y pensión, su salario total es: {emple['salario']}")
            print(f"Resumen de nómina: {nominaData}")

            # Guardar la nómina en un archivo JSON (opcional)
            with open(f"nomina_{ID}.json", 'w') as file:
                json.dump(nominaData, file, indent=4)

            return
    print("ID inválido, no se encontró el empleado.")

# Cargar empleados al inicio del programa
cargarEmpleados()
