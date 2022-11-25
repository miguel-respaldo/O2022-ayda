def merge(izquierda, derecha):
    print(f"Recibo {izquierda} y {derecha}")
    arreglo_ordenado = []
    indice_de_izquierda = 0
    indice_de_derecha = 0
    indice_arreglo_ordenado = 0
    # Recorremos ambos arreglos y vamos colocando los elementos ordenados. Colocamos siempre el que sea menor
    while indice_de_izquierda < len(izquierda) and indice_de_derecha < len(derecha):
        valor_izquierda = izquierda[indice_de_izquierda]
        valor_derecha = derecha[indice_de_derecha]
        if valor_izquierda <= valor_derecha:
            # El de la izquierda es menor, entonces lo ponemos primero
            arreglo_ordenado.append(valor_izquierda)
            # Y aumentamos en 1 el valor de la izquierda
            indice_de_izquierda += 1
        else:
            arreglo_ordenado.append(valor_derecha)
            indice_de_derecha += 1

        # Sin importar lo que hayamos movido, aumentamos el índice del actual
        indice_arreglo_ordenado += 1
    # Hasta aquí puede que el índice izquierdo o derecho hayan llegado a su fin, pero no ambos. Entonces
    # nos aseguramos de recorrerlos a ambos hasta el final
    while indice_de_izquierda < len(izquierda):
        arreglo_ordenado.append(izquierda[indice_de_izquierda])
        indice_de_izquierda += 1

    while indice_de_derecha < len(derecha):
        arreglo_ordenado.append(derecha[indice_de_derecha])
        indice_de_derecha += 1
    print(f"Los ordeno y combino. Resultado: {arreglo_ordenado}.")
    return arreglo_ordenado