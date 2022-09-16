#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Campos Luna Luis Isael
# No. Control: 19011304
# Calificación: XXX

def fibonacci(num):
    # Tomando en cuenta el 0 como posición 1
    # Modificar esta parte
    # return num**2  y esta linea
    a = 0
    b = 1
    
    for k in range(num):
        c = b+a
        a = b
        b = c
        
    return a


def main():
    numero = eval(input("Escribe un número: "))
    print("La posición", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()