#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Rodriguez Pacheco Jose Ruben
# No. Control: 19011256
# Calificación: XXX
lista = [6,7,5,3,2,4,1] #aqui se crea la lista que se va ordenar

for i in range(len(lista)-1): #este ciclo es para ve cuantas vueltas debemos dar para acomodar la lis
    for j in range(len(lista)-1): #este ciclo es para comparar un valor por el siguiente de la lista
        if lista[j] > lista[j+1]: #aqui se crea un ciclo en el que se compara cual es el menor y dentro de el se intercambian las posiciones
            temporal = lista [j] 
            lista [j] = lista[j+1] 
            lista[j+1] = temporal
print(lista)
