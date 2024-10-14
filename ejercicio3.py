"""
Ejercicio 3:
Programa que calcula la hipotenusa de un triangulo
rectangulo a partir de sus catetos
Entradas:
    cateto1: int
    cateto2: int
Salidas:    
    hipotenusa
Analisis:
    Se resuelve con el teoremab de pitagoras    
"""

cateto1 = input("Escribe el catteto 1: ")
cateto1 = int(cateto1)
cateto2 = int(input("Escribe el cateto 2: "))
hipotenusa = cateto1*cateto1+cateto2*cateto2
hipotenusa =hipotenusa ** (1/2)
print("La hipotrenusa es: ", hipotenusa)
