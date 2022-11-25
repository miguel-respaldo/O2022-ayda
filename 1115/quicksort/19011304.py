#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luis Isael Campos Luna
# No. Control: 19011304
# Calificación: XXX

numeros = [5,4,3,2,1]

def QuickSort(numeros, izq, der):

    pivote = numeros[izq]
    i = izq
    j = der
    aux = 0

    while i < j:
        while numeros[i] <= pivote and i < j:
            i += 1

        while numeros[j] > pivote:
            j -= 1

        if i < j:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

    numeros[izq] = numeros[j]
    numeros[j] = pivote

    if izq < j-1:
        QuickSort(numeros,izq,j-1)

    if j+1 < der:
        QuickSort(numeros,j+1,der)

QuickSort(numeros,0,len(numeros) - 1)
print(numeros)