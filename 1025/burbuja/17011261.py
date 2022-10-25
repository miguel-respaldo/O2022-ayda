#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Cecilia Alejandra Muriedas Ortiz
# No. Control: 1239405
# Calificación: XXX
# Python program for Limplementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 22, 11, 14, 15]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])