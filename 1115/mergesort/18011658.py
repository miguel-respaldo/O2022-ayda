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
    if len(ordenamiento) < 2:
        return ordenamiento

    medio = len(ordenamiento)//2
    izquierda = mergesort(ordenamiento[:medio])
    derecha = mergesort(ordenamiento[medio:])
    return array(izquierda, derecha)

def array(izquierda, derecha):
    lista = []
    i, k = 0, 0
    while i < len(izquierda) and k < len(derecha):
        if izquierda[i] < derecha[k]:
            lista.append(izquierda[i])
            i += 1
        else:
            lista.append(derecha[k])
            k += 1
    lista += izquierda[i:]
    lista += derecha[k:]
    return lista

print("Arreglo ordenado:",
      mergesort([5, 88, 15, 55, 84, 13, 20, 11, 32, 65, 8, 9, 3, 92, 45, 56, 1, 45321, 12345, 929283, 87635]))