'''
las LISTAS son un tipo de dato complejo en python , que tienen varias caracteristicas
- son dinamicas (se pueden redimencionar durante la ejecucion)
- se pueden mezclar los tipos de datos (int, str, float, bool, List) 
- y mas que iremos viendo a continuacion

Para crear una lista se puede hacer de 2 maneras:
    <Nombre_lista> = list()
    <nombre_lista> = []

De esta forma creamos listas vacias que se pueden redimencionar y hacer muchas
cosas mas como ordenarlas, cortarlas, etc...

Tambien podemos crear listas con elementos dentro de ellas como por ejemplo
    <nombre_lista> = [1,2,3,4,5]
'''

#creamos nuestras primeras listas
mi_lista1 = [] 
mi_lista2 = list()
mi_lista3 = [1,2,3,4,5]

#imprimimos el tipo de dato de mi_lista y sus valores
print("-----------------------------------------------------------------")
print("* tipo de dato mi_lista1 creada con []: ", type(mi_lista1))
print("* valores: ", mi_lista1)
print("-----------------------------------------------------------------")
print("* tipo de dato mi_lista2 creada con list(): ", type(mi_lista2))
print("* valores: ", mi_lista2)
print("-----------------------------------------------------------------")
print("* tipo de dato mi_lista3 creada con [1,2,3,4,5]: ", type(mi_lista3))
print("* valores: ", mi_lista3)
print("-----------------------------------------------------------------")

'''
RECORDAR QUE EN UN LISTA SE PUEDEN ALMACENAR TIPOS DE DATOS DISTINTOS, NO 
NECESARIAMENTE TIENEN QUE SER DEL MISMO TIPO
'''

mi_lista = ["nombre", 23 , 10.4 , False]
print("         LISTA CON DISTINTOS TIPOS DE DATOS")
print("-----------------------------------------------------------------------------")
print('* tipo de dato mi_lista creada con ["nombre", 23 , 10.4 , False]: ', type(mi_lista3))
print("* valores: ", mi_lista)
print("----------------------------------------------------------------------------")
