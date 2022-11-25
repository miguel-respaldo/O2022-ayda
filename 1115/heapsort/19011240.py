#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Alberto Gonzalez Martinez
# No. Control: 19011240
# Calificación: XXX

# Hijo izquierdo del arrayNumb
def izq(i):
    return 2*i + 1
 
 
# Hijo derecho del arrayNumb
def der(i):
    return 2*i + 2
 
# Intercambiar dos índices en una lista
def swap(arr, i, j):
 
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
 
def heap(arr, i, size):
 
    left = izq(i)
    right = der(i)
 
    largest = i
 
    if left < size and arr[left] > arr[i]:
        largest = left
 
    if right < size and arr[right] > arr[largest]:
        largest = right
 
    if largest != i:
        swap(arr, i, largest)
        heap(arr, largest, size)
 
 
# Función para eliminar un elemento (prioridad más alta) 
def pop(arr, size):
 
    if size <= 0:
        return -1
 
    top = arr[0]
    arr[0] = arr[size - 1]

    heap(arr, 0, size - 1)
    return top
 
# Función heapsort de tamanio n
def heapsort(arr):

    n = len(arr)
    i = (n - 2) // 2

    while i >= 0:
        heap(arr, i, n)
        i = i - 1

    while n:
        arr[n - 1] = pop(arr, n)
        n = n - 1

def main():
    arrayNum = [93, 37, 23, 53, 65, 30, 32, 44, 36]
    print(arrayNum) 
    heapsort(arrayNum) 
    print(arrayNum)

main()