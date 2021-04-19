"""
entradas
horastrabajadas->int->ht
precioporhora->float->ph
salidas
salarioneto->float->salarioneto
"""
#entradas
ht=int(input(" horas trabajadas " ))
ph=float(input("precio por hora " ))
#cajanegra
sueldobase=(ht*ph)
sueldoimpuesto=sueldobase*0.20
salarioneto=sueldobase-sueldoimpuesto
#salidas
print("el salario neto del trabajador es : "  +str(salarioneto))