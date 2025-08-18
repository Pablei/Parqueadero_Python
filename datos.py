from datetime import datetime

# Diccionario con las tarifas por hora
tarifas_por_hora = {
    "Automovil": 4000,
    "Motocicleta": 2000
}

def calcular_tiempo_estancia(hora_entrada, hora_salida):
    formato = "%H:%M"
    entrada = datetime.strptime(hora_entrada, formato)
    salida = datetime.strptime(hora_salida, formato)
    diferencia = salida - entrada
    minutos = diferencia.total_seconds() / 60
    return int(minutos)

def calcular_tarifa_total(tipo_vehiculo, minutos):
    fracciones = (minutos + 14) // 15  # Redondea hacia arriba
    tarifa_por_hora = tarifas_por_hora[tipo_vehiculo]
    tarifa_por_fraccion = tarifa_por_hora / 4
    total = fracciones * tarifa_por_fraccion
    return round(total)

def registrar_salida(listaVehiculos, estado, informe):
    placa = input("Ingrese la placa del vehículo que va a salir: ").upper().strip()
    if not placa:
        print("🚫 Placa no válida.")
        return False

    for vehiculo in listaVehiculos:
        if vehiculo['id'][0] == placa:
            hora_salida = input("Ingrese la hora de salida (formato HH:MM): ").strip()
            vehiculo['hora_salida'] = hora_salida

            minutos = calcular_tiempo_estancia(vehiculo['hora_entrada'], hora_salida)
            tarifa = calcular_tarifa_total(vehiculo['id'][1], minutos)

            print(f"\n🚗 Vehículo {placa} retirado")
            print(f"🕒 Entrada: {vehiculo['hora_entrada']}")
            print(f"🕒 Salida: {hora_salida}")
            print(f"⏱ Estancia: {minutos} minutos")
            print(f"💰 Total a pagar: ${tarifa}\n")

            informe.append({
                "placa": placa,
                "tipo": vehiculo['id'][1],
                "hora_entrada": vehiculo['hora_entrada'],
                "hora_salida": hora_salida,
                "minutos": minutos,
                "tarifa": tarifa
            })

            if vehiculo['id'][1] == 'Automovil':
                estado["celdas_automoviles"] += 1
            elif vehiculo['id'][1] == 'Motocicleta':
                estado["celdas_motocicletas"] += 1
            listaVehiculos.remove(vehiculo)
            return True

    print("🚫 Vehículo no encontrado en el parqueadero.")
    return False

def mostrar_estado(estado):
    print("\n📊 Estado actual del parqueadero:")
    print(f"Celdas disponibles para automóviles: {estado['celdas_automoviles']}")
    print(f"Celdas disponibles para motocicletas: {estado['celdas_motocicletas']}\n")

def ingreso_vehiculo():
    placa = input("Ingrese la placa del vehiculo: ").upper().strip()
    if not placa:
        print("🚫 La placa no puede estar vacía.")
        return None

    opcion_vehiculo = input("Ingrese el número correspondiente al tipo:\n(1) Automóviles\n(2) Motocicletas: ")
    if opcion_vehiculo not in ('1', '2'):
        print("🚫 Opción no válida, intenta nuevamente.")
        return None

    tipo = "Automovil" if opcion_vehiculo == '1' else "Motocicleta"
    hora_actual = datetime.now().strftime("%H:%M")

    vehiculo = {
        "id": (placa, tipo),
        "hora_entrada": hora_actual,
        "hora_salida": ""
    }
    return vehiculo

def agregar_vehiculo(listaVehiculos, estado):
    nuevo_vehiculo = ingreso_vehiculo()
    if nuevo_vehiculo:
        for yaParqueado in listaVehiculos:
            if yaParqueado['id'][0] == nuevo_vehiculo['id'][0]:
                print("🚫 Vehículo ya está en el parqueadero.")
                return False

        if nuevo_vehiculo['id'][1] == 'Automovil':
            if estado["celdas_automoviles"] == 0:
                print("🚫 No hay celdas disponibles para automóviles.")
                return False
            else:
                estado["celdas_automoviles"] -= 1
        elif nuevo_vehiculo['id'][1] == 'Motocicleta':
            if estado["celdas_motocicletas"] == 0:
                print("🚫 No hay celdas disponibles para motocicletas.")
                return False
            else:
                estado["celdas_motocicletas"] -= 1

        listaVehiculos.append(nuevo_vehiculo)
        print(f"✅ Vehículo {nuevo_vehiculo['id'][0]} agregado.")
        return True
    return False

def generar_informe(informe):
    print("\n📑 INFORME DEL PARQUEADERO 📑")
    if not informe:
        print("No hay actividades realizadas\n")
        return

    total_recaudado = 0
    for i, registro in enumerate(informe, 1):
        print(f"{i}. 🚗 {registro['placa']} | {registro['tipo']}")
        print(f"   Entrada: {registro['hora_entrada']} - Salida: {registro['hora_salida']}")
        print(f"   ⏱ Estancia: {registro['minutos']} minutos")
        print(f"   💰 Tarifa: ${registro['tarifa']}\n")
        total_recaudado += registro['tarifa']

    print("="*40)
    print(f"💵 Total recaudado: ${total_recaudado}")
    print("="*40 + "\n")
