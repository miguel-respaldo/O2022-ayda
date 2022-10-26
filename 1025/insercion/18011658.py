#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luna Gonzalez Alan Alejandro
# No. Control: 18011658
# Calificación: XXX

print("¡Bienvenido!")
print("Programmer: Alan Luna\n")

'''inserción'''

lista = [5, 88, 15, 55, 84, 13, 20, 11, 32, 65, 8, 9, 3, 92, 45, 56, 1, 45321, 12345, 929283, 87635, 909090]

print(lista)
for n in range(1, len(lista)):
    array = lista[n]

    i = n - 1
    while i >= 0 and lista[i] > array:
        lista[i + 1] = lista[i]
        i -= 1
        lista[i + 1] = array

print("Arreglo ordenado:", lista)