#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Rodriguez Garcia Leonardo
# No. Control: 18011414
# Calificación: XXX

def insercion(n):
    # Longitud del arreglo
    for i in range(1, len(n)):

        guarda = n[i]
        #indice del elemento anterior
        j = i - 1
        # En funcion del valor seran transladados
        while j >= 0 and n[j] > guarda:

            n[j + 1] = n[j]
            j -= 1
            
        # Inserta el nuevo valor
        n[j + 1] = guarda


randomNumbers = [9, 1, 91, 19, 38, 26, 67]
# Ingresar el arreglo a la funcion
insercion(randomNumbers)
print(randomNumbers)