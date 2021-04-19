"""
entradas
numerodehombres->int->h
numerodemujeres->int->m
salidas
porcentajedemujeres->float->porcentajedemujeres
porcentajedehombres->float->porcentajedehombres
"""
#entradas
h=int(input("numero de estudiantes hombres " ))
m=int(input("numero de estudiantes mujeres" ))
T=h+m
porcentajemujeres=((m*100)/T)
porcentajehombres=((h*100)/T)
#salidas
print("el porcentaje de mujeres es : "  +str(porcentajemujeres))
print("el porcentaje de hombres es : "  +str(porcentajehombres))
