#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 30
MIN_ITEM = -3999
MAX_ITEM = 3727
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
j = 1
while i + j < len(array):
    if array[i] >= 0:
        i += 1
        continue
    elif array[i + j] >= 0 or array[i] >= array[i + j]:
        j += 1
        continue
    else:
        i += j
        j = 1

print('Максимальный отрицательный элемент: ', array[i], '\nИндекс в массиве: ', i)