from math import sqrt
A = int(input("Ingrese el coeficiente de la variable cuadr�tica\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el t�rmino independiente\n"))
x1= 0
x2= 0
if ((B**2)-4*A*C) < 0:
print("La soluci�n de la ecuaci�n es con n�meros complejos")
else:
x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
print("Las soluciones de la ecuaci�n son:")
print(x1)
print(x)