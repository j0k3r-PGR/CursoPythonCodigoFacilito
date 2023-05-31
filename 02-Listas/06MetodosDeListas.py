'''
Tenemos varios metodos posibles y muy utiles como por ejemplo:
    .sort()               -> Ordena de menor a mayor
    .reverse()            -> invierte el orden de los elementos de la lista
    min(lista)            -> obtenemos el elemento de menor valor
    max(lista)            -> obtenemos el elemento de mayor valor
    elemento in lista     -> mira si el elemento se encuentra en la lista
    elemento not in lista -> mira si el elemento no esta en la lista
    .index(elemento)      -> nos retorna el indice donde se encuentra el elemento
                             Si hay mas elementos nos retornara el primer indice
                            Si el indice no se encuentra nos da error
'''

lista = [3,1,8,5,4,12,6,54,46,47,8,65767,432]

print("---------------  List Initial --------------")
print(lista)

print("---------------  Sort --------------")
lista.sort()
print(lista)

print("---------------  Reverse --------------")
lista.reverse()
print(lista)

print("---------------  Min --------------")
print(min(lista))

print("---------------  Max --------------")
print(max(lista))

print("---------------  Element in List --------------")
print(lista)
print("1 in lista: ",1 in lista)

print("---------------  Element not in List --------------")
print(lista)
print("1 not in lista: ",1 not in lista)

print("--------------- Index --------------")

print('''#primero validamos que exista en la lista para consultar su posicion
#y despues ultilizamos index por que si no puede llegar a tirar un error
#durante la ejecucion del programa
if 1 in lista:
    print(lista.index(1))
''')
if 1 in lista:
    print(lista.index(1))
