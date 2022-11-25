#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Salvador de Jesus Dueñas Muñiz
# No. Control: 19011235
# Calificación: XXX


def QuickSort(arr):

    elementos = len(arr)
    if elementos < 2:
        return arr
    
    posicion = 0

    for i in range(1, elementos): 
         if arr[i] <= arr[0]:
              posicion += 1
              temp = arr[i]
              arr[i] = arr[posicion]
              arr[posicion] = temp

    temp = arr[0]
    arr[0] = arr[posicion] 
    arr[posicion] = temp 
    
    izquierda = QuickSort(arr[0:posicion]) 
    derecha = QuickSort(arr[posicion+1:elementos]) 
    arr = izquierda + [arr[posicion]] + derecha 
    
    return arr


def main():
    arreglado_a_ordenar = [4,2,7,3,1,6]
    resultado = QuickSort(arreglado_a_ordenar)
    print(resultado)


if __name__ == "__main__":
    main()

