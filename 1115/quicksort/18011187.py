#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josue Daniel Rocha Ledezma
# No. Control: 18011187
# Calificación: XXX

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
        return quicksort(izquierda) + centro + quicksort(derecha)
    else:
        return arr


def main():

    arr = [75, 87, 1, 6, 4, 1, 10, 45, 15, 32, 44, 999, 56, 100]
    print("Este es el main y llama la función de tarea Quicksort")
    resultado = quicksort(arr)
    print("resultado", resultado)

if __name__ == "__main__":
    main()