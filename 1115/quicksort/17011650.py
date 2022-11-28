#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Emmanuel Gonzalez Gomez
# No. Control: 170111650
# Calificación: XXX

def partition(array, i, f):
    pivote = array[f]
    a = i - 1
 
    for b in range(i, f):
        if array[b] <= pivote:
            a = a + 1
            (array[a], array[b]) = (array[b], array[a])
    (array[a + 1], array[f]) = (array[f], array[a + 1])
    return a + 1

def quickSort(array, i, f):
    if i < f:
        pi = partition(array, i, f)
        quickSort(array, i, pi - 1)
        quickSort(array, pi + 1, f)
    
arreglo = [7,2,1,6,8,5,3,4]
inicio = 0
final = len(arreglo) - 1

print("Arreglo desordenado: ", arreglo)
quickSort(arreglo, inicio, final)
print("Arreglo ordenado: ", arreglo)
