def heapify(arreglo, n, i):
      maslargo = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arreglo[i] < arreglo[l]:
          maslargo = l
  
      if r < n and arreglo[maslargo] < arreglo[r]:
          maslargo = r
  
      if maslargo != i:
          arreglo[i], arreglo[maslargo] = arreglo[maslargo], arreglo[i]
          heapify(arreglo, n, maslargo)

def heapSort(arreglo):
   n = len(arreglo)
   # maxheap
   for i in range(n, -1, -1):
      heapify(arreglo, n, i)
   # element extraction
   for i in range(n-1, 0, -1):
      arreglo[i], arreglo[0] = arreglo[0], arreglo[i]
      heapify(arreglo, i, 0)
  
arreglo = [1, 12, 9, 5, 6, 10]
heapSort(arreglo)
n = len(arreglo)
print("Arreglo ordenado")

#Aqui va a imprimir todos los numeros ordenado del arreglo
for i in range(n):
    print(arreglo[i], end=', ')