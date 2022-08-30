#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Josue Daniel Rocha Ledezma
# No. Control: 18011187
# Calificación: XXX

# Factorial 30/08/2022
def factorial(n):
    aux = 1
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return "no existe factorial para este numero"
    else:
        for i in range(1, n + 1):
            aux = aux * i
        return aux


numero = int(input("ingresa un numero: "))
print(factorial(numero))
