def factorial(num):
    factor = 1
    while(num > 1):
        factor = factor*num
        num = num - 1
    return factor

print("Dame el numero para sacar el factorial: ")
numero = input()
if numero.isdigit() == False:
    print("No es valido el numero ingresado")
else:
    numero = int(numero)
    resultado = factorial(numero)
    print("el resultado factorial es: ", resultado)