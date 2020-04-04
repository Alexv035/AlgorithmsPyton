# Task 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего. Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

from collections import namedtuple
import random

firms = namedtuple('firms', ['q1', 'q2', 'q3', 'q4'])
fbase = {}
n = 0

while n <= 0:
    n = int(input("Введите количество предприятий: "))

for i in range(n):
    print('Введите данные по предприятию №',i+1)
    name = input("Название предприятия: ")
    p_q1 = float(input('прибыль за 1-й квартал: '))
    p_q2 = float(input('Прибыль за 2-й квартал: '))
    p_q3 = float(input('Прибыль за 3-й квартал: '))
    p_q4 = float(input('Прибыль за 4-й квартал: '))
    fbase[name] = firms(q1=p_q1, q2=p_q2, q3=p_q3, q4=p_q4)

total_profit = ()

for name, p in fbase.items():
    print(f'Предприятие: {name} прибыль за год: {round(sum(p),2)}')
    total_profit += p

print()
avg_profit = sum(total_profit) / len(fbase)
print(f'Средняя прибыль за год для всех предприятий: {round(avg_profit,2)} \n')

print('Предприятия, у которых прибыль выше среднего:')
for name, p in fbase.items():
    if sum(p) > avg_profit:
        print(f'{name}, прибыль: {round(sum(p),2)}')
print()
print('Предприятия, у которых прибыль ниже среднего:')
for name, p in fbase.items():
    if sum(p) < avg_profit:
        print(f'{name}, прибыль {round(sum(p),2)}')