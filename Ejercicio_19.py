"""
entradas
compranaranjas->float->x
docena->int->d
ventanaranjas->k
salidas
porcentajdeganancia->float->porcentaje
"""
x=float(input(" digite el valor de compra de naranjas " ))
d=int(input(" digite la docena " ))
k=float(input(" digite el valor de venta de las naranjas " ))
porcentaje=(((12*k)-x*d)/(x*d))*100
print("el porcentaje de ganancia es : "  +str(porcentaje))