#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Muñoz Cabrera Grecia Katya Alexandra 
# No. Control: 18011433
# Calificación: XXX

def heapify(arr, n, i):
    largest = i  # iniciar con el elemento mas grande
    l = 2 * i + 1  # izquierdo = 2*i + 1
    r = 2 * i + 2  # derecho = 2*i + 2
 
 # comparacion si el lado izquierdo es mayor 
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
 # comparacion si el lado derecho es mayor 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
 # cambio si es necesario 
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) 
 
 
        heapify(arr, n, largest)
 
 
# funcion principal para oerdenar un arreglo del tamaño dado
 
def monti(arr):
    n = len(arr)

 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
 # extracion de elemento uno por uno 
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # se hace el intercambio 
        heapify(arr, i, 0)
 

 
arr = [18, 9, 10, 1, 7, 20, ]
monti(arr)
n = len(arr)
print("ordenamiento por monticulos")
for i in range(n):
    print(arr[i])
