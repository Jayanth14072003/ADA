import time
import random
def partition(array, low, high):
 pivot = array[high]
 i = low - 1
 for j in range(low, high):
  if array[j] <= pivot:
   i = i + 1
   (array[i], array[j]) = (array[j], array[i])
   (array[i + 1], array[high]) = (array[high], array[i + 1])
 return i + 1
def quickSort(array, low, high):
 if low < high:
  pi = partition(array, low, high)
  quickSort(array, low, pi - 1)
  quickSort(array, pi + 1, high)
alist = random.sample(range(1, 1000000), 5000)
print('the unsorted elements are:',alist)
start_time = time.time()
quickSort(alist, 0, len(alist)-1)
end_time = time.time()
print('Sorted list: ', end='')
print(alist)
print('time taken for sorting is:',(end_time-start_time))
