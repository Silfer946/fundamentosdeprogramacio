"""
Pide al usuario dos partes de numero x1,y2 y x2,y2, que precentes dos putos 
en el plano. Calcula y muestra la distancia entre ello.
Entrada:
x1:int
y1:int
y1:int
x2:int
salida:
  distancia
"""

num1x = input("ingresa el primer numero x: ")
num1x = int(num1x)
num1y = input("Ingresa el primer numero y:")
num1y = int(num1y)
num2x = input("Ingresa el segundo numero x ")
num2x = int(num2x)
num2y = input("Ingresa el segundo numero y: ")
num2y = int(num2y)
distancia = num1x + num1y * num1x + num1y + num2x + num2y * num2x + num2y
resultado = distancia **(1/2)
print("La distancia es de: ", resultado)
