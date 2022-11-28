#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Salvador Serna Ramirez
# No. Control: 18011319
# Calificación: XXX

def heapify(arr, n, i):
   M=i 
   izq=2*i+1 
   der=2*i+2 
   
   if izq<n and arr[i]<arr[izq]:
      M=izq
   
   if der<n and arr[M]<arr[der]:
      M=der
   
   if M !=i:
      arr[i],arr[M]=arr[M],arr[i] 
      heapify(arr, n, M)

def HeapSort(arr):
   n=len(arr)
   
   for i in range(n, -1, -1):
      heapify(arr, n, i)
   
   for i in range(n-1, 0, -1):
      arr[i], arr[0]=arr[0], arr[i]
      heapify(arr, i, 0)

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [11,44,1,5,9,17,9,6,2,47]
    HeapSort(arr)
    n = len(arr)
    print ("la lista ordenada es: ")
    printList(arr)