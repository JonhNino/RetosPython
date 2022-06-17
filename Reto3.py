#Reto Ciclo Python MinTic 2022
# Jonh Niño
# Fecha

lista_codigo=[]
lista_nombre=[]
lista_cantidad_comprada=[]
lista_valor_unitario=[]
lista_tipo_iva=[]
lista_valor_producto=[]
lista_valor_iva=[]
lista_valor_final=[]


N=int(input("Cantidad Productos"))
total_iva=0
total_compra=0
for i in range(N):  
    codigo=int(input("Codigo Producto"))
    nombre=input("Nombre del Producto")
    cantidad_comprada=float(input("Cantidad Comprada"))
    valor_unitario=float(input("Valor unitario del producto"))
    tipo_iva=int(input("Tipo de Iva"))
    lista_codigo.append(codigo)
    lista_nombre.append(nombre)
    lista_cantidad_comprada.append(cantidad_comprada)
    lista_valor_unitario.append(valor_unitario)
    lista_tipo_iva.append(tipo_iva)
    
    
    
print(len(lista_codigo))
print(len(lista_nombre))
print(len(lista_cantidad_comprada))
print(len(lista_valor_unitario))
print(len(lista_tipo_iva))

for x in range(N):
            
    if lista_tipo_iva[x]==1:
        valor_iva=0
    elif lista_tipo_iva[x]==2:
        valor_iva=valor_producto*0.05
    elif lista_tipo_iva[x]==3:
        valor_iva=valor_producto*.19
            
    lista_valor_iva.append(valor_iva)
    valor_final=valor_producto+valor_iva
    lista_valor_final.append(valor_final)
    total_iva+=valor_iva
    total_compra+=valor_final
    print(codigo)
    print(nombre)
    print(valor_producto)
    print(valor_final)
print(total_compra)
print(total_iva)