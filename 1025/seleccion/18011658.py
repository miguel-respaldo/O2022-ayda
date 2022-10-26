#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luna Gonzalez Alan Alejandro
# No. Control: 18011658
# Calificación: XXX

print("¡Bienvenido!")
print("Programmer: Alan Luna\n")

'''selección'''

lista = [5, 88, 15, 55, 84, 13, 20, 11, 32, 65, 8, 9, 3, 92, 45, 56, 1, 45321, 12345, 929283, 87635, 909090]

for n in range(0, len(lista)):
    array = n
    for i in range(n + 1, len(lista)):
        if lista[array] > lista[i]:
            array = i

    arreglo = lista[n]
    lista[n] = lista[array]
    lista[array] = arreglo

print("Arreglo ordenado:", lista)