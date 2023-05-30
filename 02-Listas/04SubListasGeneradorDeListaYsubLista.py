'''
El siguiente codigo es de elaboracion propia el cual sirve para generar
sub-listas a partir de una lista creada con numeros el cual nosotros
decidimos la natidad de elemento que va a poseer y analiza las posibilidades
'''

fin = int(input("Ingrese cantidad de elementos para la lista: "))
mi_lista = list(range(fin))

print("----------------------------------------------------------------")
print("                      LISTA GENERADA")
print(mi_lista)
print("----------------------------------------------------------------")

while True:
    inicio = input("ingrese posicion inicial para la sublista (enter sin valor): ")
    fin = input("ingrese posicion final para la lista (enter sin valor): ")
    salto = input("ingrese saltos entre elementos a seleccionar (enter sin valor): ")

    inicio = None if "" == inicio else int(inicio)
    fin = None if "" == fin else int(fin)
    salto = None if "" == salto else int(salto)

    print("                 SUBLISTA GENERADA: ")
    print(mi_lista[inicio:fin:salto])
    print("----------------------------------------------------------------")

    if input("quiere salir del generador de Sub-Listas (s,si,SI,S)?: ") in ["si","s","SI","S"]:
        break
    print("INGRESANDO NUEVOS VALORES PARA GENERAR OTRA SUB-LISTA")

print("----------------------------------------------------------------")
print("         Muchas gracias por usar nuestros serivcios")
print("----------------------------------------------------------------")