#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Alberto Gonzalez Martinez
# No. Control: 19011240
# Calificación: XXX

#Definimos una funcion factorial con parametro de n
def factorial(num):
    #Si el numero es menor a 0 entonces no existe
    if num < 0: 
        print("No existe")
    #Si el numero es 0, el factorial es 1    
    elif num == 0: 
        return 1   
    else:
        #Creamos la variable factorial para asignar el valor 
        fact = 1
        #Mientras que el numero sea mayor a 1 deberá iterar las sig. instrucciones
        while(num > 1): 
            #Asigna al factorial la suma de este más el numero ingresado
            fact *= num 
            #El numero se restará menos 1 y se asigna al mismo numero
            num -= 1
        #Retorna el factorial    
        return fact  

#Imprime el factorial
numero = eval(input("Escribe un número: "))
print("El factorial de", numero, "es", factorial(numero))
