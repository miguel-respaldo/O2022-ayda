#!/usr/bin/env python3
# vi: establezca shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Maria Guadalupe Garcia Baltazar
# N° Control: 19011845
# Calificación: XXX

import random

def mergesort(lista):
    if len(lista) > 1: #verificar si la l0ista requiere ser ordenada
        mitad = len(lista) // 2
        primera_mitad = lista[:mitad]
        segunda_mitad = lista[mitad:]

        mergesort(primera_mitad)
        mergesort(segunda_mitad)
        i=0
        j=0
        k=0

        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i] < segunda_mitad[j]:
                lista[k] = primera_mitad[i]
                i+=1
            else:
                lista[k] = segunda_mitad[j]
                j+=1
            k+=1

        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i+=1
            k+=1

        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j+=1
            k+=1

def main():
    random_lista = random.sample(range(99), 10) #lista aleatoria
    print("Lista: ") #lista aleatoria
    print(random_lista)
    mergesort(random_lista)
    print("Lista con ordenamiento MergeSort: ") #lista con ordenamiento mergesort
    print(random_lista)
main()



