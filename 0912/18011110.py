#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josué Hiram Álvarez Martínez
# No. Control: 18011110
# Calificación: XXX

def fibonacci(num):
    if num <= 0:
        return "inexistente"
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        posicion = 2
        v1, v2 = 0,1
        while posicion < num:
            fibo = v1 + v2
            v1 = v2
            v2 = fibo
            posicion+=1
        return fibo


def main():
    numero = eval(input("Escribe un número: "))
    print("La posición", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()