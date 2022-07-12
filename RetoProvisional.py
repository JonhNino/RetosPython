
def ordenamiento_burbuja(lista_codigo,lista_valor_iva,lista_valor_final):
    for i in range(N-1):
        for j in range(i+1,N):
            if lista_codigo[i]>lista_codigo[j]:
                temp1=lista_codigo[i]
                lista_codigo[i]=lista_codigo[j]
                lista_codigo[j]=temp1

                temp2=lista_valor_iva[i]
                lista_valor_iva[i]=lista_valor_iva[j]
                lista_valor_iva[j]=temp2
           
                
                
                temp4=lista_valor_final[i]
                lista_valor_final[i]=lista_valor_final[j]
                lista_valor_final[j]=temp4
    return lista_codigo,lista_valor_iva,lista_valor_final


articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}
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
 
    cantidad_comprada=float(input())
 
    tipo_iva=int(input())
    lista_codigo.append(codigo)

    lista_cantidad_comprada.append(cantidad_comprada)

    lista_tipo_iva.append(tipo_iva)   

for x in range(N):
    valor_productos=lista_cantidad_comprada[x]*precios.get(lista_codigo[x])
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

lista_codigo,lista_valor_iva,lista_valor_final=ordenamiento_burbuja(lista_codigo,lista_valor_iva,lista_valor_final)


for x in range(N):
    print(lista_codigo[x])
    print(articulos[lista_codigo[x]])
    print(lista_valor_producto[x])
    print(lista_valor_final[x])

print(total_compra)
print(total_ivas)

