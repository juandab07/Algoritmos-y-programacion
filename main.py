"""
entradas
venta1->float->v1
venta2->float->v2
venta3->float->v3
sueldobase->float->SB 
salidas
comision->float->c
sueldototal->float->sueldototal
"""
#entradas
v1=float(input("digite la venta 1 " ))
v2=float(input("digite la venta 2 " ))
v3=float(input("digite la venta 3 " ))
sueldobase=float(input("digite el sueldo base "))
#cajanegra
c=((v1+v2+v3)/3)*0.10
#salidas
print("la comision es: "+str(c),"el sueldo total es: " +str(sueldobase+c))