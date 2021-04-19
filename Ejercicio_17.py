"""
entradas
montopresupuestado->float->presupuesto
salidas
ginecologia->float->ginecologia
traumatologia->float->traumatologia
pediatria->float->pediatria
"""
presupuesto=float(input(" digite el monto presupuestado " ))
ginecologia=presupuesto*0.40
traumatologia=presupuesto*0.30
pediatria=presupuesto*0.30
print("el monto designado para ginecologia es: "  +str(ginecologia))
print("el monto designado para traumatologia es: "  +str(traumatologia))
print("el monto designado para pediatria es: "  +str(pediatria))