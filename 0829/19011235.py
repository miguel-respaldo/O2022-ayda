#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Salvador de Jesus Dueñas Muñiz
# No. Control: 19011235
# Calificación: XXX

def factorial(n):
    if n >= 0:
        num = 0
        fact = 1
        for num in range(1, n, 1):
            fact *= n
            n-=1
        return fact
    else:
        cadena = "invalido, ingrese numeros positivos"
        return cadena
        
numero = int(input("Por favor ingrese un valor:"))
print ("El factorial de",numero,"es",factorial(numero))

