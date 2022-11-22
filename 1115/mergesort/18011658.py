#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luna Gonzalez Alan Alejandro
# No. Control: 18011658
# Calificación: XXX

print("¡Bienvenido!")
print("Programmer: Alan Luna | MergeSort.\n")

'''MergeSort'''


def mergesort(ordenamiento):
    if len(ordenamiento) > 1:
        num = len(ordenamiento) // 2
        lista_izquierda = ordenamiento[:num]
        lista_derecha = ordenamiento[num:]

        l = 0  # left
        c = 0  # center
        r = 0  # right
        mergesort(lista_izquierda)
        mergesort(lista_derecha)

        while l < len(lista_izquierda) and r < len(lista_derecha):
            if lista_izquierda[l] <= lista_derecha[r]:
                ordenamiento[c] = lista_izquierda[l]
                l += 1
            else:
                ordenamiento[c] = lista_derecha[r]
                r += 1
            c += 1

        while l < len(lista_izquierda):
            ordenamiento[c] = lista_izquierda[l]
            l += 1
            c += 1

        while r < len(lista_derecha):
            ordenamiento[c] = lista_derecha[r]
            r += 1
            c += 1


Array = [5, 88, 15, 55, 84, 13, 20, 11, 32, 65, 8, 9, 3, 92, 45, 56, 1, 45321, 12345, 929283, 87635]
mergesort(Array)
print("Arreglo ordenado:", Array)
