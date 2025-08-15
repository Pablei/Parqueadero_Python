from datetime import datetime

# Se crea un diccionario con las tarifas por hora, según el tipo de vehículo
tarifas_por_hora = {
    "Automovil": 4000,
    "Motocicleta": 2000
}

# Se crea una función que calcula el tiempo de estancia entre la hora de entrada y salida
def calcular_tiempo_estancia(hora_entrada, hora_salida):
    formato = "%H:%M"
    entrada = datetime.strptime(hora_entrada, formato)
    salida = datetime.strptime(hora_salida, formato)
    diferencia = salida - entrada
    minutos = diferencia.total_seconds() / 60
    return int(minutos)

# Se crea una función que calcula la tarifa total según el tiempo de estancia
# Se cobra por fracciones de 15 minutos
def calcular_tarifa_total(tipo_vehiculo, minutos):
    fracciones = (minutos + 14) // 15  # Redondea hacia arriba
    tarifa_por_hora = tarifas_por_hora[tipo_vehiculo]
    tarifa_por_fraccion = tarifa_por_hora / 4  # 4 fracciones por hora
    total = fracciones * tarifa_por_fraccion
    return round(total)

# Esta función se encarga de registrar la hora de salida y de retirar el vehículo de la lista
# También aumenta las celdas disponibles y calcula la tarifa a pagar
def registrar_salida(listaVehiculos, estado):
    placa = input("Ingrese la placa del vehículo que va a salir: ").upper()
    for vehiculo in listaVehiculos:
        if vehiculo['id'][0] == placa:
            # Se solicita hora de salida manualmente para fines de exposición
            hora_salida = input("Ingrese la hora de salida (formato HH:MM): ").strip()
            vehiculo['hora_salida'] = hora_salida

            # Se calcula el tiempo de estancia y la tarifa total
            minutos = calcular_tiempo_estancia(vehiculo['hora_entrada'], hora_salida)
            tarifa = calcular_tarifa_total(vehiculo['id'][1], minutos)

            # Se muestra el resumen completo de la salida
            print(f"\n🚗 Vehículo {placa} retirado")
            print(f"🕒 Entrada: {vehiculo['hora_entrada']}")
            print(f"🕒 Salida: {hora_salida}")
            print(f"⏱ Estancia: {minutos} minutos")
            print(f"💰 Total a pagar: ${tarifa}\n")

            # Se libera la celda correspondiente
            if vehiculo['id'][1] == 'Automovil':
                estado["celdas_automoviles"] += 1
            elif vehiculo['id'][1] == 'Motocicleta':
                estado["celdas_motocicletas"] += 1
            listaVehiculos.remove(vehiculo)
            return True
    print("🚫 Vehículo no encontrado.")
    return False

# Esta función muestra el estado actual del parqueadero
def mostrar_estado(estado):
    print("\n📊 Estado actual del parqueadero:")
    print(f"Celdas disponibles para automóviles: {estado['celdas_automoviles']}")
    print(f"Celdas disponibles para motocicletas: {estado['celdas_motocicletas']}\n")

# Se crea una función con la que crearemos vehículos y guardaremos la información en un diccionario
def ingreso_vehiculo():
    placa = input("Ingrese la placa del vehiculo: ").upper()
    # Se crea una variable para registrar el tipo de vehículo fácilmente
    # pero hay que convertir a moto o automóvil para guardarla en el diccionario
    opcion_vehiculo = input("Ingrese el número correspondiente al tipo:\n(1)Automoviles\n(2)Motocicletas ")
    if opcion_vehiculo not in ('1','2'):
        print("Opcion no valida, intenta nuevamente.")
        return None
    tipo = "Automovil" if opcion_vehiculo == '1' else "Motocicleta"
    # Para la fecha usamos una app de fecha que trae el python "datetime"
    # .strftime convierte la hora en un texto con el formato deseado. En este caso HH:MM
    hora_actual = datetime.now().strftime("%H:%M")

    # Creamos el diccionario de vehículos. Esto alimentará la lista en el archivo main
    vehiculo = {
        "id": (placa, tipo),
        "hora_entrada": hora_actual,
        "hora_salida": ""
    }
    return vehiculo

# Esta función va a agregar el vehículo ingresado a la lista del main
# También revisa si ya existe
# Nota: se crea en el main un diccionario llamado estado que se llamará con esta función, registra la cantidad de parqueaderos
def agregar_vehiculo(listaVehiculos, estado):
    nuevo_vehiculo = ingreso_vehiculo()
    if nuevo_vehiculo:
        for yaParqueado in listaVehiculos:
            if yaParqueado['id'][0] == nuevo_vehiculo['id'][0]:
                print("Vehiculo ya esta en el parqueadero")
                return False
        if nuevo_vehiculo['id'][1] == 'Automovil':
            if estado["celdas_automoviles"] == 0:
                print("🚫No hay celdas disponibles para automoviles.")
                return False
            else:
                estado["celdas_automoviles"] -= 1
        elif nuevo_vehiculo['id'][1] == 'Motocicleta':
            if estado["celdas_motocicletas"] == 0:
                print("🚫No hay celdas disponibles para motocicletas.")
                return False
            else:
                estado["celdas_motocicletas"] -= 1
        listaVehiculos.append(nuevo_vehiculo)
        print(f"✅ Vehiculo {nuevo_vehiculo['id'][0]} agregado")
        return True
    return False
