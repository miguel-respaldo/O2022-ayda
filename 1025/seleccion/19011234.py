#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Octavio Corral Tovar
# No. Control: 19011234
# Calificación: XXX

def selectionsort(arr): 
    for i in range(len(arr)-1): #recorremos la lista del primero hasta el penultimo dato para compararlos
        menoractual = i         #Tomamos el primer dato de la lista para comparalo y lo guardamos en una variable
        for j in range(i+1, len(arr)): #recorremos los demas datos empezando desde el segundo dato hasta el final
            if (arr[j] < arr[menoractual]): #comparamos los datos, si el segundo dato es menor que el primer dato
                menoractual = j             #sobreescribimos el valor de menor antiguo al nuevo menor

        aux = arr[menoractual]  #en la variable auxiliar guardamos el dato menor que recien encontramos
        arr[menoractual] = arr[i] #intercambiamos con el menor nuevo que encontramos al comparar los datos
        arr[i] = aux #intercambiamos los datos
    
    return arr




def main():
    arr=[5,9,8,5,6,3,2,1,4]
    resultado = selectionsort(arr)
    print(resultado)
    


if __name__ == "__main__":
    main()