# Task 4
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

def f(x):
    return -x / 2


n = int(input('Введите количество элементов: '))

k = 1
t = 1

for i in range(n - 1):
    t = f(t)
    k = k + t

print(k)
