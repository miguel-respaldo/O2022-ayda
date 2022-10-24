#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Campos Luna Luis Isael
# No. Control: 19011304
# Calificación: XXX

def ord_seleccion(arreglo):
    for i in range(len(arreglo) - 1):        # <-- bucle padre
        menor = i # primer elemento por default será el mínimo

        for j in range(i + 1, len(arreglo)): # <-- bucle hijo
            if arreglo[j] < arreglo[menor]:
                menor = j

        if menor != i:
            arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]

a = [4,5,19,11,13,16,7,10,3,18,14,15,2,20,12,6,1,8,17,9]
ord_seleccion(a)

print(a)