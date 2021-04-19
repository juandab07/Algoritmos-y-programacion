"""
entradas
notaexamenmat->float->m
notaexamenfis->float->f
notaexamenqui->float->q
tareademate1->float->m1
tareademate2->float->m2
tareademate3->float->m3
tareadefis1->float->f1
tareadefis2->float->f2
tareadequi1->float->q1
tareadequi2->float->q2
tareadequi3->float->q3
salidas
promediomat->float->promediomatematicas
promediofis->float->promediofisica
promedioqui->float->promedioquimica
promediototal->float->promediototal
"""
m=float(input(" nota examen matematicas " ))
f=float(input("nota examen fisica " ))
q=float(input("nota examen quimixa "))
m1=float(input("tarea matematicas 1"))
m2=float(input("tarea matematicas 2"))
m3=float(input("tarea matematicas 3"))
f1=float(input("tarea fisica 1"))
f2=float(input("tarea fisica 2"))
q1=float(input("tarea quimica 1"))
q2=float(input("tarea quimica 2"))
q3=float(input("tarea quimica 3"))
promediomatematicas=(m*0.90)+((m1+m2+m3)/3)*0.10
promediofisica=(f*0.80)+((f1+f2)/2)*0.20
promedioquimica=(q*0.85)+((q1+q2+q3)/3)*0.15
promediototal=(promediomatematicas+promediofisica+promedioquimica)/3
print("promedio de matematicas es: "  +str(promediomatematicas))
print("promedio fisica es : "  +str(promediofisica))
print("promedio quimica es : "  +str(promedioquimica))
print("promedio total del estudiante es : "  +str(promediototal))

