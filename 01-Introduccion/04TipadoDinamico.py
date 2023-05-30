#en python las variables son dinamicas. puedo definir una variable
#u durante la ejecucion cambiarle el valor y tipo de dato

variable_dinamica = 1
print("tipo de dato: ", type(variable_dinamica))
print("valor del dato: " , variable_dinamica)
print("*"*50)

variable_dinamica = 1.3
print("tipo de dato: ", type(variable_dinamica))
print("valor del dato: " , variable_dinamica)
print("*"*50)

variable_dinamica = "hola ! :)"
print("tipo de dato: ", type(variable_dinamica))
print("valor del dato: " , variable_dinamica)
print("*"*50)

variable_dinamica = True
print("tipo de dato: ", type(variable_dinamica))
print("valor del dato: " , variable_dinamica)
print("*"*50)

'''
Se recomienda no utilizar esta propiedad de variables dinamicas
ya que podriamos confundirno a la hora del programa para que 
fue inventada cada variable
'''