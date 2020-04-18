# Task 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import numpy as np

def adfs(graph, x, result):
    if x not in result:
        result.append(x)
        for n in graph[x]:
            adfs(graph,n, result)
    return result

def grf(n):
    r = np.random.randint(0, n, (n, n))
    for i in range(n): r[i,i] = 0
    return r


s = int(input('Введите количество вершин: '))
graph = grf(s)
print('граф: ')
print(graph)

result = adfs(graph,0, [])
result.append(0)
print('Обход вершин: ', result)