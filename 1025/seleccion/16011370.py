#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Luis Fernando Rubio Zambrano
# No. Control: 16011370
# Calificación:XXX

def seleccion(arreglo):
    longitud = len(arreglo)
    for i in range(longitud-1):
        for j in range(i+1, longitud):
            if arreglo[i] > arreglo[j]:
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]