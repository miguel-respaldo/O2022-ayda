#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
    # Nombre: Jose Ruben Rodriguez Pacheco
# No. Control: 19011256
# Calificación: XXX

def max_heapify(Lista,n,i):
    l = left(i)
    r = right(i)
    if l < n and Lista[l] > Lista[i]:
        largo = l
    else:
        largo = i
    if r < n and Lista[r] > Lista[largo]:
        largo = r
    if largo != i:
        Lista[i], Lista[largo] = Lista[largo], Lista[i]
        max_heapify(Lista,n, largo)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(Lista):
    n = len(Lista)
    for i in range(n, -1,-1):
        max_heapify(Lista,n, i)
    for i in range(n-1,0,-1):
        Lista[0],Lista[i]=Lista[i],Lista[0]
        max_heapify(Lista,i,0)




Lista=[3,7,4,9,2,5,10,6,8,1]
build_max_heap(Lista)
print(Lista)
