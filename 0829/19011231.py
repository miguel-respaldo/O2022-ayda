#Nombre: José Manuel Buendia Rodriguez
#No. Control: 19011231
#Calificación:

num = int (input ("Digita un numero: "))
fact = 1
if num<0:
    print ("No existe factorial negativo")
elif num>=0:
    for n in range(1,(num+1)):
        fact = fact * n
    print("El factorial es:", fact)
