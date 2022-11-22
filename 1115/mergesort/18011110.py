#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josue Hiram Alvarez Martinez
# No. Control: 18011110
# Calificación: XXX

def mergeSort(list):
    if  len(list) > 1:
        l = list[:len(list)//2]
        r = list[len(list)//2:]
        i, j, k = 0,0,0
        mergeSort(l)
        mergeSort(r)
        while i < len(l) and j < len(r):
            if  l[i] < r[j]:
                list[k] = l[i]
                i += 1
            else:
                list[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            list[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            list[k] = r[j]
            j += 1
            k += 1

def main():
    list = [5, 35, 56, 98, 0, 12, 4, 23]
    mergeSort(list)
    print(list)

if __name__ == "__main__":
    main()
