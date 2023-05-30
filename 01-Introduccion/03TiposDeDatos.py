#un tipo de dato es la propiedad de un valor para poder determinar que valores
#puede tomar

#String
#este tipo de dato nos permite guardar textos y se guardan entre comillas
# pueden ser simple o dobles 'texto' o "texto" hambas son validas
print("*"*30)
print("*      Variables String      *")
print("*"*30)

titulo_curso = "Curso de pyhton"
nombre_usuario = 'mauricio'
print(titulo_curso)
print(nombre_usuario)

#se pueden 
texto_combinado = "este es un texto 'que contiene comillas' "
#tambien se puede hacer de manera inversa
texto_combinado2 = 'Este es otro texto "que tiene comillas" '

print(texto_combinado)
print(texto_combinado2)

#tambien podemos guardar saltos de linea en una cadena de string
#de la siguiente manera

mensaje = '''Esta variable tiene
saltos de lineas y se imprimira
de la manera en como se ve
con la triple comilla simple'''

mensaje2 = """Esta variable tiene
saltos de lineas y se imprimira
de la manera en como se ve
con la triple comilla doble"""

print(mensaje)
print(mensaje2)


#Int
#Almacenan tipo de datos numericos enteros tanto positvos como negativos
num1 = 10
num2 = -10
#tambien podemos guardar resultado de operaciones matematicas
suma = 10 + 10
print("*"*30)
print("*        Variables Int       *")
print("*"*30)

print(num1)
print(num2)
print(suma)
print("*"*30)
print("*      Variables Float       *")
print("*"*30)

#Float
#Almacenan tipo de datos numericos reales
num3 = 2.13
print(num3)

#Bool
#solo tienen 2 tipos de valores True o False
verdadero = True
falso = False
print("*"*30)
print("*      Variables Bool        *")
print("*"*30)

print(verdadero)
print(False)