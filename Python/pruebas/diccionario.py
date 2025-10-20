# Diccionarios: pares clave-valor
# En python tienen una sintaxis similar a JSON
diccionario_vacio = {}
persona = {
    "nombre": "Lisa Simpson",
    "edad": 8,
    "casada": False,
    "hijos": None,
    "intereses": ["música", "lectura", "arte"],
    "direccion": {"calle": "Evergreen Terrace", "numero": 742},
}
print(persona)
print(f"\nNombre: {persona["nombre"]}")  # acceso
persona["edad"] = 10  # modificación
print(f"\nEdad modificada: {persona["edad"]}")
# para añadir simplemente se asigna una clave no existente
persona["profesion"] = "estudiante"
del persona["hijos"]  # eliminar
print("Finalmente:\n", persona)
# Iteración sobre diccionarios
print()
for clave, valor in persona.items():
    print("%s:%s" % (clave, valor))  # print(f"{clave}:{valor}") #también valido
