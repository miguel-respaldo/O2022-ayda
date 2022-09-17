#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Francisco Javier Ocampo Torres
# No. Control: 18011167
# Calificación: XXX

def Fibonacci(n):   
    # Si es 0
    if n < 0:
        print("Ingresa un numero entero no negativo")
    # Comprobar si n es 0
    elif n == 0:
        return 0
    # Comprobar si n es mayor a 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
num=eval(input("Ingresa un numero: "))
print("La posicion Fibonacci",num,"es",Fibonacci(num))