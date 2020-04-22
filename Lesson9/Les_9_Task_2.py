# Task 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, deque


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def htree(x):
    count_x = Counter(x)
    sorted_x = deque(sorted(count_x.items(), key=lambda item: item[1]))
    # print(sorted_x)

    while len(sorted_x) > 1:
        weight = sorted_x[0][1] + sorted_x[1][1]
        node = MyNode(left=sorted_x.popleft()[0], right=sorted_x.popleft()[0])

        for i, item in enumerate(sorted_x):
            if weight > item[1]:
                continue
            else:
                sorted_x.insert(i, (node, weight))
                break
        else:
            sorted_x.append((node, weight))
    return sorted_x[0][0]


def hcode(tree, path=''):
    if not isinstance(tree, MyNode):
        result[tree] = path
    else:
        hcode(tree.left, path=f'{path}0')
        hcode(tree.right, path=f'{path}1')


s = input('Введите строку для кодировки: ')

result = dict()
hcode(htree(s))
for i in s:
    print(result[i], end=' ')
