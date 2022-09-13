#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Nombre del Estudiante
# No. Control: 17011701
# Calificación: XXX

def fibonacci(num):

    n1, n2 = 0, 1
    count = 0

    if num <= 0:
        print("el numero es negativo")
    elif num == 1:
        
        return n1
    
    while count < num-1:
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
    return n1


def main():
    numero = eval(input("Escribe un número: "))
    print("La posición", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()

