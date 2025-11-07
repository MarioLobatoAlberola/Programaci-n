articulos = []

# Creo diccionario para cada artículo.
articulo1 = {
    "id": 1,
    "nombre": "Ratón",
    "precio": 12.5,
    "stock": 20,
    "activo": True
}

articulo2 = {
    "id": 2,
    "nombre": "Teclado",
    "precio": 15,
    "stock": 25,
    "activo": True
}

articulo3 = {
    "id": 3,
    "nombre": "Monitor",
    "precio": 50,
    "stock": 18,
    "activo": True
}

# Los guardo en mi lista articulos
articulos.append(articulo1)
articulos.append(articulo2)
articulos.append(articulo3)

# Defino funciones

# Función para generar ID
def generar_id(articulos):
    if not articulos:
        return 1
    return len(articulos) + 1

# Función para crear artículo
def crear_articulo():
    id_nuevo = generar_id(articulos)
    nombre = input("Introduce el nombre del artículo que quieres añadir: ")
    precio = float(input("Introduce el precio para tu artículo: "))
    stock = int(input("Introduce el stock disponible de tu producto: "))
    
    articulo_nuevo = {
        "id": id_nuevo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True
    }
    
    articulos.append(articulo_nuevo)
    print(f"El artículo {nombre} ha sido añadido correctamente a tu lista de artículos.")

# Función para listar artículos
def listar_articulos():
    if not articulos:
        print("No hay artículos en la tienda.")
        return
    
    for articulo in articulos:
        print(f"ID - {articulo['id']}, Nombre - {articulo['nombre']}, "
              f"Precio - {articulo['precio']}, Stock - {articulo['stock']}, "
              f"Estado - {articulo['activo']}")

# Función para buscar artículo por ID
def buscar_articulo_por_id():
    id_buscar = int(input("Introduce el ID del artículo que desees buscar: "))
    for articulo in articulos:
        if articulo['id'] == id_buscar:
            print(f"ID - {articulo['id']}, Nombre - {articulo['nombre']}, "
                  f"Precio - {articulo['precio']}, Stock - {articulo['stock']}, "
                  f"Estado - {articulo['activo']}")
            return
    print("El artículo no ha sido encontrado.")

# Función para actualizar artículo
def actualizar_articulos():
    id_buscar = int(input("Introduce el ID del artículo que desees actualizar: "))
    for articulo in articulos:
        if articulo['id'] == id_buscar:
            nuevo_nombre = input(f"Introduce el nuevo nombre que desees poner al artículo {articulo['nombre']}: ")
            if nuevo_nombre:
                articulo['nombre'] = nuevo_nombre
            
            nuevo_precio = float(input("Introduce el nuevo precio del artículo: "))
            if nuevo_precio:
                articulo['precio'] = nuevo_precio
            
            nuevo_stock = int(input("Introduce el nuevo stock del artículo: "))
            if nuevo_stock:
                articulo['stock'] = nuevo_stock
            
            print(f"{articulo['nombre']} con id: {id_buscar} ha sido actualizado.")
            return
    print("El artículo no ha sido encontrado.")

# Función para eliminar artículo
def eliminar_articulo():
    id_buscar = int(input("Introduce el ID del artículo que desees eliminar: "))
    for articulo in articulos:
        if articulo['id'] == id_buscar:
            articulos.remove(articulo)
            print(f"{articulo['nombre']} con id: {id_buscar} ha sido eliminado correctamente.")
            return
    print("El artículo no ha sido encontrado.")

# Función para alternar estado activo/inactivo
def alternar_activo():
    id_buscar = int(input("Introduce el ID del artículo que desees activar o desactivar: "))
    for articulo in articulos:
        if articulo['id'] == id_buscar:
            articulo['activo'] = not articulo['activo']
            estado = "Activo" if articulo['activo'] else "Inactivo"
            print(f"{articulo['nombre']} con id: {id_buscar} ahora está {estado}.")
            return
    print("El artículo no se ha encontrado.")
