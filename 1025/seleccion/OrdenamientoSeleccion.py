#Nombre: Jose Manuel Buendia Rodriguez
#No. Control: 19011231
#Calificacion

lista = [5,7,3,1,8,4,9,2,6]

longitud = len(lista)

for i in range(longitud-1):
    print(lista)
    menor = i 
    print("El indice actual para comprar es: ",menor)
    for j in range (i+1, longitud):
        if lista[j] < lista[menor]:
            menor = j
            print("Recorriendo lista, Es menor el indice ", menor  )

    temporal = lista[menor]
    lista[menor] = lista[i]
    lista[i] = temporal
    print("Cambiamos el elemento ", lista[menor], "por el elemento", lista[i])