def perform_heapsort(val_arr, num, cout):
max_val = count
counter1 = 2 * count + 1
counter2 = 2 * count + 2
if counter1 < num and val_arr(count) < val_arr(counter1):
max_val = counter1
if counter2 < num and val_arr(max_val) < val_arr(counter2):
max_val = counter 2
if max_val != count:
val_arr(count), val_arr(max_val) = val_arr(max_val), val_arr(count) perform_heapsort(val_arr,  num, max_val)
def heapSort(val_arr):
num = len(val_arr)
for count in range(num, -1, -1):
perform_heapsort(val_arr, num, count)
for count in range(num-1, 0, -1):
val_arr(count), val_arr(0) = val_arr(0), val_arr(count) # swap
perform_heapsort(val_arr, count, 0)
val_arr = ( 52, 91, 64, 252, 36, 91, 5, 35, 28) heapSort(val_arr)
num = len(val_arr)
print ("Values after performing heapsort")
for count in range(num):
print ("%d" %val_arr(count)),