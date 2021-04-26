print('ingrese 0 si es hombre y 1 si es mujer')
sexo=int(input())
print('ingrese cuantos meses tiene si es menor o igual a un año, sino ponga 0')
meses=int(input())
print('ingrese cuantos años tiene, si es mayor a un año, sino ponga 0')
años=int(input())
print('ingrese su nivel de hemoglobina')
h=float(input())
# LA ANEMIA SE DA SOLO CUANDO ESTA POR DEBAJO DEL NIVEL
if meses==1 and 13<h<26:
    print('negativo para anemia')
if meses==1 and h<13:
    print('positivo para anemia')
if 1<meses<=6 and 10<h<18:
    print('negativo para anemia')
if 1<meses<=6  and h<10:
    print('positivo para anemia')
if 6<meses<=12 and 11<h<15:
    print('negativo para anemia')
if 6<meses<=12  and h<11:
    print('positivo para anemia')
if 1<años<=5 and 11.5<h<15:   
    print('negativo para anemia')
if 1<años<=5 and h<11.5:
    print('positivo para anemia'
if 5<años<=10 and 12.6<h<15.5:
    print('negativo para anemia')
if 5<años<=10 and h<12.6:
    print('positivo para anemia')
if 10<años<=15 and 13<h<15.5:   
    print('negativo para anemia')
if 10<años<=15 and h<13:
    print('positivo para anemia')
if sexo=1 and años>15 and 12<h<16:
    print('negativo para anemia')
if sexo=1 and años>15 and h<12
    print('positivo para anemia')
if sexo=0 and años>15 and 14<h<18:
    print('negativo para anemia')
if sexo=0 and años>15 and h<14
    print('positivo para anemia')