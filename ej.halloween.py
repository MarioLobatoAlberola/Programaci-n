import random

# Lista de monstruos y sus niveles de dificultad 
monstruos = [
    {"nombre":'vampiro', "dificultad": 3},
    {"nombre":'momia', "dificultad": 6},  
    {"nombre":'bruja', "dificultad": 7}, 
    {"nombre":'esqueleto', "dificultad": 8}, 
    {"nombre":'fantasma', "dificultad": 10}
] 
# Lista de objetos para capturar 
objetos = [
    {"nombre": "estaca", "efectividad": 3},
    {"nombre": "pocion magica", "efectividad": 2},
    {"nombre": "hechizo", "efectividad": 4}
]

#Funcion para sacar monstruo aleatorio con random choice.
def monstruo_aleatorio():
    return random.choice(monstruos)
   
print("¡Bienvenido a la caza de monstruos!")

monstruo = monstruo_aleatorio()
print(f"¡Un/a {monstruo['nombre']} con dificultad {monstruo['dificultad']} ha aparecido!")

intentos = 3
capturado = False

#Mientras tenga intentos y no este capturado seguira intentando y eligiendo arma.
while intentos > 0 and capturado == False:
    print(f"Tienes {intentos} intentos restantes.")
    print(f"Elige un objeto para intentar capturar a {monstruo['nombre']}: {objetos}")

    eleccion = input("Escribe el nombre del objeto:")

    encontrado = False

    for objeto in objetos:
        if eleccion == objeto['nombre']:
            encontrado = True
            #Genera numero aleatorio que representa la suerte del jugador
            probabilidad = random.randint(1,10)
            #El total sera la suerte del jugador mas la efectividad del arma que elija
            total = probabilidad + objeto['efectividad']
            if total > monstruo['dificultad']:
                print(f"¡Has capturado a {monstruo['nombre']}  con un/a {objeto['nombre']}!")
                capturado = True
            else:
                intentos -= 1
                print(f"Has fallado al intentar capturar a {monstruo['nombre']} con {objeto['nombre']}")
                print(f"Te quedan {intentos} intentos.")
    if not encontrado:
        print("El objeto no se ha encontrado.")
if not capturado:
    print("Has perdido, a la proxima lo conseguiras.")


        



