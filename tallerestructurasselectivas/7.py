print('ingrese la distancia recorrida en km')
distancia=float(input())

if distancia <=300:
    print('debe cancelar $50.000')
if distancia > 300 and distancia<1000:
    extra=int(distancia-300)
    vextra=extra*30000
    print('debe cancelar $70.000 mas $',vextra,'por los',extra,'km recorridos despues de 300 km')
if distancia > 300 and distancia>1000:
    extra=int(distancia-300)
    vextra=extra*9000
    print('debe cancelar $150.000 mas $',vextra,'por los',extra,'km recorridos despues de 300 km')