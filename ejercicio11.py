"""
Realizan un algoritmo que lea un numero y que muestre su raiz cuadrada de su 
raiz cubica.
¿como se puede calcular?
Entrada:
    numero:int
Salida:
raiz cuadrada 
raiz cubica
"""
num1 = input("Ingresa un numero: ")
num1 = int(num1)
raizcuadrada = num1 **(1/2)
raizcubica =num1 **(1/3)
print("Las raiz cuadrada es: ", raizcuadrada)
print("La raiz cubica es: ", raizcubica)