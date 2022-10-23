#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Omar Ramses Lopez Pulido
# No. Control: 18012180
# Calificación: XXX

import random

def seleccion(list):
    """
        Metodo de ordenamiento por seleccion
        :param list: lista a ordenar
        :return: lista ordenada
        """
    for i in range(len(list)):
        min = list[i]
        j = i + 1
        while j < len(list):
            if list[j] < min:
                min = list[j]
                list[j] = list[i]
                list[i] = min
            j += 1
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
