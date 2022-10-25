#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Alberto Gonzalez Martinez
# No. Control: 19011240
# Calificación: XXX

def burbuja(n):
    # Cambio = True para entrar al while al menos una vez
    cambio = True
    while cambio:
        # False e iterar en la longitud del arreglo - 1
        cambio = False
        for i in range(len(n) - 1):
            # Posicion n > Posicion n + 1
            if n[i] > n[i + 1]:
                # Intercambio de datos
                n[i], n[i + 1] = n[i + 1], n[i]
                # Cambio = True porque hubo intercambio
                cambio = True

# Array de numeros
randomNumbers = [25, 13, 4, 18, 5, 78, 1]
# Ingresar el array de numeros en la funcion
burbuja(randomNumbers)
# Imprimir el array de numeros
print(randomNumbers)