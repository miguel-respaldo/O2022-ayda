#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Muñoz Cabrera Grecia Katya Alexandra 
# No. Control: 18011433
# Calificación: XXX

# Función para encontrar la posición de la partición

def partition(array, low, high):
 
    pivot = array[high]
 
    # se apunta al elemento mayor
    i = low - 1
 
    # pasa por todos los elementos 
    # se comparan
    for j in range(low, high):
        if array[j] <= pivot:
 
            # si encuentra un elemento mas peuqeños lo intermacabia con el elemento mayor señalado por i 
            i = i + 1
 
            # se hace intercambio de elemento en i con j 
            (array[i], array[j]) = (array[j], array[i])
 
    # intercambuio del elemento mayor especificado por i 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # devuelve la posicion desde donde se realiza la particion 
    return i + 1
 
    # funcion para realizar ordenacion rapida
 
 
def quickSort(array, low, high):
    if low < high:
 
        # elemetos mas chicos se encuentran a la izquierda 
        # elementos mayores del lado derecho 
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)
 
 
data = [10, 13, 8, 3, 19, 15, 2]
print("elementos a ordenar")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print("elementos ordenados por quicksort ")
print(data)
