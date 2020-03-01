#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 27
MIN_ITEM = -3999
MAX_ITEM = 3727
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
j = 1
while i + j < len(array):
    if array[i] >= array[i + j]:
        j += 1
    else:
        i += j
        j = 1
k = 0
j = 1
while k + j < len(array):
    if array[k] <= array[k + j]:
        j += 1
    else:
        k += j
        j = 1
array[i], array[k] = array[k], array[i]
print(array)
