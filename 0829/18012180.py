#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Omar Ramses Lopez Pulido
# No. Control: 18012180
# Calificación: XXX
def factorial(n):
    if n<0:
        resultado ==-1
    for i in range(0, n+1):
        resultado = 0
        if i==0 or i==1:
            resultado = 1
        elif i > 1:
            resultado = i * factorial(n-1)
    return resultado

x = int(input("Ingrese un numero: "))
if x < 0:
    print("No existe el fatoral de: ", x)
else:
    fact = factorial(x)
    print("Factorial: ",fact)