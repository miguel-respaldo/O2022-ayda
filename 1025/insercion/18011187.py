#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josue Daniel Rocha Ledezma
# No. Control: 18011187
# Calificación: XXX

def insercion(array):
    for i in range(1, len(array)):
            aux = array[i]
            j = i
            # Desplazamiento de los elementos de la matriz }
            while j > 0 and array[j - 1] > aux:
                array[j] = array[j - 1]
                j = j - 1
            # insertar el elemento en su lugar
            array[j] = aux

    return array

def main():
    arr = [75, 87, 1, 6, 4, 1, 10, 45, 15]
    print("Este es el main y llama la función de tarea insercion")
    resultado = insercion(arr)
    print("resultado", resultado)


if __name__ == "__main__":
    main()
