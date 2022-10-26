#Nombre: Jose Manuel Buendia Rodriguez
#No. Control: 19011231
#Calificacion

lista = [5,7,1,3,8,4,9,2,6]

band = false
while band == false:
	band = True
	for i in range(len(lista)-1):
		if lista[i] > lista[i+1]:
			aux = lista[i]
			lista[i] = lista[i+1]
			lista[i+1] = aux
			band = false

print(lista)
