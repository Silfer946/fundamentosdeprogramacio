"""
Una tiende ofrece un descuento del 15% sobre el total de la compra y un cliente 
desea saber cuanto debera pagar finalmente por su compra.
Entrada:
  total de la comnpra: int
Salida: 
   Total a pagar
"""
totalcompra = input("Ingresa el total de la compra: ")
totalcompra = int(totalcompra)
descuento = totalcompra * 15
descuento = descuento / 100
total = totalcompra - descuento
print ("El total a pagar aplicado el descuento es: ", total)
