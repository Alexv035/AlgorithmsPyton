# Task 4.
# Определить, какое число в массиве встречается чаще всего.

import random as rm

x, y = input('Введите диапозон четных чисел массива, в формате x,y: ').split(',')
n = int(input('Введите количество элементов в массиве: '))
x = int(x)
y = int(y)

m = [rm.randint(x, y) for _ in range(n)]
print('начальный массив: ', m)
result = 0

for i in range(len(m)):
    b = 0
    for y in range(len(m)):
        if m[i] == m[y]: b += 1
    if (b > result) or (i == 0):
        result = b
        res = m[i]

print('число в массиве встречается чаще всего:  ', res)
