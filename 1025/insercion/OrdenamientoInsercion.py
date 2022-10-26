#Nombre: Jose Manuel Buendia Rodriguez
#No. Control: 19011231
#Calificacion

lista = [5,7,1,3,8,4,9,2,6]

for i in range(1, len(lista)):

	actual = lista[i]
	indice = i

	while indice > 0 and lista[indice - 1] > actual:

		lista[indice] = lista [indice -1]
		indice = ndice - 1

	lista[indice] = actual

print (lista)