#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Jim Antonio Loza Orozco
# No. Control: 18012212
# Calificación: XXX

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


numero = int(input("Ingresa el numero factorial: "))
print(factorial(numero))
