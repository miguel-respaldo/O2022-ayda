#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Mauricio Basurto Jacobo
# No. Control: 18011057
# Calificación: XXX

import random

def MergeSort(array: list) -> list:

    def merge(left: list, right: list) -> list:
        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(array) <= 1: return array
    mid = len(array) // 2
    return merge(MergeSort(array[:mid]), MergeSort(array[mid:]))

def main():
    print("Cuantos números desea agregar")
    lenght = int(input() or "20")
    array = [random.randint(1,100) for _ in range(lenght)]
    print("Arreglo sin ordenar:\n", array)
    orderedArray = MergeSort(array)
    print("Arreglo ordenado:\n", orderedArray)

if __name__ == "__main__":
    main()