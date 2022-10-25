#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Lopez Peter Ubaldo
# No. Control: 19012245
# Calificación: XXX

def burbuja(num):
    tamano=len(num)
    for _ in range(0,tamano):
        for j in range(0,tamano-1):
            if num[j]>num[j+1]:
                aux=num[j]
                num[j]=num[j+1]
                num[j+1]=aux
    return num

def numeros(num):
    tam=len(num)
    print("Forma acendente:")
    for i in range(0,tam):
        a= num[i]
        print(a) 

num= [54,26,93,17,77,31,44,55,20]
num=burbuja(num)
numeros(num)

def sorteo(num):
    for i in range(1,len(num)):
        a = num[i]
        j = i
        while j>0 and num[j-1]>a:
            num[j]=num[j-1]
            j = j-1
        num[j]=a

num = [54,26,93,17,77,31,44,55,20]
sorteo(num)
print(num)
