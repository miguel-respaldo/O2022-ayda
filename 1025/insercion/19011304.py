#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Campos Luna Luis Isael
# No. Control: 19011304
# Calificación: XXX
def ordenamientoPorInsercion(Lista):
   for indice in range(1,len(Lista)):

     valorActual = Lista[indice]
     posicion = indice

     while posicion>0 and Lista[posicion-1]>valorActual:
         Lista[posicion]=Lista[posicion-1]
         posicion = posicion-1

     Lista[posicion]=valorActual

Lista = [5,2,4,1,3]
ordenamientoPorInsercion(Lista)
print(Lista)