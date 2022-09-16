#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Octavio Corral Tovar
# No. Control: 19011234
# Calificación: XXX

def fibonacci(num): # Creo una funcion que reciba un parametro, en este caso sera el numero digitado por el usuario.
    n1 = 0          # Inicializamos las variables en 0 y en 1 para que se puedan ir sumando
    n2 = 1 
   
    if(num < 0):    # Si el numero es menor a 0 va a retornar un error

        return "error" 
           
    else:   #Si el numero no es menor a 0, realiza el ciclo
        for i in range(num): #El ciclo se repetira hasta que se alzance el numero ingresado

            print(n1)               #Vamos imprimiendo los resultados en pantalla

            n3 = n1 + n2            #En la variable n3 se iran guardando la suma de n1 y n2
            n1 = n2                 # n1 tomara el resultado de n2 que es el resultado de la suma anterior
            n2 = n3                 # n2 tomara el resultado de la suma que se guarda en n3
                	
        return n1                   #Retornamos el n1 para tomar como posicion 1 el 0

def main():
    numero = eval(input("Escribe un número: "))      #Se le pide al usuario digitar la posicion
    print("La posición", numero, "de fibonacci es", fibonacci(numero))   #Se llama a la funcion e imprime el resutado que genere la funcion
    

if __name__ == "__main__":
    main()