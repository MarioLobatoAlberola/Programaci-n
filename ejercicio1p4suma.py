# Creo una variable que cuente las vocales para usarla después y solicito al usuario una cadena de texto
contador_vocales = 0
cadena_texto = str (input("Introduce una cadena de texto:"))

#Que tiene que pasar para que sume uno al contador, creo un bucle for en el que pase por cada letra de la cadena y que si hay alguna vocal sea mayúscula o minúscula sume uno al contador de vocales
for letra in cadena_texto:
	if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"
		or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
		contador_vocales += 1
#Imprimir el total de vocales en la cadena
print("El numero de vocales que hay en tu cadena es:", contador_vocales)	
