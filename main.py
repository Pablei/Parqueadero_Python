from datos import agregar_vehiculo, registrar_salida, mostrar_estado

vehiculos_estacionados = []
estado = {
    "celdas_automoviles": 20,
    "celdas_motocicletas": 15
}

def mostrar_menu():
    print("\n" + "="*40)
    print(" 🚗  SISTEMA DE PARQUEADERO  🏍️ ")
    print("="*40)
    print("1️⃣  Ingresar vehículo")
    print("2️⃣  Retirar vehículo")
    print("3️⃣  Ver estado del parqueadero")
    print("4️⃣  Salir")
    print("="*40)

if __name__ == '__main__':
    while True:
        mostrar_menu()
        opcion = input("👉 Seleccione una opción: ")

        if opcion == "1":
            agregar_vehiculo(vehiculos_estacionados, estado)
        elif opcion == "2":
            registrar_salida(vehiculos_estacionados, estado)
        elif opcion == "3":
            mostrar_estado(estado)
        elif opcion == "4":
            print("\n👋 Gracias por usar el sistema de parqueadero.")
            print("¡Hasta pronto!\n")
            break
        else:
            print("❌ Opción inválida, intenta nuevamente.")
