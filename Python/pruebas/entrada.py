
# 2 Formas
# print ("Dame tu nombre")
# nombre = input()





# Recuerda: No necesitamos declarar las variables
# Se podría hacer por separado (print y luego input)
nombre = input("Dime tu nombre: ")
# input siempre devuelve un String, por lo que hay que convertirlo a entero
edad = int(input("Ahora la edad: "))
temperatura = float(input("¿Qué temperatura e ºC hace ahora?\n"))
print() # deja una línea en blanco
print(nombre + ", Welcome\n to the JPython World.\n\n")
# También se importan librerías:
# El import mejor al principio
from datetime import date # del módulo datetime, importa la clase date
año_nacimiento = date.today().year - edad
print('Naciste en el año: ', año_nacimiento) # Se permite comilla simple para cadenas
# tambien permitido importar solo el módulo
import datetime
año_nacimiento = datetime.date.today().year - edad

from datetime import date 
año_nacimiento = date.today().year - edad

from datetime import date as d 
año_nacimiento = d.today().year - edad

letra = nombre[0] # Se indexa la cadena con []. Ojo, el carácter sigue siendo str.
print("la primera letra de tu nombre es %s" % letra) # Cadena de formato con %
