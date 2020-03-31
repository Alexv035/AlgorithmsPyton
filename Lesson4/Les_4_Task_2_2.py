# Task 2.
# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

# Task 2.2. без использования «Решета Эратосфена».
import cProfile

def number(k):
    res = []
    i = 2
    while True:
        u = 0
        for s in res:
            if i%s == 0: u = 1
        if u == 0: res.append(i)

        if k == (len(res)):
            break
        i +=1

    return res[k - 1]

#print(number(74))

# Выводы: Несмотря на более короткий код, расчеты идут существенно медленее особенно при больших к


#cProfile.run('number(100)')
#644 function calls in 0.001 seconds
#540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

#cProfile.run('number(20)')
#94 function calls in 0.000 seconds
#70    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


#cProfile.run('number(10)')
#42 function calls in 0.000 seconds
#28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# number(10)'
# 1000 loops, best of 5: 13.9 usec per loop
# number(20)'
# 1000 loops, best of 5: 51,1 usec per loop
# number(100)'
# 1000 loops, best of 5: 2 msec per loop

