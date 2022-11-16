#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Alan Alexander Fuentes Soto
# No. Control: 19011308
# Calificación: XXX

Array = [10,5,9,2,6,34,1,11]

def QuickSort (List):
    izquierda = []
    centro = []
    derecha = []
    if len(List) > 1:
        aux = List[0]
        for i in List:
            if i < aux:
                izquierda.append(i)
            elif i == aux:
                centro.append(i)
            elif i > aux:
                derecha.append(i)
        return QuickSort(izquierda)+centro+QuickSort(derecha)
    else:
      return List
print(Array)
print(QuickSort (Array))
