from tabulate import tabulate

#Función de generar ID para cada vez que lo necesite. def generar_id(list):
def generar_id(list):
    id = len(list)+1 
    return id

#Funcion para imprimir tabla usando tabulate, con filas, columnas y estilo def imprimir_tabla(filas, columnas, estilo="grid"):
def imprimir_tabla(filas, columnas, estilo="grid"):
        print(tabulate(filas, headers=columnas, tablefmt=estilo))
