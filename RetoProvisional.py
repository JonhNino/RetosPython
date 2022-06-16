N=int(input("Numero de Productos"))
total_iva=0
totalcompra=0
for i in range(N):
    codigo=int(input("Codigo Producto"))
    nombre=input("Nombre Producto")
    CantidadComprada=int(input("Cantidad Comprada"))
    ValorUnitario=int(input("Valor Unitario"))
    Tipo_Iva=int(input("Tipo Iva"))
    ValorProducto = ValorUnitario * CantidadComprada
    if Tipo_Iva==1:
        ValorIVa=0
    elif Tipo_Iva==2:
        ValorIVa = ValorProducto *0.05

    else :
        ValorIVa=ValorProducto*0.19


    TotalIva=ValorProducto+ValorIVa
    total_iva=total_iva+ValorIVa
    totalcompra = totalcompra + TotalIva
    print(codigo)
    print(nombre)
    print("{:.1f}".format(ValorProducto))
    print("{:.1f}".format(TotalIva))

print("total Compra","{:.1f}".format(totalcompra))
print("total de los iva","{:.1f}".format(total_iva))