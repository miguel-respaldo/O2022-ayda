#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luis Fernando Rubio Zambrano
# No. Control: 123456789
# Calificación: XXX

def fibonacci(num):
    # Tomando en cuenta el 0 como posición 1
    # Modificar esta parte
   # return num**2  y esta linea
    if num < 2:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num - 2)

def main():
    numero = eval(input("Escribe un número: "))
    print("La posición", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()

