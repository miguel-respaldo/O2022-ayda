#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Salvador Serna Ramirez
# No. Control: 18011319
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
    arr = [320,45,52,66,20,1,9,54,3,155,88,69,33,11]
    QuickSort(arr, 0, len(arr)-1)
    print("la lista ordenada es: ")
    printList(arr)