"""
entradas
cantidadmetros->float->M
salidas
cantidadpulgadas->float->pulg
cantidadpies->float->ft
"""
#entradas
M=float(input("ingrese la cantidad de metros " ))
#cajanegra
pulg=M*39.27
ft=pulg*12
#salidas
print("la cantidad de pulgadas es : "  +str(pulg))
print("la cantidad de pies es : "  +str(ft))
