#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josué Hiram Álvarez Martínez
# No. Control: 18011110
# Calificación: XXX

def bubbleSort(numbers):
    arraySize = len(numbers)-1
    for i in range(arraySize):
        for j in range(arraySize):
            if numbers[j] < numbers[j+1]:
                aux = numbers[j]
                numbers[j] = numbers[j+1]
                numbers [j+1] = aux
    return numbers


def main():
    numbers = [27,24,2,17,18,16,8, -1]
    resultado = bubbleSort(numbers)
    print(resultado)


if __name__ == "__main__":
    main()