#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Jose Manuel Buendia Rodriguez
# No. Control: 19011231
# Calificación: XXX


num = eval(input("Escribe un número: "))

if num< 0: #Si el numero es negativo, no es valido
    print("Numero no valido")
elif num > 0: #Si el numero es positivo continua

    def factorial(num): 
    
        if num < 2: #Agregar una condicional para determinar que los numeros sean mayores que 2, de lo contrario el resultado sería 0 & 1
            return num
        return factorial(num-1) + factorial(num-2) # Aplicamos la formula Fibonacci de forma Recursiva

    print ("La serie Fibonazzi de",num, "es:") 

    for x in range(num): # Imprimimos la serie del numero 
        print(factorial(x)) 


    print("La posicion Fibonacci de", num, "es", factorial(x)) #Imprimimos el numero y su posicion en fibonacci