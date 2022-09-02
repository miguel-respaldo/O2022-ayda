#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Salvador Serna Ramirez
# No. Control: 18011319
# Calificación: XXX


def fac(r):
 
    if r==1 :
        return 1;
    else:
        fac=1
        while(r>1):
            fac*=r
            r-=1
        return fac

fac_n= 5
print("El factorial de",fac_n, "es: ",fac(fac_n))