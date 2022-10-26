#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Francisco Javier Ocampo Torres
# No. Control: 18011167
# Calificación: XXX

def Insercion(N):
    for i in range(len(N)):
        for a in range(i,0,-1):
            if(N[a-1] > N[a]):
                aux=N[a]
                N[a]=N[a-1]
                N[a-1]=aux
    print(N)
 
N=[54,21,31,1,24,53,21,21,3,2,49]
print(N)
Insercion(N)