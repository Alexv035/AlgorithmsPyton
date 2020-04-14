# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

m = int(input('Введите натуральное число m: '))
size = 2*m + 1
array = [random.randint(-20,20) for i in range(size)]

n = 0
for i in range(len(array)):
    l = 0
    r = 0
    c = 0
    for j in range(len(array)):
        if (array[i] > array[j]) and (i != j): r += 1
        elif (array[i] < array[j]) and (i != j): l += 1
        elif (array[i] == array[j]) and (i != j): c += 1
        if (l > size//2) or (r > size//2): break
    n += 1
    if (l + c == r) or (l == r + c): break

print(array)
print('Median: ',array[n-1])