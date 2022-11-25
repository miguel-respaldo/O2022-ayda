#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Salvador de Jesus Dueñas Muñiz
# No. Control: 19011235
# Calificación: XXX

def maximo(arr,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
     
    if l < n and arr[l] > arr[i]:
        largo = l
    else:
        largo = i
         
    if r < n and arr[r] > arr[largo]:
        largo = r
         
    if largo != i:
        arr[i], arr[largo] = arr[largo], arr[i]
        maximo(arr, n, largo)
 
 
def heapsort(arr):
    n = len(arr)
     
    for i in range(n, -1,-1):
        maximo(arr, n, i)
         
    for i in range(n-1,0,-1):
        arr[0] ,arr[i] = arr[i], arr[0]
        maximo(arr, i, 0)
    return arr
 
def main():
    arr = [33,35,42,10,7,8,14,19,48]
    heapsort(arr)
    print(arr)


if __name__ == "__main__":
    main() 
