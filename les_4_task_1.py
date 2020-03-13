# Сформировать из введенного числа обратное по порядку входящих в него цифр

import timeit
import cProfile

# 1. Конкатенация

def reverse_conc(num):
    a = ''
    while num > 0:
        a = a + str(num % 10)
        num = num // 10
    a = int(a)
    return a

# 2. Рекурсия

def reverse_rec(num):
    if num // 10 == 0:
        return num
    else:
        a = len(str(num)) - 1
        return num % 10 * 10 ** a + reverse_rec(num // 10)

# 3. Цикл

def reverse_loop(num):
    a = 0
    while num > 0:
        a = a * 10 + num % 10
        num = num // 10
    return a

print(timeit.timeit('reverse_conc(123456789)', number=1000, globals=globals()))
# 0.008159400000000011
print(timeit.timeit('reverse_conc(123456789123456789)', number=1000, globals=globals()))
# 0.019081299999999995
print(timeit.timeit('reverse_conc(123456789123456789123456789123456789)', number=1000, globals=globals()))
# 0.039119299999999996
print(timeit.timeit('reverse_conc(123456789123456789123456789123456789123456789123456789123456789123456789)', number=1000, globals=globals()))
# 0.08071199999999998

print(timeit.timeit('reverse_rec(123456789)', number=1000, globals=globals()))
# 0.013646799999999987
print(timeit.timeit('reverse_rec(123456789123456789)', number=1000, globals=globals()))
# 0.03309029999999999
print(timeit.timeit('reverse_rec(123456789123456789123456789123456789)', number=1000, globals=globals()))
# 0.08132890000000001
print(timeit.timeit('reverse_rec(123456789123456789123456789123456789123456789123456789123456789123456789)', number=1000, globals=globals()))
# 0.2026308

print(timeit.timeit('reverse_loop(123456789)', number=1000, globals=globals()))
# 0.004581500000000016
print(timeit.timeit('reverse_loop(123456789123456789)', number=1000, globals=globals()))
# 0.010659999999999892
print(timeit.timeit('reverse_loop(123456789123456789123456789123456789)', number=1000, globals=globals()))
# 0.02254020000000012
print(timeit.timeit('reverse_loop(123456789123456789123456789123456789123456789123456789123456789123456789)', number=1000, globals=globals()))
# 0.05193300000000001

cProfile.run('reverse_conc(123456789)')
# 1    0.000    0.000    0.000    0.000 scratch_5.py:9(reverse_conc)
cProfile.run('reverse_conc(123456789123456789)')
# 1    0.000    0.000    0.000    0.000 scratch_5.py:9(reverse_conc)
cProfile.run('reverse_conc(123456789123456789123456789123456789)')
# 1    0.000    0.000    0.000    0.000 scratch_5.py:9(reverse_conc)
cProfile.run('reverse_conc(123456789123456789123456789123456789123456789123456789123456789123456789)')
# 1    0.000    0.000    0.000    0.000 scratch_5.py:9(reverse_conc)

cProfile.run('reverse_rec(123456789)')
# 9/1    0.000    0.000    0.000    0.000 scratch_6.py:4(reverse_rec)
cProfile.run('reverse_rec(123456789123456789)')
# 18/1    0.000    0.000    0.000    0.000 scratch_6.py:4(reverse_rec)
cProfile.run('reverse_rec(123456789123456789123456789123456789)')
# 36/1    0.000    0.000    0.000    0.000 scratch_6.py:4(reverse_rec)
cProfile.run('reverse_rec(123456789123456789123456789123456789123456789123456789123456789123456789)')
# 72/1    0.000    0.000    0.000    0.000 scratch_6.py:4(reverse_rec)

cProfile.run('reverse_loop(123456789)')
# 1    0.000    0.000    0.000    0.000 scratch_7.py:4(reverse_loop)
cProfile.run('reverse_loop(123456789123456789)')
# 1    0.000    0.000    0.000    0.000 scratch_7.py:4(reverse_loop)
cProfile.run('reverse_loop(123456789123456789123456789123456789)')
# 1    0.000    0.000    0.000    0.000 scratch_7.py:4(reverse_loop)
cProfile.run('reverse_loop(123456789123456789123456789123456789123456789123456789123456789123456789)')
# 1    0.000    0.000    0.000    0.000 scratch_7.py:4(reverse_loop)

# Зависимость во всех вариантах линейная.
# Быстрее остальных вариант с циклом, самый медленный - рекурсия.
# В выводах cprofile одни нули, кроме варианта с рекурсией.
