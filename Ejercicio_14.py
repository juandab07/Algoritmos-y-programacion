"""
entradas
consumoactual->float->k1
consumoanterior->float->k2
preciokilovatio->float->k
salidas
valordelafacturatotal->float->preciototal
"""
k1=float(input(" ingrese consumo actual de kilovatios " ))
k2=float(input(" ingrese el consumo anterior de kilovatios " ))
k=float(input(" ingrese el precio por kilovatio "))
preciototal=(k1-k2)*k
print("el valor de la factura por consumo es: "  +str(preciototal))

