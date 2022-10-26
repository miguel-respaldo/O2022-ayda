#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Grecia Katya Alexandra Muñoz Cabrera
# No. Control: 18011433
# Calificación: XXX

def seleccion(array, tam):
     
    for s in range(tam):
        min_idx = s
         
        for i in range(s + 1, tam):
             
            # clasificar en orden descendente
            # elemento minimo en cada ciclo
            if array[i] < array[min_idx]:
                min_idx = i
 
        #organizar el minimo en la posicion correcta
        (array[s], array[min_idx]) = (array[min_idx], array[s])
 
# elementos del arreglo
n = [ 22, 10, 1, 26 ]
tam = len (n)
seleccion(n, tam)
 
print('Arreglo ordenado en orden ascendente:')
print(n)
