#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Rodriguez Garcia Leonardo
# No. Control: 18011414
# Calificación: XXX


lista = [2,9,3,8,4,7,5] #Lista 

for i in range(len(lista)-1): 
    #cantidad de acomodos requeridos
    for j in range(len(lista)-1):
         #Comparar valores
        if lista[j] > lista[j+1]:
            #comparacion de valores y posterior acomodo
            temporalValue = lista [j] 
            lista [j] = lista[j+1] 
            lista[j+1] = temporalValue
            
print(lista)
