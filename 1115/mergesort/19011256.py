#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
    # Nombre: Jose Ruben Rodriguez Pacheco
# No. Control: 19011256
# Calificación: XXX

def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        primera_mitad = lista[:mitad]
        segunda_mitad = lista[mitad:]

        merge_sort(primera_mitad)
        merge_sort(segunda_mitad)
        i = 0
        j = 0
        k = 0

        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i] < segunda_mitad[j]:
                lista[k] = primera_mitad[i]
                i += 1
            else:
                lista[k] = segunda_mitad[j]
                j += 1
            k += 1
        
        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i += 1
            k += 1
        
        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j += 1
            k += 1


numeros = [3,7,4,9,2,5,10,6,8,1]
print(numeros)

merge_sort(numeros)
print(numeros) 
