#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Maria Guadalupe Garcia Baltazar
# No. Control: 19011845
# Calificación: XXX

def factorial(num):
    if num != 0:
        return num*factorial(num-1)
    else:
        return 1


numero = eval(input("Escribe un número: "))
print("El factorial de", numero, "es", factorial(numero))