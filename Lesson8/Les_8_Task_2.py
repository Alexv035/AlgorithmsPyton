# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

import collections

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    numbers = collections.defaultdict(list)
    quan = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    numbers[start].append(start)
    min_cost = 0
    n = start
    quan[start] = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    quan[i] = quan[start] + 1
                    parent[i] = start

                    if n == start:
                        numbers[i].append(start)
                    elif not numbers[i] and len(numbers[start]) >= 1:
                        numbers[i] = numbers[start].copy()
                        numbers[i].append(start)
                    else:
                        if numbers.get(n).count(i) == 1: numbers.get(n).remove(i)
                        numbers[i].append(start)

                # print(start, i, quan, numbers)

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, numbers


s = int(input('От какой вершины идти: '))
mcost, lh = dijkstra(g, s)

print('Стоимость пути от начальной точки до конечной: ', mcost, '\n')
print('Список вершин через которых проходит путь: ', dict(lh), '\n')
