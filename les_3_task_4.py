# 4. Определить какое число в массиве встречается чаще всего

import random

SIZE = 300
MIN_ITEM = -15
MAX_ITEM = 15
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

tmp_set = set()
count_max = 0

#  В задании не уточнено, поэтому в случае одинаковой частоты вхождений
#  нескольких чисел решил возвращать первое, встретившееся в массиве
for i in array:
    if i in tmp_set:
        continue
    else:
        tmp_set.add(i)
    count = 0
    for j in array:
        if i == j:
            count += 1
    if count > count_max:
        count_max = count
        number = i
del tmp_set
print(f'Наиболее частое число: {number} (c количеством вхождений в массив: {count_max})')

# для проверки
print(sorted(array))