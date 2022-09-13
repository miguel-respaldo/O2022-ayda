#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Omar Ramses Lopez Pulido
# No. Control: 18012180
# Calificación: XXX

def fibonacci(num):
    """
    Funcion para encontrar el numero fibonacci de x posicion.
    :param num: Posicion fibonacci a encontrar.
    :return: El numero fibonacci que se enecuentra en la posicion num.
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        L = [1,1]
        for i in range(2,num):
            posicion = L[-1] + L[-2]
            L.append(posicion)
            L.pop(0)
    print(L)
    return L[-1]


def main():
    numero = eval(input("Escribe un número: "))
    if numero < 0:
        print("No existe la serie fibonacce para numeros negativos.")
    print("La posición", numero, "de fibonacci es", fibonacci(numero))

if __name__ == "__main__":
    main()