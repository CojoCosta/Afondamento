
import string


def contarPalabras(texto):
    textoDeUso = texto.lower()
    for signo in string.punctuation:
        textoDeUso = textoDeUso.replace(signo, "")
    palabras = textoDeUso.split()
    diferentesPalabras = {}
    for palabra in palabras:
        if(palabra in diferentesPalabras):
            diferentesPalabras[palabra]+=1
        else:
            diferentesPalabras[palabra]=1
    return diferentesPalabras
    
def estadidisticasDeTexto(texto):
    diccionario = contarPalabras(texto)
    numeroPalabras = sum(diccionario.values())
    totalPalabras = 0
    for clave, valor in diccionario.items():
        totalPalabras += len(clave)*valor
    longMediaPalabras = totalPalabras / numeroPalabras
    palabraLarga = list(diccionario.keys())[0]
    frecuencia= list(diccionario.values())[0]
    palabraMasFrecuente= list(diccionario.keys())[0]
    
    for clave, valor in diccionario.items():
        if len(clave) > len(palabraLarga):
            palabraLarga = clave
        if valor > frecuencia:
            frecuencia = valor
            palabraMasFrecuente = clave
    
    return (totalPalabras, longMediaPalabras, palabraLarga, palabraMasFrecuente)

def leerDoc():
    try:
        archivo = input("Que archivo quieres examinar¿?\n")
        lectura = open(archivo, "r")
        contenido = lectura.read()
        lectura.close()
        return contenido
    except FileNotFoundError:
        print ("No existe el archivo")

# PROGRAMA PRINCIPAL
archivo = leerDoc()
diccionario = contarPalabras(archivo)
print ("Apartado A(Diccionario)", end="\n")
for clave, valor in sorted(diccionario.items()):
    print (f"{clave} : {valor}")

print ("Apartado B(Estadísticas)", end="\n")
totalPalabras, longMediaPalabras, palabraLarga, palabraMasFrecuente = estadidisticasDeTexto(archivo)
print(f"Total palabras: {totalPalabras} \nLongitud media de las palabras: {longMediaPalabras:.2f} \nPalabra más larga: {palabraLarga} \nPalabra más frecuente: {palabraMasFrecuente}")