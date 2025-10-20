numero = int(input("dame un nº"))

if numero > 0:
    print("Es positivo")

    if numero > 10:
        print("MAS identacion")

    print("Dentro primer if")

print("Fuera")

if numero > 0:
    print("El número es positivo.")
    print("Esto también está dentro del if.")
elif numero == 0:
    print("El número es el cero.")
else:
    print("El número es negativo")
print("Esto ya está fuera de la estructura por la identación.")

respuesta = input("¿Deseas continuar?\n")

#---------------------------------------------------------------------------------#

# Las cadenas sí se pueden comparar con ==
# Las operaciones lógicas son and, or y not
if respuesta =="si" or respuesta == "Si" or respuesta == "SI":
    print("Pues lo lamento porque por ahora voya a parar")
print("Fin del ejemplo")

# Ternaria
print("Positivo o 0" if numero >= 0 else "Negativo")
