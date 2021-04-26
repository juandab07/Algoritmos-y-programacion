base=float(input())
interes=float(input())

if interes > 100000:
    total=base+interes
    print('usted reinvirtio sus intereses, ahora tiene',total,'resultado de',base,'de base mas',interes,'de intereses')
else:
    print('el valor de los intereses no excede de $100.000')