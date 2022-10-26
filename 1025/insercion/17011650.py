#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Emmanuel Gonzalez Gomez
# No. Control: 17011650
# Calificación: XXX

def mi_lista(x):
   for a in range(1,len(x)):

     actual = x[a]
     position = a

     while position>0 and x[position-1]>actual:
         x[position]=x[position-1]
         position = position-1

     x[position]=actual

lista = [100,55,98,1,5,7,89,2,254,10,70,97,]
mi_lista(lista)
print(lista)