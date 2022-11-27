#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Fuentes Soto Alan Alexander 
# No. Control: 19011308
# Calificación: XXX

import math
def hIzq(i):
    return 2*i
 
def hDer(i):
    return 2*i+1
 
def intercambia(A,x,y):
    tmp=A[x]
    A[x]=A[y]
    A[y]=tmp
 
def maxHeapify (A, i, tamanoHeap):
    L=hIzq(i)
    R=hDer(i)
    if(L<=tamanoHeap and A[L]>A[i]):
        posMax=L
    else:
        posMax=i
    if (R<=tamanoHeap and A[R]>A[posMax]):
        posMax=R
    if (posMax != i):
        intercambia(A, i, posMax)
        maxHeapify (A, posMax, tamanoHeap)
 
def construirHeapMaxIni (A, tamanoHeap):
    for i in range (math.ceil((tamanoHeap-1)/2),-1,-1):
        maxHeapify (A, i, tamanoHeap)
 
def ordenacionHeapSort (A, tamanoHeap):
    construirHeapMaxIni (A, tamanoHeap)
    for i in range (len (A)-1,0,-1):
        intercambia(A,0,i)
        tamanoHeap=tamanoHeap-1
        maxHeapify (A,0, tamanoHeap)
A = [4,100,68,90,6,9,10]
print(A)
ordenacionHeapSort (A, 6)
print(A)
