#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Octavio Corral Tovar
# No. Control: 19011234
# Calificación: XXX

arr = [8,5,4,7,9,6,2,5,1]

def quicksort(arr):
    izquierda = []
    centro = []
    derecha = []

    if len(arr) > 1:
        pivote = arr[0]
        for i in arr:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        
        return quicksort(izquierda)+centro+quicksort(derecha)
    else:
      return arr

def main():
    resultado = quicksort(arr)
    print(resultado) 


if __name__ == "__main__":
    main()