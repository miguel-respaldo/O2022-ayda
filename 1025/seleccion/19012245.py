#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Lopez Peter Ubaldo
# No. Control: 19012245
# Calificación: XXX

def seleccion(arreglo):
    longitud = len(arreglo)
    for i in range(longitud-1):
        for j in range(i+1, longitud):
            if arreglo[i] > arreglo[j]:
                # Intercambiar
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]


def seleccion_descendente(arreglo):
    longitud = len(arreglo)
    for i in range(longitud-1):
        for j in range(i+1, longitud):
            if arreglo[i] < arreglo[j]:
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]


numeros = [23, 25, 30, 1, 28, 11, 96, 2, 3, 1]


print("Arreglo de números original:")
print(numeros)
seleccion(numeros)
print("Arreglo de números ordenado: ")
print(numeros)
seleccion_descendente(numeros)
print("Arreglo de números ordenado descendente: ")
print(numeros)
