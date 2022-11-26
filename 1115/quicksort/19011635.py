#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luis Antonio Hernandez Ventura
# No. Control: 19011635
# Calificación: XXX

def quicksort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = particion(arreglo, izquierda, derecha)
        quicksort(arreglo, izquierda, indiceParticion)
        quicksort(arreglo, indiceParticion + 1, derecha)


def particion(arreglo, izquierda, derecha):
    pivote = arreglo[izquierda]
    while True:
        
        while arreglo[izquierda] < pivote:
            izquierda += 1

        
        while arreglo[derecha] > pivote:
            derecha -= 1

        
        if izquierda >= derecha:
            
            return derecha
        else:
            
            
            arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
            
            izquierda += 1
            derecha -= 1



arreglo = [5, 1, 2, 1, 1, 3, 5, 1, 5, 1, 99, 231, 234, 12, 121,
           312, 123, 123, 12, 312, 321, 312, 31, 23, 12, 3123, 123, ]
print("Antes de ordenarlo: ")
print(arreglo)
quicksort(arreglo, 0, len(arreglo) - 1)
print("Después de ordenarlo: ")
print(arreglo)
