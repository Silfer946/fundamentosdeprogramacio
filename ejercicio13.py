'''
Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su 
raíz cúbica.
entradas:
v1
salidas:
raiz cuadrada
raiz cubica
'''
v1 = int(input("escribe el valor 1: "))
rc = ( v1 ** (1/2) )
rcu = ( v1 ** (1/3) )
print("la raíz cuadrada del valor1 es:",rc)
print("la raíz cúbica del valor1 es:",rcu)