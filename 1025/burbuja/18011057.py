#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Mauricio Basurto Jacobo
# No. Control: 18011057
# Calificación: XXX

import random

def insertion_sort(array):
    for indice, valor in enumerate(array[1:]):
        temp = indice
        while indice >=0 and valor < array[indice]:
            array[indice + 1] = array[indice]
            indice -= 1
        if indice != temp:
            array[indice + 1] = valor
    return array

def main():
    print("Cuantos números desea agregar")
    lenght = int(input() or "20")
    array = [random.randint(1,100) for _ in range(lenght)]
    print("Arreglo sin ordenar:\n", array)
    orderedArray = insertion_sort(array)
    print("Arreglo ordenado:\n", orderedArray)

if __name__ == "__main__":
    main()
