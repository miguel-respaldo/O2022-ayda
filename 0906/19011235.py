#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Salvador de Jesus Dueñas Muñiz
# No. Control: 19011235
# Calificación: XXX

# Definimos la funcion factorial
def factorial(numero):
    #Creamos un if si "n" es mayor a 0
    if numero > 0:
        num = 0
        fact = 1
        #Creamos un for para el numero en en cuestion a evaluar 
        for num in range(1, numero, 1):
            fact *= numero
            numero-=1
        return fact
    #elif si "n" es 0
    elif numero == 1:
        return 1
     #else si "n" menor o diferente de 0
    else:
        cadena = "invalido, ingrese numeros positivos"
        return cadena

#Pedimos al usuario que digite la entrada
numero = eval(input("Por favor ingrese un valor:"))
print ("El factorial de",numero,"es",factorial(numero))