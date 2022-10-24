#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Rodriguez Pacheco Jose Ruben
# No. Control: 19011256
# Calificación: XXX
lista = [6,7,5,3,2,4,1] #aqui se crea la lista que se va ordenar

for i in range(1,len(lista)): #aqui se crea un ciclo que toma al comienzo el segundo valor y despues el que le sigue
    actual=lista[i] #aqui se crea una variable que guarda el valor que comparamos
    indice = i #aqui se crea una variable que guarde el indice que partimos
    while indice>0 and lista[indice-1] > actual: #aqui se crea un ciclo con la condicion de que no se puede entrar si es menor que 0 y que el valor debe ser menor al que estamos comparando
        lista[indice] = lista[indice-1] #aqui se pone el elemento menor en el lugar del que andamos comparando 
        indice = indice-1 #aqui hacemos que indice se recorra a la izquierda de la lista

    lista[indice]=actual #aqui se pone el valor con el que andabamos comparando en su nuevo lugar

print(lista)
