from datetime import datetime
from operator import truediv


#se crea una funcion con la que crearemos vehiculos y guardaremos la informacion en un diccionario
def ingreso_vehiculo():
    placa = input("Ingrese la placa del vehiculo: ").upper()
    #Se crea una variable para registrar el tipo de vehiculo facilmente.
    #pero hay que convertir a moto o automovil para guardarla en el diccionario
    opcion_vehiculo = input("Ingrese el número correspondiente al tipo:\n(1)Automoviles\n(2)Motocicletas ")
    if opcion_vehiculo not in ('1','2'):
        print("Opcion no valida, intenta nuevamente.")
        return None
    tipo = "Automovil" if opcion_vehiculo == '1' else "Motocicleta"
    #Para la fecha usamos una app de fecha que trae el python "datetime"
    #.strftime convierte la hora en un texto con el formato deseado. En este caso HH:MM
    hora_actual = datetime.now().strftime("%H:%M")

    #Creamos el diccionario de vehiculos. Esto alimentara la lista en el archivo main
    vehiculo = {
        "id": (placa, tipo),
        "hora_entrada": hora_actual,
        "hora_salida": ""
    }
    return vehiculo

#Ahora se crea una funcion que va a agregar el vehiculo ingresado a la lista del main
#Tambien revisa si ya existe
#Nota.. se crea en el main un diccionario llamado estado que se llamara con la siguiente funcion, registra la cantidad de parqueaderos

def agregar_vehiculo(listaVehiculos,estado):
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
            else: estado["celdas_automoviles"]-=1
        elif nuevo_vehiculo['id'][1] == 'Motocicleta':
            if estado["celdas_motocicletas"] == 0:
                print("🚫No hay celdas disponibles para motocicletas.")
                return False
            else: estado["celdas_motocicletas"]-=1
        listaVehiculos.append(nuevo_vehiculo)
        print(f"✅ Vehiculo {nuevo_vehiculo['id'][0]} agregado")
        return True
    return False

# Esta funcion se encarga de registrar la hora de salida y de retirar el vehiculo de la lista
# Tambien aumenta las celdas disponibles
def registrar_salida(listaVehiculos,estado):
    placa = input("Ingrese la placa del vehiculo: ").upper()
    for vehiculo in listaVehiculos:
        if vehiculo['id'][0] == placa:
            hora_salida = input("Ingrese la hora de salida:(formato HH:MM:  ")
            vehiculo["hora_salida"] = hora_salida
            if vehiculo['id'][1] == 'Automovil':
                estado["celdas_automoviles"] += 1
            elif vehiculo['id'][1] == 'Motocicleta':
                estado["celdas_motocicletas"] += 1
            listaVehiculos.remove(vehiculo)
            print(f"✅ Vehiculo {placa} retirado del parqueadero.")
            return True
    print("🚫 Vehiculo no encontrado.")
    return False

def mostrar_estado(estado):
    print("\n📊 Estado actual del parqueadero:")
    print(f"Celdas disponibles para automóviles: {estado['celdas_automoviles']}")
    print(f"Celdas disponibles para motocicletas: {estado['celdas_motocicletas']}\n")