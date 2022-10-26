#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alexa Fernanda Iniguez Jimenez
# No. Control: 18011226
# Calificación: XX

def ord_selection(numeros):
    intercambio = True

    for i in range(len(numeros)):
        min = i #elemento pequeno

        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[min]:
                min = j

        numeros[i], numeros[min] = numeros[min], numeros[i]


elementos = [8, 3, 1, 19, 14, 20]
print("Lista original:",elementos)
ord_selection(elementos)
print("Lista ordenada:",elementos)
