# Task 2.
# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

# Task 2.1. алгоритм «Решето Эратосфена»
import cProfile

def number(k):
    init = []
    res = []
    if k > 10:
        n = int(k ** (1.5))
    else:
        n = k*3
    for i in range(n):
        init.append(i)

    init[1] = 0
    i = 2
    res.append(init[i])

    while True:
        if init[i] != 0:
            res.append(init[i])
            j = i + i

            while j < n:
                init[j] = 0
                j = j + i

        if k > (len(res) - 1):
            i += 1
        else:
            break

    return res[k]

#print(number(1000))

cProfile.run('number(100)')
#1645 function calls in 0.001 seconds
#540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#1101    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

#cProfile.run('number(20)')
#184 function calls in 0.000 seconds
#70    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#110    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


#cProfile.run('number(10)')
#74 function calls in 0.000 seconds
#28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#42    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# number(10)'
# 1000 loops, best of 5: 10.8 usec per loop
# number(20)'
# 1000 loops, best of 5: 27.3 usec per loop
# number(100)'
# 1000 loops, best of 5: 295 usec per loop
# number(500)'
# 1000 loops, best of 5: 3.4 msec per loop
# number(1000)'
# 1000 loops, best of 5: 9.62 msec per loop
