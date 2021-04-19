"""
entradas
Inversion->float->I
mesesdeinversion->int->M

salidas
gananciatotal->float->G
"""
#entradas
I=float(input("digite valor de la inversion " ))
M=int(input("digite el numero de meses de inversion del capital " ))
#cajanegra
G=I*(M*0.02)
#salidas
print("la ganancia total de la inversion es: " +str(G))