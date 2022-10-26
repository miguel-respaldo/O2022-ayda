#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Octavio Corral Tovar
# No. Control: 19011234
# Calificación: XXX

def bubblesort(arr):
    for i in range(len(arr)): #este ciclo nos dira cuantas vueltas tendremos que darle al arreglo
        for j in range(len(arr)-1): #seguimos recorriendo el arreglo y comparamos los datos entre si 
            if arr[j] > arr[j+1]: #realizamos un condicional que compare el dato actual con el dato con un indice de mas, si este es mayor significa que no esta acomodado
                temp = arr[j] #guardamos en una variable temporal el dato mayor
                arr[j] = arr[j+1] #el dato menor lo guardamos en la posicion del dato mayor
                arr[j+1] = temp #el dato mayor lo pasamos a la derecha del dato menor
    return arr


def main():
    arr=[5,9,8,5,6,3,2,1,4]
    resultado = bubblesort(arr)
    print(resultado)
    


if __name__ == "__main__":
    main()