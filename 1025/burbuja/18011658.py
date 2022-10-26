#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luna Gonzalez Alan Alejandro
# No. Control: 18011658
# Calificación: XXX

print("¡Bienvenido!")
print("Programmer: Alan Luna\n")

'''burbuja'''

lista = [5, 88, 15, 55, 84, 13, 20, 11, 32, 65, 8, 9, 3, 92, 45, 56, 1, 45321, 12345, 929283, 87635]

ordenamiento_burbuja = False
while not ordenamiento_burbuja:
    ordenamiento_burbuja = True
    for n in range(len(lista) - 1):

        if lista[n] > lista[n + 1]:
            arreglo = lista[n]

            lista[n] = lista[n + 1]

            lista[n + 1] = arreglo

            ordenamiento_burbuja = False

print("Arreglo ordenado:", lista)
