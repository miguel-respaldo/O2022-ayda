#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Salvador Serna Ramirez
# No. Control: 18011319
# Calificación: XXX

def Merge_Sort(arr):
    if len(arr)>1:
        a=len(arr)//2
        l=arr[:a]
        r=arr[a:]

        Merge_Sort(l)
        Merge_Sort(r) 
        b=c=d=0

        while b<len(l) and c<len(r):
            if l[b]<r[c]:
                arr[d]=l[b]
                b+=1
            else:
                arr[d]=r[c]
                c+=1
            d+=1

        while b<len(l):
            arr[d]=l[b]
            b+=1
            d+=1

        while c<len(r):
            arr[d]=r[c]
            c+=1
            d+=1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
if __name__ == '__main__':
    arr = [8,10,1,15,6,25,3,22] 
    Merge_Sort(arr) 
    print("Lista ordenada es: ")
    printList(arr)