#!/usr/bin/env python3
# vi: establezca shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Maria Guadalupe Garcia Baltazar
# N° Control: 19011845
# Calificación: XXX

import random

def heapify(lista, heap, i):
    mayor = i  # inicializar el mayor
    izquierda = 2 * i + 1  # izquierda = 2*i + 1
    derecha = 2 * i + 2  # derecha = 2*i + 2

    if izquierda < heap and lista[i] < lista[izquierda]:
        mayor = izquierda

    if derecha < heap and lista[mayor] < lista[derecha]:
        mayor = derecha

    if mayor != i: # Cambiar raiz
        (lista[i], lista[mayor]) = (lista[mayor], lista[i])  #intercambio

        heapify(lista, heap, mayor) # Acomoda la raiz

def heapsort(lista):
    n = len(lista)
    #contruir arbol binario, padre esta en ((n//2)-1)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    #extraer elementos
    for i in range(n - 1, 0, -1):
        (lista[i], lista[0]) = (lista[0], lista[i])  #intercambio
        heapify(lista, i, 0)

def main():
    random_lista = random.sample(range(99), 10) #lista aleatoria
    print("Lista: ") #lista aleatoria
    print(random_lista)
    heapsort(random_lista)
    print("Lista con ordenamiento QuickSort: ") #lista con ordenamiento heapsort
    print(random_lista)
main()