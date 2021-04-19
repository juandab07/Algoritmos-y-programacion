"""
entradas
n1->float->n1
n2->float->n2
n3->float->n3
n4->float->n4
n5->float->n5
n5->float->n6
n6->float->n7
n7->float->n8
salidas
cantidadtotal->float->cantidadtotal
"""
n1=float(input(" ngrese el numero de billetes de 50000 " ))
n2=float(input("ngrese el numero de billetes de 20000 " ))
n3=float(input("ngrese el numero de billetes de 10000 "))
n4=float(input("ngrese el numero de billetes de 5000 "))
n5=float(input("ngrese el numero de billetes de 2000 "))
n6=float(input("ngrese el numero de billetes de 1000 "))
n7=float(input("ingrese el numero de billetes de 500 "))
n8=float(input("ngrese el numero de billetes de 100 "))
cantidadtotal=(n1*50000)+(n2*20000)+(n3*10000)+(n4*5000)+(n5*2000)+(n6*1000)+(n7*500)+(n8*100)

print("a cantidad total de dinero que hay en el banco es: "  +str(cantidadtotal))

