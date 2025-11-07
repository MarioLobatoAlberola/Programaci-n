# Importo librerías
from utiles import tabulate
from utiles import generar_id
from equipos import *
from jugadores import *
from calendario import *

# Funciones

# Función de registrar resultado
def registrar_resultado():
    buscar_id = int(input("Introduce el ID del partido para guardar su resultado:"))
    for partido in partidos:
        # Si el ID que puso coincide con uno y ese partido no se ha jugado.
        if buscar_id == partido['id'] and not partido['jugado']:
            goles_local = int(input("Introduce los goles que ha metido el equipo local:"))
            goles_visitante = int(input("Introduce los goles que ha metido el equipo visitante:"))

            if goles_local >= 0 and goles_visitante >= 0:
                partido['resultado'] = (goles_local, goles_visitante)
                partido['jugado'] = True
                print(f"El resultado del partido con ID: {buscar_id} es: {partido['resultado']}")
                # Saldrá de la función una vez muestre mensaje
                return
    # Si no lo encuentra mostraré mensaje de que no lo encuentra.
    print("El partido no se ha encontrado o ya se ha jugado. ")

# Función de clasificación
def clasificacion():
    filas = []
    # Recorro todos los equipos
    for equipo in equipos:
        # Declaro todas las variables necesarias
        puntos = 0
        ganados = 0
        empates = 0
        perdidos = 0
        gf = 0
        gc = 0
        dg = 0

        # Bucle for para recorrer cada partido en lista partidos para sumar estadísticas
        for partido in partidos:
            goles_local, goles_visitante = partido['resultado']

            # Si el equipo es local
            if partido['local_id'] == equipo['id']:
                gf += goles_local
                gc += goles_visitante

                # PARTIDOS GANADO
                # GANADO DESDE PUNTO DE VISTA LOCAL
                if goles_local > goles_visitante:
                    puntos += 3
                    ganados += 1
                # EMPATADO DESDE PUNTO DE VISTA LOCAL
                elif goles_local == goles_visitante:
                    puntos += 1
                    empates += 1
                # PERDIDO DESDE PUNTO DE VISTA LOCAL
                else:
                    perdidos += 1

            # Si el equipo es visitante
            if partido['visitante_id'] == equipo['id']:
                gf += goles_visitante
                gc += goles_local

                # GANADO DESDE PUNTO DE VISTA VISITANTE
                if goles_visitante > goles_local:
                    ganados += 1
                    puntos += 3
                # EMPATADO DESDE PUNTO DE VISTA VISITANTE
                elif goles_visitante == goles_local:
                    empates += 1
                    puntos += 1
                # PERDIDO DESDE PUNTO DE VISTA VISITANTE
                else:
                    perdidos += 1

        # Así se calcula la diferencia de goles
        dg = gf - gc

        # Guardamos las estadísticas directamente en el equipo
        equipo['puntos'] = puntos
        equipo['ganados'] = ganados
        equipo['empates'] = empates
        equipo['perdidos'] = perdidos
        equipo['gf'] = gf
        equipo['gc'] = gc
        equipo['dg'] = dg

        # Ahora mostraré todo como tabla.
        filas.append([
            equipo['nombre'], puntos,
            ganados, empates, perdidos, gf,
            gc, dg
        ])

    # Ordeno por puntos desc, luego diferencia de goles, luego goles a favor
    filas_ordenadas = sorted(filas, key=lambda x: (x[1], x[7], x[5]), reverse=True)

    # Encabezado de la tabla
    columnas = ["Equipo", "Puntos", "G", "E", "P", "GF", "GC", "DG"]

    # Imprimo la tabla con tabulate
    print(tabulate(filas_ordenadas, headers=columnas, tablefmt="grid"))

# Función de estadísticas por equipo
# Solo funcionará si en clasificación ya está relleno con estadísticas.
def estadisticas_por_equipo():
    filas = []
    id_buscar = int(input("Introduce el ID del equipo que quieras buscar:"))
    for equipo in equipos:
        if id_buscar == equipo['id']:
            filas.append([
                equipo['nombre'],
                equipo['puntos'],
                equipo['ganados'],
                equipo['empates'],
                equipo['perdidos'],
                equipo['gf'],
                equipo['gc'],
                equipo['dg']
            ])
            print(tabulate(filas, headers=["Equipo", "Puntos", "G", "E", "P", "GF", "GC", "DG"], tablefmt="grid"))
            return
    print("No se ha encontrado ningún equipo con ese ID.")

#Funcion de menu def menu_ranking():
menuRanking = [
"1. Registrar resultado",
"2. Clasificacion",
"3. Estadisticas por equipo", "4. Volver al menu principal"
]
opcion_ranking = 0
while opcion_ranking != 4:
    for opcion in menuRanking: 
        print(opcion)
    opcion_ranking = int(input("Elige una opcion del menu y si quieres volver al menu principal elige la 4:"))
    match opcion_ranking: 
        case 1:
            registrar_resultado() 
        case 2:
            clasificacion() 
        case 3:
            estadisticas_por_equipo() 
        case 4:
            print("Volviendo al menu principal...")
