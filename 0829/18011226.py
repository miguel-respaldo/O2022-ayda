#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Alexa Fernanda Iñiguez Jimenez
# No. Control: 18011226
# Calificación: XXX

def factorial(num):

        if num < 0:
             print("El factorial de", numero, "no existe")

        elif num == 0 or num == 1: return 1

        else: fact = 1

        while(num > 1):
            fact *=  num
            num -=  1
        return fact

numero = 2;

print("Factorial de", numero, "es:", factorial(numero))