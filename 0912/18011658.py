#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luna Gonzalez Alan Alejandro
# No. Control: 18011658
# Calificación: XXX

# Fibonacci:
print("¡Bienvenido!")
print("Programmer: Alan Luna | Fibonacci")


def fibonacci(n):
    # Tomando en cuenta el 0 como posición 1
    # Modificar esta parte
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# return num**2

def main():
    numero = eval(input("\n***Ingresa un número: >"))
    print("La posición", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()