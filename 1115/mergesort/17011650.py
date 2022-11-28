def mergeSort(lst):
    if len(lst) > 1:
        middle = len(lst)//2
        l = lst[:middle]
        r = lst[middle:]
        
        mergeSort(l)
        mergeSort(r)
        
        i,j,k = 0,0,0
        
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                lst[k]=l[i]
                i+=1
            else:
                lst[k]=r[j]
                j+=1
            k+=1
            
        while i < len(l):
            lst[k]=l[i]
            i+=1
            k+=1
                 
        while j < len(r):
            lst[k]=r[j]
            j+=1
            k+=1
            
    return lst
                
arreglo = mergeSort([5,245,12,2,7])
print(arreglo)