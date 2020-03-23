# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

MIN = -10
MAX = 10
m = int(input('Введите натуральное число: '))
array = [random.randint(MIN, MAX) for i in range(2*m + 1)]

def mediana(array):
    for idx_i, i in enumerate(array):
        bigger = 0
        smaller = 0
        equal = 0
        for idx_j, j in enumerate(array):
            if idx_i == idx_j:
                continue
            elif i < j:
                bigger += 1
            elif i > j:
                smaller += 1
            else:
                equal += 1
        if bigger == smaller or bigger == smaller + equal or smaller == bigger + equal:
            mid = i
            break
        elif smaller + equal > bigger > smaller or bigger + equal > smaller > bigger:
            for k in range(1, equal + 1):
                if smaller < bigger:
                    smaller += 1
                else:
                    bigger += 1
            if smaller == bigger:
                mid = i
                break
            else:
                continue
    return mid

print(mediana(array))

