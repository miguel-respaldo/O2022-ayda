#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josué Hiram Álvarez Martínez
# No. Control: 18011110
# Calificación: XXX

def insertSort(numbers):
    arraySize = len(numbers)
    for i in range(1,arraySize):
        current = numbers[i]
        index = i
        while index > 0 and numbers[index] > current:
            numbers[index] = numbers[index-1]
            index -= 1
    return numbers


def main():
    numbers = [27,24,2,17,18,16,8, -1]
    resultado = insertSort(numbers)
    print(resultado)


if __name__ == "__main__":
    main()