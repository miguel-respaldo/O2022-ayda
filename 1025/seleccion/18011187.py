#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josue Daniel Rocha Ledezma
# No. Control: 18011187
# Calificación: XXX

def seleccion(array):
    nb = len(array)
    for actual in range(0, nb):
        menor = actual
        for j in range(actual + 1, nb):
            if array[j] < array[menor]:
                menor = j
        if min is not actual:
            temp = array[actual]
            array[actual] = array[menor]
            array[menor] = temp
    return array

def main():
    arr = [75, 87, 1, 6, 4, 1, 10, 45, 15]
    print("Este es el main y llama la función de tarea seleccion")
    resultado = seleccion(arr)
    print("resultado", resultado)


if __name__ == "__main__":
    main()
