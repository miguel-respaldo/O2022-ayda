#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Sebastian Garcia Quijas
# No. Control: 18011215
# Calificación: XXX
def factorial(num):
    # Solo modifican aqui
    if num == 1:
        return 1
    return num * factorial(num - 1) # y aqui claro
numero = eval(input("Escribe un número: "))
print("El factorial de", numero, "es", factorial(numero))