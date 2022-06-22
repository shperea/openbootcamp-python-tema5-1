def area_triangulo(base, altura):
	return (base * altura) / 2

print("Recuerda escribir ambos datos en las mismas unidades")

resultado = area_triangulo(float(input("Valor de la base: ")), float(input("Valor de la altura: ")))

unidades = input("¿En qué unidades has escrito los datos (m2, cm2, mm2...)? ")

print("El área del triángulo es", resultado, unidades)

#### parte 2 ####

import math #para importar el valor de pi

def area_circulo(radio):
	return math.pi * radio**2

resultado_circulo = area_circulo(float(input("Valor del radio: ")))

unidades_circulo = input("¿En qué unidades has escrito los datos (m2, cm2, mm2...)? ")

print("El área del círculo es", round(resultado_circulo, 2), unidades_circulo)