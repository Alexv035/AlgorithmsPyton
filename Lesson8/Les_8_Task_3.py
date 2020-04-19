# Task 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import collections
import random as rm

graph = collections.defaultdict(list)

def adfs(graph, x, result):
    if x not in result:
        result.append(x)
        for n in graph[x]:
            adfs(graph,n, result)
    return result

def grf(n):
    r = collections.defaultdict(list)
    for i in range(0, n):
        l = rm.randint(1, n)
        r[i].append(i)
        for j in range(0, l):
            k = rm.randint(0, n - 1)
            if i != k and r.get(i).count(k) < 1: r[i].append(k)
    return r

s = int(input('Введите количество вершин: '))
graph = grf(s)
print('граф: ', dict(graph))

result = adfs(graph,0, [])
if len(result) == s:
    print('Обход вершин: ', result)
else:
    print('Обход вершин невозможен')
