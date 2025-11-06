def pide_entero_positivo():
    try:
        numero = int (input("Escribe un numero entero positivo"))
        while(numero < 0):
            numero = int (input("Escribe un numero entero positivo"))
    except ValueError :
        print ("Escribe un numero")
    return numero


def comprueba_isbn(isbn):
    dato_sin_espacios = isbn.strip().replace(" ","").replace("-","")
    if len(dato_sin_espacios) != 10 or not dato_sin_espacios[0:9].isdigit():
            return False
    if (dato_sin_espacios[-1] or dato_sin_espacios.endswith("X")):
        return True
    return False

def pide_libro():
    

# PROGRAMA PRINCIPAL
isbn = "123456789X" 
isbn2 = "1234567890"
isbn3 = "1234X6789X"
isbn4 = "1234567890546"
isbn5 = "12-23 23451X"

print ("1º",end="\n")
print (comprueba_isbn(isbn),end="\n")
print ("2º",end="\n")
print (comprueba_isbn(isbn2),end="\n")
print ("3º",end="\n")
print (comprueba_isbn(isbn3),end="\n")
print ("4º",end="\n")
print (comprueba_isbn(isbn4),end="\n")
print ("5º",end="\n")
print (comprueba_isbn(isbn5),end="\n")