#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Alberto Gonzalez Martinez
# No. Control: 19011240
# Calificación: XXX

def seleccion(n):
    # Iterar en la longitud del arreglo
    for i in range(len(n)):
        # Primer elemento es el masBajo
        masBajo = i
        # Iterar en el elemento j, (i + 1, la longitud del arreglo)
        for j in range(i + 1, len(n)):
            # Elemento en Posicion j < Elemento en Posicion masBajo
            if n[j] < n[masBajo]:
                # masBajo toma el elemento j
                masBajo = j
        # Intercambio de datos
        n[i], n[masBajo] = n[masBajo], n[i]

# Array de numeros
randomNumbers = [10, 4, 46, 12, 31, 63, 25]
# Ingresar el array de numeros en la funcion
seleccion(randomNumbers)
# Imprimir el array de numeros
print(randomNumbers)