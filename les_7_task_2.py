# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
array = [random.randint(0, 49) + random.randint(0, 99) / 100 for _ in range(SIZE)]
print(array)

def merge_sort(array):
    def merge(left_eggs, right_eggs):
        sorted_list = []
        while len(left_eggs) > 0 and len(right_eggs) > 0:
            if left_eggs[0] < right_eggs[0]:
                sorted_list.append(left_eggs[0])
                left_eggs.pop(0)
            else:
                sorted_list.append(right_eggs[0])
                right_eggs.pop(0)
        if len(left_eggs) > 0:
            sorted_list += left_eggs
        else:
            sorted_list += right_eggs
        return sorted_list
    def devide(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        left_eggs = devide(array[:mid])
        right_eggs = devide(array[mid:])
        return merge(left_eggs, right_eggs)
    return devide(array)

print(merge_sort(array))


# Тест скорости на range(1000)
# Слияние:
# print(timeit.timeit('merge_sort(array)', number=100, globals=globals()))
# 0.6726688999999979