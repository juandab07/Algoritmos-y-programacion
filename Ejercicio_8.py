"""
entradas
lado1->float->a
lado2->float->b
lado3->float->c
salidas
areatriangulo->float->A
"""
#entradas
a=float(input(" 1er valor del lado del triangulo " ))
b=float(input("2do valor del lado del triangulo " ))
c=float(input("3er valor del lado del triangulo " ))
#cajanegra
s=(a+b+c)/2
A=(s*((s-a)*(s-b)*(s-c)))*0.5
#salidas
print("el area del triangulo es : "  +str(A))