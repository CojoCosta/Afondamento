def pide_entero_positivo():
    try:
        numero = int (input("Escribe un numero entero positivo"))
        while(numero < 0):
            numero = int (input("Escribe un numero entero positivo"))
    except ValueError :
        print ("Escribe un numero")
    return numero
# mensaje.endswith("X o un numero")
# len(mensaje)
# mensaje.strip() = trim()
# mensaje.isdigit()
def comprueba_isbn(isbn):
    dato_sin_espacios = isbn.strip()
    if " " in dato_sin_espacios and "-" in dato_sin_espacios:
        dato_sin_espacios.replace(" ","")
        dato_sin_espacios.replace("-","")
    if len(dato_sin_espacios) == 10:
        if dato_sin_espacios.isdigit() == False:
            return False
        if (dato_sin_espacios.endswith("X") and dato_sin_espacios.count("X") == 1):
            for caracter in range(len(dato_sin_espacios) - 1):
                if caracter.isdigit() == False:
                    return False
        return True
    return False

