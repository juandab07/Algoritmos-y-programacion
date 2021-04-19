"""
entradas
horastrabajadas->int->h
horasextras->int->he
pagoporhora->float->ph
hijostrabajador->int->nh
salidas
deduccionporparoforsozo->float->paro
deduccionporpoliticahabitacional->float->politica
deduccionporcajadeahorro->float->cajaahorro
asignacionporacademia->float->academia
asignacionporcadahijo->float->hijos
asignacionporhogar->float->hogar
"""
#entradas
h=int(input(" digite horas trabajadas " ))
he=int(input("digite extras trabajadas " ))
ph=float(input("digite pago por hora " ))
nh=int(input("digite el numero de hijos del trabajador"))
#cajanegra
horaextra=(((ph*0.25)+ph)*he)
sueldobase=(h*ph)+horaextra
paro=sueldobase*0.05
politica=sueldobase*0.02
cajaahorro=sueldobase*0.07
academia=sueldobase+250000
hijos=sueldobase+(nh*173000)
hogar=sueldobase+180000
sueldoneto=(sueldobase+academia+hijos+hogar)-(paro+politica+cajaahorro)
#salidas
print("deduccion por paro forsozo es : "  +str(paro))
print("deduccion por politica habitacional es : "  +str(politica))
print("deduccion por caja de ahorro es : "  +str(cajaahorro))
print("asignacion por academia es : "  +str(academia))
print("asignacion por cada hijo es : "  +str(hijos))
print("asignacion por hogar es : "  +str(hogar))
print("sueldo neto del trabajador es : "  +str(sueldoneto))