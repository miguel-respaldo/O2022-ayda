#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Maria Guadalupe Garcia Baltazar
# No. Control: 19011845
# Calificación: XXX

def burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

def main():
    lista = [7, 5, 8, 2, 19, 4, 11, 17, 14, 16];
    print(lista)
    burbuja(lista)
    print(lista)

if __name__ == "__main__":
    main()