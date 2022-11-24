#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
    # Nombre: Jose Ruben Rodriguez Pacheco
# No. Control: 19011256
# Calificación: XXX

lista = [3,7,4,9,2,5,10,6,8,1]

def separacion(lista):
    if len(lista)<1:
        return[]

    izquierda = []
    derecha = []
    pivote = lista[0]

    for i in range(1,len(lista)):
        if lista[i]<pivote:
            izquierda.append(lista[i])
        else:
            derecha.append(lista[i])    

    return izquierda, pivote, derecha

def quickSort(lista):
    if len(lista)<2:
        return lista

    izquierda, pivote, derecha = separacion (lista)

    return quickSort(izquierda) + [pivote] + quickSort(derecha)

print(quickSort(lista))
