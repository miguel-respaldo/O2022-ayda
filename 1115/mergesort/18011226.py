#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alexa Fernanda Iniguez Jimenez
# No. Control: 18011226
# Calificación: XX

def mergeSort(arr):
    if len(arr) > 1:

        # Encontrar la mitad de la matriz
        Mitad = len(arr) // 2

        # Dividir el arreglo en 2 mitades

        #Primer mitad
        PrimerMitad = arr[:Mitad]

        #Segunda mitad
        SegundaMitad = arr[Mitad:]

        # Ordenando la primer mitad que es la izquierda
        mergeSort(PrimerMitad)

        # Ordenando la segunda mitad que es la derecha
        mergeSort(SegundaMitad)

        i = j = aux = 0

        # Copiar los datos en un arreglo temporal
        while i < len(PrimerMitad) and j < len(SegundaMitad):
            if PrimerMitad[i] <= SegundaMitad[j]:
                arr[aux] = PrimerMitad[i]
                i += 1
            else:
                arr[aux] = SegundaMitad[j]
                j += 1
            aux += 1

        # Comprobando si quedo algun elemento
        while i < len(PrimerMitad):
            arr[aux] = PrimerMitad[i]
            i += 1
            aux += 1

        while j < len(SegundaMitad):
            arr[aux] = SegundaMitad[j]
            j += 1
            aux += 1

#---------------- MAIN -----------------------------------------

arr = [1, 42, 7, 33, 12, 100, 50]
print("... Mergesort ...")
print(arr)
print("------------------------")
print("Arreglo ordenado")
mergeSort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")
