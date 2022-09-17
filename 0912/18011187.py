#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Josue Daniel Rocha Ledezma
# No. Control: 18011187
# Calificación: XXX

def fibonacci(num):
    # Tomando en cuenta el 0 como posición 1
    # Modificar esta parte
    aux = 1
    cont = 1
    res = 0
    if num == 0 or num < 0:
        return "No existe debe de ingresar un numero mayor a 0"
    elif num == 2 or num == 3:
       return 1
    else:
        for i in range(0, num-3):
            res = aux + cont
            cont = aux
            aux = res

    return res # y esta linea


def main():
    numero = eval(input("Escribe un número: "))
    print("La posición", numero, "de fibonacci es:", fibonacci(numero))


if __name__ == "__main__":
    main()