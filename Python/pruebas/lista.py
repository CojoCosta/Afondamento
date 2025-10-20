# Lista: colección de elementos ordenada.
# Es mutable.
# se definen entre corchetes
pokemons = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle", "Charizard"]
print(type(pokemons))
print("\nOriginal:", pokemons)
pokemons.append("Eevee")  # añade al final
pokemons.insert(2, "Ratatta")
print("\nTras añadir:", pokemons)



pokemons.remove("Bulbasaur")  # elimina elemento
del pokemons[5]
print("\nTras eliminar:", pokemons)


f = pokemons.pop()  # extrae y elimina el último.
print("\nExtrae y elimina:", f)
print("\nQueda:", pokemons)


pokemons[0] = "Ditto"  # modificar
print("\nY tras modificar:", pokemons)
print("\n")

#--------------------------------------TUPLAS----------------------------------------#

# Similar a la lista pero no se puede modificar. INMUTABLES
colores = ("magenta", "cian", "amarillo")
print(type(colores))
print(colores)
print(colores[0])
# colores[0] ="amarillo" #error
print("\nOperaciones permitidas en tuplas:")
print("Longitud:", len(colores))
print("¿Está 'cian' en la tupla?", "cian" in colores)


# Iteración sobre listas y tuplas
# como un foreach clásico
print("\nPokemons")
for pokemon in pokemons:
    print(f"{pokemon:>10}")

print("\n Colores")
for color in colores:
    print(f"{color:>10}")
# Es posible hacer una lista o tupla de cualquier tipo, incluso de otra lista o tupla.
# En general cualquier estructura puede contener otra estructura.


# STRING FORMATEADO
a = """
            Hola
que tal
                        mariconazo"""
print(a)