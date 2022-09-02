#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Luis Isael Campos Luna
# No. Control: 19011304
# Calificación: XXX
# aki pone numerito
num = int(input("ingresa numero: "))

factorial = 1

# no existe numero factorial negativo
if num < 0:
   print("numero no aceptado :/")
elif num == 0:
   print("El factorial de 0 ser 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("El factorial de",num,"es",factorial)