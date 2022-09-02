#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Francisco Javier Ocampo Torres
# No. Control: 18011167
# Calificación: XXX

def factorial(f):
    if f<0:
        return 0
    if f==0 or f==1:
        return 1
    else:
        fact=1
        while(f>1):
            fact*=f
            f-=1
        return fact

num=eval(input("Ingresa un numero: "))
print("El factorial de ",num,"es",
factorial(num))
