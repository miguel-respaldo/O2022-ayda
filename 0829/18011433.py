#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Muñoz Cabrera Grecia Katya Alexandra
# No. Control: 18011433
# Calificación: XXX

def factorial(num):
    factor = 1
    while(num > 1):
        factor = factor*num
        num = num - 1
    return factor

print("Dame el numero para sacar el factorial: ")
numero = input()
if numero.isdigit() == False:
    print("No es un numero valido")
else:
    numero = int(numero)
    resultado = factorial(numero)
    print("El factorial es ", resultado)
