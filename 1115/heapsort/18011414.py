#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Leonardo Rodriguez Garcia
# No. Control: 18011414
# Calificación: XXX

import random
def heapsort(rea):
    n = len(rea)
    for i in range(n // 2 - 1, -1, -1):
        heapify(rea, n, i)
    for i in range(n - 1, 0, -1):
        (rea[i], rea[0]) = (rea[0], rea[i])  
        heapify(rea, i, 0)

def main():
    random_rea = random.sample(range(99), 10) 
    print(random_rea)
    heapsort(random_rea)
    print(random_rea)

def heapify(rea, heap, i):
    el = i  
    le = 2 * i + 1 
    ri = 2 * i + 2  
    if le < heap and rea[i] < rea[le]:
        el = le
    if ri < heap and rea[el] < rea[ri]:
        el = ri
    if el != i:
        (rea[i], rea[el]) = (rea[el], rea[i]) 
        heapify(rea, heap, el)
main()
