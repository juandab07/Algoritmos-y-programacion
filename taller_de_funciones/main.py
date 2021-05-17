frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt

lista_frutas=[]
for i in frutas:
    lista_frutas.append(i)
print(lista_frutas)



lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt

lista_numeros=[]
for i in numeros:
    lista_numeros.append(i)
print(lista_numeros)


#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista
valor->str-->elemento
Salidas
lista-->lista
"""
def eliminar_un_caracter(lista,valor):
    nueva=[]
    for j in lista:
        var=j.replace(valor,"")
        nueva.append(var)
    return nueva

#Realizar una funcion que retorne la copia de una lista que pasa por parametro 
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""
def copia_lista(lista):
  return lista.copy() 
#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""  
def numeros_pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  return aux 
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista
"""  
def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista
#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
Salidas
"""  
def letra():
  pass  
#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
lista->list->lista
Salidas
tamaño-->int->tamano
"""   
def tamano_lista():
  pass #RetornaUnEntero
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
Salidas
"""  
def informacion_lista():
  pass
#Retornar una lista con los numero negativos  
"""
Entradas:
Salidas
"""  
def numeros_negativos(lista):
    
  pass
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
def posicion_elemento(elemento):
    lista.index(elemento)
    return lista
  pass
#realizar una funcion que agregue al final de archivo frutas una fruta
def frutas(elemento):
    with open (frutas, 'a') as f:
        f.write("fruta añadida\r\n")
  pass
#Realizar una funcion que cuente el numero de veces que se repite un elemento  
def repetir(elemento):
    nueva=[]
    for elemento in lista:
    if not elemento in nueva:
    nueva.append(elemento)
    return nueva
  pass
  
if __name__ == "__main__":
  lista=[1,2,3,4,4]
  copy=copia_lista(lista)
  print(copy)
