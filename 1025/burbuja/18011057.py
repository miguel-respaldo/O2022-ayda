#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Mauricio Basurto Jacobo
# No. Control: 18011057
# Calificación: XXX

import random

def bubble_sort(array):
    length = len(array)
    for i in range(length -1):
        swapped = False
        for j in range(length - 1 - i):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        if not swapped: break
    return array

def main():
    print("Cuantos números desea agregar")
    lenght = int(input())
    array = [random.randint(1,100) for _ in range(lenght)]
    print("Arreglo sin ordenar:\n", array)
    orderedArray = bubble_sort(array)
    print("Arreglo ordenado:\n", orderedArray)

if __name__ == "__main__":
    main()