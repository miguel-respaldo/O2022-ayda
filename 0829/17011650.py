#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Hugo Emmanuel Gonzalez Gomez
# No. Control: 17011650
# Calificación: XXX

numero = 0
factorial = 1

print("Ingresa un numero positivo: ")
numero = int(input())

if numero < 0:
    print("ERROR!")
    print("No existe numeros negativos en el factorial")
else:
    for i in range(1, numero+1):       
        sum = factorial = factorial * i
    print("El factorial es: ", sum)

