#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:

def factorial(n):

    fact= 1

    for i in range (1,n+1):
        fact = fact*i
            
    return fact

x = int(input("Digite un numero: "))

resultado = factorial(x)

print(resultado)

# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Octavio Corral Tovar
# No. Control: 19011234
# Calificación: XXX