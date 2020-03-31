#Task 1: from Les_3_Task 7.
# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

import cProfile
import functools

# Variant 3
def test_var1(var1):
    lst =  [0,1,3,6,10,15,21,28]
    for i, item in enumerate(lst):
        assert(item) == var1(i)
#        print(f'Test {i} OK')

@functools.lru_cache()
def var1(n):
    if n < 2:
        return n
    return var1(n - 1) + n

#test_var1(var1)

# Выводы: Простые вычисления лучше и быстрее выполнять простыми функциями с использованием циклов. Рекурсивы и задествования кэша в простых вычислениях существенно замедляет процесс вычисления

#cProfile.run('var1(100)')
#103 function calls (4 primitive calls) in 0.000 seconds
#100/1    0.000    0.000    0.000    0.000 Les_4_Task1_2.py:14(var1)

#cProfile.run('var1(20)')
#23 function calls (4 primitive calls) in 0.000 seconds
#20/1    0.000    0.000    0.000    0.000 Les_4_Task1_2.py:14(var1)

#cProfile.run('var1(10)')
#13 function calls (4 primitive calls) in 0.000 seconds
#10/1    0.000    0.000    0.000    0.000 Les_4_Task1_2.py:14(var1)

# var1(10)'
# 1000 loops, best of 5: 97.7 nsec per loop
# var1(20)'
# 1000 loops, best of 5: 102 nsec per loop
# var1(100)'
# 1000 loops, best of 5: 101 nsec per loop
# var1(500)
# RecursionError: maximum recursion depth exceeded in comparison
