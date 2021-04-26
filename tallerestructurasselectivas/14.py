print('ingrese el monto a pagar en aseo urbano')
aseo=float(input())
print('ingrese el valor de lectura del mes anterior')
ant=float(input())
print('ingrese el valor de lectura del mes actual')
act=float(input())
cons=act-ant
if 0<cons<=100:
    pago=cons*4600
    print('debera pagar $',pago,'en luz electrica y',aseo,'en aseo urbano')
if 101<cons<=300:
    pago=cons*80000
    print('debera pagar $',pago,'en luz electrica y',aseo,'en aseo urbano')
if 301<cons<=500:
    pago=cons*100000
    print('debera pagar $',pago,'en luz electrica y',aseo,'en aseo urbano')
if cons>500:
    pago=cons*120000
    print('debera pagar $',pago,'en luz electrica y',aseo,'en aseo urbano')