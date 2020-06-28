x = int(input('введите число: '))
a = 0
b = ' '
while x != 0:
    a = x % 10
    b = b + str(a)
    x = x // 10
print(b)  