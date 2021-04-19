"""
entradas
chelinesaustralianos->float->CHA
dracmasgriegos->float->DG
pesetas->float->P
salidas
chelinesapesetas->float->chelinesapesetas
dracmasafrancos->float->dracmasafrancos
pesetasadolares->float->pesetasadolares
lirasitalianas->float->lirasitalianas
"""
#entradas
CHA=float(input(" digite la cantidad de chelines australianos que desea cambiar " ))
DG=float(input("digite la cantidad de dracmas griegos que desea cambiar " ))
P=float(input("digite la cantidad de pesetas que desea cambiar " ))
#cajanegra
pesetas=((CHA*956871)/100)
francofrances=(((DG*88607)/100)*(1/20110))
dolares=(P/122499)
lirasitalianas=((P*100)/9289)
#salidas
print("la cantidad de chelines a pesetas es : "  +str(pesetas))
print("la cantidad de dracmas a francos es : "  +str(francofrances))
print("la cantidad de pesetas a dolares es : "  +str(dolares))
print("la cantidad de pesetas a liras es : "  +str(lirasitalianas))