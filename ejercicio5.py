
"""
Programa que convierte un valor dado en grados fahrenheit
a grados celsius
Entrada:
  Grados fahrenheit: int 
salida:
  Grados celsius 
"""
GradosFare = input("Ingresa los grados Fahrenheit: ")
GradosFare = int(GradosFare)
celsius = GradosFare -32
celsius = celsius *5/9
print("La conversion de fahrenheit a celsius es de: ",celsius)
