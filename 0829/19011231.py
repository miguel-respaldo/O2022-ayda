#Nombre: José Manuel Buendia Rodriguez
#No. Control: 19011231
#Calificación:

num = input ("Digita un numero: ")
num1 = int(num)
from math import factorial
if num1 < 0:
    print("No existe factorial negativo")

print ("El factorial es: ", factorial(num1))