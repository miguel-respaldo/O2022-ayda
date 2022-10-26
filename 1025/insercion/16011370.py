#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Luis Fernando Rubio Zambrano
# No. Control: 16011370
# Calificación:XXX

def mostrarLista(lista, lon):
    listaordenada = ""
    for i in range(0, lon):
        listaordenada += str(lista[i]) + " "
    print(listaordenada)

arreglo = [5, 2, 4, 1, 3];

for i in range(1, len(arreglo)):
    clave = arreglo[i]
    j = i - 1
    while (j >= 0 and arreglo[j] > clave):
        arreglo[j + 1] = arreglo[j]
        j = j - 1
    arreglo[j + 1] = clave
    mostrarLista(arreglo, len(arreglo))
mostrarLista(arreglo, len(arreglo))