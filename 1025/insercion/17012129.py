#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: José Ricardo Siordia Alatorre
# No. Control: 17012129
# Calificación: XXX


def insertionSort(A):
    
    for i in range(1, len(A)):
 
        value = A[i]
        j = i
 
        while j > 0 and A[j - 1] > value:
            A[j] = A[j - 1]
            j = j - 1
 
        A[j] = value
 
if __name__ == '__main__':
 
    A = [88, 27, -12, 65, 93, 43]
 
    insertionSort(A)
    print(A)