"""
entradas
bolivaresaprestar->float->b1
añosainvertir->int->b2
tasadeinteresanual->b3
salidas
interesanualcausado->float->total

"""
b1=float(input(" indique la cantidad de bolivares que va a prestar " ))
b2=int(input(" indique por cuantos años desea invertir este dinero " ))
b3=float(input(" indique la tasa de interes anual " ))
I=(b1*b2*b3)/100
total=(I/b1)*100
print("el interes anual causado fue de: "  +str(total))
