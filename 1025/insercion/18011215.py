#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Sebastian Garcia Quijas
# No. Control: 18011215
# Calificación: XXX

def mostrar(lista, l):
	lista= " "
	for i in range(0,l):
		lista+=str(lista[i])+ " "
	print(lista)   
valores = [5,45,78,1,64,65,8]
for i in range(1,len(valores)):
	clave = valores[i]
	j = i-1
	while (j>=0 and valores[j] > clave):
		#Insertar el valor donde corresponda
		valores[j+1] = valores[j]
		j = j-1
	valores[j+1] = clave
	mostrar(valores, len(valores))
mostrar(valores, len(valores)) 

	
