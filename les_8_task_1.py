# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib

a = input('Введите строку: ')

def substring(string):
    bar = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) if i == 0 else len(string) + 1):
            bar.append(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
    return len(set(bar))

print(f'Количество подстрок в строке "{a}": {substring(a)}')