def pide_entero_positivo():
    try:
        numero = int (input("Escribe un numero entero positivo: "))
        while(numero < 0):
            numero = int (input("Escribe un numero entero positivo: "))
    except ValueError :
        print ("Escribe un numero")
    return numero


def comprueba_isbn(isbn):
    isbn = isbn.strip().replace(" ","").replace("-","")
    if len(isbn) != 10 or not isbn[0:9].isdigit():
            return False
    if (isbn[-1] or isbn.endswith("X")):
        return True
    return False

def pide_libro():
    titulo = ""
    autor = ""
    while titulo == "":
        titulo = input("Cual es el titulo del libro¿?\n").strip()
    while autor == "":
        autor = input("Cual es el autor del libro¿?\n").strip()
    isbn = input("Cual es su ISBN¿?\n")
    while comprueba_isbn(isbn) == False:
        isbn = input("Cual es su ISBN¿?\n")
        comprueba_isbn(isbn)
    print ("Nº de paginas¿?")
    numero_paginas = pide_entero_positivo()
    return titulo, autor, isbn, numero_paginas


# PROGRAMA PRINCIPAL
libros = []
try:
    archivo_lectura = open ("Python\\boletin\\Ejercicio3\\ejercicio3.txt", "r")
    linea = archivo_lectura.readline()
    while linea:
        datos = linea.split(",")
        while datos:
            libros.append(datos)
    archivo_lectura.close()
except FileNotFoundError:

    print ("Archivo no existente")
opcion = 0
while opcion != 4:
    print ("1.- Añadir libro.", end="\n")
    print ("2.- Mostrar lista.", end="\n")
    print ("3.- Eliminar libros.", end="\n")
    print ("4.- Salir.", end="\n")
    print ("Elige una opcion: ")
    opcion = pide_entero_positivo()
    if opcion == 1:
        libros.append(pide_libro())
    elif opcion == 2:
        print(f"{"Título":<20} {"Autor":<20} {"ISBN":<20} {"Nº Páginas":<20}")
        for libro in libros:
            print(f"{libro[0]:<20} {libro[1]:<20} {libro[2]:<20} {libro[3]:<20}")
    elif opcion == 3:
        titulo = input("Que libro vas a eliminar¿? \n")
        for libro in libros:
            if libro[0] == titulo:
                libros.remove(libro)
    elif opcion == 4:
        print ("Gracias por usar el programa ")
    else :
        print ("Elige una opción correcta\n")

with open ("Python\\boletin\\Ejercicio3\\ejercicio3.txt", "w") as archivo_escritura:
    for libro in libros:
        archivo_escritura.write(f"{libro[0]}, {libro[1]}, {libro[2]}, {libro[3]}")

