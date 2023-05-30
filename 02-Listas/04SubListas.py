'''
En Python podemos crear sublistas de una lista que nosotros tengamos de diferentes
maneras:
    indicando inicio y fin
    indicando solo inicio y que me traiga los ultimos elementos
    indicando el fin y que me traiga los primeros elementos
    podemos agregar un 3er parametro que es el salto (si es -1 la invierte)
'''

#POSICIONES EN LA LISTA DE LOS ELEMENTOS --------------------------
#negativo= -13 -12 -11 -10  -9  -8  -7  -6  -5  -4    -3   -2   -1
#positivo=   0   1   2   3   4   5   6   7   8   9    10   11   12
#          --------------------------------------------------------
mi_lista = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 ]

print("------------------------------------------------------------------")
print("Lista Principal: ",mi_lista)
print("------------------------------------------------------------------")

#generamos nuestra primer sub lista con [inicio:fin]
#recordar que el elemento de la posicion 7 no va a estar en la sublista
sub_lista_1 = mi_lista[2:7] 
print("Generamos la sublista con: sub_lista_1 = mi_lista[2:7] ")
print("Resultado: ",sub_lista_1)
print("------------------------------------------------------------------")

sub_lista_2 = mi_lista[5: ] 
print("Generamos la sublista con: sub_lista_2 = mi_lista[5: ] ")
print("Resultado: ",sub_lista_2)
print("------------------------------------------------------------------")

sub_lista_3 = mi_lista[ :5] 
print("Generamos la sublista con: sub_lista_3 = mi_lista[ :5] ")
print("Resultado: ",sub_lista_3)
print("------------------------------------------------------------------")


sub_lista_4 = mi_lista[:] 
print("Generamos la sublista con: sub_lista_4 = mi_lista[:] ")
print("Resultado: ",sub_lista_4)
print("------------------------------------------------------------------")

sub_lista_5 = mi_lista[ : :-1] 
print("Generamos la sublista con: sub_lista_5 = mi_lista[ : :-1]")
print("Resultado: ",sub_lista_5)
print("------------------------------------------------------------------")

sub_lista_6 = mi_lista[ : :2] 
print("Generamos la sublista con: sub_lista_6 = mi_lista[ : :2]")
print("Resultado: ",sub_lista_6)
print("------------------------------------------------------------------")

sub_lista_7 = mi_lista[1: :2] 
print("Generamos la sublista con: sub_lista_7 = mi_lista[1: :2]")
print("Resultado: ",sub_lista_7)
print("------------------------------------------------------------------")