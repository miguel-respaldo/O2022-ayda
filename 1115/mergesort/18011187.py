#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josue Daniel Rocha Ledezma
# No. Control: 18011187
# Calificación: XXX

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        mergesort(left)
        mergesort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                arr[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return  arr

def main():

    arr = [75, 87, 1, 6, 4, 1, 10, 45, 15, 32, 44, 999, 56, 100]
    print("Este es el main y llama la función de tarea mergeSort")
    resultado = mergesort(arr)
    print("resultado", resultado)

if __name__ == "__main__":
    main()