#Continuando con el proceso de sistematización del proceso de venta de productos de   la super tienda por departamentos “Tu Vecino”, además de la información ya suministrada en el Reto No. 4, se adiciona el catálogo de precios, implementado en dos diccionarios, uno para los nombres del artículo y otro para los valores unitarios. Para realizar la prueba del programa, se tomará una muestra de ocho artículos y se suministran los dos diccionarios, así:

#articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}

#Donde la clave es el código del artículo y el valor es el nombre del producto

#precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}

#Donde la clave es el código del artículo y el valor corresponde al valor unitario del producto

#Con la incorporación de los diccionarios, la entrada de información al programa cambia, eliminado la lectura del nombre del producto y el valor unitario, quedando de la siguiente forma:

#N, como la cantidad de productos a procesar.
#Para cada producto, ingresar:
#Código del producto.
#Cantidad comprada.
#Tipo de IVA, que puede ser:
#1: Exento de IVA
###2: Bienes, donde se aplica como IVA el 5%
#3: General, donde se aplica como IVA el 19%
#Al igual que en el reto anterior, la información que se ingresa de los productos debe almacenar en listas, una lista por cada elemento de entrada del producto (código, cantidad comprada, y tipo de IVA).

#El gerente de la tienda desea que a través de un programa se calcule, para cada producto, el valor del producto, que corresponde a la cantidad comprada por el valor unitario, que se encuentra en el diccionario de precios, el valor del IVA y el valor final del producto, que corresponde a la suma del valor del producto más el valor de IVA. Además, se desea conocer el valor total de la compra, es decir, la suma de los N productos (tomando el valor final del producto, es decir con IVA aplicado) y el valor total de IVA de la compra (La suma del valor de IVA de los N productos). La información calculada para cada producto, en este caso, valor producto, valor IVA y valor final se debe almacenar en listas (para valor producto, valor IVA y valor final)

#Para este Reto, con la información suministrada se solicita resolver la situación problema, generando como salida, para cada uno de los N productos, el código del producto, nombre del producto, valor del producto sin aplicar IVA y el valor final del producto, una vez aplicada el IVA, el valor total de la compra, sumando el valor final de los N productos y el valor total de IVA, sumando el valor de IVA de los N productos. Sin embargo, como requerimiento especial de salida, la información se debe imprimir ordenada ascendentemente por el código del producto. También se especifica que se puede utilizar cualquier método de ordenamiento, pero debe estar programado a través de una función, pudiendo ser el mismo utilizado en el reto anterior.
#El orden en la entrada de la información al programa es tal y como se suministra, es decir, primero la cantidad de productos (N, como dato entero)), luego para cada producto se ingresa el código del artículo como dato entero, nombre del producto, la cantidad comprada como dato flotante, el valor unitario como dato flotante y finalmente el tipo de IVA aplicar al producto (1,2 o 3)
# Jonh Niño
# Fecha

#Funcion Ordenamiento
def ordenamiento_burbuja(lista_codigo,lista_valor_iva,lista_valor_final):
    for i in range(N-1):
        for j in range(i+1,N):
            if lista_codigo[i]>lista_codigo[j]:
              #  temp=lista_nombre[i]
               # lista_nombre[i]=lista_nombre[j]
               # lista_nombre[j]=temp
                temp1=lista_codigo[i]
                lista_codigo[i]=lista_codigo[j]
                lista_codigo[j]=temp1

                temp2=lista_valor_iva[i]
                lista_valor_iva[i]=lista_valor_iva[j]
                lista_valor_iva[j]=temp2

                
                #temp3=lista_valor_producto[i]
                #lista_valor_producto[i]=lista_valor_producto[j]
                #lista_valor_producto[j]=temp3

                
                temp4=lista_valor_final[i]
                lista_valor_final[i]=lista_valor_final[j]
                lista_valor_final[j]=temp4
    return lista_codigo,lista_valor_iva,lista_valor_final

#Programa Principal
#Diccionarios
articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}
#Creacion Listas Vacias
lista_codigo=[]
lista_nombre=[]
lista_cantidad_comprada=[]
lista_valor_unitario=[]
lista_tipo_iva=[]
lista_valor_producto=[]
lista_valor_iva=[]
lista_valor_final=[]


N=int(input("Cantidad Productos"))
total_ivas=0
total_compra=0

for i in range(N):  
    codigo=int(input("Codigo Producto"))
  #  nombre=input("Nombre del Producto")
    cantidad_comprada=float(input("Cantidad Comprada"))
  #  valor_unitario=float(input("Valor unitario del producto"))
    tipo_iva=int(input("Tipo de Iva"))
    lista_codigo.append(codigo)
 #   lista_nombre.append(nombre)
    lista_cantidad_comprada.append(cantidad_comprada)
  #  lista_valor_unitario.append(valor_unitario)
    lista_tipo_iva.append(tipo_iva)    

for x in range(N):
    valor_productos=lista_cantidad_comprada[x]*precios.get(lista_codigo[i])
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
#llamar Funcion Ordenar
lista_codigo,lista_valor_iva,lista_valor_final=ordenamiento_burbuja(lista_codigo,lista_valor_iva,lista_valor_final)
#Se imprimen las listas ordenadas
print("Listas Ordenadas")
for x in range(N):
    print("Codigo Ordenado LIsta",lista_codigo[x])
    print("nombre Ordenado Lista",articulos[lista_codigo[i]])
    print("lista valor producto",lista_valor_producto[x])
    print("lista valor final",lista_valor_final[x])

print("Total compra",total_compra)
print("Total iva",total_ivas)
#print("Total compra",lista_total_compra[x])
#print("Total iva",total_ivas[x])