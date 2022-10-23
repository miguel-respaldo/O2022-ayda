#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josué Hiram Álvarez Martínez
# No. Control: 18011110
# Calificación: XXX

def selectionSort(numbers):
    arraySize = len(numbers)
    for i in range(arraySize):
        index = i
        for j in range(i+1, arraySize):
            if numbers[j] > numbers[index]:
                index = j
        numbers[i], numbers[index] = numbers[index], numbers[i]
    return numbers


def main():
    numbers = [27,24,2,17,18,16,8, -1]
    resultado = selectionSort(numbers)
    print(resultado)


if __name__ == "__main__":
    main()