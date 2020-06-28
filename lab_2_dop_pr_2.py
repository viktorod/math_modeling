a = int(input('введите 1 сторону треугольника: '))
b = int(input('введите 2 сторону треугольника: '))
c = int(input('введите 3сторону треугольника: '))
if (a + b) <= c or (a + c) <= b or (b + c) <= a:
    print('Δ нема')
elif (a == b) and (a == c) and (b == c):
    print('Δ р/с')
elif (a == b) or (b == c) or (a == c):
    print('Δ р/б')
else:
    print('разносторонний Δ ')