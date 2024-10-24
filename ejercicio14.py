"""
Dado un numero de dos sifras  diseñe un algoritmo que permita obtener el numero invertido
Entrada:
  numero:int
Salida:
  numero investido
"""
numero = input("Ingresa un numero de dos cifras: ")
numero = int(numero)
dec = numero // 10
uni = numero % 10
print("El numero investido es: ", uni,dec)
