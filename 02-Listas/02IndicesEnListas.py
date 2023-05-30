'''
Los elementos de las listas en python son como la mayoria de los lenguajes,
se empieza a contar desde el numero cero (0) el cual le corresponde al 
primer elemento de la lista...

lista    = [ elemento1 , elemento2 , elemento3 ,  ....]
posicion = [    0      ,     1     ,     2     ,  ....]

y si queremos acceder a un elemento en especifico de la lista lo haremos a
travez de esos indices... RECORDAR QUE COMIENZA DEL NUMERO 0

De la misma manera tambien tenemos los indices negativos el cual cuenta desde
la ultima posicion como -1 y de ahi va descendiendo como muesta a continuacion
'''

# Negativos        -6        -5       -4       -3      -2         -1
# Positivos         0         1        2        3       4          5
lista_cursos = ["Python", "Django", "flask", "Ruby", "Java", "JavaScript"]


print("-------------------------------------------------------------")
print("Contenido de la lista: ")
print(lista_cursos)
print("-------------------------------------------------------------")
print("Primer elemento de la lista: ",lista_cursos[0])
print("Segundo elemento de la lista: ",lista_cursos[1])
print("Ante-Ultimo elemento de la lista", lista_cursos[-2])
print("Ultimo elemento de la lista: ",lista_cursos[-1])
