#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Mauricio Basurto Jacobo
# No. Control: 18011057
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
    return array

def main():
    print("Cuantos números desea agregar")
    lenght = int(input() or "20")
    array = [random.randint(1,100) for _ in range(lenght)]
    print("Arreglo sin ordenar:\n", array)
    orderedArray = HeapSort(array)
    print("Arreglo ordenado:\n", orderedArray)

if __name__ == "__main__":
    main()