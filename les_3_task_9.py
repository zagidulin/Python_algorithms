# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_X = 7
SIZE_Y = 4
MIN_ITEM = -9
MAX_ITEM = 9
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_X)] for _ in range(SIZE_Y)]
for _ in matrix:
    print(_)

spam = None
j = 0
while j < SIZE_X:
    eggs = matrix[0][j]
    for _ in matrix:
        if eggs > _[j]:
            eggs = _[j]
    if spam is None or eggs > spam:
        spam = eggs
    j += 1

print(spam)


