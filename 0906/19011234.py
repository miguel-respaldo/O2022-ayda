#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Octavio Corral Tovar
# No. Control: 19011234
# Calificación: XXX

def factorial(num): #creo la funcion factorial que recibe un parametro el cual es num
    
    fact= 1 #inicializo la variable fact en 1 para que pueda multiplicarse 

    for i in range (1,num+1): #Creo el ciclo for con el rango de 1 al numero indicado + 1 para que pueda tomar el numero indicado
        fact = fact*i #Guardo la multiplicacion del fact * el iterador en la misma variable para que pueda ir acumulando el resultado
    return fact #Guardo el resultado retornando el resultado en "fact"


numero = eval(input("Escribe un número: ")) #guardo en la variable "numero" el numero que el usuario digito
print("El factorial de", numero, "es", factorial(numero)) #Imprimo el resultado de la funcion en pantalla