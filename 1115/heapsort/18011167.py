#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Francisco Javier Ocampo Torres
# No. Control: 18011167
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
    arr = [6,15,0,5,6,32,1,9] 
    Merge_Sort(arr) 
    print("Lista ordenada es: ")
    printList(arr)
