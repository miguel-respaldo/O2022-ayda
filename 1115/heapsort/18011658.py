#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luna Gonzalez Alan Alejandro
# No. Control: 18011658
# Calificación: XXX

print("¡Bienvenido!")
print("Programmer: Alan Luna | HeapSort.\n")

'''HeapSort'''

from heapq import heappop, heappush


def heapsort(ordenamiento):
    pivote = []
    for num in ordenamiento:
        heappush(pivote, num)

    heapsort = []
    while pivote:
        heapsort.append(heappop(pivote))

    return heapsort


print("Arreglo ordenado:")
lista = [5, 88, 15, 55, 84, 13, 20, 11, 32, 65, 8, 9, 3, 92, 45, 56, 1, 45321, 12345, 929283, 87635]
print(heapsort(lista))
