#Importo librerias.
from utiles import tabulate
from utiles import generar_id
from equipos import *
from jugadores import *

#Creo lista partidos, y añadiré algun partido.
partidos = []

partido1 = {"id": 1, "jornada": 1, "local_id": 1, "visitante_id": 2, "fecha": "2025-11-22", "hora": "18:30", "jugado": False, "resultado": None}
partido2 = {"id": 2, "jornada": 1, "local_id": 3, "visitante_id": 4, "fecha": "2025-11-22", "hora": "20:30", "jugado": False, "resultado": None}
partido3 = {"id": 3, "jornada": 2, "local_id": 2, "visitante_id": 3, "fecha": "2025-11-29", "hora": "18:00", "jugado": False, "resultado": None}
partido4 = {"id": 4, "jornada": 2, "local_id": 4, "visitante_id": 1, "fecha": "2025-11-29", "hora ": "18:00", "jugado": False, "resultado": None}
partido5 = {"id": 5, "jornada": 3, "local_id": 5, "visitante_id": 6, "fecha": "2025-12-06", "hora": "18:30", "jugado": False, "resultado": None}
partido6 = {"id": 6, "jornada": 3, "local_id": 2, "visitante_id": 4, "fecha": "2025-12-06", "hora": "20:30", "jugado": False, "resultado": None}

# Añadir partidos a la lista
partidos.append(partido1)
partidos.append(partido2)
partidos.append(partido3)
partidos.append(partido4)
partidos.append(partido5)
partidos.append(partido6)

#Funciones
#Funcion para crear partido
def crear_partido():
    id_partido = generar_id(partidos)
    jornada = int(input("Introduce la jornada en la que se jugará el partido:"))
    #Condicion de que no puede ser el jornada 0
    if jornada < 1:
        print("No se puede jugar ningun partido en la jornada 0")
        return

    fecha = input("Introduce la fecha del partido (formato YYYY-MM-DD):")
    hora = input("Introduce la hora del partido (formato HH:MM):")

    local_id = int(input("Introduce el ID del equipo local:"))
    visitante_id = int(input("Introduce el ID del equipo visitante:"))
    #Condicion de que no puede ser el mismo equipo
    if local_id == visitante_id:
        print("No se pueden enfrentar los mismos equipos")
        return

    #Condicion de que ambos equipos existen y están activos
    local_valido = False
    visitante_valido = False

    for equipo in equipos:
        if local_id == equipo['id'] and equipo['activo']:
            local_valido = True
        if visitante_id == equipo['id'] and equipo['activo']:
            visitante_valido = True

    if local_valido and visitante_valido:
        print("El partido será guardado.")
        partido_nuevo = {
            'id': id_partido,
            'jornada': jornada,
            'local_id': local_id,
            'visitante_id': visitante_id,
            'fecha': fecha,
            'hora': hora,
            'jugado': False,
            'resultado': None
        }
        partidos.append(partido_nuevo)
    else:
        print("Las condiciones no se cumplen, por lo tanto el partido no se guardará.")

#Funcion de listar partidos
def listar_partidos():
    filas = []
    for partido in partidos:
        #Busco los nombres de los equipos en mi lista equipos, para añadirlos y mostrarlos.
        nombre_local = ""
        nombre_visitante = ""
        #Bucle para recorrer lista equipos
        for equipo in equipos:
            #Si un id de la lista coincide con el del equipo local en lista partidos, pondra el nombre de ese equipo en la variable nombre_local
            if equipo['id'] == partido['local_id']:
                nombre_local = equipo['nombre']
            #Igual con el visitante.
            if equipo['id'] == partido['visitante_id']:
                nombre_visitante = equipo['nombre']
        #Añado los datos a la fila
        filas.append([
            partido['id'], partido['jornada'], nombre_local, nombre_visitante,
            partido['fecha'], partido['hora'], partido['jugado'], partido['resultado']
        ])
    #Y los pongo las columnas e imprimo todo para mostrarlo como tabla.
    columnas = ["ID", "Jornada", "Local", "Visitante", "Fecha", "Hora", "Jugado", "Resultado"]
    print(tabulate(filas, headers=columnas, tablefmt="grid"))

#Ahora la funcion de reprogramar partido
def reprogramar_partido():
    #Pido que ponga un ID para buscar el partido
    buscar_id = int(input("Introduce el ID del partido que quieres reprogramar:"))
    #Bucle para recorrer lista partidos buscando el ID que coincida
    for partido in partidos:
        #Si coincide y el partido no se ha jugado, pediré nueva fecha y hora
        if partido['id'] == buscar_id and partido['jugado'] == False:
            nueva_fecha = input("Introduce la nueva fecha para el partido:")
            nueva_hora = input("Introduce la nueva hora para el partido:")
            #Una vez puestas, actualizaré los datos del partido con su nueva fecha y hora.
            partido['fecha'] = nueva_fecha
            partido['hora'] = nueva_hora
            print(f"El partido con ID: {buscar_id}, ha sido postpuesto el dia {nueva_fecha} a las {nueva_hora}.")
            return
    #Si se ha jugado o no se encuentra pondré mensaje.
    print("El partido ya se ha jugado o no se ha encontrado.")

#Funcion eliminar partido, ahora si elimino todo, no lo dejo inactivo
def eliminar_partido():
    #Pido que ponga un ID para buscar el partido
    buscar_id = int(input("Introduce el ID del partido que quieres eliminar:"))
    #Bucle para recorrer lista partidos buscando el ID que coincida para eliminarlo.
    for partido in partidos:
        if buscar_id == partido['id']:
            #Elimino el partido.
            partidos.remove(partido)
            print(f"El partido con ID: {buscar_id} ha sido suspendido.")
            return
    #Si no encuentra el partido, mensaje.
    print(f"El partido con ID: {buscar_id} no se ha encontrado.")

#Funcion del menú
def menu_calendario():
    menuCalendario = [
        "1. Crear partido",
        "2. Listar partidos",
        "3. Reprogramar partido",
        "4. Eliminar partido",
        "5. Volver al menu principal"
    ]
    opcion_calendario = 0
    while opcion_calendario != 5: 
        for opcion in menuCalendario:
            print(opcion)
        opcion_calendario = int(input("Elige una opcion del menu y si deseas volver al menu principal elige la 5:"))
        match opcion_calendario: 
            case 1:
                crear_partido() 
            case 2:
                listar_partidos() 
            case 3:
                reprogramar_partido() 
            case 4:
                eliminar_partido() 
            case 5:
                print("Volviendo al menu principal...")
