#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Octavio Corral Tovar
# No. Control: 19011234
# Calificación: XXX

arr = [8,5,4,7,9,6,2,5,1]

def mergesort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    left_array = arr[:middle]
    right_array = arr[middle:]

    sorted_left_array = mergesort(left_array)
    sorted_right_array = mergesort(right_array)

    return Merge (sorted_left_array, sorted_right_array )

def Merge(left_arr, right_arr):
    arr_resultado = []
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] > right_arr[0]:
            arr_resultado.append(right_arr[0])
            right_arr.pop(0)
        else:
            arr_resultado.append(left_arr[0])
            left_arr.pop(0)
    while len(left_arr) > 0:
        arr_resultado.append(left_arr[0])
        left_arr.pop(0)
    while len(right_arr) > 0:
        arr_resultado.append(right_arr[0])
        right_arr.pop(0)

    return arr_resultado
    

def main():
    resultado = mergesort(arr)
    print(resultado) 


if __name__ == "__main__":
    main()