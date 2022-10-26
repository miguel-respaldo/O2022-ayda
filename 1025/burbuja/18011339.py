#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hernandez Uribe Nestor Eduardo
# No. Control: 18011339
# Calificación: XXX

import random

def burbuja(list):
    """
    Metodo de ordenamiento burbuja
    :param list: lista a ordenar
    :return: lista ordenada
    """
    a = False
    while a == False:
        a = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux
                a = False
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
    print(burbuja(lista))


if __name__ == "__main__":
    main()