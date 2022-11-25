#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Salvador de Jesus Dueñas Muñiz
# No. Control: 19011235
# Calificación: XXX

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        izq = myList[:mid]
        der = myList[mid:]

        # Llamadas recursivas en cada mitad
        mergeSort(izq)
        mergeSort(der)

        # dos iteradores para cada mitad
        i = 0
        j = 0
        
        # iterador para la lista principal
        k = 0
        
        while i < len(izq) and j < len(der):
            if izq[i] <= der[j]:
              # el valor de la mitad izquierda ya ah sido usado
              myList[k] = izq[i]
              # avanza el iterador
              i += 1
            else:
                myList[k] = der[j]
                j += 1
            # Movimiento al siguiente campo
            k += 1

        # para todos los valores restantes
        while i < len(izq):
            myList[k] = izq[i]
            i += 1
            k += 1

        while j < len(der):
            myList[k]=der[j]
            j += 1
            k += 1

        return myList

def main():
    myList = [54,26,93,17,77,31,44,55,20]
    mergeSort(myList)
    print(myList)

if __name__ == "__main__":
    main()


