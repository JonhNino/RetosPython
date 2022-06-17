#Reto 3
#Apreciado tripulante,

#Bienvenido al Reto No. 3 del ciclo de Fundamentos de Programación.

#Situación problema: Venta de Producto

#Reto3

#Continuando con el proceso de sistematización del proceso de venta de productos de   la super tienda por departamentos “Tu Vecino”, además de la información ya suministrada en el Reto No. 2, conservando la misma entrada de forma:

#N, como la cantidad de productos a procesar.
#Para cada producto, ingresar:
#Código del producto.
#Nombre al producto.
#Cantidad comprada.
#Valor unitario (sin IVA).
#Tipo de IVA, que puede ser:
#1: Exento de IVA
#2: Bienes, donde se aplica como IVA el 5%
#3: General, donde se aplica como IVA el 19%
#Como aspecto adicional en este Reto 3, la información que se ingresa de los productos debe almacenar en listas, una lista por cada elemento de entrada del producto (código, nombre, cantidad comprada, valor unitario y tipo de IVA). Una vez se ingrese la información de los N artículos, se debe imprimir, como mecanismo de control en este orden, la longitud de la lista de códigos, longitud de la lista de nombres, longitud de la lista de cantidad comprada, longitud de la lista de valor unitario y la longitud de la lista de tipo de IVA, para luego continuar con los requerimientos solicitados.

#El gerente de la tienda desea que a través de un programa se calcule, para cada producto, valor del producto, que corresponde a la cantidad comprada por el valor unitario, el valor del IVA y el valor final del producto, que corresponde a la suma del valor del producto más el valor de IVA. Además, se desea conocer el valor total de la compra, es decir, la suma de los N productos (tomando el valor final del producto, es decir con IVA aplicado) y el valor total de IVA de la compra (La suma del valor de IVA de los N productos). La información calculada para cada producto, en este caso, valor producto, valor IVA y valor final se debe almacenar en listas (para valor producto, valor IVA y valor final)

#Para este Reto, con la información suministrada se solicita resolver la situación problema, generando como salida, para cada uno de los N productos, el código del producto, nombre del producto, valor del producto sin aplicar IVA y el valor final del producto, una vez aplicada el IVA, el valor total de la compra, sumando el valor final de los N productos y el valor total de IVA, sumando el valor de IVA de los N productos

#Recomendaciones importantes:

#El orden en la entrada de la información al programa es tal y como se suministra, es decir, primero la cantidad de productos (N, como dato entero)), luego para cada producto se ingresa el código del artículo como dato entero, nombre del producto, la cantidad comprada como dato flotante, el valor unitario como dato flotante y finalmente el tipo de IVA aplicar al producto (1,2 o 3)
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
total_ivas=0
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
    print(valor_iva)
    print(valor_productos)
    print(valor_final)
    print(N)
    print(x)

print("Total compra",total_compra)
print("Total iva",total_ivas)

  
