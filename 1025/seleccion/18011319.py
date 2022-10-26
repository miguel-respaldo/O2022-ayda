#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Salvador Serna Ramirez
# No. Control: 18011319
# Calificación: XXX




def seleccion(Z):
    for i in range(len(Z)):
        minimo=i
        for y in range(i,len(Z)):
            if(Z[y] < Z[minimo]):
                minimo=y
        if(minimo != i):
            aux=Z[i]
            Z[i]=Z[minimo]
            Z[minimo]=aux
    print (Z)
 

Z=[10,20,15,11,41,72,1,5,32,5]
print (Z)
seleccion(Z)