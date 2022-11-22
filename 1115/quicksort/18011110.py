#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josue Hiram Alvarez Martinez
# No. Control: 18011110
# Calificación: XXX

def quickSort(list):
    if len(list) <= 1:
        return list
    else:
     aux = list.pop()

    bigger = []
    lower = []

    for element in list:
        if element > aux:
            bigger.append(element)
        else:
            lower.append(element)

    return quickSort(lower) + [aux] + quickSort(bigger)

def main():
    list = [5, 35, 56, 98, 0, 12, 4, 23]
    print(quickSort(list))

if __name__ == "__main__":
    main()
