'''
COMO YA SABEMOS LA FUNCION INPUT() NOS RETORNA VARIABLES DE TIPO STRIG
PERO QUE PASA SI QUEREMOS HACER OPERACIONES MATEMATICAS
-Ejemplo:
    num_1 = input("ingrese num 1: ")
    num_2 = input("ingrese num 2: ")
    resultado = num_1 + num_2
    print(resultado)

Este programa nos va a tirar un resultado distinto al que esperabamos...
supongamos que num_1 = 3 y num_2 = 10 
el resultado de la operacion anterior va a ser 310 ...

-¿PERO POR QUE SUCEDE ESTO?
    como ya anticipamos los valores que retorna la funcion input son de tipo
    string y al querer hacer la suma entre los 2 valores leidos lo que va a 
    hacer nuestro programa es concatenar las cadenas de texto que obtuvo 
    mediante la funcion input

-COMO SE RESUELVE ESO?
    En el caso de querer realizar operaciones matematicas con datos introducidos
    por el usuario lo que tenemos que hacer es la conversion de esos datos
    con funciones int(num_1)  float(num_1)  str(123)

Lo que hacen estas funciones es convertir los datos para que nosotros podamos
operar con ellos... 
'''

num1 = int(input("Ingrese el valor de num1: "))
num2 = int(input("ingrese el valor de num2: "))

resultado = num1 + num2
print(f"{num1} + {num2}= {resultado}")

'''
Ahora podemos ve que la operacion se realiza de manera correcta o por lo menos
de la manera que nosotros queramos y lo mismo se puede aplicar con otras 
funciones de conversion de datos
'''

'''Observaremos los tipos de datos y los convertiremos a nuestra conveniencia'''


print("*"*50)
num1 = input("Ingrese el valor de num1: ")
num2 = input("ingrese el valor de num2: ")
print("*"*50)
print(f"Tipo de dato: {type(num1)} , valor de dato: {num1}")
num = int(num1)
print("Convetirmos el dato a int")
print(f"Tipo de dato: {type(num1)} , valor de dato: {num1}")
print("*"*50)
print(f"Tipo de dato: {type(num2)} , valor de dato: {num2}")
num2 = float(num2)
print("Convetirmos el dato a float")
print(f"Tipo de dato: {type(num2)} , valor de dato: {num2}")

