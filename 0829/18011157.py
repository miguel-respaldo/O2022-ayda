#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Alvaro Macias Muro
# No. Control: 18011157
# Calificación: XXX

def factorial (n):

    if (n==0):
        return 1
    else:
        return n * factorial(n-1)
n = int(input("numero: "))
print ("El factorial de: "+str(n)+" : es:"+str(factorial(n)))