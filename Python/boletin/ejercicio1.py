opcion = 0;
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
        base= float(input("dime la base: "))
        exponente= int(input("dime el exponente: "))
        resultado = base**exponente
        print (f"Potencia en base {base} y de esponente {exponente} es: {resultado:.2f}")
    except ValueError:
        print("Introduce un numero", end="\n")



def menu():
    while opcion != 6:
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
            print("GRracias por usar el programa")
            break
        else:
            print("Opción no válida.", end= "\n")

menu()
    
        