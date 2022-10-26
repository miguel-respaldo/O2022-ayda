#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Grecia Katya Alexandra Muñoz Cabrera
# No. Control: 18011433
# Calificación: XXX

def insercion(list1): 
   
        for i in range(1, len(list1)): 
            print(list1)
            a = list1[i] 
            
            # mover elementos de list1[0 to i-1],
            # que sean mayores a la posicion delante de la posicion actual
            j = i - 1 
           
            while j >= 0 and a < list1[j]: 
                list1[j + 1] = list1[j] 
                j -= 1 
                 
            list1[j + 1] = a 
             
        return list1 
            
list1 = [ 22, 10, 1, 26 ] 
print("lista sin ordenar:", list1) 
print("lista ordenada:", insercion(list1))
