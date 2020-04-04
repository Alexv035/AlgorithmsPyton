# Task 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from _collections import defaultdict

rh1 = 1
rh2 = 1
res1 = []
res2 = []

# Ввод и проверка чисел
while True:
    inp1 = input("Введите первое шестнадцатеричное число: ").upper()
    inp2 = input("Введите второе шестнадцатеричное число: ").upper()
    a = 0
    r1 = 1
    r2 = 1
    num1 = []
    num2 = []
    for i in range(len(inp1)):
        if ((ord(inp1[i]) >= 65) and (ord(inp1[i]) <= 70)) or ((ord(inp1[i]) >= 48) and (ord(inp1[i]) <= 57)) or (ord(inp1[i]) == 45):
            if (ord(inp1[i]) == 45):
                r1 = -1
            else:
                num1.append(inp1[i])
        else:
            print('Первое число введенно некорректно')
            a = 1
            break
    for i in range(len(inp2)):
        if ((ord(inp2[i]) >= 65) and (ord(inp2[i]) <= 70)) or ((ord(inp2[i]) >= 48) and (ord(inp2[i]) <= 57)) or (ord(inp1[i]) == 45):
            if (ord(inp2[i]) == 45):
                r2 = -1
            else:
                num2.append(inp2[i])
        else:
            print('Второе число введенно некорректно')
            a = 1
            break

    if a == 0: break

# Создание словаря и функции возвращающей ключ через значение
h = defaultdict(int)
h = {'F': 15, 'E': 14, 'D': 13, 'C': 12, 'B': 11, 'A': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1, '0': 0}

def get_key(value):
    for q, w in h.items():
        if w == value: return q

# Перевод чисел в десятиричную систему и расчеты
n1dec = 0
for i, item in enumerate(num1):
    n1dec = n1dec + h[item]*16**(len(num1) - i - 1)
#print(n1dec)

n2dec = 0
for i, item in enumerate(num2):
    n2dec = n2dec + h[item]*16**(len(num2) - i - 1)
#print(n2dec)

result = r1*r2*n1dec*n2dec
result2 = r1*n1dec + r2*n2dec

if result < 0:
    result = -1*result
    rh1 = -1
if result2 < 0:
    result2 = -1*result2
    rh2 = -1
#print(result)
#print(result2)

# Функция перевода из десятиричной в шестнадцатиричную систему
def trans(number):
    k = 0
    r = []
    if number < 16:
        r.append(get_key(number))
    else:
        while True:
            p = number - 16*int(number/16)
#            print(p)
            r.insert(0, get_key(p))
            number = int(number/16)
            if number < 16:
                r.insert(0 , get_key(number))
                break
    return r

res1 = trans(result)
res2 = trans(result2)

if rh1 == -1: res1.insert(0, '-')
if rh2 == -1: res2.insert(0, '-')

# Ввывод результата
print('Первое число умноженние на второе равно: ',res1)
print('Первое число сложенное со вторым равно: ',res2)



