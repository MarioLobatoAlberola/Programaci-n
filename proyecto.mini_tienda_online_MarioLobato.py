#ENTREGA 1 MARIO LOBATO
#Creo lista vacía para ir metiendo mis articulos, la llamo articulos
articulos = []
#Creo diccionario para cada artículo.
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
#Los guardo en mi lista articulos
articulos.append(articulo1)
articulos.append(articulo2)
articulos.append(articulo3)
#Defino funciones
#La primera será generar_id, si no hay articulos mide con len la longitud de articulos que hay por lo tanto si hay 3 articulos me dará el proximo id como 4
def generar_id(articulos):
    if not articulos:
        return 1
    return len(articulos) + 1
#La segunda será crear artículo en la que pediré cada clave del diccionario necesario y que el usuario meta su valor
def crear_articulo():
    #En el nuevo ID para este articulo, llamaré a la función generar_id para que me haga uno nuevo.
    id_nuevo = generar_id(articulos)
    nombre = input("Introduce el nombre del articulo que quieres añadir:")
    #Pido demas valores del artículo
    precio = float(input("Introduce el precio para tu artículo:"))
    stock = int(input("Introduce el stock disponible de tu producto:"))
    #Lo añado a la lista articulos y lo guardaré como diccionario igual que los demás artículos.
    articulo_nuevo = {
        "id": id_nuevo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True
    }
    articulos.append(articulo_nuevo)
    print(f"El articulo {nombre} ha sido añadido correctamente a tu lista articulos.")

#Ahora defino funcion para listar los articulos de mi lista, si no hay, pongo mensaje de que no hay, pero si hay creo bucle for que recorra cada articulo de mi lista articulos e imprimo todas las claves junto a los valores correspondientes de cada uno.
def listar_articulos():
    #Si no hay artículos, mostrar mensaje de que no hay
    if not articulos:
        print("No hay artículos en la tienda.")
        #Pero si hay, creo bucle for para recorrer todos cada articulo de mi lista articulos, y los muestro con su respectivo valor.
        return
    for articulo in articulos:
        #Pongo comillas ya que no esta definido.
        print(f"ID - {articulo['id']}, Nombre - {articulo['nombre']}, Precio - {articulo['precio']}, Stock - {articulo['stock']}, Estado - {articulo['activo']}")

#Ahora defino la función de buscar artículo por i
def buscar_articulo_por_id():
    id_buscar = int(input("Introduce el ID del articulo que desees buscar:"))   
    for articulo in articulos:
        if articulo['id'] == id_buscar:
            print(f"ID - {articulo['id']}, Nombre - {articulo['nombre']}, Precio - {articulo['precio']}, Stock - {articulo['stock']}, Estado - {articulo['activo']}")
            return #Saldrá de la función al encontrar el artículo.
    #Si no lo encuentra mostrar mensaje de que no lo encuentra
    print("El articulo no ha sido encontrado.")

#Ahora defino funcion para actualizar articulos
def actualizar_articulos():
    id_buscar = int(input("Introduce el ID del articulo que desees actualizar:"))
    #Bucle for para que recorra cada articulo en lista articulos.
    for articulo in articulos:
        #Y si coincide con el que se busca
        if articulo['id'] == id_buscar:
            #Pido que introduzca el nuevo nombre que desea poner a este articulo
            nuevo_nombre = input(f"Introduce el nuevo nombre que desees poner al articulo {articulo['nombre']}")
            #Hago que el nuevo nombre sustituya al que había actualizandolo.
            if nuevo_nombre:
                articulo['nombre'] = nuevo_nombre
            #Igual con cada valor, ahora precio
            nuevo_precio = float(input("Introduce el nuevo precio del artículo:"))
            if nuevo_precio:
                articulo['precio'] = nuevo_precio

            #Ahora stock
            nuevo_stock = int(input("Introduce el nuevo stock del artículo:"))
            if nuevo_stock:
                articulo['stock'] = nuevo_stock
            #Imprimo que el articulo ha sido actualizado
            print(f" {articulo['nombre']} con id: {id_buscar} ha sido actualizado")
            return
        #Si no se encuentra el articulo, muestro mensaje.
    print("El artículo no ha sido encontrado.")

#Defino función ahora para eliminar un artículo.
def eliminar_articulo():
    id_buscar = int(input("Introduce el ID del articulo que desees eliminar:"))
    #Para cada articulo en lista articulos
    for articulo in articulos:
        #Si el id que  busca es igual a alguno en la lista articulos, que borre ese articulo.
        if articulo['id'] == id_buscar:
            articulos.remove(articulo)
            print(f" {articulo['nombre']} con id: {id_buscar} ha sido eliminado correctamente.")
            return
    print("El artículo no ha sido encontrado.")

#Defino función para alternar entre activo e inactivo.   
def alternar_activo():
    id_buscar = int(input("Introduce el ID del articulo que desees activar o desactivar:"))
    #Es el mismo proceso que en anteriores con id_buscar 
    for articulo in articulos:
        if articulo['id'] == id_buscar:
            #Cambia de true a false o al revés
            articulo['activo'] = not articulo['activo']
            #Si el estado es activo pasará a inactivo y viceversa.
            estado = "Activo" if articulo['activo'] else "Inactivo"       
            print(f"{articulo['nombre']} con id: {id_buscar} ahora esta {estado}.")
            return
    print("El artículo no se ha encontrado.")

#Defino función de menú principal
def menu(): 
    print("""
1. Crear artículo
2. Listar artículos
3. Buscar artículo por id
4. Actualizar artículo
5. Eliminar artículo
6. Alternar activo/inactivo
7. Salir
""")

#Ya no llamo al menu porque le llamo abajo     

#ENTREGA 2 USUARIOS
#Creo lista vacía para ir metiendo mis usuarios, la llamo usuarios
usuarios = []
#Creo diccionario para cada artículo.
usuario1 = {
    "id": 1,
    "nombre": "Ana",
    "email": "ana@example.com",
    "activo": True
}
usuario2 = {
    "id": 2,
    "nombre": "Mario",
    "email": "Mario@example.com",
    "activo": True
}
usuario3 = {
    "id": 3,
    "nombre": "Carlos",
    "email": "Carlos@example.com",
    "activo": True
}

#Los guardo en mi lista articulos
usuarios.append(usuario1)
usuarios.append(usuario2)
usuarios.append(usuario3)
#Defino funciones
#Funcion de generar id
def generar_id(usuarios):
    if not usuarios:
        return 1
    return len(usuarios) + 1

#FUNC CREAR USUARIO
def crear_usuario():
    id_nuevo = generar_id(usuarios)
    nombre = input("Introduce el nombre del usuario que quieres añadir:")
    #Pido demas valores del usuario
    email = input("Introduce el email para tu usuario:")
    #Lo añado a la lista usuarios y lo guardaré como diccionario igual que los demás usuarios
    usuario_nuevo = {
        "id": id_nuevo,
        "nombre": nombre,
        "email": email,
        "activo": True
    }
    usuarios.append(usuario_nuevo)
    print(f"El usuario {nombre} ha sido añadido correctamente a tu lista usuarios.")

#Ahora defino funcion para listar los usuarios de mi lista, si no hay, pongo mensaje de que no hay, pero si hay creo bucle for que recorra cada usuario de mi lista usuarios e imprimo todas las claves junto a los valores correspondientes de cada uno.
def listar_usuarios():
    #Si no hay usuarios, mostrar mensaje de que no hay
    if not usuarios:
        print("No hay usuarios disponibles.")
        #Pero si hay, creo bucle for para recorrer todos cada usuario de mi lista usuarios, y los muestro con su respectivo valor.
        return
    for usuario in usuarios:
        #Pongo comillas ya que no esta definido.
        print(f"ID - {usuario['id']}, Nombre - {usuario['nombre']}, , Email - {usuario['email']}, Estado - {usuario['activo']}")
    
#Ahora defino la función de buscar artículo por i
def buscar_usuario_por_id():
    id_buscar = int(input("Introduce el ID del usuario que deseas buscar:"))   
    for usuario in usuarios:
        if usuario['id'] == id_buscar:
            print(f"ID - {usuario['id']}, Nombre - {usuario['nombre']}, , Email - {usuario['email']}, Estado - {usuario['activo']}")
            return #Saldrá de la función al encontrar el usuario.
    #Si no lo encuentra mostrar mensaje de que no lo encuentra
    print("El usuario no ha sido encontrado.")

#Ahora defino funcion para actualizar usuario
def actualizar_usuario():
    id_buscar = int(input("Introduce el ID del articulo que desees actualizar:"))
    #Bucle for para que recorra cada usuario en lista usuarios.
    for usuario in usuarios:
        #Y si coincide con el que se busca
        if usuario['id'] == id_buscar:
            #Pido que introduzca el nuevo nombre que desea poner a este usuario
            nuevo_nombre = input(f"Introduce el nuevo nombre que desees poner al usuario {usuario['nombre']}")
            #Hago que el nuevo nombre sustituya al que había actualizandolo.
            if nuevo_nombre:
                usuario['nombre'] = nuevo_nombre
            #Igual con cada valor, ahora precio
            nuevo_email = input("Introduce el nuevo email del usuario:")
            if nuevo_email:
                usuario['email'] = nuevo_email
            #Imprimo que el articulo ha sido actualizado
            print(f" {usuario['nombre']} con id: {id_buscar} ha sido actualizado")
            return
        #Si no se encuentra el usuario, muestro mensaje.
    print("El usuario no ha sido encontrado.")

#Defino función ahora para eliminar un usuario.
def eliminar_usuario():
    id_buscar = int(input("Introduce el ID del usuario que desees eliminar:"))
    #Para cada usuario en la lista usuarios
    for usuario in usuarios:
        #Si el id que  busca es igual a alguno en la lista usuarios, que borre ese articulo.
        if usuario['id'] == id_buscar:
            usuarios.remove(usuario)
            print(f" {usuario['nombre']} con id: {id_buscar} ha sido eliminado correctamente.")
            return
    print("El usuario no ha sido encontrado.")

#Defino función para alternar entre activo e inactivo.   
def alternar_usuario_activo():
    id_buscar = int(input("Introduce el ID del usuario que desees activar o desactivar:"))
    #Es el mismo proceso que en anteriores con id_buscar 
    for usuario in usuarios:
        if usuario['id'] == id_buscar:
            #Cambia de true a false o al revés
            usuario['activo'] = not usuario['activo']
            #Si el estado es activo pasará a inactivo y viceversa.
            estado = "Activo" if usuario['activo'] else "Inactivo"       
            print(f"{usuario['nombre']} con id: {id_buscar} ahora esta {estado}.")
            return
    print("El usuario no se ha encontrado.")

#Defino el menu principal
def menu_principal_final():
    print("""
MENU PRINCIPAL
1. Gestion de Articulos
2. Gestion de Usuarios
3. Usuarios y ventas
3. Salir
""")

#Defino el menu de gestión de usuarios
def menu_usuarios():
    print("""
GESTIÓN DE USUARIOS
1. Crear usuario
2. Listar usuarios
3. Buscar usuario por ID
4. Actualizar usuario
5. Eliminar usuario
6. Alternar activo/inactivo
7. Volver
""" )

#Ahora que ya tengo los 3 menús, el de articulos ya lo tenia en la entrega 1 y el principal y el de usuarios los he hecho ahora.
#Ahora muestro primero el menú principal y elegirá entre el menú articulos y el usuario, dependiendo de cual elija le meto en uno o en otro.
#Creo primer bucle para el menu principal
#Borraré en la entrega 1 la llamada al menú artículos para que no salga ahora y salga en su lugar el menu principal.
#BORRO MENU PARA QUE NO SE ME PEGUE CON EL DE LA ENTREGA 3


#ENTREGA 3 MARIO LOBATO
#Creo las listas necesarias, de ventas, carrito actual.
ventas = []
carrito_actual = []

#También creo variable de usuario_activo
usuario_activo = None

#Defino funciones de carrito y de ventas
#Primero función de seleccionar al usuario que hara la compra
def seleccionar_usuario_activo(usuarios):
    #Pido que introduzca un id para buscar al usuario que hará la compra
    id_usuario = int(input("Introduce el ID del usuario que hará la compra:"))
    #Bucle for para recorrer cada usuario en lista usuarios
    for usuario in usuarios:
        #Si el id que ha puesto coincide con uno de la lista, y esta activo.
        if usuario['id'] == id_usuario and usuario ['activo']:
            #Imprimo que ese usuario ha sido seleccionado para hacer la compra.
            print(f"{usuario['nombre']} con {id_usuario} ha sido seleccionado correctamente.")
            #Devuelve el id_usuario
            return id_usuario
    #Si no encuentra nada o esta inactivo, mostrar mensaje.    
    print("Usuario no encontrado o inactivo.")
    return None
#Ahora defino funcion de añadir al carrito.
def añadir_al_carrito(carrito, articulos, usuario_activo):
    #Compruebo que si no hay usuario para hacer la compra que muestre mensaje de que no hay.
    if usuario_activo is None:
        print("Selecciona antes de comprar un usuario para hacer la compra.")
        #Devuelvo el carrito vacío
        return carrito
    #Pido el id de artículo y la cantidad que quiere.
    id_articulo = int(input("Introdce el ID del artículo que deseas añadir al carrito:"))
    cantidad = int(input("Introduce la cantidad que deseas:"))

    #Buscamos el articulo en la lista articulos para ver si esta
    for articulo in articulos:
        #Si el id que ha puesto coincide con alguno de la lista articulos y solo si esta activo y si hay stock se añadirá
        if articulo['id'] == id_articulo and articulo['activo']:
            #Y también si no supera el stock del mismo artículo
            if cantidad > articulo['stock']:
                print("No hay stock del articulo que buscas.")
                return carrito
            #Compruebo también si está también en el carrito y sumo cantidades
            #Para ello creo bucle for para recorrer cada elemento en este caso el item del carrito y enumerate devuelve cada elemento con sus valores
            for i, item in enumerate(carrito):
                #Compruebo que si el articulo que el usuario quiere añadir está en el carrito item[0] se refiere a ID y [1] a cantidad.
                if item[0] == id_articulo:
                    #Si ya está sumo la cantidad que ya estaba con la cantidad que el usuario quiere añadir
                    nueva_cantidad = item[1] + cantidad
                    #Si la nueva cantidad supera al stock mostraré mensaje de que no se puede hacer eso.
                    if nueva_cantidad > articulo['stock']:
                        print("No se puede superar el stock disponible.")
                        #Devuelvo el carrito.
                        return carrito
                    #Se actualiza la cantidad, con la i que es el indice del articulo en mi lista y los nuevos valores.
                    carrito[i] = (id_articulo, nueva_cantidad)
                    print("Cantidad actualizada en el carrito:")
                    return carrito
            carrito.append((id_articulo, cantidad))
            print("El artículo ha sido añadido al carrito.")
            return carrito
    #Si no lo encuentra o esta inactivo
    print("El artículo no ha sido encontrado o esta inactivo.")
    return carrito

#Función para quitar articulo del carrito
def quitar_del_carrito(carrito):
    id_articulo = int(input("Introduce el ID del artículo que deseas quitar:"))
    #Creo bucle for para recorrer cada elemento de mi carrito
    for item in carrito:
        #Si algun id del carrito coincide con el id que ha puesto el usuario, lo borraré del carrito
        if item[0] == id_articulo:
            carrito.remove(item)
            print("El artículo ha sido eliminado correctamente del carrito.")
            #Y devolveré 0
            return carrito
    print("El artículo que buscas no esta en el carrito.")
    return carrito

#Funcion para ver carrito
def ver_carrito(carrito, articulos):
    #Si hay menos de un artículo mostrar mensaje que diga que esta vacío
    if len(carrito) < 1:
        print("El carrito esta vacío")
        return 0
    
    #Creo variable para acumular el total del carrito. 
    total = 0 
    print("Carrito actual")
    #Recorro cada articulo del carrito
    for item in carrito:
        #Desempaqueto la tupla
        id_articulo, cantidad = item
        #Busco el artículo correspondiente en la lista articulos
        for articulo in articulos:
            #Si coincide calcularé el subtotal
            if articulo['id'] == id_articulo:
                subtotal = articulo['precio'] * cantidad
                #Y lo sumaré al total general
                total += subtotal
                #Muestro nombre, cantidad y subtotal de cada artículo
                print(f"{articulo['nombre']} - {cantidad} unidades - Subtotal: {subtotal} $")
    print(f"Total: {total}$")
    return total

#Defino funcion para confirmar compra.
def confirmar_compra(carrito, articulos, usuario_activo, ventas):
    #Compruebo que hay un usuario activo
    if usuario_activo is None:
        print("No hay usuario activo seleccionado.")
        #Asique devuelvo las listas sin cambios
        return ventas, carrito
    #Compruebo que el carrito no esta vacío
    if len(carrito) < 1:
        print("El carrito esta vacío.")
        return ventas, carrito
    
    #Creo variables, la de total para acumular el total de la compra, una lista vacia de elementos que se registrarán en la venta.
    total = 0
    venta_items = []

    #Recorremos cada artículo del carrito
    for item in carrito:
        id_articulo, cantidad = item
        #Busco el articulo en la lista articulos
        for articulo in articulos:
            if articulo['id'] == id_articulo:
                #Valido también que hay suficiente stock
                #Si no hay stock de ese articulo, muestro mensaje y devuelvo las listas
                if cantidad > articulo['stock']:
                    print(f"No hay suficiente stock de {articulo['nombre']}.")
                    return ventas, carrito
                #Pero si hay restaré la cantidad que elija el usuario al stock del articulo.
                articulo['stock'] -= cantidad
                #Calculo también el subtotal
                subtotal = articulo['precio'] * cantidad
                #Y lo sumo al total
                total += subtotal
                # Guardamos un "snapshot" de la venta: id, cantidad y precio.LO HE BUSCADO
                #Significa registro exacto en el momento.
                #Guardamos el precio tal como estaba al comprar, aunque después cambie en la lista de artículos.
                venta_items.append((id_articulo, cantidad, articulo['precio']))
    
    #Creo el diccionario de la venta
    id_venta = len(ventas) + 1 #Id incremental
    venta = {
        "id_venta": id_venta,
        "usuario_id": usuario_activo,
        "items": venta_items,
        "total": total
    }
    #Añadiré la venta a mi lista de ventas
    ventas.append(venta)
    #Vacio el carrito cuando acabe la compra.
    carrito = []
    print(f"Compra confirmada. Total: {total}€. Venta registrada con ID {id_venta}.")
    #Devuelvo listas actualizadas
    return ventas, carrito

# Función para ver historial de ventas por usuario
def historial_ventas_por_usuario(ventas):
    id_usuario = int(input("Introduce el ID del usuario para ver su historial: "))
    #Booleano para saber si encuentra ventas o no
    encontrado = False  
    #Creo bucle for para cada recorrer cada venta en ventas
    for venta in ventas:
        #Si un id coincide con el que ha puesto el usuario, buscará la venta de dicho usuario
        if venta['usuario_id'] == id_usuario:
            #Muestro la venta encontrada de ese usuario
            print(f"Venta ID {venta['id_venta']} - Total: {venta['total']}€")
            #Si esto pasa el bool será verdadero porque lo ha encontrado.
            encontrado = True
    #Si no hay ventas para este usuario, avisaré de ello con un mensaje
    if not encontrado:
        print("No hay ventas registradas para este usuario.")

#Funcion para vaciar el carrito
def vaciar_carrito():
    print("Carrito vaciado correctamente.")
    #Devuelvo lista vacía
    return[]

#Por ultimo la funcion del menu
# Menú de ventas
def menu_ventas():
    print("""
=== MENÚ DE VENTAS ===
1. Seleccionar usuario activo
2. Añadir artículo al carrito
3. Quitar artículo del carrito
4. Ver carrito
5. Confirmar compra
6. Historial de ventas por usuario
7. Vaciar carrito
8. Volver
""")

#Defino el menu principal final
def menu_principal_final():
    print("""
MENU PRINCIPAL
1. Gestion de Articulos
2. Gestion de Usuarios
3. Ventas y carrito
4. Salir
""")
    
#Inicio variables principales para el menú, y borro las de la entrega dos porque si no se me mezcla todo
#BORRO EL MENU DE LA ENTREGA 2
opcion_principal = 0
usuario_activo = None

while opcion_principal != 4:
    menu_principal_final()
    opcion_principal = int(input("Introduce una opcion del menu principal y si deseas salir escribe 4: "))
    match opcion_principal:
        case 1:
            opcion_articulos = 0
            while opcion_articulos != 7:
                menu()
                opcion_articulos = int(input("Introduce una opcion del menu de articulos y si deseas salir escribe 7: "))
                match opcion_articulos:
                    case 1:
                        crear_articulo()
                    case 2:
                        listar_articulos()
                    case 3:
                        buscar_articulo_por_id()
                    case 4:
                        actualizar_articulos()
                    case 5:
                        eliminar_articulo()
                    case 6:
                        alternar_activo()
        case 2:
            opcion_usuarios = 0
            while opcion_usuarios != 7:
                menu_usuarios()
                opcion_usuarios = int(input("Introduce una opcion del menu de usuarios y si deseas salir escribe 7: "))
                match opcion_usuarios:
                    case 1:
                        crear_usuario()
                    case 2:
                        listar_usuarios()
                    case 3:
                        buscar_usuario_por_id()
                    case 4:
                        actualizar_usuario()
                    case 5:
                        eliminar_usuario()
                    case 6:
                        alternar_usuario_activo()
        case 3:
            opcion_ventas = 0
            while opcion_ventas != 8:
                menu_ventas()
                opcion_ventas = int(input("Introduce una opcion del menu de ventas y si deseas volver escribe 8: "))
                match opcion_ventas:
                    case 1:
                        usuario_activo = seleccionar_usuario_activo(usuarios)
                    case 2:
                        carrito_actual = añadir_al_carrito(carrito_actual, articulos, usuario_activo)
                    case 3:
                        carrito_actual = quitar_del_carrito(carrito_actual)
                    case 4:
                        ver_carrito(carrito_actual, articulos)
                    case 5:
                        ventas, carrito_actual = confirmar_compra(carrito_actual, articulos, usuario_activo, ventas)
                    case 6:
                        historial_ventas_por_usuario(ventas)
                    case 7:
                        carrito_actual = vaciar_carrito()

print("Hasta pronto.")

