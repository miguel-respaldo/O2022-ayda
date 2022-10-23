#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Omar Ramses Lopez Pulido
# No. Control: 18012180
# Calificación: XXX

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
    print(burbuja([3, 2, 1]))


if __name__ == "__main__":
    main()
