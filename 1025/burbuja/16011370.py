#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Luis Fernando Rubio Zambrano
# No. Control: 16011370
# Calificación:XXX


def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):      
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

elementos = [8, 3, 1, 19, 14]
ord_burbuja(elementos)

print(elementos)