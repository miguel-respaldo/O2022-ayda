# Practica: Factorial
#Nombre: Luis Antonio Palacios Montufar 
# N° Control: 18011162
# Calificación: XXX

print('Ingresa el numero a calcular: ')
f = int(input())
fact = 1
for i in range(1, f+1):
    fact = fact*i
print("El factorial de el numero ",f,"es -> ",fact)