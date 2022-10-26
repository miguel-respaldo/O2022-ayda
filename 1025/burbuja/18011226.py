#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alexa Fernanda Iniguez Jimenez
# No. Control: 18011226
# Calificación: XX

def ord_burbuja(numeros):
    intercambio = True

    while intercambio:
        intercambio = False

        for i in range(len(numeros) - 1):
            if numeros[i] > numeros[i + 1]:
                numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
                intercambio = True

elementos = [8, 3, 1, 19, 14, 20]
print("Lista original:",elementos)
ord_burbuja(elementos)
print("Lista ordenada:",elementos)