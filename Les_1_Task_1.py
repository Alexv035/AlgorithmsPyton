# Task 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6
print(a, '=', bin(a))
print(b, '=', bin(b))

print("%d AND %d = %d (%s)" % (a, b, a & b, bin(a & b)))
print("%d OR %d = %d (%s)" % (a, b, a | b, bin(a | b)))
print("%d exc OR %d = %d (%s)" % (a, b, a ^ b, bin(a ^ b)))
print("%d shift << 2 = %d (%s)" % (a, a << 2, bin(a << 2)))
print("%d shift >> 2 = %d (%s)" % (a, a >> 2, bin(a >> 2)))
