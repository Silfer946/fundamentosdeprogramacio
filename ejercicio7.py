"""
Realiza un 'programa que reciba una cantidad en minutos y 
muestra por pantalla a cuantas horas y minutos corresponde
Entrada:
   minutos: int
Salida:
   minutois y horas correpondientes
"""
minutos = input("Ingresa los minutos: ")
minutos = int(minutos)
hora = minutos/60
minutores = minutos % 60
print("Las horas son : ",hora , minutores)
