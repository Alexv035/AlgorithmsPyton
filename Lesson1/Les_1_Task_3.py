import random as rm

# a. случайное целое число,
x, y = input('Введите диапазон целых чисел в формате x,y: ').replace(' ','').split(',')
print(rm.randint(int(x),int(y)))

# b. случайное вещественное число
x, y = input('Введите диапазон вещественных чисел в формате x,y: ').replace(' ','').split(',')
print(rm.uniform(float(x),float(y)))

# c. случайный символ.
x, y = input('Введите диапазон символов от a до z в формате x,y: ').replace(' ','').split(',')
c = ord(x)
d = ord(y)
f = rm.randint(c,d)
print(chr(f))

