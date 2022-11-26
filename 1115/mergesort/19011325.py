#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre:Samuel Rodriguez Garcia
# No. Control: 19011325
# Calificación: XXX

def merge_sort(arreglo):
    longitud = len(arreglo)
    mitad = longitud//2  # El doble / es para dividir y redondear hacia abajo
    # Condición de salida de recursividad es que el arreglo mida 1 o 0
    if longitud <= 1:
        return arreglo
    mitad_izquierda = arreglo[:mitad]
    mitad_derecha = arreglo[mitad:]
    mitad_izquierda = merge_sort(mitad_izquierda)
    mitad_derecha = merge_sort(mitad_derecha)
    return merge(mitad_izquierda, mitad_derecha)
