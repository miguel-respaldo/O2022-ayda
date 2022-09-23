#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Nombre del Estudiante
# No. Control: 123456789
# Calificación: XXX

def fibonacci(num):
    n1 = 0
    n2 = 1
    ret = 0

    if num <= 0:
        return "indefinida"

    if num == 1:
        return n1

    if num == 2:
        return n2
    
    for i in range(num-2):
        ret = n1 + n2
        n1 = n2
        n2 = ret
    return ret

def main():
    numero = eval(input("Escribe un número: "))
    print("La posición", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()

