#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Lopez Peter Ubaldo
# No. Control: 19012245
# Calificación: XXX

from heapq import heappop, heappush

def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)

    ordered = []

    # While we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))

    return ordered

array = [13, 21, 15, 5, 66, 56, 12, 26, 4, 17, 18, 24, 2]
print(heap_sort(array))
