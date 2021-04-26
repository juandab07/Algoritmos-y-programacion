print('ingrese el salario')
salario=float(input())
print('ingrese la cantidad de ventas de meta')
ventas=int(input())
print('ingrese las ventas del departamento 1')
d1=int(input())
print('ingrese las ventas del departamento 2')
d2=int(input())
print('ingrese las ventas del departamento 1')
d3=int(input())
meta=ventas*1.33
total=salario*1.2
if d1>meta:
    print('el departamento 1 cumplio la meta y ganara un total de',total)
else:
    print('el departamento 1 no cumplio la meta y ganara un total de',salario)
if d2>meta:
    print('el departamento 2 cumplio la meta y ganara un total de',total)
else:
    print('el departamento 2 no cumplio la meta y ganara un total de',salario)
if d3>meta:
    print('el departamento 3 cumplio la meta y ganara un total de',total)
else:
    print('el departamento 3 no cumplio la meta y ganara un total de',salario)


