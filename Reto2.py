#Reto Ciclo Python MinTic 2022
# Jonh Niño
# Fecha


N=int(input("Cantidad Productos"))
total_iva=0
total_compra=0
for i in range(N):  
    codigo=int(input("Codigo Producto"))
    nombre=input("Nombre del Producto")
    cantidad_comprada=float(input("Cantidad Comprada"))
    valor_unitario=float(input("Valor unitario del producto"))
    tipo_iva=int(input("Tipo de Iva"))
    valor_producto=valor_unitario*cantidad_comprada       
    if tipo_iva==1:
        valor_iva=0
    elif tipo_iva==2:
        valor_iva=valor_producto*0.05
    elif tipo_iva==3:
        valor_iva=valor_producto*.19
            
    
    valor_final=valor_producto+valor_iva
    total_iva+=valor_iva
    total_compra+=valor_final
    print(codigo)
    print(nombre)
    print(valor_producto)
    print(valor_final)
print(total_compra)
print(total_iva)