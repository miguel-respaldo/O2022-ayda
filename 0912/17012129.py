#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: José Ricardo Siordia Alatorre
# No. Control: 17012129
# Calificación: XXX

def Fibonacci(n):
   
    if n < 0:
        print("dato incorrecto")
 
    elif n == 0:
        return 0
 

    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(10))