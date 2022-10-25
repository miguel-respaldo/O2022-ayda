#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Salvador de Jesus Dueñas Muñiz
# No. Control: 19011235
# Calificación: XXX

import random

def Inserccion(list):
    for i in range(1, len(list)):
        aux = list[i]
        w = i - 1
        while w >= 0 and list[w] > aux:
            list[w + 1] = list[w]
            w -= 1
        list[w + 1] = aux
    return list


def main():
    resultado =[]
    print("Cuantos números desea agregar")
    lenght = int(input() or "20")
    array = [random.randint(1,100) for _ in range(lenght)]
    print("Arreglo sin ordenar:\n", array)
    resultado = Inserccion(array)
    print("Arreglo ordenado:\n", resultado)
    resultado = Inserccion(array)

if __name__ == "__main__":
    main()