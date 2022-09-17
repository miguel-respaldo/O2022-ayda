#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Grecia Katya Alexandra Muñoz Cabrera
# No. Control: 18011433
# Calificación: XXX

def fibonacci2(num2): # El metodo de fibonacci
    if (num2 == 0):
        return 0
    elif (num2 == 1):
        return 1
    else:
        return fibonacci2(num2 - 1) + fibonacci2(num2 - 2)

def fibonacci(num): # verifica lo numeros negativos y reduce la posicion en 1
    if (num < 1): # si el numero es menor a 1 sera invalido
        return "invalida"
    else:
        return fibonacci2(num - 1) #se quita uno al numero que mando el usuario



def main():
    numero = eval(input("Escribe un número: "))
    print("La posición", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()
