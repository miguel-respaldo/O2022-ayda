#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hernandez Uribe Nestor Eduardo
# No. Control: 18011339
# Calificación: XXX


def QuickSort(arreglo):

    elementos = len(arreglo)

    # Base case
    if elementos < 2:
        return arreglo

    posicion = 0

    for i in range(1, elementos):
        if arreglo[i] <= arreglo[0]:
            posicion += 1
            temporal = arreglo[i]
            arreglo[i] = arreglo[posicion]
            arreglo[posicion] = temporal

    temporal = arreglo[0]
    arreglo[0] = arreglo[posicion]
    arreglo[posicion] = temporal

    left = QuickSort(arreglo[0:posicion])
    right = QuickSort(arreglo[posicion+1:elementos])

    arreglo = left + [arreglo[posicion]] + right

    return arreglo


datos = [9, 1, 10, 85, 23, 6]
print(datos)
print(QuickSort(datos))