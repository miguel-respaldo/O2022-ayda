#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Muñoz Cabrera Grecia Katya Alexandra 
# No. Control: 18011433
# Calificación: XXX

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # creaciones temporales 
    L = [0] * (n1)
    R = [0] * (n2)
 
    # copia de datos de los arreglos
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # combinacion de los arreglos temporales 
    i = 0     #primer arreglo
    j = 0     # segundo arreglo
    k = l     # indice del subarreglo
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # se copia los elementos restantes si queda alguno 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # copia de los elemtentos restantes
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l es para el indice izquierdo y la r para el derecho 

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
 
        # ordenacion de la primera mitad con la segunda mitad 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 
# elementos a ordenar 
arr = [18, 9, 11, 2, 16, 1]
n = len(arr)
print("elementos a ordenar")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergeSort(arr, 0, n-1)
print("\n\nOrdenado por el metodo por mezcla:")
