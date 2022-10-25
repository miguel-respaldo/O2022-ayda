#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Alberto Gonzalez Martinez
# No. Control: 19011240
# Calificación: XXX

def insercion(n):
    # Iterar en el elemento i, (1, la longitud del arreglo) "1" es el segundo elemento
    for i in range(1, len(n)):
        guarda = n[i]
        # j toma el indice del elemento anterior
        j = i - 1
        # Mueve los elementos adelante si es mayor que el elemento a insertar
        while j >= 0 and n[j] > guarda:
            n[j + 1] = n[j]
            j -= 1
        # Inserta el elemento
        n[j + 1] = guarda

# Array de numeros
randomNumbers = [9, 1, 91, 19, 38, 26, 67]
# Ingresar el array de numeros en la funcion
insercion(randomNumbers)
# Imprimir el array de numeros
print(randomNumbers)