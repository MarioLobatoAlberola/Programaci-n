import articulos
import usuarios
import ventas 

# Menús
def menu_articulos():
    print("""
1. Crear artículo
2. Listar artículos
3. Buscar artículo por id
4. Actualizar artículo
5. Eliminar artículo
6. Alternar activo/inactivo
7. Salir
""")

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
""")

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

def menu_principal_final():
    print("""
MENU PRINCIPAL
1. Gestion de Articulos
2. Gestion de Usuarios
3. Ventas y carrito
4. Salir
""")
# Variables principales
opcion_principal = 0
usuario_activo = None
carrito_actual = []

while opcion_principal != 4:
    menu_principal_final()
    opcion_principal = int(input("Introduce una opcion del menu principal y si deseas salir escribe 4: "))
    
    match opcion_principal:
        case 1:
            opcion_articulos = 0
            while opcion_articulos != 7:
                menu_articulos()
                opcion_articulos = int(input("Introduce una opcion del menu de articulos y si deseas salir escribe 7: "))
                
                match opcion_articulos:
                    case 1:
                        articulos.crear_articulo()
                    case 2:
                        articulos.listar_articulos()
                    case 3:
                        articulos.buscar_articulo_por_id()
                    case 4:
                        articulos.actualizar_articulos()
                    case 5:
                        articulos.eliminar_articulo()
                    case 6:
                        articulos.alternar_activo()
        
        case 2:
            opcion_usuarios = 0
            while opcion_usuarios != 7:
                menu_usuarios()
                opcion_usuarios = int(input("Introduce una opcion del menu de usuarios y si deseas salir escribe 7: "))
                
                match opcion_usuarios:
                    case 1:
                        usuarios.crear_usuario()
                    case 2:
                        usuarios.listar_usuarios()
                    case 3:
                        usuarios.buscar_usuario_por_id()
                    case 4:
                        usuarios.actualizar_usuario()
                    case 5:
                        usuarios.eliminar_usuario()
                    case 6:
                        usuarios.alternar_usuario_activo()
        
        case 3:
            opcion_ventas = 0
            while opcion_ventas != 8:
                menu_ventas()
                opcion_ventas = int(input("Introduce una opcion del menu de ventas y si deseas volver escribe 8: "))
                
                match opcion_ventas:
                    case 1:
                        usuario_activo = ventas.seleccionar_usuario_activo(usuarios)
                    case 2:
                        carrito_actual = ventas.añadir_al_carrito(carrito_actual, articulos, usuario_activo)
                    case 3:
                        carrito_actual = ventas.quitar_del_carrito(carrito_actual)
                    case 4:
                        ventas.ver_carrito(carrito_actual, articulos)
                    case 5:
                        ventas, carrito_actual = ventas.confirmar_compra(carrito_actual, articulos, usuario_activo, ventas)
                    case 6:
                        ventas.historial_ventas_por_usuario(ventas)
                    case 7:
                        carrito_actual = ventas.vaciar_carrito()

print("Hasta pronto.")













            
    


    