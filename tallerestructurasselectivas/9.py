print('ingrese su nombre')
nombre=input()
print('ingrese el monto de la compra')
monto=float(input())

if monto < 50000:
    pago=monto
    print(nombre,'el monto fue de',monto,'y usted pagará',pago,'porque no tuvo descuento')
if 50000<monto<100000:
    pago=monto*0.95
    print(nombre,'el monto fue de',monto,'y usted pagará',pago,'y tuvo un descuento del 5%')
if 100000<monto<700000:
    pago=monto*0.89
    print(nombre,'el monto fue de',monto,'y usted pagará',pago,'y tuvo un descuento del 11%')
if 700000<monto<1500000:
    pago=monto*0.82
    print(nombre,'el monto fue de',monto,'y usted pagará',pago,'y tuvo un descuento del 18%')
if monto>1500000:
    pago=monto*0.75
    print(nombre,'el monto fue de',monto,'y usted pagará',pago,'y tuvo un descuento del 25%')