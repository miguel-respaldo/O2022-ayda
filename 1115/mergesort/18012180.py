#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
    # Nombre: Omar Ramses Lopez Pulido
# No. Control: 18012180
# Calificación: XXX

import random

# Funcion de ordenamiento merge short
def funcion_de_tarea(arr):
    if len(arr) == 1:
        return arr

    mitad = len(arr) // 2
    p_izquierda = arr[:mitad]
    p_derecha = arr[mitad:]

    p_o_i = funcion_de_tarea(p_izquierda)
    p_o_d = funcion_de_tarea(p_derecha)

    return Merge(p_o_i, p_o_d)

# Funcion apoyo marge short 
def Merge(p_izquierda, p_derecha):
    arr_ordenado = []
    while len(p_izquierda) > 0 and len(p_derecha) > 0:
        if p_izquierda[0] < p_derecha[0]:
            arr_ordenado.append(p_izquierda[0])
            p_izquierda.pop(0)
        else:
            arr_ordenado.append(p_derecha[0])
            p_derecha.pop(0)

    while len(p_izquierda) > 0:
        arr_ordenado.append(p_izquierda[0])
        p_izquierda.pop(0)

    while len(p_derecha) > 0:
        arr_ordenado.append(p_derecha[0])
        p_derecha.pop(0)

    return arr_ordenado

def main():
    lista = []
    print("Ingrese la longitud de la lista:")
    length = int(input())
    print("Ingrese el rango de numeros:")
    print("Desde:")
    inicio = int(input())
    print("Hasta:")
    fin = int(input())

    for i in range(length):
        r = random.randint(inicio, fin)
        lista.append(r)

    print("Lista desordenada:")
    print(lista)
    print("Lista ordenada:")
    print(funcion_de_tarea(lista))

if __name__ == "__main__":
    main()
