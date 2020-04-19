# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

size = int(input('Введите размер массива: '))
array = [random.uniform(0,49.99) for i in range(size)]

def merge(left, right):
    sorted = []
    left_i = 0
    right_i = 0
    for i in range(len(left) + len(right)):
#        print('sorted: ', sorted)
        if left_i < len(left) and right_i < len(right):
            if left[left_i] <= right[right_i]:
                sorted.append(left[left_i])
                left_i += 1
            else:
                sorted.append(right[right_i])
                right_i += 1
        elif left_i == len(left):
            sorted.append(right[right_i])
            right_i += 1
        elif right_i == len(right):
            sorted.append(left[left_i])
            left_i += 1
    return sorted

def merge_sort(x):
    if len(x) < 2:
        return x
    mid = len(x) // 2
    left = merge_sort(x[:mid])
    right = merge_sort(x[mid:])
#    print(left,right)
    return merge(left, right)

print('Исходный массив:         ',array)
print('Массив после сортировки: ',merge_sort(array))

