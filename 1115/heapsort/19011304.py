#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luis Isael Campos Luna
# No. Control: 19011304
# Calificación: XXX

# limite del amontonamiento 
def max_heaport(val, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and val[largest] < val[left]: #se comparan los valores con el monton mas grande
        largest = left


    if right < n and val[largest] < val[right]: #viceversa de comparacion 
        largest = right
        
    if largest!=i:
        val[i], val[largest] = val[largest], val[i]
        max_heaport(val, n, largest) #llamada recursiva 

val = [2,66,30,5,9,10]
n = len(val)

def heapSort(val):
    for i in range(n-1, 0, -1):
        val[i], val[0] = val[0], val[i] #se intercambian los valores para amontonar
        max_heaport(val, i, 0)

for i in range(n//2 - 1, -1, -1): #se hace el amontonamiento max
    max_heaport(val, n, i)

heapSort(val)

print("moticulo ordenado ")
for i in range(n):
   print(val[i]),

