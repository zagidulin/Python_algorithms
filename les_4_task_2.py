import timeit
import cProfile

# 1. С решетом

def eratosfen(x):
    if x == 1:
        return 2
    number_list = [_ for _ in range(x)]
    number_list[1] = 0
    prime_list = []
    m = 2
    c = 0
    while len(prime_list) < x:
        if m >= len(number_list): # т.к. поиски зависимости длины числового ряда на просторах интернета не удались,
            c += 1
            number_list += [_ for _ in range(x * c, x * (c+1))] # то увеличиваю его по мере необходимости
            m = 2
        if number_list[m] != 0:
            if number_list[m] not in prime_list:
                prime_list.append(number_list[m])
            j = m*2
            while j < len(number_list):
                if number_list[j] == 0:
                    j += m
                    continue
                number_list[j] = 0
                j += m
        m += 1
    return prime_list[x-1]


# 2. Без решета

import math

def primes(n):
    prime_list = [2]
    if n == 1:
        return prime_list[0]
    k = 2
    while len(prime_list) < n:
        for j in prime_list:
            if k % j == 0:
                break
            elif j > math.sqrt(k):
                prime_list.append(k)
                break
        k += 1
    return k-1

print(timeit.timeit('eratosfen(5)', number=100, globals=globals()))
# 0.002890900000000002
print(timeit.timeit('eratosfen(15)', number=100, globals=globals()))
# 0.0155507
print(timeit.timeit('eratosfen(45)', number=100, globals=globals()))
# 0.0752942

print(timeit.timeit('primes(5)', number=100, globals=globals()))
# 0.000858500000000012
print(timeit.timeit('primes(15)', number=100, globals=globals()))
# 0.003752499999999992
print(timeit.timeit('primes(45)', number=100, globals=globals()))
# 0.01963680000000001

cProfile.run('eratosfen(5)')
#  2    0.000    0.000    0.000    0.000 les_4_task_2.py:17(<listcomp>)
# 71    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#  5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('eratosfen(15)')
#   3    0.000    0.000    0.000    0.000 les_4_task_2.py:17(<listcomp>)
# 476    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#  15    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('eratosfen(45)')
#    4    0.000    0.000    0.000    0.000 les_4_task_2.py:17(<listcomp>)
# 2473    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   45    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('primes(5)')
# 11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#  9    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#  4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('primes(15)')
# 47    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 55    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
# 14    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('primes(45)')
# 197    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 306    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#  44    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


# Excel показывает больший коэффициент детерминации для степенной зависимости. 
# Вариант без решета быстрее (более чем в 3 раза).
# В выводах cprofile видно, что вариант с решетом больше вызывает различные методы
# и количество вызовов растёт более быстрыми темпами, чем в варианте без решета.
