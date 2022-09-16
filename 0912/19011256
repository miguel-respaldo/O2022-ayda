#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Rodriguez Pacheco Jose Ruben
# No. Control: 19011256
# Calificación: XXX
def fibonacci(num):
    a=0
    b=1
    c=0
    print("Cadena de fibonacci: 0",end=" ")#imprime el titulo de la cadena y el valor 0
    for i in range(0,num):
        c=a+b
        print(c,end=" ")#imprime el resto de la cadena
        a=b
        b=c
    return c     
        
print("Ingrese un numero",end=" ")
num = int(input())

if num==0:#si el valor de numero es 0 entra en este if
    print("la posicion de fibonacci de 0 es 0")
elif num==1:#si el valor de numero es 1 entra en este elif
    print("la posicion de fibonacci de 1 es 0")
elif num>1:#se encarga de que todos los valores sean mayor que 1 y sean positivos
    print("la posicion de fibonacci de",num,"es:",fibonacci(num))#imprime la posicion de fibonacci y el numero
else:#manda a imprimir un mensaje cuando el valor no es ni 0, ni 1 o mayor que uno
    print("No puede ingresar un valor negativo o un caracter diferente a un numero")  
