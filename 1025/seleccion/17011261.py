#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Cecilia Alejandra Muriedas Ortiz
# No. Control: 1239405
# Calificación: XXX

import sys
A = [65, 67, 68, 22, 11]

for i in range(len(A)):
    
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
            
    A[i], A[min_idx] = A[min_idx], A[i]
    
print ("Arreglo ordenado")
for i in range(len(A)):
    print("%d" %A[i])
