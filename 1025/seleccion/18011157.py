#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alvaro Macias Muro
# No. Control: 18011157
# Calificación: XXX

def seleccion(arreglo):
    longitud = len(arreglo)
    for i in range(longitud-1):
        for j in range(i+1, longitud):
            if arreglo[i] > arreglo[j]:
                # Intercambiar
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]