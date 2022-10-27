#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alvaro Macias Muro
# No. Control: 18011157
# Calificación: XXX

# Declaración de Funciones

def burbuja(A):
    for i in range(1, len(A)):
        for j in range(0, len(A) - i):
            if (A[j + 1] < A[j]):
                aux = A[j];
                A[j] = A[j + 1];
                A[j + 1] = aux;
    print
    A;


# Programa Principal
A = [7,8,9,6, 5, 3, 1, 8, 7, 2, 4];
print
A
burbuja(A);