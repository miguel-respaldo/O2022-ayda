'''

Nombre: Cecilia Alejandra Muriedas Ortiz
No. de conrol: 17011261
Calificación:XXX

'''
def factorial(n):
    if n>1:
        n = n * factorial(n-1)
        print("fac ",n)
    return n
    
numero = eval(input("Escribe un numero: "))
if numero<=1:
    print("El factorial de ",numero, "es", factorial(numero))
else:
    print("el factorial de ",numero," es ",factorial(numero))
