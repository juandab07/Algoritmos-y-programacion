print('ingrese el valor total de la compra')
valor=float(input())
if valor > 5000000:
propio=valor*0.055
banco=valor*0.3
credito=valor*0.645
interes=credito*0.2
print('el total de la compra es',valor,'de la forma en
que',propio,'seran de su dinero,',banco,'seran prestados por el
banco,',credito,'seran por un credito al fabricante y',interes,'de
interes por el credito al fabricante')
else:
propio=valor*0.7
credito=valor*0.3
interes=credito*0.2
print('el total de la compra es',valor,'de la forma en que',propio,'seran de su dinero,',credito,'seran por un credito al fabricante y',interes,'de interes por el credito al fabricante')