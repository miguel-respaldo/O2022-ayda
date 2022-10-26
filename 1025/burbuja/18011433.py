#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Grecia Katya Alexandra Muñoz Cabrera
# No. Control: 18011433
# Calificación: XXX

def burbuja(arr):
     
    n = len(arr)
    print(len(arr))
    # elemento del arreglo
    for i in range(n):
        print(i)
        print(arr)
        for j in range(0, n - i - 1):
             
            # el rango del arreglo es de 0 hasta n-i-1
            # intercambia los elementos si el elemento encontrado es mayor al adyacente  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# numeros agregados al arreglo
arr = [ 22, 10, 1, 26 ]
burbuja(arr)
 
print("El arreglo ordenado es:")
for i in range(len(arr)):
    print("%d" % arr[i])
