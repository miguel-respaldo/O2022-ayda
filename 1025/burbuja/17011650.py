#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Emmanuel Gonzalez Gomez
# No. Control: 17011650
# Calificación: XXX

def burbuja(x):
    for i in range(1,len(x)):
        for j in range(0,len(x)-i):
            if(x[j+1] < x[j]):
                aux=x[j]
                x[j]=x[j+1]
                x[j+1]=aux
    print(x)

lista=[12,5,11,8,25,85,9,7,1,99]
print(lista)
burbuja(lista)
