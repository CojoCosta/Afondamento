from random import randint



def division():
    try:
        dato1 = float(input("Escribe un numero: "))
        dato2 = float(input("Escribe otro numero: "))
        if dato2 == 0:
            print ("No dividimos entre 0")
            return
        cociente = int(dato1 // dato2);
        resto = dato1 % dato2
        division = dato1 / dato2
        print(f"Cociente: {cociente}", end="\n")
        print(f"Resto: {resto}", end="\n")
        print(f"Resultado división: {division:.4f}", end="\n")
    except ValueError:
        print("Introduce un numero", end="\n")

def potencia():
    try:
        base= float(input("Escribe la base: "))
        exponente= int(input("Escribe el exponente: "))
        resultado = base**exponente
        print (f"Potencia en base {base} y de esponente {exponente} es: {resultado:.2f}")
    except ValueError:
        print("Introduce un numero", end="\n")

def rango():
    try:
        dato1= int(input("Escribe el primer numero: "))
        dato2= int(input("Escribe el segundo numero: "))
        suma=0
        if(dato1>dato2):
            print(f"{dato1} es mayor que {dato2}", end="\n")
            datoAux= dato2
            dato2=dato1
            dato1=datoAux
        else:
            print(f"{dato2} es mayor que {dato1}", end="\n")
        acu = 0
        for numero in range(dato1,dato2+1):
            acu += numero;
        print(f"La suma de los numeros entre {dato1} y {dato2} es: {acu}", end="\n")
    except ValueError:
        print("Introduce un numero", end="\n")

def listas():
    try:
        longitudLista = int(input("Elige la longitud de esta lista: "))
        if longitudLista <= 0:
            return
        lista = []
        lista2 = []
        lista3 = []
        for i in range(1, longitudLista + 1):
            lista.append(randint(1,20))
            lista2.append(randint(1,20))
            lista3.append(lista[i-1]+ lista2[i-1])
        print(f"Lista 1: {lista}", end="\n") 
        print(f"Lista 2: {lista2}", end="\n") 
        print(f"Lista 3: {lista3}", end="\n") 
    except ValueError:
        print("Introduce un numero", end="\n")
    
def menu():
    while  True:
        print ("1.- Divisiones.", end= "\n")
        print ("2.- Potencia.", end= "\n")
        print ("3.- Rango.", end= "\n")
        print ("4.- Listas.", end= "\n")
        print ("5.- Salir.", end= "\n")
        opcion = int(input("Elije una opcion: "))
    
        if opcion == 1:
            division()
        if opcion == 2:
            potencia()
        if opcion == 3:
            rango()
        if opcion == 4:
            listas()
        if opcion == 5:
            print("Gracias por usar el programa")
            break
        else:
            print("Opción no válida.", end= "\n")

menu()
    
        