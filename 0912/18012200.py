#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Brandon Oswaldo Nila Torres 
# No. Control: 18012200
# Calificación: XXX

def fibonacci(posicion):#declaracion de la funcion y recibe el parametro como posicion
    if posicion == 0:#evaluamos si la posicion es igual a cero
        return 0
    if posicion == 1:#evaluamos si la posicion es igual a uno
        return 1
    
    #variables para calculo fibonacci
    a = 0 #es el valor de F n-2
    b = 1 #es el valor de F n-1
    c = 0 #la suma de a + b
    
    for i in range(2,posicion+1):#defino un rango desde 2 hasta la posicion que ingresó el usuario
        c= a + b 
        a= b 
        b= c
    return c
        
posicion = int(input("Dame la posicion: "))
print(f"el fibonacci es:  {fibonacci(posicion)}")
