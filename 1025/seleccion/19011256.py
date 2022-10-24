#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Rodriguez Pacheco Jose Ruben
# No. Control: 19011256
# Calificación: XXX
lista = [6,7,5,3,2,4,1] #aqui se crea la lista que se va ordenar
longitud = len(lista) #aqui se crea la variable longitud para que se recorran solo la cantidad de datos que tiene la lista
for i in range(longitud-1): # en este ciclo se la posicion del primer valor aun no comparado de la lista con los demas
    print(lista)
    menor=i
    for j in range(i+1,longitud): #en este ciclo se recorre los demas valores que van despues de el valor de i 
        if lista[j] < lista[menor]: #en este se compara que el valor que tenemos sea el menor de los restantes
            menor=j #al ser menor j se le se guarda en menor
    temporal = lista[menor] #aqui se crea la variable que guarda el valor menor que encontramos
    lista[menor] = lista[i] #aqui hacemos que el valor que estaba en la posicion del primer valor aun no comparado se guarde en la posicion del valor menor que encontramos
    lista[i] = temporal #aqui hacemos que el valor menor que encontramos se guarde en la posicion del la posicion del primer valor aun no comparado

print(lista)
