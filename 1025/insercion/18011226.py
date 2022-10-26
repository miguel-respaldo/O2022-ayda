#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alexa Fernanda Iniguez Jimenez
# No. Control: 18011226
# Calificación: XX

def ord_insercion(numeros):

     for i in range(1, len(numeros)):
        insercion = numeros[i]
        j = i - 1

        while j >= 0 and numeros[j] > insercion:
            numeros[j + 1] =  numeros[j]
            j -= 1

        numeros[j + 1] = insercion



elementos = [8, 3, 1, 19, 14, 20]
print("Lista original:",elementos)
ord_insercion(elementos)
print("Lista ordenada:",elementos)

