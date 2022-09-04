# Nombre: Mauricio Basurto Jacobo
# No. Control: 18011057
# Calificación: XXX


def fact(n):
    if(n==1):
        return 1
    else:
        return n* fact(n-1)

print("ingrese un número entero positivo")
m = int(input())
print(fact(m))
