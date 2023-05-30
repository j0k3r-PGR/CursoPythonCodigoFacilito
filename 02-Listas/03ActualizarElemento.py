'''
Para actualizar elementos de la lista lo hacemos accediento a el atravez del
indice ya sea positivo o negativo y le asignamos el nuevo valor
'''

# Negativos        -6        -5       -4       -3      -2         -1
# Positivos         0         1        2        3       4          5
lista_cursos = ["Python", "Django", "flask", "Ruby", "Java", "JavaScript"]

print("----------------------------------------------------------------------------------")
print("contenido inicial: ", lista_cursos)
print("----------------------------------------------------------------------------------")
lista_cursos[0] = "nuevoDato"
lista_cursos[-1] = "otroDato"
print('''---Aplicamos los siguiente cambios
---lista_cursos[0] = "nuevoDato"
---lista_cursos[-1] = "otroDato"
---mostramos en pantalla''')
print("-----------------------------------------------------------------------------------")
print("contenido modificado: ", lista_cursos)
print("-----------------------------------------------------------------------------------")