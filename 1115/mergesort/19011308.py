def merge_sort(arreglo):
    longitud = len(arreglo)
    mitad = longitud//2  
    if longitud <= 1:
        return arreglo
    mitad_izquierda = arreglo[:mitad]
    mitad_derecha = arreglo[mitad:]
    mitad_izquierda = merge_sort(mitad_izquierda)
    mitad_derecha = merge_sort(mitad_derecha)
    return merge(mitad_izquierda, mitad_derecha)


def merge(izquierda, derecha):
    arreglo_ordenado = []
    indice_de_izquierda = 0
    indice_de_derecha = 0
    indice_arreglo_ordenado = 0
    while indice_de_izquierda < len(izquierda) and indice_de_derecha < len(derecha):
        valor_izquierda = izquierda[indice_de_izquierda]
        valor_derecha = derecha[indice_de_derecha]
        if valor_izquierda <= valor_derecha:
            arreglo_ordenado.append(valor_izquierda)
            indice_de_izquierda += 1
        else:
            arreglo_ordenado.append(valor_derecha)
            indice_de_derecha += 1

        indice_arreglo_ordenado += 1
    
    while indice_de_izquierda < len(izquierda):
        arreglo_ordenado.append(izquierda[indice_de_izquierda])
        indice_de_izquierda += 1

    while indice_de_derecha < len(derecha):
        arreglo_ordenado.append(derecha[indice_de_derecha])
        indice_de_derecha += 1
    return arreglo_ordenado


arreglo = [6, 5, 3, 1, 8, 7, 2, 4]
print(f"Arreglo original: {arreglo}")
print("Ordenando con merge sort")
arreglo_ordenado = merge_sort(arreglo)
print(f"Arreglo ordenado: {arreglo_ordenado}")
