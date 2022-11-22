#!/usr/bin/env python3
# vi: establezca shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Maria Guadalupe Garcia Baltazar
# N° Control: 19011845
# Calificación: XXX

import random

def quicksort(lista, inicio, final):
    if inicio < final: #indices de la lista
        pivote_indice = partition(lista, inicio, final) #se obtiene el indice del pivote
        #sublista izquierda
        quicksort(lista, inicio, pivote_indice - 1) #inicio-pivote
        #sublista derecha
        quicksort(lista, pivote_indice + 1, final) #pivote + 1 - final

def partition(lista, inicio, final): #ordena los elementos
    pivote = lista[final] #ultimo elemento es pivote
    i = inicio
    for j in range(inicio, final):
        if lista[j] < pivote: #mover elementos menores al pivote a la izquierda
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
    i_pivote = i #mover pivote a su posicion correcta
    lista[i_pivote], lista[final] = lista[final], lista[i_pivote]
    return i_pivote

def main():
    random_lista = random.sample(range(99), 10) #lista aleatoria
    inicio = 0
    final = len(random_lista) - 1
    print("Lista: ") #lista aleatoria
    print(random_lista)
    quicksort(random_lista, inicio, final)
    print("Lista con ordenamiento QuickSort: ") #lista con ordenamiento quicksort
    print(random_lista)
main()


