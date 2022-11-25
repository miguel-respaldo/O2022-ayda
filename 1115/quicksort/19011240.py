#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Alberto Gonzalez Martinez
# No. Control: 19011240
# Calificación: XXX

def sort(lista):
    
    left = []
    center = []
    right = []

    if len(lista) > 1:

        pivote = lista[0]
        for i in lista:
            if i < pivote:
                left.append(i)
            elif i == pivote:
                center.append(i)
            elif i > pivote:
                right.append(i)
        return sort(left) + center + sort(right)
        
    else:
      return lista

def main():
    arrayNum = [93, 37, 23, 53, 65, 30, 32, 44, 36]
    print(arrayNum)
    print(sort(arrayNum))

main()    