#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Josué Hiram Álvarez Martínez 
# No. Control: 18011110
# Calificación: XXX

def factorial(n):
    if n < 0:
        return "inexistente"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)



number = int(input("Calcular factorial de:"))
print("El factorial de ", number, "es ", factorial(number))
