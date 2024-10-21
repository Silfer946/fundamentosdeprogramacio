"""
un vendedor recibe un sueldo base mas un 10% extra por comicion de sus ventas 
el vendedor desa saber cuanto dinero obtendra por concepto de las tres ventas que realiza
entradas:
   sueldobase, v1, v2, v3, comision
monto de comicion
pago total
"""
venta1 = input("Ingresa el total de la primer venta: ")
venta1 = int(venta1)
venta2 = input("Ingresa el total de la segunda venta: ")
venta2 = int(venta2)
venta3 = input("Ingresa el total de la tercera venta: ")
venta3 = int(venta3)
sueldo = input("Ingresa el sueldo base: ")
sueldo = int(sueldo)
ventatotal = venta1 + venta2 + venta3
comision =ventatotal * 0.1
sueldototal = sueldo + comision
print ("El sueldo total es de: ", sueldototal)