#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Octavio Corral Tovar
# No. Control: 19011234
# Calificación: XXX

arr = [8,5,4,7,9,6,2,5,1]

def heapSort(arr, n, i):
    largo = i  
    l = 2 * i + 1  
    r = 2 * i + 2 
 
    if l < n and arr[i] < arr[l]:
        largo = l
 
    if r < n and arr[largo] < arr[r]:
        largo = r

 
    if largo != i:
        (arr[i], arr[largo]) = (arr[largo], arr[i]) 

 
        heapSort(arr, n, largo)
 

 
def heapSort2(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapSort(arr, n, i)
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  
        heapSort(arr, i, 0)

n = len(arr)
heapSort2(arr)
for i in range(n):
    print(arr[i])
 

def main():
    resultado = heapSort2(arr)
    print(resultado) 


if __name__ == "__main__":
    main()