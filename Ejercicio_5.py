"""
entradas
parcial1->float->p1
parcial2->float->p2
parcial3->float->p3
examenfinal->float->ef
trabajofinal->float->tf
salidas
notafinalprogramacion->float->notafinalprogramacion
"""
#entradas
p1=float(input("digite la nota del primer parcial " ))
p2=float(input("digite la nota del segundo parcial " ))
p3=float(input("digite la nota del terce parcial " ))
ef=float(input("digite la nota del examen final " ))
tf=float(input("digite la nota del trabajo final " ))
#cajanegra
P=((p1+p2+p3)/3)*0.55
E=ef*0.30
T=tf*0.15
#salidas
print("la nota final de programacion es : " +str(P+E+T))