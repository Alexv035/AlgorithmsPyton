# Task 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random as rm

x, y = input('Введите диапозон четных чисел массива, в формате x,y: ').split(',')
n = int(input('Введите количество элементов в массиве: '))
x = int(x)
y = int(y)

m = [rm.randint(x,y) for _ in range(n)]
result = list.copy(m)
print('начальный массив: ', m)
#print(result)

rmin =[]
rmax = []
a = 0
b = 0

for i in range(len(m)):
    if (m[i] < a) or (i == 0): a = m[i]
    if (m[i] > b) or (i == 0): b = m[i]
#    print(a,b,m[i])

for i in range(len(m)):
    if m[i] == a: rmin.append(i)
    if m[i] == b: rmax.append(i)

for i in range(len(rmin)):
    result[rmin[i]] = b

for i in range(len(rmax)):
    result[rmax[i]] = a

print('min: ',a,'  max: ',b)
print('конечный массив:  ',result)


