#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Salvador de Jesus Dueñas Muñiz
# No. Control: 19011235
# Calificación: XXX

# Definimos la funcion factorial
def factorial(n):
    #Creamos un if si "n" es mayor a 0
    if n > 0:
        num = 0
        fact = 1
        #Creamos un for para el numero en en cuestion a evaluar 
        for num in range(1, n, 1):
            fact *= n
            n-=1
        return fact
    #elif si "n" es 0
    elif n == 1:
        return 1
     #else si "n" menor o diferente de 0
    else:
        cadena = "invalido, ingrese numeros positivos"
        return cadena

#Pedimos al usuario que digite la entrada
numero = int(input("Por favor ingrese un valor:"))
print ("El factorial de",numero,"es",factorial(numero))

