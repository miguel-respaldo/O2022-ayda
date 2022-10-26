#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Sebastian Garcia Quijas
# No. Control: 18011215
# Calificación: XXX

def sel(arreglo):
    for m in range(len(arreglo) - 1): 
        h = m
        for j in range(m + 1, len(arreglo)):
            if arreglo[j] < arreglo[h]:
                h = j
        if h != m:
            arreglo[h], arreglo[m] = arreglo[m], arreglo[h]

valores = [5,45,78,1,64,65,8]
sel(valores)

print(valores)
