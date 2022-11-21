#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luna Gonzalez Alan Alejandro
# No. Control: 18011658
# Calificación: XXX

print("¡Bienvenido!")
print("Programmer: Alan Luna | QuickSort.\n")

'''QuickSort'''


def quicksort(ordenamiento):
    lenght = len(ordenamiento)
    if lenght <= 1:
        return ordenamiento
    else:
        pivote = ordenamiento.pop()
        mayor, menor = [], []
        for num in ordenamiento:
            if num > pivote:
                mayor.append(num)
            else:
                menor.append(num)
        return quicksort(menor) + [pivote] + quicksort(mayor)


print("Arreglo ordenado:")
print(quicksort([5, 88, 15, 55, 84, 13, 20, 11, 32, 65, 8, 9, 3, 92, 45, 56, 1, 45321, 12345, 929283, 87635]))
