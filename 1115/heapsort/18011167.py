#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Francisco Javier Ocampo Torres
# No. Control: 18011167
# Calificación: XXX

def heapify(arr, n, i):
   M=i 
   l=2*i+1 
   r=2*i+2 
   
   if l<n and arr[i]<arr[l]:
      M=l
   
   if r<n and arr[M]<arr[r]:
      M=r
   
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
    for i in range(n):
        print (arr[i],end=" ")
    print()

if __name__ == '__main__':
    arr = [49,47,3,0,4,15,6,3,2,49]
    HeapSort(arr)
    n = len(arr)
    print ("Lista ordenada es: ")
    printList(arr)

