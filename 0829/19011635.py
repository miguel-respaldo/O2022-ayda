#Nombre: Hernandez Ventura Luis Antonio
#No. Control: 19011635
#Calificación: XXX

def factorial(num): 
    if num < 0: 
        print("No existe el factorial")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

numero = eval(input("Escriba un numero a sacar el factorial: ")) 

print("El factorial de", numero, "es", factorial(numero))
