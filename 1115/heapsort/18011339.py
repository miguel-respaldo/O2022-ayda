#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Nestor Eduardo Hernandez Uribe
# No. Control: 18011339
# Calificación: XXX

import random

def Heapify(unsorted, index, size):
    largest = index
    left_index = 2* index + 1
    right_index = 2* index + 2

    if left_index < size and unsorted[left_index] > unsorted[largest]: largest = left_index
    if right_index < size and unsorted[right_index] > unsorted[largest]: largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        Heapify(unsorted, largest, size)

def HeapSort(array):
    length = len(array)
    for i in range(length): Heapify(array, i, length)
    for i in range(length -1, 0, -1):
        array[0], array[i] = array[i], array[0]
        Heapify(array, 0, i)
    return 