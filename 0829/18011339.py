#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Henrnandez Uribe Nestor Eduardo
# No. Control: 18011339
# Calificación: XXX

def factorial(num):
    factor = 1
    while(num > 1):
        factor = factor*num
        num = num - 1
    return factor

print("Ingresa el NUmero para obtener el factorial: ")
numero = input()
if numero.isdigit() == False:
    print("No es valido el numero ingresado")
else:
    numero = int(numero)
    resultado = factorial(numero)
    print("el resultado factorial es: ", resultado)
