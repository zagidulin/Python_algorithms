# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 15
MIN_ITEM = -95
MAX_ITEM = 95
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
j = 1
min_1 = array[i]
min_2 = array[j]
while i + j < len(array):
    if array[i] <= array[i + j]:
        min_1 = array[i]
        if array[i + j] <= min_2:
            min_2 = array[i + j]
        j += 1
    else:
        min_1 = array[i + j]
        min_2 = array[i]
        i += j
        j = 1

print(min_1, min_2)