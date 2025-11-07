#Importo todas las librerias. import equipos
import jugadores 
import calendario 
import ranking
import equipos
#Menu principal 
menuPrincipal = [
"1. Gestion de equipos",
"2. Gestion de jugadores",
"3. Calendario de partidos", 
"4. Resultados y clasificacion", 
"5. Salir"
]
opcion_principal = 0
while opcion_principal != 5: 
    for opcion in menuPrincipal:
        print(opcion)
    opcion_principal = int(input("Elige una opcion del menu principal y si deseas volver salir pon la 5:"))
    match opcion_principal: 
        case 1:
            equipos.menu_equipos() 
        case 2:
            jugadores.menu_jugadores() 
        case 3:
            calendario.menu_calendario() 
        case 4:
            ranking.menu_ranking() 
        case 5:
            print("Hasta pronto.")
