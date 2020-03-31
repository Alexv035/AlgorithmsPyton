#Task 1: from Les_3_Task 7.
# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

import cProfile

# Variant 1
def test_var1(var1):
    lst =  [0,1,3,6,10,15,21,28]
    for i, item in enumerate(lst):
        assert(item) == var1(i)
#        print(f'Test {i} OK')


def var1(n):
    k = 0
    for i in range(n): k = k + i + 1
    return(k)

#test_var1(var1)

#cProfile.run('var1(500)')
#4 function calls in 0.000 seconds
#1    0.000    0.000    0.000    0.000 Les_4_Task_1.py:15(var1)

#cProfile.run('var1(20)')
#4 function calls in 0.000 seconds
#1    0.000    0.000    0.000    0.000 Les_4_Task_1.py:15(var1)

#cProfile.run('var1(10)')
#4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 Les_4_Task_1.py:15(var1)

# var1(10)'
# 1000 loops, best of 5: 809 nsec per loop
# var1(20)'
# 1000 loops, best of 5: 1.22 usec per loop
# var1(100)'
# 1000 loops, best of 5: 6.17 usec per loop
# var1(500)'
# 1000 loops, best of 5: 36,4 usec per loop
# var1(1000)'
# 1000 loops, best of 5: 71,5 usec per loop

