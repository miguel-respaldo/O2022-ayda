#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alexa Fernanda Iniguez Jimenez
# No. Control: 18011226
# Calificación: XX

def quicksort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)

        return quicksort(izquierda)+centro+quicksort(derecha)
    else:
      return lista

#---------------- MAIN -----------------------------------------

arr = [1, 42, 7, 33, 12, 100, 50]
print("... Quicksort ...")
print(arr)
print("------------------------")
print("Arreglo ordenado")
quicksort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")