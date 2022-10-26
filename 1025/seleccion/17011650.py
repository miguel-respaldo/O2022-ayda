
#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Hugo Emmanuel Gonzalez Gomez
# No. Control: 17011650
# Calificación: XXX

def mi_lista(lista):
  n = len(lista)

  for i in range(0, n-1):
    k = i
    t = lista[i]
    for j in range(i,n):
        if lista[j] < t:
          k = j
          t = lista[j]
    lista[k] = lista[i]
    lista[i] = t

  return lista

lista = [88,2,5,7,955,87,47,9,10,97]
print(mi_lista(lista))