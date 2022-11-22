#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josue Daniel Rocha Ledezma
# No. Control: 18011187
# Calificación: XXX

from heapq import heappop, heappush

def heapsort(arr):
    heap = []
    for ele in arr:
        heappush(heap, ele)
    sort = []
    while heap:
        sort.append(heappop(heap))
    return sort

def main():

    arr = [75, 87, 1, 6, 4, 1, 10, 45, 15, 32, 44, 999, 56, 100]
    print("Este es el main y llama la función de tarea Heapsort")
    resultado = heapsort(arr)
    print("resultado", resultado)

if __name__ == "__main__":
    main()