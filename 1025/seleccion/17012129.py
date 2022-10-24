#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: José Ricardo Siordia Alatorre
# No. Control: 17012129
# Calificación: XXX

def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 

def selectionSort(A):
 
    for i in range(len(A) - 1):
        min = i
 
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j        
        swap(A, min, i)
 
 
if __name__ == '__main__':
 
    A = [88, 27, -12, 65, 93, 43]
 
    selectionSort(A)
 
    print(A)