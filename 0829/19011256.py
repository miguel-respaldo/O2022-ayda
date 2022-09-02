#Alumno: Rodriguez Pacheco Jose Ruben
#Numero De Control: 19011256
#Calificacion:
print("Ingrese un numero ")
num = int(input())
facto = 1

if num == 0:
    	print("El factorial de 0 es 1")

elif num>0:
    for i in range(1, num+1):
        facto*=i    	
    print("El factorial de ",num,"es",facto)

else:
    print("Usted ingreso un numero negativo o un valor que no es un numero")
