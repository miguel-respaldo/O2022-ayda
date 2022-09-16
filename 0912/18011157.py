#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alvaro Macias Muro
# No. Control: 18011157
# Calificación: XXX


def Fibonacci(Numero):
    if(Numero==0):
        return 0
    if(Numero==1):
        return 1
    else:
        return (Fibonacci(Numero-2)+Fibonacci(Numero-1))
n=int(input("El valor es 'n': "))
print("Secuencia:")
for n in range(0, n):
  print(Fibonacci(n))