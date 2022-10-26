#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Salvador Serna Ramirez
# No. Control: 18011319
# Calificación: XXX


def insercion(Z):
    for i in range(len(Z)):
        for y in range(i,0,-1):
            if(Z[y-1] > Z[y]):
                aux=Z[y]
                Z[y]=Z[y-1]
                Z[y-1]=aux
    print (Z)
 

Z=[6,8,12,25,15,20,22,5,35,1]
print (Z)
insercion(Z)