#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Maria Guadalupe Garcia Baltazar
# No. Control: 19011845
# Calificación: XXX

def insercion(lista):

    for i in range(len(lista)):
        for j in range(i, 0, -1):
            if(lista[j-1] > lista[j]):
                aux = lista[j];
                lista[j] = lista[j-1];
                lista[j-1] = aux;

    print(lista);

def main():
    lista =  [7, 5, 8, 2, 19, 4, 11, 17, 14, 16];
    print(lista);
    insercion(lista);

if __name__ == "__main__":
    main()