#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Octavio Corral Tovar
# No. Control: 19011234
# Calificación: XXX

def factorial(n): #creo la funcion factorial que recibe un parametro el cual es n

    fact= 1 #inicializo la variable fact en 1 para que pueda multiplicarse

    for i in range (1,n+1): #Creo el ciclo for con el rango de 1 al numero indicado + 1 para que pueda tomar en cuenta el numero indicado
        fact = fact*i #Guardo la multiplicacion del fact * i en la misma variable fact, para que pueda ir acumulando el resultado
            
    return fact #Guardo el resultado retornando el resultado en "fact"

x = int(input("Digite un numero: ")) #guardo en la variable "x" el numero que el usuario digito

resultado = factorial(x) #guardo el resultado que la funcion realizo en la variable "resultado"

print(resultado) #Imprimo el resultado de la funcion en pantalla

