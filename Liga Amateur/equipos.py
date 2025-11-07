#Importo funcion generar_id desde mi libreria utiles 
from utiles import generar_id

#Tambien importo la de tabulate para los listados. 
from tabulate import tabulate

#Lista equipos 
equipos = []

#Creo algun equipo 
equipo1 = {
    "id": 1,
    "nombre": "Tigres",
    "ciudad": "Leganes", 
    "activo": True
}

equipo2 = {
    "id": 2,
    "nombre": "Leones",
    "ciudad": "Madrid", 
    "activo": True
}

equipo3 = {
    "id": 3,
    "nombre": "Águilas", 
    "ciudad": "Barcelona", 
    "activo": True
}

equipo4 = {
    "id": 4,
    "nombre": "Panteras", 
    "ciudad": "Valencia", 
    "activo": True
}

equipo5 = {
    "id": 5,
    "nombre": "Tiburones", 
    "ciudad": "Sevilla", 
    "activo": True
}

equipo6 = {
    "id": 6,
    "nombre": "Lobos",
    "ciudad": "Bilbao", 
    "activo": True
}

#Añado los equipos a la lista equipos 
equipos.append(equipo1)
equipos.append(equipo2)
equipos.append(equipo3)
equipos.append(equipo4)
equipos.append(equipo5)
equipos.append(equipo6)

#Defino funciones 
#Crear equipo
def crear_equipo():
    id_nuevo = generar_id(equipos)
    nombre = input("Introduce el nombre del equipo:") 
    ciudad = input("Introduce el nombre de la ciudad:") 
    activo = True

    equipo_nuevo = { 
        "id": id_nuevo, 
        "nombre": nombre, 
        "ciudad": ciudad, 
        "activo": True
    }
    equipos.append(equipo_nuevo)
    print(f"El equipo {nombre} ha sido añadido correctamente a la lista equipos.")

#Listar todos los equipos activos, en tabla con tabulate. HE BUSCADO COMO HACER LO DE LA TABLA.
def listar_equipos():
    #Creo variable filas que serán los equipos activos 
    filas = []
    #Bucle for para recorrer cada equipo de la list. 
    for equipo in equipos:
        #Comprueba que esta activo y si es así imprimo los equipos activos de mi lista equipos
        if equipo['activo']:
            filas.append([equipo['id'], equipo['nombre'], equipo['ciudad'], equipo['activo']])
    #Defino ahora los encabezados de la tabla 
    columnas = ["ID", "Nombre", "Ciudad", "Activo"]
    #Por ultimo imprimo la tabla con tabulate con las filas, encabezado que serán las columnas y con su estilo.
    print(tabulate(filas, headers=columnas, tablefmt="grid"))

#Buscar equipo por ID, voy a intentar imprimir el equipo que busca como tabla, con tabulate como hemos hecho antes.
def buscar_equipo_por_id(): 
    filas = []
    id_buscar = int(input("Introduce el ID del equipo que deseas buscar:")) 
    for equipo in equipos:
        if equipo['id'] == id_buscar: 
            filas.append([equipo['id'],equipo['nombre'], equipo['ciudad'],
            equipo['activo']])

    columnas = ["ID", "Nombre", "Ciudad", "Activo"]

    #Si la longitud de mi lista filas esta vacia osea que no se ha encontrado id muestro mensaje pero si si se encuentra que siga con el proceso.
    if len(filas) > 0:
        print(tabulate(filas, headers=columnas,tablefmt="grid")) 
    else:
        (print(f"No se encontró ningún equipo con ID {id_buscar}."))

#Actualizar datos, tambien mostraré el equipo actualizado como tabla con tabulate ya que lo he aprendido.
#El id seguirá siendo el mismo. 
def actualizar_datos():
    filas = []
    id_buscar = int(input("Introduce el ID del equipo que deseas actualizar:"))
    for equipo in equipos:
        #Si el id que puso coincide con alguno de los equipos pediré que ponga los nuevos datos.
        if equipo['id'] == id_buscar:
            nombre_nuevo = input(f"Introduce el nuevo nombre para el equipo {equipo['nombre']}:")
            ciudad_nueva = input(f"Introduce la nueva ciudad para el equipo {equipo['ciudad']}:")
            #Sustituyo valores 
            if nombre_nuevo:
                equipo['nombre'] = nombre_nuevo 
            if ciudad_nueva:
                equipo['ciudad'] = ciudad_nueva
            filas.append([equipo['id'], equipo['nombre'], equipo['ciudad'], equipo['activo']])

    columnas = ["ID", "Nombre", "Ciudad", "Activo"]

    #iGUAL QUE ANTES SI NO HAY FILAS SIGNIFICA QUE NO SE HA ENCONTRADO ID POR LO TANTO NO AVANZO PERO SI HAY SIGNIFICA QUE LO ENCONTRO POR LO TANTO SIGUE EL PROCESO
    if len(filas) > 0:
        print(tabulate(filas, headers=columnas,tablefmt="grid")) 
    else:
        print(f"No se ha encontrado equipo con ID: {id_buscar}")

#eLIMINAR EQUIPO, PONER COMO INACTIVO
def eliminar_equipo():
    id_buscar = int(input("Introduce el ID del equipo que deseas eliminar/poner inactivo:"))
    for equipo in equipos:
        #Si el id que puso coincide con alguno de los equipos pediré que ponga los nuevos datos.
        if equipo['id'] == id_buscar: 
            equipo['activo'] = False
            print(f"El equipo {equipo} con id {id_buscar} ahora esta inactivo.")
            return
    print(f"No se encontro el equipo con {id_buscar}")

#MENU EQUIPO
def menu_equipos(): 
    menuEquipos = [
        "1. Crear Equipo",
        "2. Listar Equipos",
        "3. Buscar equipo por ID", 
        "4. Actualizar Equipo",
        "5. Eliminar Equipo / INACTIVO", 
        "6. Volver al menu principal"
    ]
    opcion_equipos = 0
    #Bucle while para que mientras la opcion no sea 6 siga preguntando e imprimiendo cada str del menu para que el usuario lo vea antes de meter la opcion
    while opcion_equipos != 6:
        for opcion in menuEquipos: 
            print(opcion)
        opcion_equipos = int(input("Elige una opcion del menu y si deseas volver al menu principal elige la 6:"))
#Match case con las funciones. match opcion_equipos:
        match opcion_equipos:
            case 1:
                crear_equipo() 
            case 2:
                listar_equipos() 
            case 3:
                buscar_equipo_por_id() 
            case 4:
                actualizar_datos() 
            case 5:
                eliminar_equipo() 
            case 6:
                print("Volviendo al menu principal...")
