#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Maria Guadalupe Garcia Baltazar
# No. Control: 19011845
# Calificación: XXX

def seleccion(arreglo):
    for i in range(len(arreglo) - 1):
        menor = i

        for j in range(i + 1, len(arreglo)):
            if arreglo[j] < arreglo[menor]:
                menor = j

        if menor != i:
            arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]

def main():
    lista = [7, 5, 8, 2, 19, 4, 11, 17, 14, 16];
    print(lista)
    seleccion(lista)
    print(lista)

if __name__ == "__main__":
    main()