# Creo las listas necesarias
ventas = []
carrito_actual = []

# Variable de usuario activo
usuario_activo = None

# Función para seleccionar al usuario que hará la compra
def seleccionar_usuario_activo(usuarios):
    id_usuario = int(input("Introduce el ID del usuario que hará la compra: "))
    for usuario in usuarios:
        if usuario['id'] == id_usuario and usuario['activo']:
            print(f"{usuario['nombre']} con ID {id_usuario} ha sido seleccionado correctamente.")
            return id_usuario
    print("Usuario no encontrado o inactivo.")
    return None

# Función para añadir artículo al carrito
def añadir_al_carrito(carrito, articulos, usuario_activo):
    if usuario_activo is None:
        print("Selecciona antes un usuario activo para hacer la compra.")
        return carrito

    id_articulo = int(input("Introduce el ID del artículo que deseas añadir al carrito: "))
    cantidad = int(input("Introduce la cantidad que deseas: "))

    for articulo in articulos:
        if articulo['id'] == id_articulo and articulo['activo']:
            if cantidad > articulo['stock']:
                print("No hay stock suficiente del artículo.")
                return carrito

            # Verificar si ya está en el carrito
            for i, item in enumerate(carrito):
                if item[0] == id_articulo:
                    nueva_cantidad = item[1] + cantidad
                    if nueva_cantidad > articulo['stock']:
                        print("No se puede superar el stock disponible.")
                        return carrito
                    carrito[i] = (id_articulo, nueva_cantidad)
                    print("Cantidad actualizada en el carrito.")
                    return carrito

            # Si no estaba en el carrito
            carrito.append((id_articulo, cantidad))
            print("El artículo ha sido añadido al carrito.")
            return carrito

    print("El artículo no ha sido encontrado o está inactivo.")
    return carrito

# Función para quitar artículo del carrito
def quitar_del_carrito(carrito):
    id_articulo = int(input("Introduce el ID del artículo que deseas quitar: "))
    for item in carrito:
        if item[0] == id_articulo:
            carrito.remove(item)
            print("El artículo ha sido eliminado correctamente del carrito.")
            return carrito
    print("El artículo que buscas no está en el carrito.")
    return carrito

# Función para ver carrito
def ver_carrito(carrito, articulos):
    if len(carrito) < 1:
        print("El carrito está vacío")
        return 0

    total = 0
    print("Carrito actual:")
    for item in carrito:
        id_articulo, cantidad = item
        for articulo in articulos:
            if articulo['id'] == id_articulo:
                subtotal = articulo['precio'] * cantidad
                total += subtotal
                print(f"{articulo['nombre']} - {cantidad} unidades - Subtotal: {subtotal} €")
    print(f"Total: {total} €")
    return total

# Función para confirmar compra
def confirmar_compra(carrito, articulos, usuario_activo, ventas):
    if usuario_activo is None:
        print("No hay usuario activo seleccionado.")
        return ventas, carrito

    if len(carrito) < 1:
        print("El carrito está vacío.")
        return ventas, carrito

    total = 0
    venta_items = []

    for item in carrito:
        id_articulo, cantidad = item
        for articulo in articulos:
            if articulo['id'] == id_articulo:
                if cantidad > articulo['stock']:
                    print(f"No hay suficiente stock de {articulo['nombre']}.")
                    return ventas, carrito

                articulo['stock'] -= cantidad
                subtotal = articulo['precio'] * cantidad
                total += subtotal
                venta_items.append((id_articulo, cantidad, articulo['precio']))

    id_venta = len(ventas) + 1
    venta = {
        "id_venta": id_venta,
        "usuario_id": usuario_activo,
        "items": venta_items,
        "total": total
    }

    ventas.append(venta)
    carrito = []
    print(f"Compra confirmada. Total: {total} €. Venta registrada con ID {id_venta}.")
    return ventas, carrito

# Función para ver historial de ventas por usuario
def historial_ventas_por_usuario(ventas):
    id_usuario = int(input("Introduce el ID del usuario para ver su historial: "))
    encontrado = False

    for venta in ventas:
        if venta['usuario_id'] == id_usuario:
            print(f"Venta ID {venta['id_venta']} - Total: {venta['total']} €")
            encontrado = True

    if not encontrado:
        print("No hay ventas registradas para este usuario.")

# Función para vaciar el carrito
def vaciar_carrito():
    print("Carrito vaciado correctamente.")
    return []
