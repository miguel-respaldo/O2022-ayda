#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Emmanuel Gonzalez Gomez
# No. Control: 17011650
# Calificación: XXX

def fibonacci(num):
    #variables inside function
    res, n1, n2, i = 0, 0, 1, 2

    if i == 0:
        pass
    print(n1, end=", ")

    if i == 1:
        pass
    print(n2, end=", ")

    while i <= num:       # var "i" will make a loop to reach the limit of "num"
      res = n1 + n2        
      n1 = n2             
      n2 = res
      i+=1                #This is my count that will increment my variable "i"
      print(n2, end=",")  #show the fibonacci result got
    return res 

def main():
    numero = eval(input("Escribe un numero: "))
    print("\nLa posicion", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()

