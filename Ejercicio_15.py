"""
entradas
preciofabrica->float->pf
precioalpublico->float->pv
salidas
porcentajdedescuento->float->porcentaje

"""
pf=float(input(" digite el precio de fabrica " ))
pv=float(input(" digite el precio de venta al publico " ))
porcentaje=((pv-pf)/pf)*100
print("el porcentaje de descuento aplicado es : "  +str(porcentaje))