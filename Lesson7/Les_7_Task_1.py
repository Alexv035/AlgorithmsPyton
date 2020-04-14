# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

size = int(input('Введите размер массива: '))
array = [random.randint(-100,99) for i in range(size)]

def sort(x):
    k = 0
    result = x.copy()
    for n in range(1, len(result)):
        a = 0
        for i in range(len(result) - n):
            if result[i] < result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
            else: a += 1
            k += 1
        if a == size: break
    print('Число итераций:', k)
    return result

print('Исходный массив:         ',array)
print('Массив после сортировки: ',sort(array))