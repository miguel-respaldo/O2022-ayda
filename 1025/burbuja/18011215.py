#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Sebastian Garcia Quijas
# No. Control: 18011215
# Calificación: XXX
def burbuja (array):
    lenght = len(array)-1
    for i in range(0, lenght):
        for k in range(0,lenght):
            if array[k]> array [k+1]:
                aux = array[k]
                array[k] = array [k + 1]
                array[k+1] = aux

    return array
valores = [5,45,78,1,64,65,8]

print (burbuja(valores));
