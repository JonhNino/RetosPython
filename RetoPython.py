#Reto Ciclo Python MinTic 2022
# Jonh Niño
# Fecha

codigo=int(input("Codigo Producto"))
nombre=input("Nombre del Producto")
cantidad_comprada=float(input("Cantidad Comprada"))
valor_unitario=float(input("Valor unitario del producto"))

valor_producto=cantidad_comprada*valor_unitario
valor_iva=valor_producto*0.19
valor_final=valor_producto+valor_iva
print(valor_producto)
print(valor_iva)
print(valor_final)