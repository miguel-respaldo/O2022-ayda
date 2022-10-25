#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Salvador de Jesus Dueñas Muñiz
# No. Control: 19011235
# Calificación: XXX

import random

def burbuja(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j + 1] < array[j]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux

    return array

def main():
    print("Cuantos números desea agregar")
    lenght = int(input() or "20")
    array = [random.randint(1,100) for _ in range(lenght)]
    print("Arreglo sin ordenar:\n", array)
    orderedArray = burbuja(array)
    print("Arreglo ordenado:\n", orderedArray)

if __name__ == "__main__":
    main()