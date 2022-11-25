#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Lopez Peter Ubaldo
# No. Control: 19012245
# Calificación: XXX

def particion(array, min, max):
    pivot = array[max]
    i = min - 1
    for j in range(min, max):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[max]) = (array[max], array[i + 1])
    return i + 1


def sorteo(array, min, max):
    if min < max:
        sub_array = particion(array, min, max)
        sorteo(array, min, sub_array - 1)
        sorteo(array, sub_array + 1, max)
        
array = [1,9,0,3,9,8,2,8]
print("Array actual")
print(array)
size = len(array)
sorteo(array, 0, size - 1)
print('Array ordenado: ')
print(array)
