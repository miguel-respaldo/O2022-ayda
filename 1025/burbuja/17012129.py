#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: José Ricardo Siordia Alatorre
# No. Control: 17012129
# Calificación: XXX

A = [88, 27, 12, 65, 93, 43]

num = len(A)

i = 0

while i < num:

      j = i

      while j < num:


              if A[i] > A[j]:

                      aux = A[i]

                      A[i] = A[j]

                      A[j] = aux

              j = j + 1
              
      i = i + 1

print("Lista ordenada en Burbuja: ")
print(A)