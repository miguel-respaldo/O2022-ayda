#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Rodriguez Pacheco Jose Ruben
# No. Control: 19011256
# Calificación: XXX
print("Ingrese un numero ")
num = int(input())
facto = 1

if num == 0:
    	print("El factorial de 0 es 1")

elif num>0:
    for i in range(1, num+1):
        facto*=i    	
    print("El factorial de ",num,"es",facto)

else:
    print("Usted ingreso un numero negativo o un valor que no es un numero")
