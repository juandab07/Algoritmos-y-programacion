p=int(input())
if p>=100000:
    queda=p//100000
    print(str(queda),'billetes de $100000')
    p=p%100000
if p>=50000:
    queda=p//50000
    print(str(queda),'billetes de $50000')
    p=p%50000
if p>=20000:
    queda=p//20000
    print(str(queda),'billetes de $20000')
    p=p%20000
if p>=10000:
    queda=p//10000
    print(str(queda),'billetes de $10000')
    p=p%10000
if p>=5000:
    queda=p//5000
    print(str(queda),'billetes de $5000')
    p=p%5000
if p>=2000:
    queda=p//2000
    print(str(queda),'billetes de $2000')
    p=p%2000
if p>=1000:
    queda=p//1000
    print(str(queda),'billetes de $1000')
    p=p%1000
if p>=500:
    queda=p//500
    print(str(queda),'monedas de $500')
    p=p%500
if p>=200:
    queda=p//200
    print(str(queda),'monedas de $200')
    p=p%200
if p>=100:
    queda=p//100
    print(str(queda),'monedas de $100')
    p=p%100
if p>=50:
    queda=p//50
    print(str(queda),'monedas de $50')
    p=p%50