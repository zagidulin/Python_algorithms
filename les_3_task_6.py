# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 30
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
if i > k:
    i, k = k, i
sum_between = 0
for _ in array[i + 1:k]:
    sum_between += _

print(sum_between)
