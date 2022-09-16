#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Maria Guadalupe Garcia Baltazar
# No. Control: 19011845
# Calificación: XXX

def fibonacci(num):
    # el 0 como posición 1
    if(num==1):
        return 0
    # el 1 como posición 2
    elif(num==2):
        return 1
    else:
        # formula recursiva de fibonacci fibo(n)=fibo(n-1)+fibo(n-2)
        return (fibonacci(num-1)+fibonacci(num-2))

def main():
    numero = eval(input("Escribe un número: "))
    print("La posición", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()