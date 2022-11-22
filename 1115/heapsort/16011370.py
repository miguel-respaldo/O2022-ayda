#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
    # Nombre: Luis Fernando Rubio Zambrano
# No. Control: 16011370
# Calificación: XXX

import random

def heapify(arr, n, i):
    mayor = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        mayor = l
    if r < n and arr[mayor] < arr[r]:
        mayor = r
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor)

def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

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
    print(heapSort(lista))

if __name__ == "__main__":
    main()
