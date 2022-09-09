#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def factorial(num):

    if num < 0:
        return "invalido, porque no existen factorial de negativo"

    resultado = 1

    while num > 1:
        resultado *= num
        num -= 1

    return resultado


def main():
    numero = eval(input("Escribe un número: "))
    print("El factorial de", numero, "es", factorial(numero))


if __name__ == "__main__":
    main()

