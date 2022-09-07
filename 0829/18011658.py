#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Luna Gonzalez Alan Alejandro
# No. Control: 18011658
# Calificación: XXX

# Factorial de un número:
print("¡Bienvenido!")
print("Programmer: Alan Luna")

numero = int(input("\nIngrese un número: >"))
factorial = numero
if numero != 0:
    for i in range(1, numero * 1):
        factorial = factorial * i

print("\nEl Factorial es:", factorial)
