#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alexa Fernanda Iniguez Jimenez
# No. Control: 18011226
# Calificación: XX

def heapify(arr, n, i):
    # Encontrar el elemento mas grande
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Si en dado caso no es el mas grande, hacer el intercambio y continuar con cada elemento...
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        # Swap (inveritr)
        arr[i], arr[0] = arr[0], arr[i]

        # Elemento raiz
        heapify(arr, i, 0)

#---------------- MAIN -----------------------------------------
arr = [1, 42, 7, 33, 12, 100, 50]
n = len(arr)
print("... Heapsort ...")
print(arr)
print("------------------------")
print("Arreglo ordenado: ")
heapSort(arr)
for i in range(n):
    print("%d " % arr[i], end=' ')