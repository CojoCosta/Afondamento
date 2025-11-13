# 7. Realiza una simulación de aciertos en el juego de la lotería primitiva usando
# colecciones. Para ello haz las siguientes funciones:

# Realiza una función (denominada rellenaCol) que tenga como parámetro una
# colección de enteros. Debe limpiarla y rellenarla con 6 valores aleatorios distintos
# entre 1 y 49 ambos inclusive.

# Otra función (denominada compara) a la que se le pasan dos colecciones de
# enteros y comprueba cuantos elementos de una colección están en la otra.
# Devuelve dicho valor.

# En el main el usuario introducirá 6 números diferentes entre 1 y 49 separados por
# comas y se guardarán en una colección (se deben hacer las comprobaciones
# pertinentes). Si quieres haz alguna función más para modularizar esta parte.
# A continuación lanza un millón de loterías mediante la función rellenaCol y por cada
# una comprueba los aciertos que ha tenido el usuario mediante compara. Usa un
# array de 7 posiciones para ir incrementando cada una de ellas según los aciertos.

# Es decir, si compara devuelve 0 incrementas la posición 0 de ese array, si compara
# devuelve 3 pues rellenas la posición 3. De esa forma al final de la simulación tienes
# la cantidad de veces que han salido 0 aciertos, 1 acierto, 2, aciertos, etc. Muestra
# estos datos por pantalla y comprueba que efectivamente no vale la pena jugar.
import random
def rellenaCol(listaEnteros: list):
    listaEnteros.clear()
    while  len(listaEnteros) < 7:
        listaEnteros.append(random.randint(1,50))
    return listaEnteros


def compara(enteros1: list, enteros2: list):
    contador = 0
    for i in range(0, len(enteros1)):
        if (enteros1[i] in enteros2):
            contador += 1
    return contador

# MAIN
def main(): # KeyboardException
    flag = True
    listaFinal = []
    contador = 0
    while flag:
        usuario = input("Dime 6 numeros, entre el 1 y el 49, ambos son válidos, separalos por ',': ")
        numerosSplited = usuario.split(",")
        if len(numerosSplited) == 6:
            for i in range(len(numerosSplited)):
                if numerosSplited[i].isdigit() and (int(numerosSplited[i]) > 0 and int(numerosSplited[i])<50):
                    listaFinal.append(int(numerosSplited[i]))
            if len(listaFinal)==6:
                flag = False
        else:
            print ("METE 6 PUTOS NÚMEROS SUBNORMAL")
    for i in range(0, 1000000):
        nuevaLista = []
        rellenaCol(nuevaLista)
        if compara(nuevaLista, listaFinal) == 6:
            contador + 1
            print ("SOY MILLONARIO PERRAS")


main()


