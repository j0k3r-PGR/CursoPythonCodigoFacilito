'''
Para modifical las listas tenemos varios metodos... 
    agregar        -> lista.append(elemento) 
    insertar       -> lista.insert(indice, elemento)
    eliminar       -> lista.remove(elemento)
    extender       -> lista.extend(otraLista)
    elimiarTodo    -> lista.clear() 
    eliminarIndice -> del lista[indice]
'''

lista = [1,2,3]

print(lista)
print("longitud de la lista", len(lista))

print("----------- Append -------------")
lista.append(4)
lista.append(10)
print(lista)
print("longitud de la lista", len(lista))

print("----------- Insert -------------")
lista.insert(0,100)
print(lista)
print("longitud de la lista", len(lista))

print("----------- Extend -------------")
lista2 = [10,20,30]
print(lista,"y",lista2)
lista.extend(lista2)
print(lista)
print("longitud de la lista", len(lista))

print("----------- Del -------------")
del lista[0]
print(lista)
print("longitud de la lista", len(lista))

print("----------- Clear -------------")
lista.clear()
print(lista)
print("longitud de la lista", len(lista))