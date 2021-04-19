"""
entradas
galonessurtidos->float->galones
salidas
valoracobrar->float->precio
"""
galones=float(input(" digite cuantos galones surtio el cliente " ))
litros=galones*3.785
precio=litros*50000
print("el valor a cobrar al cliente es: "  +str(precio))

