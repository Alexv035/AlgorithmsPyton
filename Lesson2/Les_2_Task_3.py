# Task 3
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

a = int(input('Введите целое число: '))
k = 0

while a > 0:
    b = a // 10
    c = a - b * 10
    if c != 0 and k == 0:
        k = 1
    if c == 0 and k == 0:
        pass
    else:
        print(c, end='')
    a = b
