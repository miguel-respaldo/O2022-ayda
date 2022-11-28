# Nombre: Luis Antonio Palacios Montufar
# No. Control: 18011162
# Calificación: XXX

import random
from random import randrange

def QuickSort(array: list) -> list:

    if len(array) < 2:
        return array
    pivot_index = randrange(len(array))
    pivot = array[pivot_index]
    greater: list[int] = []
    lesser: list[int] = []

    for element in array[:pivot_index]:
        (greater if element > pivot else lesser).append(element)

    for element in array[pivot_index + 1 :]:
        (greater if element > pivot else lesser).append(element)

    return QuickSort(lesser) + [pivot] + QuickSort(greater)


def main():
    print("Numeros que desea agregar:\n")
    lenght = int(input() or "20")
    array = [random.randint(1,100) for _ in range(lenght)]
    print("Arreglo sin ordenar:\n", array)
    orderedArray = QuickSort(array)
    print("Arreglo ordenado:\n", orderedArray)

if __name__ == "__main__":
    main()
print("Fin :)")