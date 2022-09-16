#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alexa Fernanda Iniguez Jimenez
# No. Control: 18011226
# Calificación: XX

def fibonacci(num):
    #Modificar esta parte
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
        #return num**2

def main():
    numero = eval(input("Escribe un numero: "))
    print("La posicion", numero, "de fibonacci es", fibonacci(numero))

if __name__ == "__main__":
    main()
