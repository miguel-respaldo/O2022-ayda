#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Leonardo Rodriguez Garcia
# No. Control: 18011414
# Calificación: XXX

def fibonacci(num):
    num1 = 0
    num2 = 1

    for i in range(num):
        num3 = num1+num2
        num1 = num2
        num2 = num3
    return num2 


def main():
    numero = eval(input("Escribe un número: "))
    print("La posición", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()

