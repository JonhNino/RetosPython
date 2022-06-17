lista_codigo=[]
lista_nombre=[]
lista_cantidad_comprada=[]
lista_valor_unitario=[]
lista_tipo_iva=[]
lista_valor_producto=[]
lista_valor_iva=[]
lista_valor_final=[]


N=int(input())
total_ivas=0
total_compra=0

for i in range(N):  
    codigo=int(input())
    nombre=input()
    cantidad_comprada=float(input())
    valor_unitario=float(input())
    tipo_iva=int(input())
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
    valor_productos=lista_cantidad_comprada[x]*lista_valor_unitario[x]
    lista_valor_producto.append(valor_productos)
    if lista_tipo_iva[x] ==1:
        valor_iva=0
    elif lista_tipo_iva[x] ==2:
        valor_iva=0.05*valor_productos
    elif lista_tipo_iva[x] ==3:
        valor_iva=0.19*valor_productos
    lista_valor_iva.append(valor_iva)
    valor_final=valor_productos+valor_iva
    lista_valor_final.append(valor_final)
    total_ivas+=valor_iva
    total_compra+=valor_final
    print(lista_codigo[x])
    print(lista_nombre[x])
    print(valor_productos)
    print(valor_final)
 
print(total_compra)
print(total_ivas)