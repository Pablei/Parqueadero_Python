from datos import agregar_vehiculo, registrar_salida, mostrar_estado
from datos import ingreso_vehiculo
vehiculos_estacionados = []
estado = {
    "celdas_automoviles": 20,
    "celdas_motocicletas": 15
}

if __name__ == '__main__':
    while True:
        print("1. Ingresar vehículo")
        print("2. Retirar vehículo")
        print("3. Ver estado del parqueadero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_vehiculo(vehiculos_estacionados, estado)
        elif opcion == "2":
            registrar_salida(vehiculos_estacionados, estado)
        elif opcion == "3":
            mostrar_estado(estado)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")