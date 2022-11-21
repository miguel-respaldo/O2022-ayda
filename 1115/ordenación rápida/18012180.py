#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
    # Nombre: Omar Ramses Lopez Pulido
# No. Control: 18012180
# Calificación: XXX

import random

def quicksort(arr, menor, mayor):
    if menor < mayor:
        pivote = particion(arr, menor, mayor)
        quicksort(arr, menor, pivote - 1)
        quicksort(arr, pivote + 1, mayor)

def particion(arr, menor, mayor):
    pivote = arr[mayor]
    i = menor - 1
    for j in range(menor, mayor):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[mayor] = arr[mayor], arr[i + 1]
    return i + 1

def main():
    lista = []
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
    quicksort(lista, 0, len(lista) - 1)
    print(lista)

if __name__ == "__main__":
    main()
