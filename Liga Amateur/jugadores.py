#Importo librerias necesarias
from utiles import generar_id
from equipos import *
from utiles import tabulate

#Lista jugadores, y creo jugadores y los meto en mi lista. Ahora sin append, los meto directamente.
jugadores = [
    {"id": 1, "nombre": "Laura", "posicion": "Delantera", "equipo_id": 1, "activo": True},
    {"id": 2, "nombre": "Carlos", "posicion": "Portero", "equipo_id": 1, "activo": True},
    {"id": 3, "nombre": "Marta", "posicion": "Defensa", "equipo_id": 2, "activo": True},
    {"id": 4, "nombre": "Javier", "posicion": "Centrocampista", "equipo_id": 2, "activo": True},
    {"id": 5, "nombre": "Lucia", "posicion": "Delantera", "equipo_id": 3, "activo": True},
    {"id": 6, "nombre": "Pablo", "posicion": "Defensa", "equipo_id": 3, "activo": True},
    {"id": 7, "nombre": "Elena", "posicion": "Centrocampista", "equipo_id": 4, "activo": False},
    {"id": 8, "nombre": "Diego", "posicion": "Portero", "equipo_id": 4, "activo": True},
    {"id": 9, "nombre": "Sofia", "posicion": "Delantera", "equipo_id": 5, "activo": True},
    {"id": 10, "nombre": "Andres", "posicion": "Defensa", "equipo_id": 5, "activo": False}
]

#Defino funciones
def alta_jugador():
    #Genero ID con funcion creada
    id_nuevo = generar_id(jugadores)
    nombre = input("Introduce el nombre del jugador que quieres dar de alta:")
    posicion = input("Introduce la posicion del jugador:")
    equipo_id = int(input("Introduce el ID del equipo al que pertenecerá:"))

    #Declaro variable equipo encontrado y la pongo como false
    equipo_encontrado = False

    #Bucle for para recorrer equipo en lista equipos
    for equipo in equipos:
        #Si el id que puso coincide con alguno de la lista y esta activo
        if equipo_id == equipo['id'] and equipo['activo']:
            #Variable equipo encontrado sera true
            equipo_encontrado = True

    #Otra condicion de que si lo hemos encontrado daremos de alta al jugador.
    if equipo_encontrado:
        print(f"El equipo al que {nombre} va a pertenecer existe, por lo tanto será dado de alta.")
        jugador_nuevo = {
            "id": id_nuevo,
            "nombre": nombre,
            "posicion": posicion,
            "equipo_id": equipo_id,
            "activo": True
        }
        jugadores.append(jugador_nuevo)
        print(f"Jugador {nombre} dado de alta correctamente.")
    else:
        print(f"El equipo al que {nombre} va a pertenecer NO existe o esta inactivo, asique no será dado de alta.")


#Funcion listar jugadores, lo haré con tabulate para que se vea como tabla.
def listar_jugadores():
    filas = []
    for jugador in jugadores:
        filas.append([jugador['id'], jugador['nombre'], jugador['posicion'], jugador["equipo_id"], jugador['activo']])
    #Defino ahora los encabezados de la tabla
    columnas = ["ID", "Nombre", "Posicion", "ID EQUIPO", "Activo"]
    #Por ultimo imprimo la tabla con tabulate con las filas, encabezado que serán las columnas y con su estilo.
    print(tabulate(filas, headers=columnas, tablefmt="grid"))


#Funcion buscar_por_id, con tabulate para formato tabla.
def buscar_jugador_por_id():
    filas = []
    buscar_id = int(input("Introduce el ID del jugador que deseas buscar:"))
    for jugador in jugadores:
        if buscar_id == jugador['id']:
            filas.append([jugador['id'], jugador['nombre'], jugador['posicion'], jugador['equipo_id'], jugador['activo']])
    columnas = ["ID", "Nombre", "Posicion", "ID EQUIPO", "Activo"]

    #Si hay filas se hace la tabla si no, muestro mensaje porque no se ha encontrado.
    if len(filas) > 0:
        print(tabulate(filas, headers=columnas, tablefmt="grid"))
    else:
        (print(f"No se encontró ningún equipo con ID {buscar_id}."))


#Funcion para actualizar jugador.
def actualizar_jugador():
    filas = []
    buscar_id = int(input("Introduce el ID del jugador que deseas actualizar:"))
    for jugador in jugadores:
        if buscar_id == jugador['id']:
            nombre_nuevo = input("Introduce el nombre nuevo para el jugador:")
            posicion_nueva = input("Introduce la nueva posicion del jugador:")
            id_nuevo_equipo = int(input("Introduce ID del equipo al que pertenecerá el jugador:"))

            #Verificar que el equipo existe y está activo.
            verificar_equipo = False
            for equipo in equipos:
                if id_nuevo_equipo == equipo['id'] and equipo['activo']:
                    verificar_equipo = True

            #Si está verificado actualizo datos
            if verificar_equipo:
                print(f"El equipo existe, y esta activo, por lo tanto {nombre_nuevo} con ID {buscar_id} será actualizado. ")
                #Sustituirá lo que se ponga en nombre_nuevo, etc por lo que hay, osea actualizará
                jugador['nombre'] = nombre_nuevo
                jugador['posicion'] = posicion_nueva
                jugador['equipo_id'] = id_nuevo_equipo
                filas.append([jugador['id'], jugador['nombre'], jugador['posicion'], jugador['equipo_id'], jugador['activo']])

    columnas = ["ID", "Nombre Nuevo", "Posicion Nueva", "Equipo Nuevo", "Activo"]

    #iGUAL QUE ANTES SI NO HAY FILAS SIGNIFICA QUE NO SE HA ENCONTRADO ID POR LO TANTO NO AVANZO PERO SI HAY SIGNIFICA QUE LO ENCONTRO POR LO TANTO SIGUE EL PROCESO
    if len(filas) > 0:
        print(f"Jugador {nombre_nuevo} actualizado correctamente.")
        print(tabulate(filas, headers=columnas, tablefmt="grid"))
    else:
        print(f"No se ha encontrado jugador con ID: {buscar_id} o el equipo al que va a pertenecer no existe o esta inactivo, asique no sera actualizado.")


#Funcion Eliminar/inactivar jugador
def eliminar_jugador():
    id_eliminar = int(input("Introduce el ID del jugador que deseas poner como inactivo:"))
    for jugador in jugadores:
        if id_eliminar == jugador['id']:
            jugador['activo'] = False
            print(f"El jugador {jugador['nombre']} con id {id_eliminar} ahora esta inactivo.")
            return
    print(f"No se encontro el jugador con {id_eliminar}, o ya esta inactivo.")


#Funcion menu jugadores
def menu_jugadores():
    menuJugadores = [
        "1. Dar de alta jugador",
        "2. Listar jugadores",
        "3. Buscar jugador por ID",
        "4. Actualizar jugador",
        "5. Eliminar/desactivar jugador",
        "6. Volver al menu principal"
    ]
    opcion_jugadores = 0
    while opcion_jugadores != 6:
        for opcion in menuJugadores:
            print(opcion)
        opcion_jugadores = int(input("Elige una opcion del menu y si deseas volver al menu principal elige la 6:"))
        match opcion_jugadores:
            case 1:
                alta_jugador()
            case 2:
                listar_jugadores()
            case 3:
                buscar_jugador_por_id()
            case 4:
                actualizar_jugador()
            case 5:
                eliminar_jugador()
            case 6:
                print("Volviendo al menu principal...")