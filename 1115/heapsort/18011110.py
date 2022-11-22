#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josue Hiram Alvarez Martinez
# No. Control: 18011110
# Calificación: XXX

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def siftDown(list, i, upper):
    while(True):
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper:
            if list[i] >= max(list[l], list[r]): break
            elif list[l] > list[r]:
                swap(list, i, l)
                i = l
            else:
                swap(list, i, r)
                i = r
        elif l < upper:
            if list[l] > list[i]:
                swap(list, i, l)
                i < l
            else: break
        elif r < upper:
            if list[r] > list[i]:
                swap(list, i, r)
            else: break
        else: break


def heapSort(list):
    for i in range((len(list)-2)//2, -1, -1):
        siftDown(list, i, len(list))

    for j in range(len(list)-1, 0, -1):
        swap(list, 0, j)
        siftDown(list, 0, j)

    return list


def main():
    list = [5,35,56,98,0,12,4,23]
    resultado = heapSort(list)
    print(resultado)


if __name__ == "__main__":
    main()