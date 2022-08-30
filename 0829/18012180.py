def factorial(n):
    for i in range(0, n+1):
        resultado = 0
        if i==0 or i==1:
            resultado = 1
        elif i > 1:
            resultado = i * factorial(n-1)
    return resultado

x = int(input("Ingrese un numero: "))
fact = factorial(x)
print("Factorial: ",fact)