﻿# 1) Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = int(input("Введите целое трёхзначное число: "))
i = num//100
j = num%100//10
k = num%100%10

b = i*j*k
c = i+j+k
print("Произведение цифр числа - ", b)
print("Сумма цифр числа - ", c)


