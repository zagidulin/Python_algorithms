# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import random
import sys

SIZE = 17
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
a = {}

# вариант 1
def func_while(lst):
    i = 0
    j = 1
    while i + j < len(lst):
        if lst[i] >= lst[i + j]:
            j += 1
        else:
            i += j
            j = 1
    k = 0
    j = 1
    while k + j < len(lst):
        if lst[k] <= lst[k + j]:
            j += 1
        else:
            k += j
            j = 1
    if i > k:
        i, k = k, i
    sum_between = 0
    for item in lst[i + 1:k]:
        sum_between += item
    a[func_while] = [*locals().values()] # добавление к исходному коду для задания
    return f'Сумма: {sum_between}'

# вариант 2
def func_for(lst):
    i = 0
    j = 0
    for k in range(1, len(lst)):
        if lst[k] < lst[i]:
            i = k
        elif lst[k] > lst[j]:
            j = k
    if i > j:
        i, j = j, i
    sum_between = 0
    for k in range(i + 1, j):
        sum_between += lst[k]
    a[func_for] = [*locals().values()]  # добавление к исходному коду для задания
    return f'Сумма = {sum_between}'

# вариант 3
def func_builtin(lst):
    if lst.index(min(lst)) < lst.index(max(lst)):
        sum_between = sum(lst[lst.index(min(lst))+1:lst.index(max(lst))])
    else:
        sum_between = sum(lst[lst.index(max(lst))+1:lst.index(min(lst))])
    a[func_builtin] = [*locals().values()]  # добавление к исходному коду для задания
    return f'Сумма = {sum_between}'


def show(obj, l = 0):
    if l == 0: # введено, чтобы не подсчитывался список со значениями, которого в функции нет
        total = 0
    else:
        total = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                total += show(key, l + 1)
                total += show(value, l + 1)
        elif not isinstance(obj, str):
            for item in obj:
                total += show(item, l + 1)
    return total

func_while(array)
func_for(array)
func_builtin(array)

for key in a:
    print(f'Объём занимаемой памяти функцией "{key.__name__}":')
    print(show(a[key]))

print(sys.platform)

# Объём занимаемой памяти функцией "func_while":
# 872
# Объём занимаемой памяти функцией "func_for":
# 844
# Объём занимаемой памяти функцией "func_builtin":
# 760

# Оптимальный вариант - с использованием встроенных функций,
# т.к. не содержит временных переменных.
# while чуть больше for из-за введённой переменной-счетчика

# win32, Python '64bit'
