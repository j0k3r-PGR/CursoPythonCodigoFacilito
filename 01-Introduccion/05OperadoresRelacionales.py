'''
    tenemos 6 operadores relacionales el cual como resultado nos dara valores
    booleanos (true o false)
    mayor que           >
    menor que           <
    mayor o igual que   >=
    menor o igual que   <=
    igual que           ==
    distinto que        !=

    al ejecutar este programa podemos ingresar los valores 
    de NUMERO_UNO y NUMERO_DOS para poder hacer nuestras
    pruebas
'''

NUMERO_UNO = input("ingrese valor de NUMERO_UNO: ")
NUMERO_DOS = input("ingrese valor de NUMERO_DOS: ")

print("numero_uno: ",NUMERO_UNO)
print("numero_dos: ",NUMERO_DOS)
resultado = NUMERO_UNO > NUMERO_DOS
print("----------------Operacion 'mayor que' -------------------")
print("numero_uno > numero_dos: ", resultado)

resultado = NUMERO_UNO < NUMERO_DOS
print("----------------Operacion 'menor que' -------------------")
print("numero_uno < numero_dos: ", resultado)

resultado = NUMERO_UNO >= NUMERO_DOS
print("-------------Operacion 'mayor o igual que' --------------")
print("numero_uno >= numero_dos: ", resultado)

resultado = NUMERO_UNO <= NUMERO_DOS
print("---------------Operacion 'menor o igual que' ------------")
print("numero_uno <= numero_dos: ", resultado)

resultado = NUMERO_UNO == NUMERO_DOS
print("----------------Operacion 'igual que' -------------------")
print("numero_uno == numero_dos: ", resultado)

resultado = NUMERO_UNO != NUMERO_DOS
print("----------------Operacion 'distinto que' --------------------")
print("numero_uno != numero_dos: ", resultado)