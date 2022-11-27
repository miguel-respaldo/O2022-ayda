#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Francisco Javier Ocampo Torres
# No. Control: 18011167
# Calificación: XXX

def QuickSort(arr, izq, der):
    if izq<der:
        indPart=Particion(arr, izq, der)
        QuickSort(arr, izq, indPart)
        QuickSort(arr, indPart+1, der)

def Particion(arreglo, izq, der):
    piv=arr[izq]
    while True:
        while arr[izq]<piv:
            izq+=1

        while arr[der]>piv:
            der-=1

        if izq>=der:
            return der
        else:
            arr[izq], arr[der]=arr[der], arr[izq]
            izq+=1
            der-=1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [402,56,32,87,56,0,6,56,1,109,78,77,87,6]
    QuickSort(arr, 0, len(arr)-1)
    print("Lista ordenada es: ")
    printList(arr)