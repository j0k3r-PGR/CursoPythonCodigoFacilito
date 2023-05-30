'''
Como ya sabemos a estas alturas nosotros creamos una variable y le asignamos
un valor para la misma:

    <nombre_de_variable1> = <valor1>
    <nombre_de_variable2> = <valor2>
    <nombre_de_variable3> = <valor3>

Python nos permite crear varias  variables y darles valores al mismo tiempo
en una misma linea siempre manteniendo un orden:

    <nombre_var1>,  <nombre_var>, <nombre_var3> = <valor1>, <valor2>, <valor3>

VEAMOS UNOS EJEMPLOS
'''
nombre = "persona1"
apellido = "apellido1"
edad = 13
print(f"Hola me llamo {nombre} {apellido}, tengo {edad} años")

nombre , apellido, edad = "presona1", "apellido2" , 117 
print(f"Hola me llamo {nombre} {apellido}, tengo {edad} años")

''''
Al ejecutar el programa veremos que las 2 opciones son validas y llendo un
poco mas lejos podemos hacer lo mismo con las funciones como por ejemplo
con la funcion input()
'''

nombre, apellido = input("Ingrese nombre: "), input("Ingrese apellido: ")
print(f"Bienvenido señor {nombre} {apellido}")

'''
PODEMOS HACER TODAS LAS COMBINACIONES POSIBLES E INCLUSO APLICAR CONVERSION
DE TIPO DE DATOS COMO VIMOS ANTERIORMENTE...
            ---- A SEGUIR PROBANDO ----
'''