#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Francisco Javier Ocampo Torres
# No. Control: 18011167
# Calificación: XXX

def Seleccion(N):
    for i in range(len(N)):
        min=i
        for a in range(i,len(N)):
            if(N[a] < N[min]):
                min=a
        if(min!= i):
            aux=N[i]
            N[i]=N[min]
            N[min]=aux
    print(N)
 
N=[45,45,32,33,2,0,4,21,85,72,2]
print(N)
Seleccion(N)