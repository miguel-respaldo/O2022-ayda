#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Omar Ramses Lopez Pulido
# No. Control: 18012180
# Calificación: XXX

import random


def insercion(list):
    """
    Metodo de ordenamiento por insercion
    :param list: lista a ordenar
    :return: lista ordenada
    """
    for i in range(1, len(list)):
        aux = list[i]
        w = i - 1
        while w >= 0 and list[w] > aux:
            list[w + 1] = list[w]
            w -= 1
        list[w + 1] = aux
    return list


def main():
    lista =[]
    print("Ingrese la longitud de la lista:")
    length = int(input())
    print("Ingrese el rango de numeros:")
    print("Desde:")
    inicio = int(input())
    print("Hasta:")
    fin = int(input())

    for i in range(length):
        r = random.randint(inicio, fin)
        lista.append(r)

    print("Lista desordenada:")
    print(lista)
    print("Lista ordenada:")
    print(insercion(lista))


if __name__ == "__main__":
    main()
