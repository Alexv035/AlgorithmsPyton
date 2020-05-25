'''
Task 2.
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
'''

# Task 2.1. алгоритм «Решето Эратосфена»
import cProfile


def ftest(tfuc):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i, item in enumerate(lst):
        assert (item) == tfuc(i)


#       print(f'Test {i} OK')


def number(k):
    init = []
    res = []
    n = int(k ** (1.5))
    for i in range(n):
        init.append(i)

    init[1] = 0
    i = 2
    res.append(init[i])

    while True:
        if init[i] != 0:
            res.append(init[i])
            j = i + i
            print(res)
            print(i, j, n)

            #           if j > n/2:
            # print(init)
            # t +=2
            # for p in range(n, n*t):
            #    init.append(p)
            # print(init)
            # n = n*t

            while j < n:
                init[j] = 0
                j = j + i

        if k > (len(res) - 1):
            i += 1
        else:
            break

    print(init)
    print(res)
    return res[k]


print(number(50))

# cProfile.run('number(100)')
# 1673 function calls in 0.001 seconds
# 671    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 998    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('number(20)')
# 323 function calls in 0.000 seconds
# 121    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 198    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


# cProfile.run('number(10)')
# 157 function calls in 0.000 seconds
# 55    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 98    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# number(10)'
# 1000 loops, best of 5: 15.9 usec per loop
# number(20)'
# 1000 loops, best of 5: 32.6 usec per loop
# number(100)'
# 1000 loops, best of 5: 192 usec per loop
# number(500)'
# 1000 loops, best of 5: 1.09 msec per loop
# number(1000)'
# 1000 loops, best of 5: 2.28 msec per loop
