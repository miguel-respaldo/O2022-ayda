#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Octavio Corral Tovar
# No. Control: 19011234
# Calificación: XXX

def insertsort(arr):
    for i in range(1, len(arr)): #recorremos el arreglo emepzando desde el segundo dato para compararlo con el dato de la izquierda
        act = arr[i] #guardamos en una variable el dato que se este comparando 
        indice = i #guardamos el indice del cual vamos a ir iterando en el arreglo
        while indice > 0 and arr[indice - 1] > act: #comparamos los indices diciendo que si en dato con un indice menos es mayor que el dato actual
            arr[indice] = arr[indice - 1] #cambiamos las posiciones del elemento con un indice menos con el actual
            indice = indice - 1 #le restamos 1 al indice para acercarnos al principio del arreglo
        arr[indice] = act #colocamos el elemento actual en el ultimo elemento que se movio
        
    return arr


def main():
    arr=[5,9,8,5,6,3,2,1,4]
    resultado = insertsort(arr)
    print(resultado)
    
    

if __name__ == "__main__":
    main()