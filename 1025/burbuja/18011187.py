#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josue Daniel Rocha Ledezma
# No. Control: 18011187
# Calificación: XXX

def burbuja(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j + 1] < array[j]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux

    return array

def main():
    arr = [75, 87, 1, 6, 4, 1, 10, 45, 15]
    print("Este es el main y llama la función de tarea")
    resultado = burbuja(arr)
    print("resultado", resultado)


if __name__ == "__main__":
    main()
