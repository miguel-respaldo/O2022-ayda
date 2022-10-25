#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Salvador de Jesus Dueñas Muñiz
# No. Control: 19011235
# Calificación: XXX

import random

def Seleccion(array):
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
    resultado = Seleccion(array)
    print("Arreglo ordenado:\n", resultado)
    resultado = Seleccion(array)

if __name__ == "__main__":
    main()