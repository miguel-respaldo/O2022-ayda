#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Francisco Javier Ocampo Torres
# No. Control: 18011167
# Calificación: XXX

def Burbuja(N):
    for i in range(1,len(N)):
        for a in range(0,len(N)-i):
            if(N[a+1] < N[a]):
                aux=N[a]
                N[a]=N[a+1]
                N[a+1]=aux
    print(N)
 

N=[5,10,1,21,19,58,4,15,1,90,54,90]
print(N)
Burbuja(N)