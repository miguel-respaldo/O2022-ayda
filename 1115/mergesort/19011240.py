#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Alberto Gonzalez Martinez
# No. Control: 19011240
# Calificación: XXX

def mergeSort(arrayNum):

    if len(arrayNum) > 1:

        mid = len(arrayNum) // 2
        left = arrayNum[:mid]
        right = arrayNum[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0        
        k = 0
        
        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
              arrayNum[k] = left[i]
              i += 1

            else:
                arrayNum[k] = right[j]
                j += 1
            k += 1
    
        while i < len(left):
            arrayNum[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arrayNum[k] = right[j]
            j += 1
            k += 1

def main():
    arrayNum = [93, 37, 23, 53, 65, 30, 32, 44, 36]
    print(arrayNum) 
    mergeSort(arrayNum) 
    print(arrayNum)

main()