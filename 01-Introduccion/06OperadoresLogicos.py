'''
     ---EJECUTAR EL PROGRAMA PARA HACER PRUEBAS CON 3 NUMEROS----
Los operadores logicos nos sirven para comparar valores booleanos y son 3
and = y
or = o
not = invertir valor

--------------------tabla de verdad and: --------------------
True  and True  = True
True  and False = False
False and True  = False
False and False = False

--------------------tabla de verdad or: ---------------------
True  or True  = True
True  or False = True
False or True  = True
False or False = False

--------------------tabla de verdad not: ---------------------

not True  = False
not False = True

Recordar que True o False pueden ser operaciones Relacionales 
como mostraremos a continuacion
'''

NUMERO_UNO = input("ingrese valor de NUMERO_UNO: ")
NUMERO_DOS = input("ingrese valor de NUMERO_DOS: ")
NUMERO_TRES = input("ingrese valor de NUMERO_TRES: ")

print(f'''
-------------------------------------------------------------------------
NUMERO_UNO < NUMERO_DOS and NUMERO_DOS < NUMERO_TRES

el resultado de esta operacion logica se evaluaria de la siguiente manera
1- analiza NUMERO_UNO < NUMERO_DOS -> nosotros usamos {NUMERO_UNO} < {NUMERO_DOS} = {NUMERO_UNO<NUMERO_DOS}
2- amaliza NUMERO_DOS < NUMERO_TRES -> nosotros usamos {NUMERO_DOS} < {NUMERO_TRES} = {NUMERO_DOS<NUMERO_TRES}
3- analiza los resultados obtenidos -> {NUMERO_UNO<NUMERO_DOS} and {NUMERO_DOS<NUMERO_TRES} = {NUMERO_UNO<NUMERO_DOS and NUMERO_DOS<NUMERO_TRES}
Por lo tanto el resultado final es {NUMERO_UNO<NUMERO_DOS and NUMERO_DOS<NUMERO_TRES}
-------------------------------------------------------------------------''')

print(f'''
-------------------------------------------------------------------------
NUMERO_UNO > NUMERO_DOS or NUMERO_DOS > NUMERO_TRES

el resultado de esta operacion logica se evaluaria de la siguiente manera
1- analiza NUMERO_UNO > NUMERO_DOS -> nosotros usamos {NUMERO_UNO} > {NUMERO_DOS} = {NUMERO_UNO>NUMERO_DOS}
2- amaliza NUMERO_DOS > NUMERO_TRES -> nosotros usamos {NUMERO_DOS} > {NUMERO_TRES} = {NUMERO_DOS>NUMERO_TRES}
3- analiza los resultados obtenidos -> {NUMERO_UNO>NUMERO_DOS} or {NUMERO_DOS>NUMERO_TRES} = {NUMERO_UNO>NUMERO_DOS or NUMERO_DOS>NUMERO_TRES}
Por lo tanto el resultado final es {NUMERO_UNO>NUMERO_DOS or NUMERO_DOS>NUMERO_TRES}
---------------------------------------------------------------------------''')

print(F'''
-------------------------------------------------------------------------
not (NUMERO_UNO == NUMERO_DOS) or (NUMERO_DOS == NUMERO_TRES)

el resultado de esta operacion logica se evaluaria de la siguiente manera
1- analiza NUMERO_UNO == NUMERO_DOS -> nosotros usamos {NUMERO_UNO} == {NUMERO_DOS} = {NUMERO_UNO==NUMERO_DOS}
2- analiza not({NUMERO_UNO==NUMERO_DOS}) -> nos quedaria : invertido => {not (NUMERO_UNO==NUMERO_DOS)}
3- amaliza NUMERO_DOS == NUMERO_TRES -> nosotros usamos {NUMERO_DOS} == {NUMERO_TRES} = {NUMERO_DOS==NUMERO_TRES}
4- analiza los resultados obtenidos -> {not (NUMERO_UNO==NUMERO_DOS)} or {NUMERO_DOS==NUMERO_TRES} = {not(NUMERO_UNO==NUMERO_DOS) or NUMERO_DOS==NUMERO_TRES}
Por lo tanto el resultado final es {not(NUMERO_UNO==NUMERO_DOS) or NUMERO_DOS==NUMERO_TRES}
-------------------------------------------------------------------------''')
