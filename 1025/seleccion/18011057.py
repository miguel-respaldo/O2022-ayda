#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Mauricio Basurto Jacobo
# No. Control: 18011057
# Calificación: XXX
import random

def selection_sort(array):
    length = len(array)
    for i in range(length - 1):
        menor = i
        for j in range(i + 1, length):
            if array[j] < array[menor]: menor = j
        if menor != i: array[menor], array[i] = (array[i], array[menor])
    return array


def main():
    print("Cuantos números desea agregar")
    lenght = int(input() or "20")
    array = [random.randint(1,100) for _ in range(lenght)]
    print("Arreglo sin ordenar:\n", array)
    orderedArray = selection_sort(array)
    print("Arreglo ordenado:\n", orderedArray)

if __name__ == "__main__":
    main()