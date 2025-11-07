# Creo lista vacía para ir metiendo mis usuarios
usuarios = []

# Creo diccionario para cada usuario
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

# Los guardo en mi lista usuarios
usuarios.append(usuario1)
usuarios.append(usuario2)
usuarios.append(usuario3)

# Función para generar ID
def generar_id(usuarios):
    if not usuarios:
        return 1
    return len(usuarios) + 1

# Función para crear usuario
def crear_usuario():
    id_nuevo = generar_id(usuarios)
    nombre = input("Introduce el nombre del usuario que quieres añadir: ")
    email = input("Introduce el email para tu usuario: ")
    
    usuario_nuevo = {
        "id": id_nuevo,
        "nombre": nombre,
        "email": email,
        "activo": True
    }
    
    usuarios.append(usuario_nuevo)
    print(f"El usuario {nombre} ha sido añadido correctamente a tu lista de usuarios.")

# Función para listar usuarios
def listar_usuarios():
    if not usuarios:
        print("No hay usuarios disponibles.")
        return
    
    for usuario in usuarios:
        print(f"ID - {usuario['id']}, Nombre - {usuario['nombre']}, "
              f"Email - {usuario['email']}, Estado - {usuario['activo']}")

# Función para buscar usuario por ID
def buscar_usuario_por_id():
    id_buscar = int(input("Introduce el ID del usuario que deseas buscar: "))
    for usuario in usuarios:
        if usuario['id'] == id_buscar:
            print(f"ID - {usuario['id']}, Nombre - {usuario['nombre']}, "
                  f"Email - {usuario['email']}, Estado - {usuario['activo']}")
            return
    print("El usuario no ha sido encontrado.")

# Función para actualizar usuario
def actualizar_usuario():
    id_buscar = int(input("Introduce el ID del usuario que desees actualizar: "))
    for usuario in usuarios:
        if usuario['id'] == id_buscar:
            nuevo_nombre = input(f"Introduce el nuevo nombre que desees poner al usuario {usuario['nombre']}: ")
            if nuevo_nombre:
                usuario['nombre'] = nuevo_nombre
            
            nuevo_email = input("Introduce el nuevo email del usuario: ")
            if nuevo_email:
                usuario['email'] = nuevo_email
            
            print(f"{usuario['nombre']} con id: {id_buscar} ha sido actualizado.")
            return
    print("El usuario no ha sido encontrado.")

# Función para eliminar usuario
def eliminar_usuario():
    id_buscar = int(input("Introduce el ID del usuario que desees eliminar: "))
    for usuario in usuarios:
        if usuario['id'] == id_buscar:
            usuarios.remove(usuario)
            print(f"{usuario['nombre']} con id: {id_buscar} ha sido eliminado correctamente.")
            return
    print("El usuario no ha sido encontrado.")

# Función para alternar estado activo/inactivo del usuario
def alternar_usuario_activo():
    id_buscar = int(input("Introduce el ID del usuario que desees activar o desactivar: "))
    for usuario in usuarios:
        if usuario['id'] == id_buscar:
            usuario['activo'] = not usuario['activo']
            estado = "Activo" if usuario['activo'] else "Inactivo"
            print(f"{usuario['nombre']} con id: {id_buscar} ahora está {estado}.")
            return
    print("El usuario no se ha encontrado.")
